# coding:utf-8
'''
    Author:minning
    Date:2017/11/13
    代码目的：
    
'''

import numpy
# import pandas
import os


# print "hello"
print os.getcwd()  # /home/limingyang/4GRecommend/preprocess
bcpPath = r'/data/marketing/bcp'
folders = os.listdir(bcpPath)
for file in folders:
    print file