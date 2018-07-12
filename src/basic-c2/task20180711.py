# 絶対に勝てないじゃんけん
nyuuryoku = input("1,2,3どれかを入力してね\n何を出しますか? 1:グー、2:チョキ、3:パー\n")
# 入力を文字型に変換する。
nyuuryoku = str(nyuuryoku)
if nyuuryoku == "1":
    aite = "パー"
    print("CPUが{}を出しました。あなたの負けです。".format(aite))
elif nyuuryoku == "2":
    aite = "グー"
    print("CPUが{}を出しました。あなたの負けです。".format(aite))
elif nyuuryoku == "3":
    aite = "チョキ"
    print("CPUが{}を出しました。あなたの負けです。".format(aite))
else:
    print("入力が不正です。終了します。")
