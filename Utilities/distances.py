from math import sqrt
def euclidean(x,y):
    s=0
    for i in range(len(x)):
        s+=(x[i]-y[i])**2
    return sqrt(s)
def manhattan(x,y):
    s=0
    for i in range(len(x)):
        s+=(x[i]-y[i])**2
    return s
def minkowski(x,y,n=3):
    s=0
    for i in range(len(x)):
        s+=(x[i]-y[i])**n
    return s**(1/n)
def dot(x,y):
    s=0
    for i in range(len(x)):
        s+=x[i]*y[i]
    return s
def cosine(x,y):
    return ((dot(x,y))/(sqrt(dot(x,x))*sqrt(dot(y,y))))
