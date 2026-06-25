#変数ageに数字を代入し、
#そのageを使って何かしらの条件分岐をして、
#条件に応じてメッセージを出力しよう。

age = 99

if age <= 10:
    print("You can't ride this yet")
elif age <= 30:
    print("You can finally ride this!")
elif age <= 60:
    print("The day you will no longer be able to ride this is drawing near.")
elif age > 60:
    print("You can't longer ride this..")
