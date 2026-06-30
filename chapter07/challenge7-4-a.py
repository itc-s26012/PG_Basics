answers = [23,6,19,37,43]

while True:
    #なにか数字を入力してもらう
    n = input("なにか数字を入れてください->")
  #"q"が入力されていたら終了
    if n == "q" :
    #無限ループから強制的に抜ける
        break
    else:
        if int(n) in answers:
            print("正解")
        else:
            print("数字で入力するか、qで終了します")

print("終了")
