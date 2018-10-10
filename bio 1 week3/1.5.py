# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 17:08:24 2017

@author: xc
"""
#import sys # you must import "sys" to read from STDIN
#text, para = sys.stdin.read().splitlines() # read in the input from STDIN
#raise Exception(para)

"""
file = open("dataset_159_3.txt")
string = file.readline().strip()
k = file.readline().strip()

profile = file.read().splitlines()

file.close()

k = int(k)
tmp_profile = []
for item in profile:
    tmp_profile.append(item.split())
    
profile = tmp_profile
"""

def hamming_distance(p, q):
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count

def key_with_maxval(d):
    """ a) create a list of the dict's keys and values; 
        b) return the key with the max value"""  
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]
 
def find_consensus(motifs):
    consensus = ''
    for i in range(len(motifs[0])):
        #tmp_freq = {'A':0, 'T':0, 'C':0, 'G':0}
        tmp_freq = {'A': 0, 'C': 0, 'G': 0, 'T':0} 
        for motif in motifs:
            tmp_freq[motif[i]] += 1
        consensus += key_with_maxval(tmp_freq)
    return consensus

def score(motifs):
    consensus = find_consensus(motifs)
    score = 0
    for motif in motifs:
        score += hamming_distance(consensus, motif)    
    return score


def profile_most_probable_kmer(string, k, profile):
    to_number_dict = {'A': 0, 'C': 1, 'G': 2, 'T':3}        
    kmer_prob_list = []
    for i in range(len(string) - k + 1):
        tmp_prob = 1
        for j in range(k):      
            #print(profile[to_number_dict[string[i + j]]][j])
            tmp_prob = tmp_prob * float(profile[to_number_dict[string[i+j]]][j])
        #print(tmp_prob)
        
        kmer_prob_list.append(tmp_prob)
    #print(kmer_prob_list)
    max_prob = max(kmer_prob_list)
    max_index = kmer_prob_list.index(max_prob)
    return string[max_index: max_index + k]

#profile[0].split()  
    
#print(profile_most_probable_kmer(string, k, profile))


def motifs_to_profile(motifs):
    k = len(motifs[0])
    t = len(motifs)
    profile = []
    for i in range(4):
        profile.append([])
    for i in range(k):
        tmp_freq = {'A':0, 'C':0, 'G':0, 'T':0}
        for motif in motifs:
            tmp_freq[motif[i]] += 1 / t
        for index, key in enumerate(tmp_freq.keys()):
            profile[index].append(tmp_freq[key])    
    return profile

def laplace_motifs_to_profile(motifs):
    k = len(motifs[0])
    t = len(motifs)
    profile = []
    for i in range(4):
        profile.append([])
    for i in range(k):
        laplace_tmp_freq = {'A':1, 'C':1, 'G':1, 'T':1}
        #tmp_freq = {'A':0, 'C':0, 'G':0, 'T':0}
        for motif in motifs:
            laplace_tmp_freq[motif[i]] += 1 / t
        for index, key in enumerate(laplace_tmp_freq.keys()):
            profile[index].append(laplace_tmp_freq[key])    
    return profile

def greedy_motif_search(dna, k, t):
    k = int(k)
    t = int(t)
    best_motifs = []
    for item in dna:
        best_motifs.append(item[0:k])
    for i in range(len(dna[0]) - k + 1):
        tmp_motifs = []
        tmp_motifs.append(dna[0][i: i+k])
        for j in range(1, t):
            profile = laplace_motifs_to_profile(tmp_motifs)
            tmp_motifs.append(profile_most_probable_kmer(dna[j], k, profile))
        if score(tmp_motifs) < score(best_motifs):
            best_motifs = tmp_motifs
        #for i in range(1, t):
    return best_motifs




"""
dna = ['GCCCAA',
'GGCCTG',
'AACCTA',
'TTCCTT']
k = 3
t = 4
"""


file = open("dataset_160_9.txt")
k, t = file.readline().strip().split()
dna = file.read().splitlines()
file.close()

for item in greedy_motif_search(dna, k, t):
    print(item)
    
#print(greedy_motif_search(dna, k, t))
