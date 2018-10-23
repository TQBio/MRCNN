# MRCNN
MRCNN provides a deep-learning method for prediction of single-CpG-site methylation level with only local DNA sequences. It is implemented by deep learning library Tensorflow (version of tensorflow-gpu 1.2.0). It can be used for regression of continuous value of methylation and at present it is used for human methylation.

Installation

Download MRCNN by

https://github.com/TQBio/MRCNN.git

1)Installation has been tested in Linux with Python 2.7.

2)Since the package is written in python 2.7, python 2.7 with the pip tool must be installed first. MRCNN uses the following dependencies: numpy, scipy, pandas, scikit-learn, keras, tensorflow-gpu version>=1.2.0 

You can install these packages first, by the following commands:

  pip install pandas
  
  pip install numpy
  
  pip install scipy
  
  pip install scikit-learn
  
  pip install tensorflow-gpu
  
  pip install keras
  
Run the different functions

Preprocess.py --- For Data pre-processing and extract DNA sequences with corresponding CpG loci.

Model.py --- For contribution of convolutional neural networks, MRCNN gets different structure with CNN.

Run.py --- For training the model and output the predicted values.

Evalution.py --- For evalution of model performances and including regression and classification performances.

Motifs.py --- For obtaining the conventional position weight matrices which can be visualized as sequence logos.

Figure.py --- For drawing the corresponding images to visualize the results.
