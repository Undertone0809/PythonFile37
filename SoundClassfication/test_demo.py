import os
import matplotlib.pyplot as plt
import tensorflow as tf
import random
# tf.set_random_seed(5)
# random.seed(123)
from attention import attention
import numpy as np
import librosa  # pip install librosa
from tqdm import tqdm  # pip install tqdm
import datetime

class Operate:
    def __init__(self):
        super(Operate, self).__init__()
        self.starttime = datetime.datetime.now()


    def run(self):
        # 获得训练用的wav文件路径列表
        self.parent_dir = r"E:\ceydafile\我的比赛\互联网加\测试demo代码"
        # self.sub_dirs=['fold1/','fold2/','fold3/']
        self.sub_dirs = ['test_audio/']#sub.dirs为List类型
        self.wav_files = self.get_wav_files()
        # 获取文件mfcc特征和对应标签
        self.tr_features, self.tr_labels = self.extract_features()

        np.save('tr_features_demo.npy', self.tr_features)
        np.save('tr_labels_demo.npy', self.tr_labels)

        # tr_features=np.load('tr_features.npy',allow_pickle=True)
        # tr_labels=np.load('tr_labels.npy',allow_pickle=True)

        # (batch,step,input)
        # (50,173,40)
        # 这段代码是遍历整个特征，找到最长的特征长度为173，由于音频的长度不同，所有不是每个都是173，所以少的用0填充
        # 计算最长的step
        # wav_max_len = max([len(feature) for feature in tr_features])
        # print("max_len:",wav_max_len)

        # 填充0
        tr_data = []
        for mfccs in self.tr_features:
            while len(mfccs) < int(173):  # 只要小于wav_max_len就补n_inputs个0
                mfccs.append([0] * 40)
            tr_data.append(mfccs)

        tr_data = np.array(tr_data)

        test_x2 = tr_data
        test_y2 = self.tr_labels

        # placeholder
        x = tf.placeholder("float", [None, 173, 40])
        y = tf.placeholder("float", [None])
        dropout = tf.placeholder(tf.float32)
        # learning rate
        lr = tf.Variable(0.005, dtype=tf.float32, trainable=False)

        # 定义RNN网络
        # 初始化权制和偏置
        weights = tf.Variable(tf.truncated_normal([300, 10], stddev=0.1, seed=10))
        biases = tf.Variable(tf.constant(0.1, shape=[10]))

        keep_prob = tf.placeholder(tf.float32, name='keep_prob')

        # LSTM多层网络
        num_layers = 1

        '''--------------------------------------------------------'''

        cell = tf.contrib.rnn.MultiRNNCell([self.grucell() for _ in range(num_layers)])

        outputs, final_state = tf.nn.dynamic_rnn(cell, x, dtype=tf.float32)
        with tf.name_scope('Attention_layer'):
            attention_output, alphas = attention(outputs, 50, return_alphas=True)
        aa = tf.matmul(attention_output, weights) + biases
        # 预测值
        prediction = tf.nn.softmax(aa)  # 0代表3个隐藏层中最接近输出层的一层，2代表最接近输入层的一层

        # labels转one_hot格式
        one_hot_labels = tf.one_hot(indices=tf.cast(y, tf.int32), depth=10)

        # loss
        cross_entropy = tf.reduce_mean(
            tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=one_hot_labels))

        # optimizer
        optimizer = tf.train.AdamOptimizer(learning_rate=lr).minimize(cross_entropy)

        # Evaluate model
        correct_pred = tf.equal(tf.argmax(prediction, 1), tf.argmax(one_hot_labels, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

        init = tf.global_variables_initializer()
        # 定义saver
        saver = tf.train.Saver()
        tf.add_to_collection('pred_network', prediction)

        with tf.Session() as sess:
            sess.run(init)
            new_saver = tf.train.import_meta_graph('sounds_models/model-2500.meta')
            new_saver.restore(sess, 'sounds_models/model-2500')

            # prediction = tf.get_collection('pred_network')[0]

            graph = tf.get_default_graph()

            # input_x = graph.get_operation_by_name('x').outputs[0]
            x = graph.get_tensor_by_name('Placeholder:0')
            y = graph.get_tensor_by_name('Placeholder_1:0')  # 获取输出变量
            keep_prob = graph.get_tensor_by_name('Placeholder_2:0')  # 获取dropout的保留参数
            # keep_prob = graph.get_operation_by_name('keep_prob').outputs[0]

            # print(sess.run(aa, feed_dict={x:test_x,y:test_y,keep_prob:1.0}))
            #    dvector = [[] for _ in range(10)]
            #     for i in range(10):
            #         result=sess.run(aa, feed_dict={x:ln[i],y:le,keep_prob:1.0})
            #         dvector[i] = result.mean(axis=0)
            #         pass
            nn = sess.run(prediction, feed_dict={x: test_x2, y: test_y2, keep_prob: 1.0})

            num = (sess.run(y, feed_dict={x: test_x2, y: test_y2, keep_prob: 1.0}))

            print('真实标签：', int(num))  #################################标签真实值####################################

        ####################################预测值########################################
        self.ans = []
        for i in range(len(tr_data)):
            self.ans.append(np.argmax(nn[i]))
        print('预测标签：', self.ans)

        endtime = datetime.datetime.now()
        print(endtime - self.starttime)


    def get_wav_files(self):
        # 获得训练用的wav文件路径列表
        wav_files = []
        for l, sub_dir in enumerate(self.sub_dirs):
            wav_path = os.path.join(self.parent_dir, sub_dir)
            print("wav_path: ", wav_path)
            for (dirpath, dirnames, filenames) in os.walk(wav_path):
                for filename in filenames:
                    if filename.endswith('.wav') or filename.endswith('.WAV'):
                        filename_path = os.sep.join([dirpath, filename])
                        wav_files.append(filename_path)
        return wav_files

    # 获取文件mfcc特征和对应标签
    def extract_features(self):
        inputs = []
        labels = []

        for wav_file in tqdm(self.wav_files):
            # 读入音频文件
            audio, fs = librosa.load(wav_file)

            # 获取音频mfcc特征
            # [n_steps, n_inputs]#[帧数，特征]
            mfccs = np.transpose(librosa.feature.mfcc(y=audio, sr=fs, n_mfcc=40), [1, 0])
            inputs.append(mfccs.tolist())
            # 获取label
        for wav_file in self.wav_files:
            label = wav_file.split('/')[-1].split('-')[1]
            labels.append(label)
        return inputs, np.array(labels, dtype=np.int)

    def grucell(self):
        cell = tf.contrib.rnn.GRUCell(300)
        # cell = tf.contrib.rnn.LSTMCell(300)
        cell = tf.contrib.rnn.DropoutWrapper(cell, output_keep_prob=dropout)
        return cell
