'''
Script to plot speedup of gpu vs. jumba acceleration
'''

import matplotlib.pyplot as plt

N = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

# Speedups:
speedup = [586.095588235294, 614.300992779783, 755.326144366197, 725.14171833481, 1023.42775077331, 1057.20061055386, 1414.16659340659, 1956.97870452529, 2553.82150727193, 3317.18733850129]


f = plt.figure()
plt.scatter(N, speedup, marker='x', color='black', zorder=2)
plt.plot(N, speedup, color='lime', zorder=1)
plt.xlabel('N')
plt.ylabel('speedup')
plt.title('cuda vs. numba speedup')
f.savefig("speedup.pdf", bbox_inches='tight')
plt.show()