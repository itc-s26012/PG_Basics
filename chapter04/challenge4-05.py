#文字列をfloat型に変換して戻り値とする関数を書いてみよう起こりうる例外をキャッチする例外処理を書こう

def to_float(text):
    return float(text)

try:
    s = input()
    result = to_float(s)
    print(result)
except valueError:
    print("変換できません")
