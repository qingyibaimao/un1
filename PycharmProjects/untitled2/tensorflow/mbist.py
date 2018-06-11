# coding=utf-8
#　数据集识别
'''
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#one_hot 独热编码，也叫一位有效编码。在任意时候只有一位为1，其他位都是0
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

train_images = mnist.train.images
train_labels = mnist.train.labels
test_images = mnist.test.images
test_labels = mnist.test.labels

print("train_images_shape:", train_images.shape)
print("train_labels_shape:", train_labels.shape)
print("test_images_shape:", test_images.shape)
print("test_labels_shape:", test_labels.shape)
print("train_images:", train_images[0])
print("train_images_length:",len(train_images[0]))
print("train_labels:", train_labels[0])
print("train_labels:", train_labels[1])
print("train_labels:", train_labels[2])
print("train_labels:", train_labels[3])
print("train_labels:", train_labels[4])


------------------------================================

import tensorflow as tf
import numpy as np
x = tf.placeholder(tf.float32, shape=(4, 4))
y = tf.add(x, x)
argmax_paramter = tf.Variable([[1,32,44,56],[89,12,90,33],[35,69,1,10]])
argmax_0 = tf.argmax(argmax_paramter, 0) # 最大列索引
argmax_1 = tf.argmax(argmax_paramter, 1) # 最大行索引
#　平均数
reduce_0 = tf.reduce_mean(argmax_paramter, reduction_indices= 0)
reduce_1 = tf.reduce_mean(argmax_paramter, reduction_indices= 1)
# 相等
equal_0 = tf.equal(1,2)
equal_1 = tf.equal(2,2)
# 类型转化
cast_0 = tf.cast(equal_0, tf.int32)
cast_1 = tf.cast(equal_1, tf.float32)

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)

    rand_array = np.random.rand(4,4)
    print("argmax_0", sess.run(argmax_0))
    print("argmax_1", sess.run(argmax_1))
    print("reduce_0", sess.run(reduce_0))
    print("reduce_1", sess.run(reduce_1))
    print("equal_0", sess.run(equal_0))
    print("equal_1", sess.run(equal_1))
    print("cast_0", sess.run(cast_0))
    print("cast_1", sess.run(cast_1))
    print("ergmest", sess.run(argmax_paramter))

=======================================================
# 手写数字识别
import ssl
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
ssl._create_default_https_context = ssl._create_unverified_context
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

batch_size = 100
# 训练的x(image), y(label)
x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])
# 模型权重
w = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
# 使用softmax构建逻辑回归模型
pred = tf.nn.softmax(tf.matmul(x, w) + b)

# 损失函数
cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(pred), 1))

# 低度下降
optimizer = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    #开始训练
    for epoch in range(25):
        avg_cost = 0.
        total_batch = int(mnist.train.num_examples/batch_size)
        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            sess.run(optimizer, {x: batch_xs, y: batch_ys})
            #计算损失平均值
            avg_cost += sess.run(cost, {x: batch_xs, y: batch_ys}) / total_batch
        if (epoch + 1) % 5 == 0:
            print("Epoch:", '%04d' % (epoch+ 1), "cost=", "{:.9f}".format(avg_cost))
    print("运行完成")

    correct = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct, tf.float32))
    print("正确率:", accuracy.eval({x: mnist.test.images, y: mnist.test.labels}))

=================================================================================

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

def init_weights(shape, name):
    return tf.Variable(tf.random_normal(shape, stddev=0.01), name=name)

# This network is the same as the previous one except with an extra hidden layer + dropout
def model(X, w_h, w_h2, w_o, p_keep_input, p_keep_hidden):
    # Add layer name scopes for better graph visualization
    with tf.name_scope("layer1"):
        X = tf.nn.dropout(X, p_keep_input)
        h = tf.nn.relu(tf.matmul(X, w_h))
    with tf.name_scope("layer2"):
        h = tf.nn.dropout(h, p_keep_hidden)
        h2 = tf.nn.relu(tf.matmul(h, w_h2))
    with tf.name_scope("layer3"):
        h2 = tf.nn.dropout(h2, p_keep_hidden)
        return tf.matmul(h2, w_o)

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
trX, trY, teX, teY = mnist.train.images, mnist.train.labels, mnist.test.images, mnist.test.labels
X = tf.placeholder("float", [None, 784], name="X")
Y = tf.placeholder("float", [None, 10], name="Y")

w_h = init_weights([784, 625], "w_h")
w_h2 = init_weights([625, 625], "w_h2")
w_o = init_weights([625, 10], "w_o")

# Add histogram summaries for weights
tf.summary.histogram("w_h_summ", w_h)
tf.summary.histogram("w_h2_summ", w_h2)
tf.summary.histogram("w_o_summ", w_o)

p_keep_input = tf.placeholder("float", name="p_keep_input")
p_keep_hidden = tf.placeholder("float", name="p_keep_hidden")
py_x = model(X, w_h, w_h2, w_o, p_keep_input, p_keep_hidden)

with tf.name_scope("cost"):
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=py_x, labels=Y))
    train_op = tf.train.RMSPropOptimizer(0.001, 0.9).minimize(cost)
    # Add scalar summary for cost
    tf.summary.scalar("cost", cost)

with tf.name_scope("accuracy"):
    correct_pred = tf.equal(tf.argmax(Y, 1), tf.argmax(py_x, 1)) # Count correct predictions
    acc_op = tf.reduce_mean(tf.cast(correct_pred, "float")) # Cast boolean to float to average
    # Add scalar summary for accuracy
    tf.summary.scalar("accuracy", acc_op)

with tf.Session() as sess:
    # create a log writer. run 'tensorboard --logdir=./logs/nn_logs'
    writer = tf.summary.FileWriter("./logs/nn_logs", sess.graph)
    merged = tf.summary.merge_all()

    # you need to initialize all variables
    tf.global_variables_initializer().run()

    for i in range(10):
        for start, end in zip(range(0, len(trX), 128), range(128, len(trX)+1, 128)):
            sess.run(train_op, feed_dict={X: trX[start:end], Y: trY[start:end],
                                          p_keep_input: 0.8, p_keep_hidden: 0.5})
        summary, acc = sess.run([merged, acc_op], feed_dict={X: teX, Y: teY,
                                          p_keep_input: 1.0, p_keep_hidden: 1.0})
        writer.add_summary(summary, i)  # Write summary
        print(i, acc)

'''
import tensorflow as tf

