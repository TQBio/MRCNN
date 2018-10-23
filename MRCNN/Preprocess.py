


import gc
import numpy as np
import datetime 
import linecache






#Data Preprocessing£º  
#starttime = datetime.datetime.now()   
#Read the 400bp sequence upstream and downstream of each cg site and store it in wgbs['seq']
#################################################


def convertSeqToArray(Seq_charnum):
 '''
 
 Chromosome sequence number
 File name of the DNA sequences data to be read = file_in_name
 File name of the encoded array  data to be read = file_out_name
 
  '''
  
 #Parameter Setting
 bp = 200
 i = 0
 fl=open(seq_out_name , 'w')
 number = 1 #the number of Chromosome changed add one column for '1'
 wgbs_name = 'GSM432685_H1_WGBS-chr%d.txt' % number
 chr_name = 'chr%d.fa' % number
 seq_out_name = "/xxx/Seq-num%d.fa" % number #where you want to save the after-preprocessed data 
 unames = ['location' , 'methvalue']
 wgbs = pd.read_table(wgbs_name , sep='\t' , header = None , names = unames)
 f = open(wgbs_name ,'r')
 lineNum = 0
 lineNum = len(f.readlines()) 
 f.close()
 #Create a list to store the sequence
 all_seq = []
 seq = ""
 #Timing begins
 while i < lineNum:
    
    numline = np.divide(wgbs['location'][i] , 50) + 2
    count = linecache.getline(chr_name , numline)
    index = wgbs['location'][i] - np.divide(wgbs['location'][i] , 50)*50 - 1 
    wnumline = np.divide((bp-index),50)
    snumline =  numline - wnumline - 1             
    slocation = 50 -  (bp - index - wnumline*50)       
    scount = linecache.getline(chr_name , snumline)
    str_list = []
    str_list.append(scount[slocation:50])
    startline = snumline
    for j in range(0,wnumline-1):
        startline = startline + 1
        wcount = linecache.getline(chr_name , startline)
        str_list.append(wcount[0:50])
    if (index == -1):
        startline = startline + 1
        wcount = linecache.getline(chr_name , startline)
        str_list.append(wcount[0:50+index])
    else:
        startline = startline + 1
        wcount = linecache.getline(chr_name , startline)
        str_list.append(wcount[0:50])
    if (index != -1):
        str_list.append(count[0:index])
    str_list.append(count[index+2:50])
    wnumline = np.divide((bp-(50-index-2)),50)    
    enumline = numline + wnumline + 1
    elocation = bp - (50-index-2) - wnumline*50 - 1
    startline = numline
    for k in range(0,wnumline):
        startline = startline + 1
        wcount = linecache.getline(chr_name , startline)
        str_list.append(wcount[0:50])  
        
    ecount = linecache.getline(chr_name , enumline)
    str_list.append(ecount[0:elocation+1])
    seq = ''.join(str_list)
    seq = seq.replace("N","0")
    seq = seq.replace("a","1")
    seq = seq.replace("A","1")
    seq = seq.replace("t","4")
    seq = seq.replace("T","4")
    seq = seq.replace("c","3")
    seq = seq.replace("C","3")
    seq = seq.replace("g","2")
    seq = seq.replace("G","2")
    seq = "".join(list(seq))
    all_seq.append(seq)
    fl.write(all_seq[i])
    fl.write("\n")
    i = i+1
 fl.close()
 #End of time
 #endtime = datetime.datetime.now()   
 #print (endtime - starttime).seconds

 #Optional operation£ºIf the computer is out of memory, you can split the original data
 LIMIT = 200000;
 file_cout = 0;
 url_list = [];
 with open("Seq_charnum.fa") as f:
	for line in f:
		url_list.append(line)
		if len(url_list) < LIMIT:
			continue
		file_name = str(file_cout)+".csv"
		with open(file_name,"w") as file:
			for url in url_list[:-1]:
				file.write(url)
			file.write(url_list[-1].strip())
			url_list=[]
			file_cout+=1
 if url_list:
	file_name = str(file_cout)+"sp0_part_train.csv"
	with open(file_name,"w") as file:
		for url in url_list:
			file.write(url)
 print("Done")

#produce .npy object
 k = 2
 while(2<=k<=9):
 In_name  = '%d.csv' % k
 out_name = 'file_out_name' % k
 seq = []
 with open(In_name) as f:
	for line in f:
	 seq.append(line)
 seq = "".join(list(seq))
 seq = seq.splitlines()
 oc = [[] for i in range(0,len(seq))]
 for i in range(0,len(seq)):
  for j in range(0,len(seq[i])):
	 if(seq[i][j] == '0'):
	  oc[i].append([0,0,0,0])
	 if(seq[i][j] == '1'):
	  oc[i].append([0,0,0,1])
   if(seq[i][j] == '2'):
	  oc[i].append([0,0,1,0])
   if(seq[i][j] == '3'):
    oc[i].append([0,1,0,0])
	 if(seq[i][j] == '4'):
	  oc[i].append([1,0,0,0])
 del seq
 Array = np.array(oc)
 np.save(out_name,Array) 
 del Array
 k = k + 1
 
 
 
 return Array
  
  
  
##################
