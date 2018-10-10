# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 10:04:12 2017

@author: xc
"""

#import traceback
#import sys # you must import "sys" to read from STDIN
#text, para = sys.stdin.read().splitlines() # read in the input from STDIN
#raise Exception(para)

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


import math
def score_entropy(motifs):
    score = 0
    #tmp_freq = {'A':0, 'T':0, 'C':0, 'G':0}
    for i in range(len(motifs[0])):
        tmp_freq = {'A':0, 'T':0, 'C':0, 'G':0}
        for motif in motifs:
            tmp_freq[motif[i]] += 1
        print(tmp_freq)
        for value in tmp_freq.values():
            if value != 0:
                p = value / len(motifs)
                score += p * math.log2(p)
    return -score

def median_string(dna, k):
    k = int(k)
    dist = float("inf")
    patterns = []
    for index in range(4 ** k):
        patterns.append(number_to_pattern(index, k))
    #print(len(patterns))
    for pattern in patterns:
        tmp_dist = dna_dist(pattern, dna)
        if dist > tmp_dist:
            dist = tmp_dist
            median = pattern
    return median

def text_dist(pattern, text):
    distance = float("inf")
    motif =''
    for i in range(len(text) - len(pattern) + 1):
        q = text[i: i+len(pattern)]
        tmp_dis = hamming_distance(pattern, q)
        if tmp_dis < distance:
            distance = tmp_dis
            motif = q
    #return motif
    return distance

def dna_dist(pattern, dna):
    distance = float("inf")
    motif =''
    tmp_dist = 0
    for text in dna:
        #q = text[i: i+len(pattern)]
        tmp_dist += text_dist(pattern, text)
    if tmp_dist < distance:
        distance = tmp_dist
           # motif = q
    #return motif
    return distance
    
def distance_pattern_string(pattern, dna):
    k = len(pattern)
    distance = 0
    for text in dna:
        hamming_dist = math.inf
        #
        for i in range(len(text) - k + 1):
            tmp_pattern = text[i: i + k]
            #print(tmp_pattern)
            if hamming_dist > hamming_distance(pattern, tmp_pattern):
                #print(hamming_distance(pattern, tmp_pattern))
                   
                hamming_dist = hamming_distance(pattern, tmp_pattern)
                #print(tmp_pattern)
                #print(hamming_dist)
                
                #print(hamming_distance(pattern, tmp_pattern))
        distance = distance + hamming_dist
    return distance


motifs = [
"TCGGGGGTTTTT",
"CCGGTGACTTAC",
"ACGGGGATTTTC",
"TTGGGGACTTTT",
"AAGGGGACTTCC",
"TTGGGGACTTCC",
"TCGGGGATTCAT",
"TCGGGGATTCCT",
"TAGGGGAACTAC",
"TCGGGTATAACC"
]
#print(score(motifs))

"""

file = open("dataset_158_9.txt")
k = file.readline()
dna = file.read().splitlines()
file.close()

print(median_string(dna, k))       

"""
"""
file = open("dataset_5164_1.txt")
pattern = file.readline().strip()
dna = file.read().split()
file.close()

print(distance_pattern_string(pattern, dna))   
""" 