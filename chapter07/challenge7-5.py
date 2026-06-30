#2つのリストに含まれるすべての数字の組み合わせで掛け算しよう。
#1つめのリストは　[8, 19, 148, 4],
#2つめのリストは  [9, 1, 33, 83]  で、それぞれ掛け算した結果は新しいリストに格納しよう。

list1 = [8, 19, 148, 4]

list2 = [9, 1, 33, 83]

multiplied = []

for i in list1:
    for j in list2:
        multiplied.append(i * j)

print(multiplied)
