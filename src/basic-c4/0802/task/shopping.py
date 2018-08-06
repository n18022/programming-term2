# calc_tax.pyからインポート
from calc_tax import calc_incl_tax

# 定義達
zeinuki = 0
syojikin = 2000
Banana = 200
Apple = 200
Orange = 450

def kaikei(syouhin, kosuu, zeinuki):
    """
    購入する商品の値段と個数を求める。

    Parameters
    ----------
    syouhin : str
        購入する商品名
    kosuu: int
        購入する個数
    zeinuki: int
        購入する商品の税抜価格
    """
    print("{}を{}個買いました。商品計は{}円です。".format(syouhin, kosuu, zeinuki))

kaikei("Banana", 2, 200)
kaikei("Apple", 1, 200)
kaikei("Orange", 3, 450)

zeinuki_goukei = Banana + Apple + Orange
zeikomi = zeinuki_goukei * calc_incl_tax(0.08)
zeikomi = int(round(zeikomi, 1))
print("総計の税抜き額は{}円、税込価格は{}円です。".format(zeinuki_goukei, zeikomi))
print("残金は{}円です。".format(syojikin - zeikomi))

help(kaikei)
