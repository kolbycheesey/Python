import numpy as np
from timeit import default_timer as timer
from numba import vectorize		##uncomment when testing

@vectorize(["float32(float32,float32)"], target='cuda')		##uncomment when testing
#def VectorAdd(a,b,c):
def VectorAdd(a,b):		##when testing uncomment this line and comment line above
	#for i in range(a.size):
		#c[i] = a[i] + b[i]
	return a + b	##uncomment this line and comment the two above when testing

def main():
	N = 32000000
	
	A = np.ones(N, dtype=np.float32)
	B = np.ones(N, dtype=np.float32)
	C = np.zeros(N, dtype=np.float32)
	
	start = timer()
	#VectorAdd(A,B,C)
	C = VectorAdd(A,B)	##uncomment this line and comment previous line when testing
	vectoradd_time = timer() - start
		
	print("C[:5] = " + str(C[:5]))
	print("C[-5:] = " + str(C[-5:]))
		
	print("VectorAdd took %f seconds" % vectoradd_time)
		
if __name__ == '__main__':
	main()
