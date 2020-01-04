import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf
import numpy as np

'''matrix1 = tf.constant([[3,3]])
matrix2 = tf.constant([[2],
                       [2]])
print("matrix1.shape():", matrix1.shape.as_list())
print("matrix2.shape():", matrix2.get_shape().as_list())
product = tf.matmul(matrix1, matrix2)
print("product.shape():", product.shape.as_list())
with tf.Session() as sess:
  result = sess.run(product)
  print("result:",result)'''



state = tf.Variable(0, name='counter')
one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state,new_value)
init = tf.global_variables_initializer()

with tf.Session() as sess:
  sess.run(init)
  for i in range(3):
	  sess.run(update)
	  print(sess.run(state))
  

