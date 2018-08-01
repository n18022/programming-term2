arasi_list = [
    ("Aiba", 175),
    ("Matsumoto", 172),
    ("Ninomiya", 168),
    ("Oono", 166),
    ("Sakurai", 171)
]

faster_list = sorted(
    arasi_list,
    key=lambda ara: ara[1],
)

for i in faster_list:
    print(i)
