# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 20:01:32 2017

@author: xiangyin
"""

#def randomized_motif_search(dna, k, t):


import random

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
            #print(to_number_dict[string[i+j]])
            #print(profile[to_number_dict[string[i + j]]][j])
            tmp_prob = tmp_prob * float(profile[to_number_dict[string[i+j]]][j])
        #print(tmp_prob)
        
        kmer_prob_list.append(tmp_prob)
    #print(kmer_prob_list)
    max_prob = max(kmer_prob_list)
    max_index = kmer_prob_list.index(max_prob)
    return string[max_index: max_index + k]

def get_motifs(profile, dna):
    k = len(profile[0])
    t = len(dna)
    motifs = []    
    for j in range(t):
        motifs.append(profile_most_probable_kmer(dna[j], k, profile))
    return motifs
    
    
def randomized_motif_search(dna, k, t):
    k = int(k)
    t = int(t)
    motifs = []
    num_choice = len(dna[0]) - k + 1
    for item in dna:
        tmp_index = random.randrange(num_choice)
        motifs.append(item[tmp_index: tmp_index + k])
    best_motifs = motifs
    while True:
        profile = laplace_motifs_to_profile(motifs)
        motifs = get_motifs(profile, dna)
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
        else:
            return best_motifs
        
def n_motif_search(n):
    best_motifs = randomized_motif_search(dna, k, t)
    for i in range(n):
        motifs = randomized_motif_search(dna, k, t)
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    return best_motifs
        
        
#import sys # you must import "sys" to read from STDIN
#text, para = sys.stdin.read().splitlines() # read in the input from STDIN
#raise Exception(para)
    
"""
file = open("dataset_161_5.txt")
k, t = file.readline().strip().split()
dna = file.read().splitlines()
file.close()

n = 1000

for item in n_motif_search(n):
    print(item)
    
"""

def profile_randomly_generated_kmer(string, k, profile):
    # Profile-randomly generated k-mer in the i-th sequence

    num_choice = len(string) - k + 1
    # calculate weights list
    to_number_dict = {'A': 0, 'C': 1, 'G': 2, 'T':3}        
    weights_list = []
    for i in range(num_choice):
        tmp_prob = 1
        for j in range(k):      
            #print(profile[to_number_dict[string[i + j]]][j])
            tmp_prob = tmp_prob * float(profile[to_number_dict[string[i+j]]][j])
        weights_list.append(tmp_prob)

    index = random.choices(range(num_choice), weights=weights_list)
    motif = string[index: index + k]    
    return motif
    
def gibbs_sampler(dna, k, t, n):
    
    motifs = []
    best_motifs = []
    num_choice = len(dna[0]) - k + 1
    num_starts = 50
    for i in range(num_starts):
        for item in dna:
            tmp_index = random.randrange(num_choice)
            motifs.append(item[tmp_index: tmp_index + k])
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    best_motifs = motifs
    for j in range(n):
        i = random(t)
        tmp_motifs = list(motifs)
        del tmp_motifs[i]        
        profile = laplace_motifs_to_profile(tmp_motifs)
        # Profile-randomly generated k-mer in the i-th sequence        
        motifs[i] = profile_randomly_generated_kmer(dna[i], k, profile)
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    return best_motifs 
        
        
file = open("dataset_163_4.txt")
k, t, n = file.readline().strip().split()
dna = file.read().splitlines()
file.close()

k = int(k)
t = int(t)
n = int(n)


for item in n_motif_search(n):
    print(item)        
        
        
        
    