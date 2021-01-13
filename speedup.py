'''
Script to plot speedup of gpu vs. jumba acceleration
'''

import matplotlib.pyplot as plt

N = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

# Speedups:
speedup = [641.091152815013, 609.078747203579, 750.700349956256, 720.990752972258, 1014.01795096322, 1040.41244635193, 1398.7952173913, 1962.20195729538, 2519.40043478262, 3354.75130662021]

f = plt.figure()
plt.scatter(N, speedup, marker='x', color='black', zorder=2)
plt.plot(N, speedup, color='lime', zorder=1)
plt.xlabel('N')
plt.ylabel('speedup')
plt.title('cuda vs. numba speedup')
f.savefig("speedup.pdf", bbox_inches='tight')
plt.show()