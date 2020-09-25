import pandas as pd
import numpy as np


# Pandas Data Frame의 마스킹
# 값보다 작거나 큰지 bool 형태로 출력 가능
# query 문으로도 사용 가능, 값으로 출력
df = pd.DataFrame(np.random.randint(1,10,(2,2)), index=[0,1], columns=['A', 'B'])
print(df['A'] < 5)
print(df.query('A<=5 and B <=8'))


# Pandas Data Frame의 개별 연산 1
# apply(lambda x : 연산) : 모든 데이터 값에 대해 개별 연산
df = pd.DataFrame([[1, 2, 3, 4], [1, 2, 3, 4]], index=[0, 1], columns=["A", "B", "C", "D"])
df = df.apply(lambda x: x+1)


# Pandas Data Frame의 개별 연산 2
#replace({'column': 'Name'}) : 해당 column들을 Name으로 대체 연산
df = pd.DataFrame([['Apple', 'Apple', 'Carrot', 'Banana'],
                ['Durian', 'Banana', 'Apple', 'Carrot']],
                index=[0, 1], columns=["A", "B", "C", "D"])
df = df.replace({'Apple': 'Air'})


# Pandas Data Frame의 그룹화 1 
# 원하는대로 가공하거나, 시각화 할 때 많이 사용
# groupy(['Name']).sum()) : Name에 해당하는 그룹화 하여 sum 연산
df = pd.DataFrame([
  ['Apple', 7, 'Fruit'],
  ['Banana', 3, 'Fruit'],
  ['Beef', 5, 'Meal'],
  ['Kimchi', 4, 'Meal']],
  columns=["Name", "Frequency", "Type"])
grp = df.groupby(['Type']).sum()


# Pandas Data Frame의 그룹화 2
# groubpy(['Name']).aggregate([min,max,np.average])
# : Name을 그룹화하여 여러개의 연산을 한번에 보여줌, 정수형 연산만 가능
df = pd.DataFrame([
  ['Apple', 7, 5, 'Fruit'],
  ['Banana', 3, 6, 'Fruit'],
  ['Beef', 5, 2, 'Meal'],
  ['Kimchi', 4, 8, 'Meal']],
  columns=["Name", "Frequency", "Importance", "Type"])
print(df.groupby(["Type"]).aggregate([min, max, np.average]))


# Pandas Data Frame의 그룹화 3
# groupby('Name').filter(function) 
# : Name 데이터들을 function에 해당하는 filter을 적용
df = pd.DataFrame([
  ['Apple', 7, 5, 'Fruit'],
  ['Banana', 3, 6, 'Fruit'],
  ['Beef', 5, 2, 'Meal'],
  ['Kimchi', 4, 8, 'Meal']],
  columns=["Name", "Frequency", "Importance", "Type"])


def my_filter(data):
  return data["Frequency"].mean() >= 5


df = df.groupby("Type").filter(my_filter)


# Pandas Data Frame의 그룹화 4
# groupby('Name').get_group('GroupName') : Name Column 중에서 해당 GroupName 그룹만 가져옴
df = df.groupby("Type").get_group("Fruit")


# Pandas Data Frame의 그룹화 5
# groupby('Column')['Name'].apply(lambda x: 연산 ) : 그룹화하여 연산하고 연산 값 자체 새 컬럼 생성
df["Gap"] = df.groupby("Type")["Frequency"].apply(lambda x: x - x.mean())


# 데이터 프레임의 다중화
# df([['Name1','Name2']].loc['Column']) : 다중화 된 데이터에 대해
df = pd.DataFrame(
  np.random.randint(1, 10, (4, 4)),
  index=[['1차', '1차', '2차', '2차'], ['공격', '수비', '공격', '수비']],
  columns=['1회', '2회', '3회', '4회']
)
print(df[["1회", "2회"]].loc["2차"])


# 피벗 테이블의 기초
# 열&행을 서로 바꿔서 보여줌
# df = df.pivot_table(
#     index="indxe", columns="column", values="values", aggfunc=np.max )
# : index에 index를 column에 column별로 생성, 값은 values 중에서 aggfunc에 해당하는 것(max)을 사용

df = pd.DataFrame([
    ['Apple', 7, 5, 'Fruit'],
    ['Banana', 3, 6, 'Fruit'],
    ['Coconut', 2, 6, 'Fruit'],
    ['Rice', 8, 2, 'Meal'],
    ['Beef', 5, 2, 'Meal'],
    ['Kimchi', 4, 8, 'Meal']],
   columns=["Name", "Frequency", "Importance", "Type"])

print(df)
df = df.pivot_table(
    index="Importance", columns="Type", values="Frequency",
    aggfunc=np.max
)

