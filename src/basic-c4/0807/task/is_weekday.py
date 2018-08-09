from datetime import datetime, timedelta
end = 0
while True:
    try:
        input_date = input("日付を入力してください。")
        target_date = datetime.strptime(input_date, "%Y/%m/%d")
        yobi = ["Man", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]

        if yobi[target_date.weekday()] == "Sat":
            print(f"{input_date}は{yobi[target_date.weekday()]}です。平日ではありません。")
            n_weekday = target_date + timedelta(days=2)
            str_n_weekday = n_weekday.strftime("%Y/%m/%d")
            print(f"次の平日は{str_n_weekday}です。")
            end = 1
            break
        elif yobi[target_date.weekday()] == "Sun":
            print(f"{input_date}は{yobi[target_date.weekday()]}です。平日ではありません。")
            n_weekday = target_date + timedelta(days=1)
            str_n_weekday = n_weekday.strftime("%Y/%m/%d")
            print(f"次の平日は{str_n_weekday}です。")
            end = 1
            break
        else:
            print(f"{input_date}は{yobi[target_date.weekday()]}です。平日です。")
            end = 1
            break
    except:
        print("そんな日ないんだけど(笑)\n")
        if end == 1: break
