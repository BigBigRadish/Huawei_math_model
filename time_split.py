# -*- coding: utf-8 -*-
'''
Created on 2018年9月17日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
#一种基于贪心的生成航班方法
import goto
import pandas as pd
import random
import sys
from goto import with_goto
sys.setrecursionlimit(1000000)
# S1=[]#存储按时间到达停机位的航班
s_time=pd.read_csv('pucks_2_4.csv')
port1=pd.read_csv(r'dataset/Gates.csv')
port=pd.read_csv(r'window.csv')
s1_time=s_time.sort_index(by=['到达序列号'])#按到达顺序排序
s2_time=s_time.sort_index(by=['出发序列号'])#按出发顺序排序
# print(s2_time)
# time_dict=[]
# for i in range(-287,236):
#     list=[]
#     for j in s_time.iterrows():
#         if j[1]['到达序列号']<=i & i<=j[1]['到达序列号']:
#             list.append(j)
#     if len(list)>0:
#         time_dict.append({i:list})  
# print(time_dict)
#给登机口一个初始化开启时间
    
#每个航班可停靠登机口,pk01,pk02
D={}     #初始化每个时刻可使用登机口集合
for i in s1_time['飞机转场记录号']:
    list_D=[]  
    for j in port.iterrows():
        if(str(i)==j[1]['飞机转场记录号']):
            list_D.append(j[1]['登机口'])
    list_D.append('t70')
    list_D=list(set(list_D))
    D.setdefault(str(i),list_D)
#print(D)
G={}#所有停机位初始化时间，包括G1,G2,G3
#port1=pd.read_csv(r'Gates。csv')
print(len(port1['登机口']))
for i in port1['登机口']:
    G.setdefault(str(i),-350)  #默认时间序号最早是-300，19号12点，最晚为+300
G.setdefault('t70',-350)
@with_goto
def init(D,G):
    D1=D
    G1=G
    s=[]
    T=[]
    I=[]
    for t in range(-350,300):#每一个时间片安排需要使用的航班
        for i  in  s1_time.iterrows():
            if(i[1]['到达序列号']==str(t)):
                i1=0
                Di=D1[str(i[1]['飞机转场记录号'])]#获取航班i的可停靠集合
                if len(Di)<1:
                    init(D,G)
                else:
                    if len(Di)>0:
                        bi=random.randint(0,len(Di)-1)
                    else:
                        bi=0    
                        if str(Di[bi])!='t70':
                            if int(i[1]['到达序列号'])>=(int(G1[Di[bi]])+9):
                                #init(D, G)
                                up={Di[bi]:int(i[1]['出发序列号'])}
                                G.update(up)
                                for k,v in D1.items():
                                    v=list(v)
                                    if len(v)==0:
                                        init(D,G)
                                    else:
                                        print(Di[bi]) 
                                        print(v)                      
                                        if str(Di[bi]) in list(v):                             
                                            D1[k].remove(str(Di[bi]))
                                for k1,v1 in D1.items():
                                    if len(v1)==0:
                                        #print(D1)
                                        init(D,G) 
                    T.append(Di[bi])
                    print(bi)   
                    s.append(bi)       
                I.append(i[1]['飞机转场记录号'])
                
        return D1,s,T,I               
                            
if __name__ == '__main__':
    
    file=open('可行解.txt','a')
    _,s,t,I=init(D,G)
    file.write(str(I)+'\n')
    file.write(str(t)+'\n')
    file.write(str(s)+'\n')

#     f=open('initial_1txt','a') 
#     D2=init(D)
#     print(D2)
#     s1_time=s_time.sort_index(by=['到达序列号'])
#     for i in s1_time['飞机转场记录号']:
#         f.write(str(i)+':'+str(D2[i])+'\n')
#     f=open('initial_hangban_fenpei.txt','a') 
#      
#     for i in s1_time['飞机转场记录号']:
#         f.write(i+':'+str(D[i])+'\n')
        
        
        
    #print('123')
    #print(D2)                    
                    
            
        
    
 
        
  

