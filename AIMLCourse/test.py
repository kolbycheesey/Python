import pandas as pd
import numpy as np

A='1234567'
#print(A[1::2])
Name = "Michael Jackson"
#print(Name.find('el'))
#print(Name.upper())
#print(Name[-1])

A=((11,12),[21,22])
V={'A','B','C'}
V.add('C')
print(V)

x = 1
y = bool(1)
#if y:
#    print("That worked")
    
y = "6543210".find('1')
#print(y)

name='Lizz'
#print(name[0:2])
#print(name.upper())

var = '01234567'
#print(var[::2])
#print('1'+'2')

A=(0,1,2,3)
#print(A[3])
#print(A[-1])

B=["a", "b", "c"]
#print(B[1:])

S={'a','z','c'}
U={'a','b','c'}
#print(U.union(S))   ##prints S then adds what parts of u are not in s after s

D = {'a':0,'b':1,'c':2}
#print(D.values())
#print(D['b'])



A = ['1','2','3']
#for a in A:
#    print(2*a)


B=["a", "c", "b"]
B.sort()
#print(B)


df=pd.DataFrame({'a':[1,2,1],'b':[1,1,1]}) 
#print(df['a'] == 1)

z = np.array([1,-1])*np.array([1,1])
#print(z)

#print(np.dot(np.array([1,-1]),np.array([1,1]))) 

A = np.array([[1,2],[3,4],[5,6],[7,8]])
B = np.array([[1,2,3],[4,5,6],[7,8,9]])
#np.dot(A,B) 