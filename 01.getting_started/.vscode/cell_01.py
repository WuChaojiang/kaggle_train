# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
msg = "Hell, Kaggle!"
print(msg)


# %%
# initialze variable msg

import numpy as np
import matplotlib.pyplot as plt

# 在指定的间隔内返回均匀间隔的数字（数组）
x = np.linspace(0,20,100)
# plt.plot直接画x和y点
plt.plot(x,np.sin(x), "r+")
plt.show()

msg = "Hello, World! It's a fantastic world and I found something to learn and study for a life time."
print(msg)

n = 50
fibonacci = np.zeros((n))
fibonacci[0] = 0
fibonacci[1] = 1

index = 2
arr = [0, 1]
for index in range(2, n):
    fibonacci[index] = fibonacci[index-1] + fibonacci[index-2]
    arr.append(index)
# plt.plot(range(200), fibonacci)
# plt.show()


# %%


