#!/usr/bin/env python
# coding: utf-8

# # Pubmed

# In[1]:

import random
import math
import numpy as np
import pandas as pd
import time


# ### Readfile Functions

# In[2]:


#input filename(str)
#output file(list)
def readfile(filename):
    with open(filename) as file_in:
        lines = []
        for line in file_in:
            lines.append(line)
    return lines


# In[3]:


import json
#input file(list)
#output json(list of dic)
def list2json(lines):
    jsons = []
    for i in range(len(lines)):
        tmp = json.loads(lines[i])
        jsons.append(tmp)
    return jsons


# ### Calculus Functions

# In[4]:


# input: article
# output: number
def avg_token(article):
    if len(article)==0:
        return 0
    else:
        s = 0
        for sentence in article:
            token = sentence.split()
            n = len(token)
            s += n
        return s/len(article)


# In[5]:


def total_token(article):
    s = 0
    for sentence in article:
        token = sentence.split()
        n = len(token)
        s += n
    return s


# In[6]:


#input (list of dic)
#output numbers
def min_max_avg(jsons, name, type_no):
    Min = len(jsons[0][name])
    Max = len(jsons[0][name])
    SUM = 0
    numbers = []
    
    for i in range(len(jsons)):
        article = jsons[i][name]
        if type_no == 1:
            N = avg_token(article)
        elif type_no == 2:
            N = total_token(article)
        else:
            N = len(article)
            
        numbers.append(N)
        SUM += N    
        if Min>N:
            Min = N
        if Max<N:
            Max = N
            
    Avg = SUM//len(jsons)

    return (Min, Max, Avg, len(jsons), numbers)


# ### Print Output Functions

# In[7]:


from matplotlib import pyplot as plt

def plot_graph(bin_list, numbers, image_name):
    plt.hist(numbers, bins = bins_list)
    plt.savefig(image_name)
    plt.show()


# In[8]:


def print_result(title, Min, Max, Avg, l):
    #--------------------------------
    print(title)
    print('-------------------------------------------------------------')
    print('Number of articles:'+str(l))
    print('Longest:'+str(Max))
    print('Shortest:'+str(Min))
    print('Average:'+str(Avg))


# In[9]:


def print_out(jsons, name_str, output_str, type_no):
    Min, Max, Avg, l, numbers = min_max_avg(jsons, name_str, type_no)
    print_result(output_str, Min, Max, Avg, l)
    return numbers


# # Test data

# In[10]:


test = readfile('pubmed-dataset/test.txt')
test_jsons= list2json(test)


# ### Test data: number of  sentences in an article

# In[11]:


test_s_numbers = print_out(test_jsons, 'article_text', 'Test Data', 3)


# In[12]:


bins_list = list(range(0,1090,10))
plot_graph(bins_list, test_s_numbers, 'test_s_1.png')

bins_list = list(range(0,300,5))
plot_graph(bins_list, test_s_numbers, 'test_s_2.png')


# ### Test data: number of tokens in a sentence

# In[13]:


test_t1_numbers = print_out(test_jsons, 'article_text', 'Test Data', 1)


# In[14]:


bins_list = list(range(0, 120, 2))
plot_graph(bins_list, test_t1_numbers, 'test_t1_1.png')

bins_list = list(range(10, 60, 1))
plot_graph(bins_list, test_t1_numbers, 'test_t1_2.png')


# ### Test data: number of tokens in an article

# In[15]:


test_t2_numbers = print_out(test_jsons, 'article_text', 'Test Data', 2)


# In[16]:


bins_list = list(range(100,50000,100))
plot_graph(bins_list, test_t2_numbers, 'test_t2_1.png')

bins_list = list(range(0,10000,50))
plot_graph(bins_list, test_t2_numbers, 'test_t2_2.png')


# # Train data

# In[17]:


start = time.time()
#-------------------------------------------------------------------------
train = readfile('pubmed-dataset/train.txt')
train_jsons= list2json(train)
#-------------------------------------------------------------------------
print(time.time()-start)


# ### Train data: number of  sentences in an article

# In[18]:


train_s_numbers = print_out(train_jsons, 'article_text', 'Train Data', 3)


# In[19]:


bins_list = list(range(0,2510,10))
plot_graph(bins_list, train_s_numbers, 'train_s_1.png')

bins_list = list(range(0,500,5))
plot_graph(bins_list, train_s_numbers, 'train_s_2.png')


# ### Train data: number of tokens in a sentence

# In[20]:


train_t1_numbers = print_out(train_jsons, 'article_text', 'Train Data', 1)
bins_list = list(range(0, 300, 2))
plot_graph(bins_list, train_t1_numbers, 'train_t1_1.png')

bins_list = list(range(0, 70, 1))
plot_graph(bins_list, train_t1_numbers, 'train_t1_2.png')


# ### Train data: number of  tokens in an article

# In[21]:


train_t2_numbers = print_out(train_jsons, 'article_text', 'Train Data', 2)


# In[22]:


bins_list = list(range(100,110000,100))
plot_graph(bins_list, train_t2_numbers, 'train_t2_1.png')

bins_list = list(range(0,10000,50))
plot_graph(bins_list, train_t2_numbers, 'train_t2_2.png')


# ### Validation

# In[23]:


start = time.time()
#-------------------------------------------------------------------------
val = readfile('pubmed-dataset/val.txt')
val_jsons= list2json(val)
#-------------------------------------------------------------------------
print(time.time()-start)


# ### Validation data: number of  sentences in an article

# In[24]:


print(len(val_jsons))
val_s_numbers = print_out(val_jsons, 'article_text', 'Validation Data', 3)


# In[25]:


bins_list = list(range(0, 1100, 10))
plot_graph(bins_list, val_s_numbers, 'val_s_1.png')

bins_list = list(range(0, 350, 5))
plot_graph(bins_list, val_s_numbers, 'val_s_2.png')


# ### Validation data: number of tokens in a sentence

# In[26]:


val_t1_numbers = print_out(val_jsons, 'article_text', 'Validation Data', 1)
bins_list = list(range(0, 140, 2))
plot_graph(bins_list, val_t1_numbers, 'val_t1_1.png')

bins_list = list(range(10, 60, 1))
plot_graph(bins_list, val_t1_numbers, 'val_t1_2.png')


# ### Validation data: number of  tokens in an article

# In[27]:


val_t2_numbers = print_out(val_jsons, 'article_text', 'Validation Data', 2)
bins_list = list(range(0,120000,100))
plot_graph(bins_list, val_t2_numbers, 'val_t2_1.png')

bins_list = list(range(0,12500,50))
plot_graph(bins_list, val_t2_numbers, 'val_t2_2.png')


# # Train+Validation+Test

# In[28]:


all_jsons = train_jsons + val_jsons + test_jsons


# ### Number of  sentences in an article

# In[29]:


s_numbers = print_out(all_jsons, 'article_text', 'Validation Data', 3)


# In[30]:


bins_list = list(range(0,2510,10))
plot_graph(bins_list, s_numbers, 's_1.png')

bins_list = list(range(0,300,5))
plot_graph(bins_list, s_numbers, 's_2.png')


# ### Number of tokens in a sentence

# In[31]:


t1_numbers = print_out(all_jsons, 'article_text', 'Validation Data', 1)
bins_list = list(range(0, 280, 2))
plot_graph(bins_list, t1_numbers, 't1_1.png')

bins_list = list(range(0, 60, 1))
plot_graph(bins_list, t1_numbers, 't1_2.png')


# ### Number of  tokens in an article

# In[32]:


t2_numbers = print_out(all_jsons, 'article_text', 'Validation Data', 2)
bins_list = list(range(0,120000,100))
plot_graph(bins_list, t2_numbers, 't2_1.png')

bins_list = list(range(0,10000,50))
plot_graph(bins_list, t2_numbers, 't2_2.png')

