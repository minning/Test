# coding:utf-8
'''
    Author:minning
    Date:2017/10/18
    代码目的：merge 的一些特性
    
'''
import pandas as pd
from pandas import DataFrame


# df1=DataFrame({'key':['a','b','b'],'data1':range(3)})
# df2=DataFrame({'key':['a','b','c', 'd'],'data2':range(4)})
# df3 = pd.merge(df1,df2,how='outer')
# print df1
# print df2
# print df3
right=DataFrame({'key1':['foo','foo','bar','bar'],'key2':['one','one','one','two'],'lval':[4,5,6,7]})
left=DataFrame({'key1':['foo','foo','bar'],'key2':['one','two','one'],'lval':[1,2,3]})
print right
print "*"*20
print left
print "*"*20
mer = pd.merge(left,right,on=['key1','key2'],how='inner')  #传出数组
print mer
