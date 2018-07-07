print("会計いくら？")
bi_runedan = 200
bi_rukazu = 2
bi_rukaikei = bi_runedan * bi_rukazu
otumaminedan = 100
otumamikazu = 1
otumamikaikei = otumaminedan * otumamikazu
yakitorinedan = 100
yakitorikazu = 2
waribikiritu = 1 - 0.2
yakitorikaikei = (yakitorinedan * waribikiritu) * yakitorikazu
pointo = 150
kaikei = bi_rukaikei + otumamikaikei + yakitorikaikei - pointo
print(kaikei)
