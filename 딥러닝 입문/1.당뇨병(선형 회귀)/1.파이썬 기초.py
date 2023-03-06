import numpy as np
print(np.__version__)
my_arr = np.array([[10,20,30],[50,60,70]])
print(type(my_arr))
print(my_arr) 
print(my_arr[0][2])

my_list = [10,'hello',13]
print(my_list)

my_list1 = [[10,20,30],[20,30,40]]
print(my_list1[0][2])
print(np.sum(my_arr))

# 맷플롯립으로 그래프 그리기
import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5],[1,4,9,16,25]) # x축,  y축 값을 파이썬 리스트로 전달
plt.show()
# 산점도
plt.scatter([1,2,3,4,5],[1,4,9,16,25]) 
plt.show()
# 산점도
x=np.random.randn(1000)
y=np.random.randn(1000)
plt.scatter(x,y)
plt.show()
plt.plot(x,y)
plt.show()