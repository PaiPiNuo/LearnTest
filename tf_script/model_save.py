#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 12:00:11 2020

@author: caizhi
"""
import tensorflow as tf
step = 1
w1 = tf.Variable(tf.random_normal(shape=[2], name='w1'))
w2 = tf.Variable(tf.random_normal(shape=[5], name='w2'))
#saver = tf.train.Saver()
saver = tf.train.Saver([w1,w2])
sess = tf.Session()
sess.run(tf.global_variables_initializer())
saver.save(sess,'./checkpoint/myModel', global_step=step, write_meta_graph=True)	

print("--------------- Load Graph and Load Weights Bias --------------")
with tf.Session() as sess:
  new_saver = tf.train.import_meta_graph('./checkpoint/myModel-1.meta')
  new_saver.restore(sess,tf.train.latest_checkpoint('./checkpoint'))
  print(sess.run('w1:0'))
