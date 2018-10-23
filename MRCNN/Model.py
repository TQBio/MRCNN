#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import gc
import numpy as np
import tensorflow as tf




def weight_variable(shape):  
 initial = tf.truncated_normal(shape, stddev=0.1)   
 return tf.Variable(initial) 
 
 
 
 
 
def bias_variable(shape):  
 initial = tf.constant(0.1, shape=shape) 
 return tf.Variable(initial)  
 
 
 
 
 
def net_MRCNN(x_fs):
 W_conv1 = weight_variable([1, 4, 1, 16])
 b_conv1 = bias_variable([16])
 h_conv1 = tf.nn.conv2d(x_fs, W_conv1, strides=[1,1,4,1], padding='VALID') + b_conv1 
 h_conv1 = tf.reshape(h_conv1, [-1, 20, 20, 16])
 print (h_conv1)

 W_conv2 = weight_variable([3, 3, 16, 32])
 b_conv2 = bias_variable([32])  
 h_conv2 = tf.nn.relu(tf.nn.conv2d(h_conv1, W_conv2, strides=[1,1,1,1], padding='VALID') + b_conv2)
 h_pool2 = tf.nn.max_pool(h_conv2,ksize=[1,3,3,1], strides=[1,3,3,1], padding='VALID')
 print (h_pool2)

 W_conv3 = weight_variable([3, 3, 32, 48])
 b_conv3 = bias_variable([48]) 
 h_conv3 = tf.nn.conv2d(h_pool2, W_conv3, strides=[1,1,1,1], padding='VALID')+ b_conv3  
 W_conv4 = weight_variable([3, 3, 48, 64])
 b_conv4 = bias_variable([64]) 
 h_conv4 = tf.nn.conv2d(h_conv3, W_conv4, strides=[1,1,1,1], padding='VALID')+ b_conv4  

 W_fc1 = weight_variable([2*2*64, 80])  
 b_fc1 = bias_variable([80])  
 h_pool4 = tf.reshape(h_conv4, [-1, 2*2*64])  
 h_fc1 = tf.matmul(h_pool4, W_fc1) + b_fc1
 h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob) 
 print (h_fc1_drop)
 
 W_fc2  = weight_variable([80, 1])  
 b_fc2  = bias_variable([1])  
 y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2
 print (y_conv)
 loss = tf.reduce_mean(tf.square(y - y_conv),reduction_indices=[1])
 train_step = tf.train.AdamOptimizer(1e-3).minimize(loss)
 
 
 return MRCNN 
 
 
 
 

def net_CNN(x_fs):
 W_conv1 = weight_variable([1, 4, 1, 16])
 b_conv1 = bias_variable([16]) 
 h_conv1 = tf.nn.relu(tf.nn.conv2d(x_fs, W_conv1, strides=[1,1,4,1], padding='VALID') + b_conv1) 
 h_pool1 = tf.nn.max_pool(h_conv1,ksize=[1,4,1,1], strides=[1,4,1,1], padding='VALID')
 print h_pool1
 W_conv2 = weight_variable([3, 3, 16, 32]) 
 b_conv2 = bias_variable([32])  
 h_conv2 = tf.nn.relu(tf.nn.conv2d(h_pool1, W_conv2, strides=[1,1,1,1], padding='VALID') + b_conv2)
 h_pool2 = tf.nn.max_pool(h_conv2,ksize=[1,4,4,1], strides=[1,4,4,1], padding='VALID')
 print h_pool2
 W_fc1 = weight_variable([2*2*32, 64])  
 b_fc1 = bias_variable([64])  
 h_pool3 = tf.reshape(h_pool2, [-1, 2*2*32])  
 h_fc1 = tf.nn.elu(tf.matmul(h_pool3, W_fc1) + b_fc1)  
 h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)  
 print h_fc1_drop
 W_fc2  = weight_variable([64, 1])  
 b_fc2  = bias_variable([1])  
 y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2
 print y_conv
 loss = tf.reduce_mean(tf.square(y - y_conv),reduction_indices=[1])
 train_step = tf.train.AdamOptimizer(1e-3).minimize(loss)
 
 return CNN
 
 
 
 