# -*- coding: utf-8 -*-

print("装備による異常耐性率の計算ツール\n(MEN: 255の場合)\n")
try:
	stutus = int(input("MEN: "))
except:
	print("MEN = 255")
	stutus = 255
try:
	MENADD_1 = int(input("MEN装備(%) part 1: "))
except:
	MENADD_1 = int("0")
try:
	MENADD_2 = int(input("MEN装備(%) part 2: "))
except:
	MENADD_2 = int("0")
try:
	MENADD_3 = int(input("MEN装備(%) part 3: "))
except:
	MENADD_3 = int("0")
try:
	MENADD_4 = int(input("MEN装備(%) part 4: "))
except:
	MENADD_4 = int("0")
try:
	MENADD_5 = int(input("MEN装備(%) part 5: "))
except:
	MENADD_5 = int("0")
try:
	MENADD_6 = int(input("MEN装備(%) part 6: "))
except:
	MENADD_6 = int("0")
try:
	MENADD_7 = int(input("MEN装備(%) part 7: "))
except:
	MENADD_7 = int("0")
try:
	MENADD_8 = int(input("MEN装備(%) part 8: "))
except:
	MENADD_8 = int("0")

fmen = str(int(MENADD_1 + MENADD_2 + MENADD_3 + MENADD_4 + MENADD_5 + MENADD_6 + MENADD_7 + MENADD_8 +(stutus / 3.4)))
print("\nあなたの異常耐性率は" + fmen + "%です")
input()
