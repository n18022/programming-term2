import random
name = ["安倍総理", "野々村議員", "マイケル・ジャクソン"]
nickname = ["ジェニファー", "キャサリン", "ヨッシー"]
everyone = ["仲良くしてください", "結婚してください", "死ね"]
fname = random.randint(0, len(name)-1)
fnickname = random.randint(0, len(nickname)-1)
feveryone = random.randint(0, len(everyone)-1)
print("私の名前は{}です。あだ名は{}です。皆さん私と{}".format(name[fname], nickname[fnickname], everyone[feveryone]))
