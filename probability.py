import numpy as np
# N = 1000000
# M = 10
# heads = np.zeros(M+1)
# for i in range(N):
#     flips = np.random.randint(0,2,M)
#     h,_ = np.bincount(flips, minlength=2)
#     heads[h] += 1
# prob = heads /N
# print(f"Probablilites:{np.array2string(prob)}")
my_list =np.array([0.000965, 0.009717, 0.044338, 0.117143, 0.204977, 0.246173, 0.205204, 0.116795,
 0.043988, 0.009713, 0.000987])
print(np.max(my_list))