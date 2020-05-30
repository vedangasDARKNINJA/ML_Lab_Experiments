import numpy as np
import matplotlib.pyplot as plt

try:
    F = open("data.txt", "r")
except:
    print("Something went wrong while opening the file!")


data = []
for line in F:
    values = []
    temp = list(line.split(' '))
    faulty = False
    for v in temp:
        try:
            values.append(float(v))
        except ValueError:
            print('Unknown character!')
            faulty = True

    if not faulty:
        data.append(values)

F.close()
data = np.array(data)
means = np.mean(data, axis=0)
diff = data - means
print("data:")
print(data)
cov_mat = np.cov(data.T)

e_vals, e_vecs = np.linalg.eig(cov_mat)


e_pair = [(e_vals[i], np.array(e_vecs[i])) for i in range(len(e_vals))]
e_pair.sort(reverse=True)
print("Sorted Pairs: ")
print(*e_pair)


e_vec_sort = []
for i in range(len(e_pair)):
    e_vec_sort.append(np.array(e_pair[i][1]))

e_vec_sort = np.column_stack(e_vec_sort)
pc1 = e_vec_sort[0].T.dot(diff.T)
pc2 = e_vec_sort[1].T.dot(diff.T)
print("PCA: ")
print(np.array([[pc1[i], pc2[i]] for i in range(len(pc1))]))


plt.figure(1)
plt.scatter(data[:, 0], data[:, 1])
plt.title("Original Data")
plt.xlabel("X")
plt.ylabel("Y")

plt.figure(2)
plt.scatter(pc1, pc2)
plt.title("Principle Components")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()
