import numpy as np
import pandas as pd
def box(sample):
    flag = False
    s = 0
    for i in sample:
        for k in i:
            s = s + k
            if k <= 0 or k >= 10:
                flag = True
    if s != 45:
        flag = True
    return flag
def roworcol(t):
    flag = False
    for i, j in t:
        s = 0
        for k in j:
            s = s + k
            if k <= 0 or k >= 10:
                flag = True
        if s != 45:
            flag = True
    return flag
    
l = [[]]
l = eval(input('Enter elements:'))
arr = np.array(l, dtype = np.int32)
df = pd.DataFrame(l)
x, y, z = np.hsplit(arr, 3)
a, b, c = np.vsplit(x, 3)
d, e, f = np.vsplit(y, 3)
g, h, i = np.vsplit(z, 3)
if roworcol(df.iteritems()) or roworcol(df.iterrows()):
    print('invalid')
elif box(a) or box(b) or box(c) or box(d) or box(e) or box(f) or box(g) or box(h) or box(i):
    print('invalid')
else:
    print('valid')