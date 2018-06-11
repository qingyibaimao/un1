import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
'''

a = tf.add(3,4)
print(a)
sess = tf.Session()
print(sess.run(a))
---------------------------------------------------
matrix1 = tf.constant([[4.,3.]])
matrix2 = tf.constant([[2.], [2.]])
product = tf.matmul(matrix1, matrix2)
sess = tf.Session()
print(sess.run(product))
sess.close()
# 青祜 : 十大汉族古曲 : 《高山流水》《梅花三弄》《夕阳箫鼓》《汉宫秋月》
# 《阳春白雪》《渔樵问答》《胡笳十八拍》《广陵散》《平沙落雁》《十面埋伏》.
------------------------------------------------------------------
a = tf.Variable(tf.constant(0.0), dtype = tf.float32)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(a))
sess.close()
--------------------------------------------------------------------

a = tf.Variable(0, name= 'counter')
new_value = tf.add(a, 2)
update = tf.assign(a, new_value)   #创建一个op,使a + 2

init_op = tf.global_variables_initializer() #启动图,初始化变量

with tf.Session() as sess:
    sess.run(init_op)
    print(sess.run(a))
    for _ in range(3):
        sess.run(update)
        print(sess.run(a))

--------------------------------------------------------------------

a = tf.placeholder("float")  #定义符号变量(占位符)
b = tf.placeholder('float')
y = tf.multiply(a, b)  #创建一个op节点
sess = tf.Session()
print(sess.run(y, feed_dict = {a: 3, b: 3}))
sess.close()

--------------------------------------------------------------------

c = tf.constant([[1.0, 2.0,3.0], [4.0, 5.0, 6.0]])
print(c.get_shape())

---------------------------------------------------------------------
#获取张量形状
import matplotlib.image as mping

filename = "example_image.jpg"
image = mping.imread(filename)
x = tf.Variable(image, name = 'x')
model = tf.global_variables_initializer()

with tf.Session() as session:
    session.run(model)
    result= session.run(x)
    print(x.get_shape())
session.close()

---------------------------------------------------------------------

sess = tf.InteractiveSession()
x = tf.Variable([1.0, 2.0])
a = tf.constant([3.0,3.0])
x.initializer.run()
# sub = tf.subtract(x,a)  # ==> [-2. -1.]减
# sub = tf.add(x,a)  # ==>[4. 5.] 加
# sub = tf.div(x, a) # 除
print(sub.eval())
sess.close()

-----------------------------------------------------------------------------

t1 = [[1,2,3,],[4,5,6]]
t2 = [[7,8,9], [10,11,12]]
#t3 = tf.concat([t1, t2], 0)
t3 = tf.concat([t1,t2], 1)
sess = tf.Session()
arr = sess.run(t3)
print(arr)
----------------------------------------------------------------------------------


a = tf.constant([[2,3,4],[3,4,6]])
result = tf.exp(a)
with tf.Session() as sess:
    s=sess.run(result)
    print(s)
sess.close()

----------------------------------------------------------------
'''
import numpy as np
x_data = np.float32(np.random.rand(2, 100))
y_data = np.dot([0.100, 0.200], x_data) +0.300

b= tf.Variable(tf.zeros([1]))
w = tf.Variable(tf.random_uniform([1,2], -1.0, 1.0))
y = tf.matmul(w, x_data) + b
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()
sess= tf.Session()
sess.run(init)
for step in range(0,201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(w), sess.run(b))