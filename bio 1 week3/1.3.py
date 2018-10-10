# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 16:36:39 2017

@author: xc
"""
#import traceback
#import sys # you must import "sys" to read from STDIN
#text, para = sys.stdin.read().splitlines() # read in the input from STDIN

#raise Exception(para)
def appro_pattern_count(genome, pattern, d):
    count = 0
    for i in range(len(genome) - len(pattern) + 1):
        q = genome[i : i + len(pattern)]
        if hamming_distance(pattern, q) <= d:
            count = count + 1
    return count

def hamming_distance(p, q):
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count

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
    return neighbors
    
    
def motif_enumation(dna, k, d):
    k = int(k)
    d = int(d)
    patterns = set([])
    for i in range(len(dna[0]) - k + 1):
        pattern = dna[0][i: i+k]
        tmp_patterns = get_neighbors(pattern, d)
        if d == 0:
            tmp_patterns = []
            tmp_patterns.append(pattern)
        for tmp_pat in tmp_patterns:
            #print(tmp_pat)
            flag = True
            for item in dna:
                if appro_pattern_count(item, tmp_pat, d) == 0:
                    flag = False
                    break            
            if flag == True:
                patterns.add(tmp_pat)
    return patterns
                
            
file = open("dataset_156_8.txt")
k, d = file.readline().split()
dna = file.read().splitlines()
file.close()

#print(motif_enumation(dna, k, d)) 

print(' '.join(motif_enumation(dna, k, d)))        
                
                
                
                
                