import pandas as pd
import numpy as np


word_dict = {
    'Apple': '사과',
    'Banana': '바나나',
    'Carrot': '당근',
    'Durian': '두리안'
}

frequency_dict = {
    'Apple': 3,
    'Banana': 5,
    'Carrot': np.nan,
    'Durian': 2
}

importance_dict = {
    'Apple': 3,
    'Banana': 2,
    'Carrot': 1,
    'Durian': 1
}

word = pd.Series(word_dict)
frequency = pd.Series(frequency_dict)
importance = pd.Series(importance_dict)

word = pd.Series(word_dict)
frequency = pd.Series(frequency_dict)
importance = pd.Series(importance_dict)

summary = pd.DataFrame({
    'word': word,
    'frequency': frequency,
    'importance': importance
})


# Pandas Data Frame 에서 Null 여부 확인
# nan, Null : 공백
# isnull() : null 이면 True, 아니면 False
# notnull() : null 이면 False, 아니면 True
# dataframe['Name'].fillna('데이터X') : Name에 해당하는 Null을 데이터X로 보여줌
print(summary.isnull())
print(summary.notnull())
# summary['frequency'] = summary['frequency'].fillna('데이터 없음')
print(summary)
#         word frequency     importance
# Apple    사과         3              3
# Banana  바나나         5              2
# Carrot   당근    데이터 없음           1
# Durian  두리안         2              1


# Pandas Series 연산
# Series도 Null 값 존재
# 기본적으로 연산시 겹칠때만 연산하고, 없을 경우 기본값을 0을 가지고 있다고 생각하고 연산
# array.add(array, fill_value=value) : array에 array값을 더함, 같은 index가 없을 경우, 기본값 value로 생각하고 연산
# array.add(array) : 같은 index가 없을 경우, Null 값으로 저장 됨
array1 = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
array2 = pd.Series([4, 5, 6], index=['B', 'C', 'D'])
array3 = array1.add(array2, fill_value=0)
# A    1.0
# B    6.0
# C    8.0
# D    6.0
# dtype: float64


# Pandas Data Frame 연산
# Series와 동일하게 사용
array4 = pd.DataFrame([[1, 2], [3, 4]], index=['A', 'B'])
array5 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['B', 'C', 'D'])
array6 = array4.add(array5, fill_value=0)


# Pandas Data Frame 집계 함수
# sum() : 각각 시리즈에 대해서 Sum하고 저장
# array[index].sum() : 해당하는 index 값만 저장
array7 = pd.DataFrame([[1, 2], [3, 4]], index=['A', 'B'])
array8 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['B', 'C', 'D'])
array9 = array7.add(array8, fill_value=0)
sum = array9.sum()
# 0    16.0
# 1    21.0
# 2    18.0


# Pandas Data Frame 정렬 함수
# sort_values('Name', ascending=False) : 'Name'을 정렬, 오름차순 정렬기본
summary = summary.sort_values('frequency', ascending=False)
#        word  frequency  importance
# Banana  바나나        5.0           2
# Apple    사과        3.0           3
# Durian  두리안        2.0           1
# Carrot   당근        NaN           1
