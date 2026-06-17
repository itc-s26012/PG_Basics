#文字列"どこで？　誰が？　いつ？"をメソッドで分解して、["どこで？","誰が？","いつ？"]のようなリストにしよう。
where = input("どこで:")
who = input("誰が:")
when = input("いつ:")

r = "{}で{}が{}。".format(where, who, when)
print(r)

