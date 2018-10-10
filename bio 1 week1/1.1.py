# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 12:24:29 2017

@author: xc
"""
"""
import sys # you must import "sys" to read from STDIN
text, k = sys.stdin.read().splitlines() # read in the input from STDIN
"""



def pattern_count(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i: i + len(pattern)] == pattern:
            count = count + 1
    return count



#text = 'CTGTTTTTGATCCATGATATGTTATCTCTCCGTCATCAGAAGAACAGTGACGGATCGCCCTCTCTCTTGGTCAGGCGACCGTTTGCCATAATGCCCATGCTTTCCAGCCAGCTCTCAAACTCCGGTGACTCGCGCAGGTTGAGTA'
#pattern = 'CTC'

"""
file = open("dataset_2_7.txt")

text = file.readline()
#print(len(text))
pattern = file.readline().strip()
file.close()

print(pattern)
print(len(pattern))
print(pattern_count(text, pattern))
"""

def frequent_words(text, k):
    k = int(k)
    frequent_patterns = set()
    count = []
    for i in range(len(text) - k + 1):
        count.append(0)
        pattern = text[i:i + k]
        count[i] = pattern_count(text, pattern)
    max_count = max(count)
    for i in range(len(text) - k + 1):
        if count[i] == max_count:
            frequent_patterns.add(text[i:i + k])
        set(frequent_patterns)
    return frequent_patterns

def frequent_words1(text, k):
    k = int(k)
    words_frequency = dict()
    for i in range(len(text) - k + 1):
        #count.append(0)
        pattern = text[i:i + k]
        if pattern in words_frequency:
            words_frequency[pattern] += 1
        else:
            words_frequency[pattern] = 1
        #count[i] = pattern_count(text, pattern)
    max_count = max(words_frequency.values())
    frequent_patterns = []
    for item in words_frequency.items():
        if item[1] == max_count:
            frequent_patterns.append(item[0])
    return frequent_patterns

def frequent_words2(text, k, t):
    k = int(k)
    words_frequency = dict()
    for i in range(len(text) - k + 1):
        #count.append(0)
        pattern = text[i:i + k]
        if pattern in words_frequency:
            words_frequency[pattern] += 1
        else:
            words_frequency[pattern] = 1
        #count[i] = pattern_count(text, pattern)
    #max_count = max(words_frequency.values())
    frequent_patterns = []
    for item in words_frequency.items():
        if item[1] >= int(t):
            frequent_patterns.append(item[0])
    return frequent_patterns


#text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
#k = 4
"""   
file = open("dataset_2_10.txt")
text = file.readline()
#print(len(text))
k = file.readline().strip()
file.close()

feq_pattern_list = frequent_words1(text, k)
for pattern in feq_pattern_list:
    print(pattern)
"""

def reverse_complement(text):
    reverse_dict = {'A':'T','T':'A', 'C':'G','G':'C'}
    tmp = []
    tmp = [reverse_dict[word] for word in list(text)]        
    tmp.reverse()    
    answer = ''.join(tmp)

    return answer

"""
file = open("dataset_3_2.txt")
text = file.readline().strip()
file.close()

text = 'AAAACCCGGT'
answer = reverse_complement(text)

print(answer)
"""

def pattern_matching(text, pattern):
    tmp = ''
    tmp1 = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            tmp += str(i)+ ' '
            tmp1.append(i)
            #print(i + 1,end=' ')
    return tmp1

"""
pattern = 'ATAT'
text = 'ATATATGCATATACTT'


file = open("Vibrio_cholerae.txt")
text = file.readline().strip()
#pattern = file.readline().strip()
file.close()

pattern = 'CTTGATCAT'
print(pattern_matching(text, pattern))
"""

def clump_finding(genome, k, t, l):
    ans = []
    t = int(t)
    l = int(l)
    k = int(k)
    frequent_patterns = frequent_words2(genome, k, t)
    for pattern in frequent_patterns:
        matched_pattern = pattern_matching(genome, pattern)
        #print(matched_pattern)
        for i in range(len(matched_pattern) - t + 1):
            if matched_pattern[i] + l > matched_pattern[i + t -1] + k -1:
                ans.append(pattern)
                break  
    return(ans)
  
    
def pattern_to_number(pattern):
    to_number_dict = {'A': 0, 'C': 1, 'G': 2, 'T':3}
    pattern = list(pattern)
    pattern.reverse()
    number = 0
    for i in range(len(pattern)):
        number += to_number_dict[pattern[i]] * 4 ** i    
    return number

def pattern_to_number1(pattern):
    symbol_to_number = {'A': 0, 'C': 1, 'G': 2, 'T':3}
    if len(pattern) == 0:
        return 0
    symbol = pattern[-1]
    prefix = pattern[0:-1]
    return 4 * pattern_to_number1(prefix) + symbol_to_number[symbol]
    
#print(pattern_to_number('AATTTAGCCGTGCAGAGGT'))
#print(pattern_to_number1('AATTTAGCCGTGCAGAGGT'))
    
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

def number_to_pattern1(index, k):
    to_number_dict = {'A': 0, 'C': 1, 'G': 2, 'T':3}
    number_to_symbol = {value: key for key, value in to_number_dict.items()}
    if k == 1:
        return number_to_symbol[index]
    prefix_index = index // 4
    r = index % 4
    symbol = number_to_symbol[r]
    prefix_pattern = number_to_pattern(prefix_index, k - 1)
    return prefix_pattern + symbol
 
print(number_to_pattern(16950989355,19))    
print(number_to_pattern1(16950989355,19)) 
    

def computing_frequencies(text, k):
    frequency_array = [0 for i in range(4**k - 1 + 1)]
    for i in range(len(text) - k + 1):
        pattern = text[i: i + k]
        j = pattern_to_number(pattern)
        frequency_array[j] += 1
    #return frequency_array
    return ' '.join([str(number) for number in frequency_array])

#print(computing_frequencies('ACGCGGCTCTGAAA', 2))
    
def clump_finding2(genome, k, t, l):
    ans = []
    t = int(t)
    l = int(l)
    k = int(k)
    frequent_patterns = frequent_words3(genome, k, t)
    for pattern in frequent_patterns:
        matched_pattern = pattern_matching(genome, pattern)
        #print(matched_pattern)
        for i in range(len(matched_pattern) - t + 1):
            if matched_pattern[i] + l > matched_pattern[i + t -1] + k -1:
                ans.append(pattern)
                break  
    return(ans)
    
def clump_finding2(genome, k, t, l):
    k = int(k)
    words_frequency = {}
    words_position = {}
    for i in range(len(genome) - k + 1):
        #count.append(0)
        pattern = genome[i:i + k]
        index = pattern_to_number(pattern)
        if index in words_frequency:
            words_frequency[index] += 1
            words_position[index].append(i)
        else:
            words_frequency[index] = 1
            words_position[index] = []
            words_position[index].append(i)
        #count[i] = pattern_count(text, pattern)
    #max_count = max(words_frequency.values())
    count = 0
    for key, value in words_frequency.items():
        if value >= int(t):
            matched_position = words_position[key]
            for i in range(len(matched_position) - t + 1):
                if matched_position[i] + l > matched_position[i + t -1] + k -1:
                    count += 1
                    break             
    return count
#print(number_to_pattern(5437, 7))
"""    
genome = 'CCACGCGGTGTACGCTGCAAAAAGCCTTGCTGAATCAAATAAGGTTCCAGCACATCCTCAATGGTTTCACGTTCTTCGCCAATGGCTGCCGCCAGGTTATCCAGACCTACAGGTCCACCAAAGAACTTATCGATTACCGCCAGCAACAATTTGCGGTCCATATAATCGAAACCTTCAGCATCGACATTCAACATATCCAGCG'
para = '3 25 3'
k, l, t = para.split()
#print(frequent_words2(text, k, t))
"""

"""
#file = open("dataset_4_5.txt")
file = open("E_coli.txt")
genome = file.readline().strip()
#para = file.readline().strip()
#k, l, t = para.split()
k = 9
l = 500
t = 3


#print(len(text))
#genome, k, l, t = file.readline().strip()
#file.close()


ans = clump_finding2(genome, k, t, l)
#print(' '.join(ans))
print(ans)
"""
