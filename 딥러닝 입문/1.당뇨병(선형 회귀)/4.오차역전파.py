from sklearn.datasets import load_diabetes #당뇨병 환자 데이터
import matplotlib.pyplot as plt
diabetes=load_diabetes()
x=diabetes.data[:,2]# 2번째 column의 모든 row를 선택
y=diabetes.target
w=1.0
b=1.0
for i in range(1,50):
    for x_i,y_i in zip(x,y):
        y_hat = x_i * w + b
        err = y_i - y_hat
        w_rate = x_i
        w = w + w_rate * err
        b = b + 1 * err

print(w,b)

plt.scatter(x,y)#산점도
# plt1 = (-0.1, -0.1 * w + b)
# plt2 = (0.16, 0.16 * w + b)
# plt.plot([plt1[0],plt2[0]],[plt1[1],plt2[1]])
x=[-0.1, 0.16]
y=[-0.1 * w + b, 0.16 * w + b]
plt.plot(x,y,)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

""" 
plt.plot()
x: x 축 데이터
y: y 축 데이터
fmt: 선 스타일을 지정하는 문자열입니다. 기본값은 'b-'(파란색 선)입니다.
color: 선 색상을 지정하는 문자열이나 RGB 튜플입니다.
label: 범례에 표시될 문자열입니다.
linewidth: 선 굵기를 지정하는 값입니다.
linestyle: 선 스타일을 지정하는 문자열입니다.
"""

