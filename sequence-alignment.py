import numpy as np
a='TGTTACGG'
b='GGTTGACTA'
mat=np.zeros((len(a)+1)*(len(b)+1)).reshape((len(b)+1),(len(a)+1))
c=0
def bias(mat):
    if i==j:
        score=mat[c-1,d-1]+3
    else:
        score=mat[c-1,d-1]-3
    return score


def gap(mat):
    gscore=max(mat[c,d-1],mat[c-1,d])-2
    return gscore


for i in b:
    c=c+1
    d=0
    for j in a:
        d=d+1
        mat[c,d]=max(bias(mat),gap(mat),0)
else:
    print(mat)
