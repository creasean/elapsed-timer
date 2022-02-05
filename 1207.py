#from numpy import float64
#넘파이 모듈 부르기
import pandas as pd
#판다스 모듈 부르고 이름을 pd로 단축해서 정하기

data=pd.Series([1,2,3,4])
print(data.dtype)
print(type(data))

data=pd.Series([5,6,7,8],dtype=float)
#data의 값을 기존(정수)에서 실수 형태로 변경함.
print(data)
print(data.dtype)
print(type(data))

data[0]=9
#0번 인덱스의 값을 5->9로 변경
print(data)

data=pd.Series([2,4,6,8], index=['a','b','c','d'])
#0~3까지의 인덱스를 a,b,c,d로 변경함
print(data['d'])

data['c']=12
#인덱스 값을 이용하여 데이터 값을 변경 가능, 인덱스 c를 찾아내어 그 값을 변경함
print(data)

pop_dict={'a':1213,'b':456,'c':789,'d':741}
#딕셔너리를 이용하여 시리즈 생성가능
population=pd.Series(pop_dict)
print(population)