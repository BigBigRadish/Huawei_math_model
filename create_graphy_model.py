'''
Created on 2018年9月18日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''

import random
import math
import pandas as pd
#import time_split
# s_time=pd.read_csv('../dataset/pucks_2_4.csv')
# port=pd.read_csv('../dataset/可停靠登机口.csv')
# s1_time=s_time.sort_index(by=['到达序列号'])#按到达顺序排序
# s2_time=s_time.sort_index(by=['出发序列号'])#按出发顺序排序
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
# D={}     
# for i in s1_time['飞机转场记录号']:
#     list_D=[]  
#     for j in port.iterrows():
#         if(str(i)==j[1]['飞机转场记录号']):
#             list_D.append(j[1]['登机口'])
#     list_D.append('t70')
#     D.setdefault(str(i),list_D)
#print(D)
############################################贪心算法
import sys
sys.setrecursionlimit(1000000)
# S1=[]#存储按时间到达停机位的航班
s_time=pd.read_csv('pucks_2_4.csv')
port=pd.read_csv('window.csv')
port1=pd.read_csv(r'dataset/Gates.csv')
s1_time=s_time.sort_index(by=['到达序列号'])#按到达顺序排序
s2_time=s_time.sort_index(by=['出发序列号'])#按出发顺序排序
# decode_diction={}  
# import re
# pattern=re.compile(r'[(.*)]')
# for i in f.readlines():
#     print(i)
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

# for k,j in air_no.items():
#     print(k,j)   
#每个航班可停靠登机口,pk01,pk02

def init(D,G):#分配航班模块
    D1=D
    G1=G
    s=[]
    T=[]
    I=[]
    for i  in  s1_time.iterrows():
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
                    if int(i[1]['到达序列号'])>(G1[Di[bi]]+9):
                        #init(D, G)
                        up={Di[bi]:int(i[1]['出发序列号'])}
                        G1.update(up)
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
            s.append(bi)       
        I.append(i[1]['飞机转场记录号'])
        
    return s             
#####################################################################################
# def b2d(b): #将二进制转化为十进制 x∈[0,10]  
#     t = 0  
#     for j in range(len(b)):  
#         t += b[j] * (math.pow(2, j))  
#     t = t * 10 / 1023  
#     return t  
def calfitvalue(objvalue):#转化为适应值，目标函数值越大越好，负值淘汰。  
    fitvalue = []  
    temp = 0.0  
    Cmin = 0;  
    for i in range(len(objvalue)):  
        if(objvalue[i] + Cmin > 0):  
            temp = Cmin + objvalue[i]  
        else:  
            temp = 0.0  
        fitvalue.append(temp)  
    return fitvalue  
 
# def decodechrom(pop): #将种群的二进制基因转化为十进制（0,1023）  
#     temp = [];  
#     for i in range(len(pop)):  
#         t = 0;  
#         for j in range(10):  
#             t += pop[i][j] * (math.pow(2, j))  
#         temp.append(t)  
#     return temp  

 
def calobjvalue(pop,lines): #计算目标函数值  
    #DDD=DD
    file=open('gene_initial.txt','a')
    line=lines
    line1=[]
    temp1 = pop; 
    
    objvalue = [];
    #weight1={}#对于分配到非 临时机位的航班，权重为个体中出现相同分配航站的次数，临时机位取0.5
    #temp1 = decodechrom(pop) 
    k=0 
    for i in temp1:
        i=list(i)
        sum1=0
        temp2=[] 
        temp3=[]
        weight1={}#对于分配到非 临时机位的航班，权重为个体中出现相同分配航站的次数，临时机位取0.5
        print(len(i))
        for j in range(0,len(i)):
           # print(line[j])
           # print((i[j]))
            gene=str(line[j]).strip().split(',')[int(i[j])]
            temp2.append(gene)   
        for var in temp2:
            weight1.update({var:temp2.count(var)})
            #print(weight1)  
            
        for k1,v in weight1.items():
            if(k1!='t70'):
                sum1=+ v*v
            else :
                sum1=+v
           
                            
        file.write('第'+str(k)+'个体：：'+str(temp2)+'\n')
        file.write('第'+str(k)+'次航班分配情况:'+str(weight1)+'\n')    
        objvalue.append(sum1) 
        k+=1
    #print(objvalue) 
    return objvalue #目标函数值objvalue[m] 与个体基因 pop[m] 对应   
def best(pop, fitvalue): #找出适应函数值中最大值，和对应的个体  
    px = len(pop)  
    bestindividual = []  
    bestfit = fitvalue[0]  
    for i in range(1,px):  
        if(fitvalue[i] > bestfit):  
            bestfit = fitvalue[i]  
            bestindividual = pop[i]  
    return [bestindividual, bestfit]  
  
  
def sum(fitvalue):  
    total = 0  
    for i in range(len(fitvalue)):  
        total += fitvalue[i]  
    return total  
  
def cumsum(fitvalue):  
    for i in range(len(fitvalue)):  
        t = 0;  
        j = 0;  
        while(j <= i):  
            t += fitvalue[j]  
            j = j + 1  
        fitvalue[i] = t;  
  
def selection(pop, fitvalue): #自然选择（轮盘赌算法）  
    newfitvalue = []  
    totalfit = sum(fitvalue)  
    for i in range(len(fitvalue)):
        if(fitvalue[i]==0):
            newfitvalue.append(0)
        else:
            newfitvalue.append(fitvalue[i]/ totalfit)  
    cumsum(newfitvalue)  
    ms = [];  
    poplen = len(pop)  
    for i in range(poplen):  
        ms.append(init(D,G)) #random float list ms  
#     ms.sort()  
    fitin = 0  
    newin = 0  
    newpop = pop  
    while newin < poplen:  
        if(ms[newin]< newfitvalue[fitin]):  
            newpop[newin] = pop[fitin]  
            newin = newin + 1  
        else:  
            fitin = fitin + 1  
    pop = newpop  
   
def crossover(pop, pc): #个体间交叉，实现基因交换  
    poplen = len(pop)  
    for i in range(poplen - 1):  
        if(random.random() < pc):  
            cpoint = random.randint(0,len(pop[0]))  
            temp1 = []  
            temp2 = []  
            temp1.extend(pop[i][0 : cpoint])  
            temp1.extend(pop[i+1][cpoint : len(pop[i])])  
            temp2.extend(pop[i+1][0 : cpoint])  
            temp2.extend(pop[i][cpoint : len(pop[i])])  
            pop[i] = temp1  
            pop[i+1] = temp2  
  
def mutation(pop, pm): #基因突变  
    px = len(pop)  
    py = len(pop[0])  
      
    for i in range(px):  
        if(random.random() < pm):  
            mpoint = random.randint(0,py-1)  
            if(pop[i][mpoint] == 1):  
                pop[i][mpoint] = 0  
            else:  
                pop[i][mpoint] = 1
if __name__ == '__main__':
    file=open('initial_hangban_fenpei_2.csv','r')
    lines=file.readlines()
    D={}     
    for i in s1_time['飞机转场记录号']:
        list_D=[]  
        for j in port.iterrows():
            if(str(i)==j[1]['飞机转场记录号']):
                list_D.append(j[1]['登机口'])
        list_D.append('t70')
        D.setdefault(str(i),list_D)
    #print(D)
    G={}#所有停机位初始化时间，包括G1,G2,G3
    #port1=pd.read_csv(r'Gates。csv')
    #print(len(port1['登机口']))
    for i in port1['登机口']:
        G.setdefault(str(i),-350)  
    G.setdefault('t70',-350)
#     DD={}
#     k=0     
#     for i in s1_time['飞机转场记录号']:
#         list_DD=[]  
#         for j in port.iterrows():
#             if(str(i)==j[1]['飞机转场记录号']):
#                 list_DD.append(j[1]['登机口'])
#         list_DD.append('t70')
#         DD.setdefault(str(k),list_DD)
#         k+=1
#     print(DD)
        
#     for i in s1_time['']
#     air_no={}
#     j1=0
#     for i1 in s1_time['飞机转场记录号']:
#         air_no.update({j1:str(i1)})#创建一个映射表
#         j1+=1
#     #D=D    
    popsize = 50 #种群的大小  
    #用遗传算法求解f题：  
    #min(停机位)   
    chromlength = 250 #基因片段的长度  
    pc = 0.6 #两个个体交叉的概率  
    pm = 0.001; #基因突变的概率  
    results = [[]]  
    bestindividual = []  
    bestfit = 0  
    fitvalue = []  
    tempop = [[]] 
    pop=[]
    for i in range(popsize):
        pop.append(init(D,G))#生成大小为50的种群
    print(len(pop))
    for i in range(50): #繁殖100代  
        objvalue = calobjvalue(pop,lines) #计算目标函数值  
        fitvalue = calfitvalue(objvalue); #计算个体的适应值  
        [bestindividual, bestfit] = best(pop, fitvalue) #选出最好的个体和最好的函数值  
        results.append([bestfit,bestindividual]) #每次繁殖，将最好的结果记录下来  
        #selection(pop, fitvalue) #自然选择，淘汰掉一部分适应性低的个体  
#         crossover(pop, pc) #交叉繁殖  
#         mutation(pop, pc) #基因突变  
          
      
    results.sort()    
    print(results[-1]) #打印函数最大值和对应的  