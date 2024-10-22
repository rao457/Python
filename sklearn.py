# # # import numpy as np
# # # import matplotlib.pyplot as plt
# # # x = np.random.random(100)
# # # plt.plot(x)
# # # plt.show()
# # import numpy  as np
# # from mpl_toolkits.mplot3d import Axes3D
# # import matplotlib.pylab as plt
# # x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
# # y =  np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
# # z = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
# # fig  = plt.figure()
# # ax = fig.add_subplot(111, projection='3d')
# # ax.scatter(x,y,z)
# # plt.show()
# import pprint
# import numpy as np
# a = np.random.randint(0, 5, (3, 4))
# # pprint.PrettyPrinter().pprint(a)
# np.save("myfile.npy", a)
# b = np.load("myfile.npy")
# print(b)
