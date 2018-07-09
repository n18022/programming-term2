print("会計いくら？")
#ビールの会計
bi_runedan = 200
bi_rukazu = 2
bi_rukaikei = bi_runedan * bi_rukazu

#おつまみの会計
otumaminedan = 100
otumamikazu = 1
otumamikaikei = otumaminedan * otumamikazu

#焼き鳥の会計
yakitorinedan = 100
yakitorikazu = 2
waribikiritu = 1 - 0.2
yakitorikaikei = (yakitorinedan * waribikiritu) * yakitorikazu

#割引ポイント
pointo = 150
#すべての会計
kaikei = bi_rukaikei + otumamikaikei + yakitorikaikei - pointo
print(kaikei)
