from datetime import datetime, timedelta
input_date = 1
while input_date != 0:
    try:
        input_date = input("日付を入力してください。")
        target_date = datetime.strptime(input_date, "%Y/%m/%d")
        yobi = ["Man", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]

        if yobi[target_date.weekday()] == "Sat":
            print(f"{input_date}は{yobi[target_date.weekday()]}です。平日ではありません。")
            print(f"次の平日は{input_date + datetime.timedelta(days=2)}です。")
            break
        elif yobi[target_date.weekday()] == "Sun":
            print(f"{input_date}は{yobi[target_date.weekday()]}です。平日ではありません。")
            print(f"次の平日は{input_date + datetime.timedelta(days=1)}です。")
            break
        else:
            print(f"{input_date}は{yobi[target_date.weekday()]}です。平日です。")
            break
    except:
        print("そんな日ないんだけど(笑)\n")
