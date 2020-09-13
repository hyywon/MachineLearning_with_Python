import pandas as pd


# Padas 시리즈 사용
# Dict 데이터를 바로 Series로 바꿀 수 있음
array1 = pd.Series(['사과', '바나나', '토마토'], index=['a', 'b', 'c'])
# a     사과
# b    바나나
# c    토마토
# dtype: object


# Pandas Data Frame 사용
# 인덱스를 기준으로 구성
word_dict = {
    'Apple': '사과',
    'Banana': '바나나',
    'Tomato': '토마토'
}
frequency_dict = {
    'Apple': 3,
    'Banana': 3,
    'Tomato': 5
}
word = pd.Series(word_dict)
frequency = pd.Series(frequency_dict)

Summary = pd.DataFrame({
    'word': word,
    'frequency': frequency
})
#         word    frequency
# Apple    사과           3
# Banana  바나나          3
# Tomato  토마토          5


# Pandas Series 연산
# 동일 인덱스를 가지고 연산을 하고 새로운 시리즈를 만들 수 있음
importance_dict = {
    'Apple': 3,
    'Banana': 2,
    'Tomato': 1
}
importance = pd.Series(importance_dict)
Summary2 = pd.DataFrame({
    'word': word,
    'frequency': frequency,
    'importance': importance
})
score = Summary2['frequency'] * Summary2['importance']
Summary2['score'] = score
#          word  frequency  importance  score
# Apple    사과           3           3      9
# Banana  바나나          3           2      6
# Tomato  토마토          5           1      5


# Pandas Data Frame의 슬라이싱
# loc['row':'row', 'col':'col'] : 열/행을 기준으로 슬라이싱, row - row 까지 / col - col 까지
print(Summary2.loc['Banana':'Tomato', 'importance':])
#         importance  score
# Banana           2      6
# Tomato           1      5

# iloc[a:b, c:d] : 인덱스를 기준으로 슬라이싱
print(Summary2.iloc[1:2, 2:])


# Pandasd Data Frame의 연산
# loc['Name', 'Data'] = n : 'Name':'Data'의 내용을 변경
# loc['Name'] = ['Data', data, data] : 'Name'이라는 새로운 데이터 생성
Summary2.loc['Apple', 'importance'] = 5
Summary2.loc['Orange'] = ['오렌지', 5, 5]


# 엑셀로 데이터를 내보내고 가져오기
# to.csv('file.csv', encoding="utf-8-sig") : 엑셀 파일로 내보내기
# read_csv('file.csv', index_col=index) : 해당 index만 엑셀 파일 가져오기
Summary2.to.csv('Summary.csv', encoding="utf-8-sig")
saved = pd.read_csv('Summary.csv', index_col=0)

