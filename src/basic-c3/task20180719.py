def _3_(parameter1, parameter2, calculation_method):
    """
    ２つの値と演算方法を入力して計算する。

    parameters
    ----------
    parameter1 : float
      第1入力パラメータ入力

    parameter2 : float
      第2入力パラメータ入力

    calculation_method
      演算方法を入力

    Returns
    """

print("四則計算のプログラムです。")
true = True
# 第1と第2のパラメータに数字が入るまで繰り返す。
while True:
    parameter1 = input("第1パラメータを入力してください\n")
    p1True = str.isnumeric(parameter1)
    if p1True != true:
        continue
    parameter2 = input("第2パラメータを入力してください\n")
    p2True = str.isnumeric(parameter2)
    if p2True != true:
        continue
    parameter1 = float(parameter1)
    parameter2 = float(parameter2)
    break

# 四則演算のどれかを入力するまで繰り返す
# 入力後、第1と第2のパラメータを使って計算する。
while True:
    calculation_method = input("演算方法を入力してください\n")
    if calculation_method == "+":
        add = parameter1 + parameter2
        print(add)
        break
    if calculation_method == "-":
        sub = parameter1 - parameter2
        print(sub)
        break
    if calculation_method == "*":
        mul = parameter1 * parameter2
        print(mul)
        break
    if calculation_method == "/":
        div = round((parameter1 / parameter2), 2)
        print(div)
        break
    print("入力が不正です。")

help(_3_)
