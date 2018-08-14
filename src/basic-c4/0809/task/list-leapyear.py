uruu_list = []
gomi_list = []

for u in range(2000, 2100 + 1):
    uruu_list.append(u) if (u % 4 == 0 and u != 2100) else gomi_list.append(0)

print(uruu_list)
