'''
Script to plot speedup of gpu vs. jit acceleration
'''

import matplotlib.pyplot as plt

N = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

# Non-Blender Python Speedups:
speedup = [551.282051282051, 574.108818011257, 608.058608058608, 664.884135472371, 823.315118397086, 1010.98901098901, 1309.25925925926, 1784.27787934186, 1978.29716193656, 3200.36101083032]

f = plt.figure()
plt.scatter(N, speedup, marker='x', color='black', zorder=2)
plt.plot(N, speedup, color='lime', zorder=1)
plt.xlabel('N')
plt.ylabel('speedup')
plt.title('cuda vs. jit speedup')
f.savefig("speedup.pdf", bbox_inches='tight')
plt.show()