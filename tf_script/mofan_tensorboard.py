import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def add_layer(inputs, in_size, out_size, layer_num, activate_function = None):
    layer_name = 'layer%s'%layer_num	
    with tf.name_scope(layer_name):
	Weights = tf.Variable(tf.random_normal([in_size, out_size]), name='W')
	tf.summary.histogram(layer_name+'weights', Weights)
	biases = tf.Variable(tf.zeros([1, out_size])+0.1, name='b')
	tf.summary.histogram(layer_name+'bias', biases)
	matmul_ = tf.matmul(inputs,Weights) + biases
	if activate_function is None:
	    outputs = matmul_
	else:
	    outputs = activate_function(matmul_)
	return outputs
with tf.name_scope('input'):
    xs = tf.placeholder(tf.float32, [None,1], name='input_x')
    ys = tf.placeholder(tf.float32, [None,1], name='input_y')

layer1 = add_layer(xs, 1, 10, layer_num = 1, activate_function = tf.nn.relu)

prediction = add_layer(layer1, 10, 1, layer_num =2, activate_function=None)
with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),reduction_indices=[1]))
    tf.summary.scalar('loss', loss)
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()

x_data = np.linspace(-1, 1,300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise

with tf.Session() as sess:
    merged = tf.summary.merge_all()
    writer = tf.summary.FileWriter("tensorboard_log/", sess.graph)
    sess.run(init)
    for i in range(1000):
        sess.run(train_step, feed_dict={xs:x_data, ys:y_data})
	if i%50 == 0:
	    result = sess.run(merged, feed_dict={xs:x_data,ys:y_data})
	    writer.add_summary(result, i)
