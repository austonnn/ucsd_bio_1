# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 14:51:47 2017

@author: xc
"""

#import traceback
#import sys # you must import "sys" to read from STDIN
#text, para = sys.stdin.read().splitlines() # read in the input from STDIN

#raise Exception(para)

def appro_pattern_count1(genome, k, d):
    #words_frequency = {}
    max_count = 0
    ans_list = []
    for index in range(4**k):
        count = 0
        pattern = number_to_pattern(index, k)
        count = appro_pattern_count(genome, pattern, d)
        if count == max_count:
            ans_list.append(number_to_pattern(index, k))
        elif count > max_count:
            max_count = count
            ans_list = []
            ans_list.append(number_to_pattern(index, k))
    #return ans_list
    return ' '.join(ans_list)

def appro_pattern_count(genome, pattern, d):
    count = 0
    for i in range(len(genome) - len(pattern) + 1):
        q = genome[i : i + len(pattern)]
        if hamming_distance(pattern, q) <= d:
            count = count + 1
    return count

def number_to_pattern(index, k):
    to_number_dict = {'A': 0, 'C': 1, 'G': 2, 'T':3}
    to_word_dict = {value: key for key, value in to_number_dict.items()}
    pattern = []
    tmp_number = int(index)
    tmp_k = int(k)
    while tmp_k > 0:
        int_part = tmp_number // 4**(tmp_k - 1)
        tmp_number = tmp_number % 4**(tmp_k - 1)
        tmp_k = tmp_k - 1
        pattern.append(to_word_dict[int_part])    
    return ''.join(pattern)

def hamming_distance(p, q):
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count

def reverse_complement(text):
    reverse_dict = {'A':'T','T':'A', 'C':'G','G':'C'}
    tmp = []
    tmp = [reverse_dict[word] for word in list(text)]        
    tmp.reverse()    
    answer = ''.join(tmp)
    return answer

def appro_pattern_count2(genome, k, d):
    #words_frequency = {}
    max_count = 0
    ans_list = []
    for index in range(4**k // 2):
        count = 0
        pattern = number_to_pattern(index, k)
        rc_pattern = reverse_complement(pattern)
        count += appro_pattern_count(genome, pattern, d)
        count += appro_pattern_count(genome, rc_pattern, d)
        if count == max_count:
            ans_list.append(number_to_pattern(index, k))
        elif count > max_count:
            max_count = count
            ans_list = []
            ans_list.append(number_to_pattern(index, k))
    #return ans_list
    return ' '.join(ans_list)
"""
file = open("dataset_9_7.txt")
text = file.readline()
#print(len(text))
k, d= file.readline().strip().split()
k = int(k)
d = int(d)
file.close()
"""

#print(appro_pattern_count2('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4, 1))


def get_neighbors(text, d):
    neighbors = set([])
    wordlist = ['A', 'T', 'C', 'G']
    tmp_neighbors = []
    tmp_neighbors.append(text)
    len_text = len(text)
    while d > 0:
        tmp_neighbors2 = []
        for item in tmp_neighbors:
            for i in range(len_text):
                for word in wordlist:
                    tmp = list(item)
                    tmp[i] = word                
                    tmp = ''.join(tmp)
                    tmp_neighbors2.append(tmp)
        tmp_neighbors = (tmp_neighbors2)
        neighbors.update(tmp_neighbors2)

        d = d -1
    #return neighbors
    return ' '.join(neighbors)

print(get_neighbors('TATAATCT', 2))
print(len(get_neighbors('TATAATCT', 2).split()))
