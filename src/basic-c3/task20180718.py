# メニューを見せる
mainmenue = {"DripCoffee": 280, "ColdBrewCoffee": 320, "CafeLatte": 330, "SoyLatte": 380, "Cappuccino": 330, "CaramelFrappuccino": 470, "MacchaCreamFrappuccino": 470}
# オプションを見せる
option = {"LowFatMilk": 0, "NonFatMilk": 0, "SoyMilk": 50, "DeepCoffee": 60}
# 注文内容
Order_content = []
while True:
    menue = input("メインメニューを選んでください。")
    if menue == "" or menue == "q":
        print("購入をキャンセルします。")
        End = 1
        break
    if menue in mainmenue:
        print("メインメニューを承りました。")
        Order_content.append(menue)
        End = 0
        break
    print("選択されたメニューはありません。")
while End != 1:
    is_option_ordering = input("オプションメニューを選んでください。")
    if is_option_ordering == "" or is_option_ordering == "q":
        print("注文内容は{}{}です。".format(menue, ))
        break
    if is_option_ordering in option:
        print("オプションを承りました。")
        Order_content.append(is_option_ordering)
        continue
    print("選択されたメニューはありません。")
