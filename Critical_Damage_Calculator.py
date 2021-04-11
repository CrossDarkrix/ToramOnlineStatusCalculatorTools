from math import floor as flr

print('クリティカルダメージ計算ツール\n')

try:
	BasicSTR = 150 + (int(input('STR値(ステータス): ')) / 5)
except:
	BasicSTR = 150 + (255 / 5)
	
try:
	CriticalDamage = int(input('合計クリティカルダメージ: '))
except:
	CriticalDamage = 1
try:
	CriticalDamage_Percent = BasicSTR * (int(input('合計クリティカルダメージ(%): ')) / 100)
except:
	CriticalDamage_Percent = 1

AllCriticalDamage = BasicSTR + CriticalDamage + flr(CriticalDamage_Percent)
print("\nあなたのクリティカルダメージは: {CRTDAMAGE}です".format(CRTDAMAGE=flr(AllCriticalDamage)))
input()