print("こんにちは、{}".format("ウィリアム・フォークナー") )
name = "ウィリアム・フォークナー"
print("こんにちは、{}".format(name) )
author = "ウィリアム・フォークナー"
year_born = "1897"
print("{}　は {} 年に生まれました。".format(author,year_born) )
#formatメソッドには複数の値が指定できる
author ="宮沢賢治"
year_born = "1896"
print("{}は{}年に生まれました。".format(author, year_born) )
#別のやり方_f文字列_こっちのほうがいいかもしれない
print(f"{author}は{year_born}年に生まれました。")

