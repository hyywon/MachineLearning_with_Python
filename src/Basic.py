import numpy as np


# Numpy배열의 초기화

# arrange(n) : n개 1차원 배열
array1 = np.arange(4)

# 초기화
# zeros((n,n), dtype=type) : (n, n) 형태 행렬을 type 으로 이루어진 0으로 초기화
# ones((n,n), dtype=type) : (n, n) 형태 행렬을 type 으로 이루어진 1로 초기화
array2 = np.zeros((4, 4), dtype=float)
array3 = np.ones((4, 4), dtype=str)

# 랜덤하게 초기화
# random.randint(a, b, (n, n)) :
array4 = np.random.randint(0, 10, (3, 3))

# 평균이 0이고, 표준편차 1인 표준 정규 띄는 배열
# random.normal(a, b, (n, n))
array5 = np.random.normal(0, 1, (3, 3))


# Numpy 배열 합치기
# concatenate([array, array])
array6 = np.array([1, 2, 3])
array7 = np.array([4, 5, 6])
array8 = np.concatenate([array6, array7])
# > [1,2,3,4,5,6]


# Numpy 배열 형태 바꾸기
# reshap() : 가로축으로 배열 바꾸기
array9 = np.array([1, 2, 3, 4])
array10 = array9.reshape((2, 2))
# > [[1 2]
#   [3 4]]

# concatenate.([array, array], axis=0) : 세로축을 기준으로 배열 합치기
array11 = np.arange(4).reshape(1, 4)
array12 = np.arange(8).reshape(2, 4)
array13 = np.concatenate([array11, array12], axis=0)
# > [[0 1 2 3]
#   [0 1 2 3]
#   [4 5 6 7]]


# Numpy 배열 나누기
# split(array, [index], axis=1) : index를 기준으로 왼쪽과 오른쪽으로 나뉨
left, right = np.split(array12, [2], axis=1)
# left
# > [[0 1]
#   [4 5]]
# right
# > [[2 3]
#   [6 7]]