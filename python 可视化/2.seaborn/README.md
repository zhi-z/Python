# Seaborn 可视化应用

## 1.简介

Seaborn是一个在Python中制作有吸引力和信息丰富的统计图形的库。它建立在[matplotlib](http://matplotlib.org/)之上，并与[PyData](http://pydata.org/)堆栈紧密集成，包括支持来自[scipy](http://scipy.org/)和[statsmodels的](http://statsmodels.sourceforge.net/)[numpy](http://www.numpy.org/)和[pandas](http://pandas.pydata.org/)数据结构和统计例程。 Seaborn旨在将可视化作为探索和理解数据的核心部分。绘图函数对包含整个数据集的数据框和数组进行操作，并在内部执行必要的聚合和统计模型拟合以生成信息图。如果matplotlib“试图让事情变得简单容易和难以实现”，seaborn会试图使一套明确的方案让事情变得容易。 Seaborn可以认为是对matplotlib的补充，而不是它的替代品。在数据可视化方面能够很好的表现。 

## 2.单变量分布


```python
%matplotlib inline
import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)
np.random.seed(sum(map(ord, "distributions")))
```

### 灰度图
最方便快捷的方式~


```python
x = np.random.normal(size=100)
sns.distplot(x, kde=True)
```


    <matplotlib.axes._subplots.AxesSubplot at 0x1ed5fe22d30>


![png](output_3_1.png)


想得到更精细的刻画？调节bins，对数据更具体的做分桶操作。


```python
sns.distplot(x, kde=True, bins=20)
```


    <matplotlib.axes._subplots.AxesSubplot at 0x1ed5fe22cc0>




![png](output_5_1.png)


想配合着实例一起看？


```python
sns.distplot(x, kde=False, bins=20, rug=True)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x1ed60183518>




![png](output_7_1.png)


配合着实例一起看有什么好处？指导你设置合适的bins。

### 核密度估计
通过观测估计概率密度函数的形状。
有什么用呢？待定系数法求概率密度函数~

核密度估计的步骤：
* 每一个观测附近用一个正态分布曲线近似
* 叠加所有观测的正太分布曲线
* 归一化

在seaborn中怎么画呢？


```python
sns.kdeplot(x)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x1ed605a6908>




![png](output_10_1.png)


bandwidth的概念：用于近似的正态分布曲线的宽度。


```python
sns.kdeplot(x)
sns.kdeplot(x, bw=.2, label="bw: 0.2")
sns.kdeplot(x, bw=2, label="bw: 2")
plt.legend()
```




    <matplotlib.legend.Legend at 0x1ed606f15c0>




![png](output_12_1.png)


### 模型参数拟合


```python
x = np.random.gamma(6, size=200)
sns.distplot(x, kde=False, fit=stats.gamma)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x11098fd50>




![png](output_14_1.png)


## 3.双变量分布


```python
mean, cov = [0, 1], [(1, .5), (.5, 1)]
data = np.random.multivariate_normal(mean, cov, 200)
df = pd.DataFrame(data, columns=["x", "y"])
```

两个相关的正态分布~
### 散点图


```python
sns.jointplot(x="x", y="y", data=df)
```




    <seaborn.axisgrid.JointGrid at 0x7ff06dc1c110>




![png](output_18_1.png)


### 六角箱图


```python
x, y = np.random.multivariate_normal(mean, cov, 1000).T
with sns.axes_style("ticks"):
    sns.jointplot(x=x, y=y, kind="hex")
```


![png](output_20_0.png)


### 核密度估计


```python
sns.jointplot(x="x", y="y", data=df, kind="kde")
```


    <seaborn.axisgrid.JointGrid at 0x7ff06d678e10>


![png](output_22_1.png)

```python
f, ax = plt.subplots(figsize=(6, 6))
sns.kdeplot(df.x, df.y, ax=ax)
sns.rugplot(df.x, color="g", ax=ax)
sns.rugplot(df.y, vertical=True, ax=ax)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7ff06d48b310>




![png](output_23_1.png)


想看到更连续梦幻的效果~


```python
f, ax = plt.subplots(figsize=(6, 6))
cmap = sns.cubehelix_palette(as_cmap=True, dark=1, light=0)
sns.kdeplot(df.x, df.y, cmap=cmap, n_levels=60, shade=True)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7ff06ce1e850>




![png](output_25_1.png)



```python
g = sns.jointplot(x="x", y="y", data=df, kind="kde", color="m")
g.plot_joint(plt.scatter, c="w", s=30, linewidth=1, marker="+")
g.ax_joint.collections[0].set_alpha(0)
g.set_axis_labels("$X$", "$Y$")
```


    <seaborn.axisgrid.JointGrid at 0x7ff06d48b190>




![png](output_26_1.png)


## 4.数据集中的两两关系


```python
iris = sns.load_dataset("iris")
iris.head()
```

![]()


```python
sns.pairplot(iris);
```


![png](output_29_0.png)


属性两两间的关系 + 属性的灰度图


```python
g = sns.PairGrid(iris)
g.map_diag(sns.kdeplot)
g.map_offdiag(sns.kdeplot, cmap="Blues_d", n_levels=20)
```




    <seaborn.axisgrid.PairGrid at 0x119c17310>




![png](output_31_1.png)

