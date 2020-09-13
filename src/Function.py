import numpy as np


# Numpy데이터 저장, 불러오기
# save('file.npy', array) : 단일 객체 저장
# load('file.npy') : 단일 객체 불러오기
array1 = np.arange(0, 10)
np.save('saved.npy', array1)
result = np.load('saved.npy')

# savez('file.npz', name=array, name=array) : 복수 객체 저장
# data['name'] : 복수 객체 배열 접근
array2 = np.arange(10, 20)
np.savez('savedz.npz', array1=array1, array2=array2)
data = np.load('savedz.npz')
result1 = data['array1']
result2 = data['array2']


# Numpy 원소의 정렬 [Default : 오름차순]
# sort() : 오름차순으로 정렬함
# array[::-1] : 오름차순 후 내림차순으로 접근
array3 = np.array([5, 9, 10, 1, 3])
# Ascending
array3.sort()
# Descending
Descending = array3[::-1]

# Numpy 열을 기준으로 정렬
# sort(axis=axis) : axis 축 기준으로 정렬
array4 = np.array([[5, 9, 10, 1, 3], [8, 3, 5, 9, 1]])
array4.sort(axis=0)
# > [[ 5  3  5  1  1]
#   [ 8  9 10  9  3]]


# Numpy 균일한 간격으로 데이터 생성
# linspace(a, b, n) : a부터 b까지 n개의 데이터 생성
array5 = np.linspace(0, 10, 5)
# > [ 0.   2.5  5.   7.5 10. ]


# Numpy 난수의 재연 (실행마다 결과 동일)
# ML 모델 학습할 때, 난수가 달라서 학습 결과가 달라지지 않도록 함
np.random.seed(7)
np.random.randint(0, 10, (2, 3))


# Numpy 배열 객체 복사
# 배열 복사하면, 배열 주소를 공유
# copy() 사용하면 배열 주소 공유하지 않고 복사 가능
array6 = array1.copy()


# Numpy 중복된 원소 제거
# unique(array)
array7 = np.array([1, 1, 2, 3, 3, 3, 4, 5])
array8 = np.unique(array7)
# > [1 2 3 4 5]