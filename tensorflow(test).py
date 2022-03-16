# import tensorflow as tf

# 텐서 = tf.constant( [3,4,5] )
# 텐서2 = tf.constant( [6,7,8] )
# print(텐서 * 텐서2)


import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
hallo = tf.constant('why?' )
print(hallo)