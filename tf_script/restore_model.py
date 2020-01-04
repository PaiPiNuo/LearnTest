import tensorflow as tf

w1 = tf.placeholder("float",name="w1")
w2 = tf.placeholder("float",name="w2")
b1 = tf.Variable(2.0,name="bias")

with tf.device('/gpu:0'):
  add_ = tf.add(w1,w2)
  mul_ = tf.multiply(add_,b1,name="op_to_restore")
with tf.Session() as sess:
  sess.run(tf.global_variables_initializer())
  saver = tf.train.Saver()
  print(sess.run(mul_,feed_dict={w1:4,w2:8}))
  saver.save(sess,'./checkpoint_restore/myModel',global_step=1000)
