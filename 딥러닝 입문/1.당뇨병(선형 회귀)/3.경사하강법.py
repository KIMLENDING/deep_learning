from sklearn.datasets import load_diabetes #당뇨병 환자 데이터
import matplotlib.pyplot as plt
diabetes=load_diabetes()
x=diabetes.data[:,2]# 2번째 column의 모든 row를 선택
y=diabetes.target
plt.scatter(x,y)
plt.xlabel('x') # 그래프의 x축을 x라고 부르겠다
plt.ylabel('y') # 그래프의 y축을 y라고 부르겠다

plt.show()
"""경사 하강법
선형 회귀 모델에서 slope(변화율을)를 사용하여 모델을 조금씩 초기화 시키는 방법이다.
회귀 모델을 푸는 방법은 Normal Equation, Decision Tree, Support Vector Machine ...
slope a를 가중치(w)나 계수를 의미하는 (θ)로 표기한다.
y =  ax + b -> 모델 표기 y^ = wx + b 
y와 y^의 차이는 (실제값=y, 예측값=y^) 이라는 차이이다.

훈련 데이터와 잘 맞는 w,b 찾는 방법
1. 무작위로 w,b를 정한다.
2. x에서 셈플 하나 선택한 후 y^을 예측한다.
3. y값과 y^ 값을 비교
4..y^이 y값과 가까워 지도록 w,b 조정
위 과정 반복 
-------------------------결론---------------------------- 
            노가다 뒤지게 하다보면 나온다.

"""
w=1.0
b=1.0
y_hat = x[0] * w + b
print(y_hat) # 1.0616962065186832
print(y[0]) # 151.0
print(x[0]) # 0.061696206518683294
w_inc=w + 0.1 # w값 조절 해서 바꾸기
y_hat_inc = x[0] * w_inc + b
print(y_hat_inc) # 1.0678658271705517
print(y[0]) # 151.0

# 0.1만큼 증가 했을때 y_hat의 값이 얼마나 증가하는지 알아보기
w_rate = (y_hat_inc-y_hat)/(w_inc-w)
print(w_rate) # 0.06169620651868429 == w_rate == 샘플의 값 x[?]

w_new = w + w_rate # 1.06169620651868429

b_inc = b+0.1
y_hat_inc = x[0] * w + b_inc
print(y_hat_inc) # 1.1616962065186833
b_rate = (y_hat_inc-y_hat)/(b_inc-b)
print(b_rate) # b_rate==1
new_b = b + b_rate # new_b==2
# -------------------------------------------------- #
err = y[0]-y_hat
w_new = w + w_rate*err
b_new = b + b_rate*err
print(w_new,b_new)
