from collections import deque
from functools import cache
import json
 
 
path = "input.txt"
# path = "test.txt"
 
with open(path) as f:
    buyers = [int(l.strip()) for l in f.readlines()]
    
def mix(secret, n):
    return secret ^ n
 
def prune(secret):
    return secret%16777216
 
def randomize(number):
    secret = number
    
    step_1 = secret * 64
    secret = prune(mix(secret, step_1))
    
    step_2 = secret//32
    secret = prune(mix(secret, step_2))
    
    step_3 = secret * 2048
    secret = prune(mix(secret, step_3))
    
    return secret
 
prices = {}
variations = {}
p1 = []
sequences = {}
for i,b in enumerate(buyers):
    secret = b
    prices[i] = [secret%10]
    variations[i] = [secret%10]
    seen = set()
    for j in range(2000):
        secret = randomize(secret)
        prices[i].append(secret%10)
        variations[i].append(prices[i][-1] - prices[i][-2])
        v = variations[i]
        if j >= 4:
            sequence = str((v[-4], v[-3], v[-2], v[-1]))
            if sequence not in seen:
                sequences[sequence] = sequences.get(sequence, 0) + prices[i][-1]
            seen.add(sequence)
        
    
    p1.append(secret)  
 
sequence = max(sequences, key=sequences.get)
print(f'p2: {sequence} - {sequences[sequence]}')