import matplotlib.pyplot as plt

x = [3, 8, 5]
y = [7, 4, 9]

plt.plot(x, y, color='b', label='graf 1', marker='<', ms=5)
plt.plot(y, x, color='r', label='graf 2', marker='o', ms=15)
plt.xlabel('Name x')
plt.ylabel('Name y')
plt.legend()
plt.title('graf')
plt.grid()
plt.show()
plt.savefig('fig_2.png')