import matplotlib.pyplot as plt

fig=plt.figure(figsize=(10,7))
plt.boxplot(([100,97,99,22,1],[1,2,3,4,5,6,7]))
plt.grid()
plt.show()
# fig.savefig("graph.png")