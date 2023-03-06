from sklearn.datasets import load_diabetes #당뇨병 환자 데이터
diabetes=load_diabetes()
# <class 'sklearn.utils._bunch.Bunch'>
print(type(diabetes))
# [데이터]의 크기는 442*10 422는 샘플의 갯수 10은 특성의 갯수 / 2차원 배열
# [타겟]의 크기는 442 샘플은 총 422개 / 1차원 배열
print(diabetes.data.shape,diabetes.target.shape)
print(diabetes.data[:3])
print(diabetes.target[:3])

import matplotlib.pyplot as plt
x=diabetes.data[:,2]# 2번째 column의 모든 row를 선택
y=diabetes.target
plt.scatter(x,y)
plt.xlabel('x') # 그래프의 x축을 x라고 부르겠다
plt.ylabel('y') # 그래프의 y축을 y라고 부르겠다
plt.show()