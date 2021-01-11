'''
Script to plot speedup of gpu vs. jumba acceleration
'''

import matplotlib.pyplot as plt

N = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

# Blender Python Speedups:
speedup = [557.544594594595, 638.088071825566, 715.597431355182, 780.640105078809, 885.64, 1047.09451877428, 1292.40608465608, 1797.50155073106, 2591.39937943262, 3201.45603944125]

f = plt.figure()
plt.scatter(N, speedup, marker='x', color='black', zorder=2)
plt.plot(N, speedup, color='lime', zorder=1)
plt.xlabel('N')
plt.ylabel('speedup')
plt.title('cuda vs. numba speedup')
f.savefig("speedup.pdf", bbox_inches='tight')
plt.show()