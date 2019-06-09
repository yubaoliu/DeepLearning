import numpy as np

def identity_function(x):
    return x

def sigmoid(x):
    return 1/(1+np.exp(-x))

def softmax(x):
    x = x - np.max(x)
    return np.exp(x)/np.sum(np.exp(x))

def cross_entropy_error(y, t):
    #one-hot-vectorの場合、正解ラベルのインデックスに変換
    if t.size == y.size:
        t = t.argmax(axis = 1)

    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7))/batch_size

 
