import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap
import sklearn
import math 
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.model_selection import train_test_split
import collections

# 设置参数
print("输入一个点：")
a,b=map(float,input().split())



# 读入数据
column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
data = np.array(pd.read_csv('D:\cs\EAIcourse\\03KNN/Boston.csv', index_col=0))
X = data[: , [2, 5]]    #取了第二行和第五行
y = data[: , 13]

# 选定K值
n_neighbors = 21 # 改成了奇数

#设置标签
def make_label(input):
    if input < 10.0:
        return 0
    elif input < 20:
        return 1
    elif input < 30:
        return 2
    else:
        return 3
# change the `MEDV` column data into label
vfunc = np.vectorize(make_label)
label = vfunc(y)

# 把标签和数据合并
label=np.array(label).transpose()
Z=np.c_[X,label]

# 选一个点，输入坐标
test_input_to_predict = np.array([a,b]) # define a point to predict

# 输出他的label
neighbor_list = sorted(Z, key=lambda x :abs(x[0]-test_input_to_predict[0])+abs(x[1]-test_input_to_predict[1])) # write your own key function to find test input's neighbors
#用的是曼哈顿距离
# n_neighbors就是k值
K_nearest_neighbors = neighbor_list[: n_neighbors]  # 按距离排序后选前K个
for i in range(len(K_nearest_neighbors)):
    K_nearest_neighbors[i]=K_nearest_neighbors[i][2]
counter = collections.Counter(K_nearest_neighbors)  # 在前K个里面投票
res=counter.most_common(1)[0][0]
print(res)     #选票数最多的


# 画图
clf = KNeighborsClassifier(n_neighbors, weights="distance")
clf.fit(X, label)
cmap_light = ListedColormap(["salmon", "cornflowerblue", "limegreen", "orange"])
cmap_bold = ["red", "blue", "green",  "orange"]
income_level = ["poor", 'enough', 'median', 'rich']
h = 1.0

# *plotting section, you do not need to pay attention
# Plot the decision boundary. 
# For that, we will assign a color to each grid-point in total 2D area
# This is done by K-Means model predict, see how model split the 2D space
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)


# *you don't need pay attention: plotting section
plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, Z, cmap=cmap_light)
sns.scatterplot(
    x=X[:, 0],
    y=X[:, 1],
    hue=np.array(income_level)[label],
    palette=cmap_bold,
    alpha=1.0,
    edgecolor="black",
)

plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title(
    "4-Class classifiction by INDUS and NOX (k = %i, weights = distance)" % (n_neighbors)
)
plt.xlabel("INDUS")
plt.ylabel("NOX")



# 接下来我会在图里把预测的点标出来
plt.scatter(test_input_to_predict[0],test_input_to_predict[1],marker='*',c='red',s=200)
plt.text(test_input_to_predict[0],test_input_to_predict[1],str(income_level[int(res)]))
plt.show()