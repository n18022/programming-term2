# 定義達
import random
saikoronome = 0
susumume = 0
# 関数達
def shake_dice():
    """
    サイコロの目の数。

    Parameters
    ----------
    shake_dice : int
        サイコロの値

    Returns
    -------
    saikoronome : int
        サイコロの目。
    """
    saikoronome = random.randint(1, 6)
    return saikoronome
def go_forword(susumume):
    """
    今までのサイコロの目の合計。

    Parameters
    ----------
    go_forword : int
    サイコロの目の合計。

    Returns
    -------
    susumume : int
        サイコロの合計値。
    """
    susumume += saikoronome
    return susumume
while True:
    while susumume < 10:
        enter = input("サイコロを振ってください。\n(※ enterkey押すだけ)")
        if enter != "":
            continue
        saikoronome = shake_dice()
        susumume = go_forword(susumume)
        print("{}が出ました。現在位置{}はです。\n".format(saikoronome, susumume))
        continue
    while susumume > 10:
        enter = input("サイコロを振ってください。\n(※ enterkey押すだけ)")
        if enter != "":
            continue
        saikoronome = shake_dice() * -1
        susumume = go_forword(susumume)
        print("{}が出ました。現在位置{}はです。\n".format(saikoronome, susumume))
        continue
    if susumume == 10:
        break
    continue
print("{}が出ました。おめでとうございます、ゴールしました!".format(susumume))
help(shake_dice)
help(go_forword)
