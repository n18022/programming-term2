print("  |   1  2  3  4  5  6  7  8  9")
print("--+----------------------------")
i = 1
while(i < 10):
    print("{:>2}|  {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}".format(i, i, 2*i, 3*i, 4*i, 5*i, 6*i, 7*i, 8*i, 9*i))
    i += 1
