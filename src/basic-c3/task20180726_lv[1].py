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

while susumume < 10:
    enter = input("サイコロを振ってください。\n(※ enterkey押すだけ)")
    if enter != "":
        continue
    saikoronome = shake_dice()
    susumume = go_forword(susumume)
    if susumume < 10:
        print("{}が出ました。現在位置{}はです。".format(saikoronome, susumume))
        continue
    break
print("{}が出ました。おめでとうございます、ゴールしました!".format(saikoronome))
help(shake_dice)
help(go_forword)
