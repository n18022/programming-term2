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
# 第1のパラメータの入力。
parameter1 = float(input("第1パラメータを入力してください\n"))
print("第1パラメータが確定しました。")

# 第2のパラメータの入力。
parameter2 = float(input("第2パラメータを入力してください\n"))
print("第2パラメータが確定しました。")

# 四則演算のどれかを入力するまで繰り返す
# 入力後、第1と第2のパラメータを使って計算する。
while True:
    calculation_method = input("演算方法を入力してください\n")
    if calculation_method == "+":
        add = parameter1 + parameter2
        dicision = add
        break
    if calculation_method == "-":
        sub = parameter1 - parameter2
        dicision = sub
        break
    if calculation_method == "*":
        mul = parameter1 * parameter2
        dicision = mul
        break
    if calculation_method == "/":
        div = round((parameter1 / parameter2), 2)
        dicision = div
        break
    print("入力が不正です。")

print("計算は{} {} {}で結果は{}です。"
      .format(parameter1, calculation_method, parameter2, dicision))
help(_3_)
