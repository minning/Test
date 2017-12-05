# coding:utf-8
'''
    Author:minning
    Date:2017/11/15
    代码目的：
    
'''
import pickle
import os
import pandas as pd


file_path = "data.pkl"
if os.path.exists(file_path):
    data = pickle.load(open(file_path))  # 反序列话，把数据解析为一个python对象。存进去是dataframe,解析出来还是dataframe
    print data.shape
else:
    data = pd.read_csv("hebei_jf.csv")
    # 中间一系列转换操作
    pickle.dump(data, open(file_path, 'wb'))  # 通过dump把处理好的数据序列化
