what = input("何が:")
when = input("いつ:")
where = input("どこで:")
do = input("どうした:")

r = "{}は{}に{}で{}。".format(what, when, where, do)
print(r)
#f文字列を使っての書式指定だとこうなります
print(f"{what}は{when}、{where}で{do}。")

