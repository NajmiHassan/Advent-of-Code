import re 
import numpy as np

iters = 100
w, h = 101, 103

nums = np.array([[int(x) for x in re.findall(r'[-]?\d+', y)] for y in     open('input.txt').read().split('\n')])
p, v = nums[:,:2], nums[:,2:]
mods = p.copy()
mods[:,0], mods[:,1] = w, h

for i in range(iters):
    p = np.remainder(p + v, mods)

print(np.shape(p[(p[:,0] < w//2) & (p[:,1] < h//2),:])[0] * np.shape(p[(p[:,0] < w//2) & (p[:,1] > h//2),:])[0] * np.shape(p[(p[:,0] > w//2) & (p[:,1] < h//2),:])[0]* np.shape(p[(p[:,0] > w//2) & (p[:,1] > h//2),:])[0])