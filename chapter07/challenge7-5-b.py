num1 = [8,19,148,4]
num2 = [9,1,33.83]
multi = [] #かけあわせた結果を格納するリスト

#ループ処理を入れ子にすると、num1とnum2それそれの値をかけ合わせられる
for n1 in num1:  #外側のループ(num1)
    #print(f" j={j})
    for n2 in num2:  #内側のループ(num2)
       # mluti.append( i * j )
        multi.append( n1 * n2 ) #かけあわせた結果をmultiに追加
    #内側のループの終わり
#外側のループの終わり

#multiを表示する
print(multi)
