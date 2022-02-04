import os
import tensorflow as tf
import time
import numpy as np

from utils import DKT
from load_data import DKTData
from load_data import OriginalInputProcessor

import matplotlib.pyplot as plt


'''
dataset = 'errex'
if dataset == 'errex':
    train_path = '/home/thales/deep-knowledge-tracing-plus/data/errex/preprocessed_errex_data.csv'
    test_path = '/home/thales/deep-knowledge-tracing-plus/data/errex/preprocessed_errex_data.csv'
    save_dir_prefix = '/home/thales/deep-knowledge-tracing-plus/data/errex/'


rnn_cells = {
    "LSTM": tf.contrib.rnn.LSTMCell,
    "GRU": tf.contrib.rnn.GRUCell,
    "BasicRNN": tf.contrib.rnn.BasicRNNCell,
    "LayerNormBasicLSTM": tf.contrib.rnn.LayerNormBasicLSTMCell,
}

# train_path = os.path.join('./data/', 'skill_id_train.csv')
# test_path = os.path.join('./data/', 'skill_id_test.csv')

network_config = {}
network_config['batch_size'] = 32
network_config['hidden_layer_structure'] = [200]
network_config['learning_rate'] = 0.01
network_config['keep_prob'] = 0.333
network_config['rnn_cell'] = rnn_cells["LSTM"]

network_config['lambda_o'] = 0.1
network_config['lambda_w1'] = 0.003
network_config['lambda_w2'] = 3.0

# save_dir_prefix = 'checkpoints/n200.lo0.1.lw10.03.lw230.0'

num_runs = 1
num_epochs = 1
batch_size = 32
keep_prob = 0.333

tf.reset_default_graph()

'''


problem_seq= [55, 45, 55, 55, 55, 45, 98, 98, 98, 33, 32, 33, 32, 33, 32, 33, 32, 32, 33, 32, 33, 32, 33, 32, 33, 33, 32, 33, 32, 32, 33, 32, 33, 33, 32, 32, 33, 33, 32, 33, 32, 33, 32, 33, 32, 33, 33]
correct_seq = [1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1]

input_processor = OriginalInputProcessor()
result = input_processor.process_problems_and_corrects(problem_seq,correct_seq,150,is_train=False)

print(result)