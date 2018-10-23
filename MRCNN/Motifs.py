from __future__ import division
from __future__ import print_function

from collections import OrderedDict
import re
import pandas as pd


def Intomtom(path):
    d = pd.read_table(path)
    d.rename(columns={'#Query ID': 'Query ID'}, inplace=True)
    d.columns = [x.lower() for x in d.columns]
    d['idx'] = [int(x) for x in d['query id'].str.replace('filter', '')]
    return d


def MEME(meme_db_file):
    motifs = []
    motif = None
    for line in open(meme_db_file):
        if line.startswith('MOTIF'):
            if motif:
                motifs.append(motif)
                motif = None
            tmp = line.split()[1:]
            if len(tmp) < 2:
                continue
            motif = OrderedDict()
            motif['id'] = tmp[0]
            motif['url'] = ''
        elif motif and line.startswith('URL'):
            motif['url'] = line.split()[1]
    if motif:
        motifs.append(motif)
    for i, motif in enumerate(motifs):
        motifs[i] = pd.DataFrame(motif, index=[0])
    motifs = pd.concat(motifs)
    return motifs


def Getport(filter_stats_file, tomtom_file, meme_motifs):
    filter_stats = pd.read_table(filter_stats_file)
    tomtom = read_tomtom(tomtom_file)
    tomtom = tomtom.sort_values(['idx', 'p-value'])
    tomtom = tomtom.loc[:, ~tomtom.columns.isin(['query id', 'optimal offset'])]
    d = pd.merge(filter_stats, tomtom, on='idx', how='outer')
    meme_motifs = meme_motifs.rename(columns={'id': 'target id'})
    d = pd.merge(d, meme_motifs, on='target id', how='left')
    d.index.name = None
    return d