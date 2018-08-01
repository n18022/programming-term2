Tax_rate = 8
zeinuki = [13600, 14500, 16000, 11111, 11667]
zeikomi = lambda keisan: round(keisan * (1 + Tax_rate / 100), 0)
print(list(map(zeikomi, zeinuki)))
