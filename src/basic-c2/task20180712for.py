print("  |   1  2  3  4  5  6  7  8  9")
print("--+----------------------------")
# kaisuuはループの回数を表す。
kaisuu = 1
for _ in range(kaisuu):
    # kaisiはiループの開始の値
    kaisi = 1
    # owariはiループの終わりの値
    owari = 10
    for i in range(kaisi, owari):
        print("{:>2}|  {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}".format(i, i, 2*i, 3*i, 4*i, 5*i, 6*i, 7*i, 8*i, 9*i))
