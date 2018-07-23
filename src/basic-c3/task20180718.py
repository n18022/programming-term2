# 定義達
order_content = []
sum_price = []
decision = ""
end = 1

# メニューを見せる
mainmenues = {
    "DripCoffee": 280,
    "ColdBrewCoffee": 320,
    "CafeLatte": 330,
    "SoyLatte": 380,
    "Cappuccino": 330,
    "CaramelFrappuccino": 470,
    "MacchaCreamFrappuccino": 470
    }

# オプションを見せる
option = {
    "LowFatMilk": 0,
    "NonFatMilk": 0,
    "SoyMilk": 50,
    "DeepCoffee": 60,
    "WhipCream": 70,
    "CaramelShrup": 60,
    "ChocoSource": 0,
    "DeDafe": 50
    }

# メインメニュー注文
while True:
    get_main_menue = input("メインメニューを選んでください。\n")
    # 入力なしかqの場合のみ購入をキャンセルする。
    if get_main_menue == "" or get_main_menue == "q":
        print("購入をキャンセルします。")
        break
    # 入力したオプションメニューが正しければ実行
    if get_main_menue in mainmenues:
        print("メインメニューを承りました。")
        order_content.append(get_main_menue)
        sum_price = mainmenues[get_main_menue]
        end = 0
        break
    print("選択されたメニューはありません。\n")

# メインメニューが注文されていたらオプションメニュー注文
while end != 1:
    # 最初だけ
    if decision != "１回目以降":
        get_option_menue = input("オプションメニューを選んでください。\n")
    # １回目以降以降
    if decision == "１回目以降":
        get_option_menue = input("他にオプションメニューの注文はございますか？\n")
    # ""か"p"だったら注文終了
    if get_option_menue == "" or get_option_menue == "q":
        break
    # オプションメニュー正しければ実行するよ。
    while get_option_menue in option:
        # name, priceにそれぞれキー, 値を入力してるよ。
        for name, price in option.items():
            # どのオプションメニューを求めてるのか調べてべてるよ。
            if name == get_option_menue:
                decision = "オプションを承りました。"
                print("オプションを承りました。")
                order_content.append(get_option_menue)
                sum_price += price
                break
        if decision == "オプションを承りました。":
            break
    if decision == "オプションを承りました。":
        decision = "１回目以降"
        continue
    if decision != "オプションを承りました。":
        print("選択されたメニューはありません。")

# メインメニューが注文されていたら実行するよ。
if end != 1:
    print("注文内容は{}です。".format(order_content))
    print("合計金額は{}円です。右奥のカウンターにてお待ちください。".format(sum_price))
