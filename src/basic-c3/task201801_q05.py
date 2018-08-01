arasi_list = [
    ("Aiba", 35),
    ("Matsumoto", 34),
    ("Ninomiya", 35),
    ("Oono", 37),
    ("Sakurai", 36)
]

faster_list = sorted(
    arasi_list,
    key=lambda ara: ara[1],
    reverse=True)

for i in faster_list:
    print(i)
