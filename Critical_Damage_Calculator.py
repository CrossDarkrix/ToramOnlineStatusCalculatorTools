#!/usr/bin/env python3
from math import floor as flr
import sys
print('クリティカルダメージ計算ツール\n')

try:
	STR = int(input('STR値(ステータス): '))
	StrPercent = STR * (int(input('STR値(%)の合計値: ')) / 100)
	AllSTR = 150 + ((StrPercent + STR) / 5)
	CRtSTR = 150 + (STR / 5)
except ValueError:
	AllSTR = 150 + (255 / 5)
	CRtSTR = 150 + (255 / 5)
except KeyboardInterrupt:
	print()
	sys.exit(0)
try:
	CriticalDamage = int(input('合計クリティカルダメージ: '))
except ValueError:
	CriticalDamage = 1
except KeyboardInterrupt:
	print()
	sys.exit(0)
try:
	CriticalDamage_Percent = CRtSTR * (int(input('合計クリティカルダメージ(%): ')) / 100)
except ValueError:
	CriticalDamage_Percent = 1
except KeyboardInterrupt:
	print()
	sys.exit(0)

AllCriticalDamage = AllSTR + CriticalDamage + flr(CriticalDamage_Percent)
print("\nあなたのクリティカルダメージは: {CRTDAMAGE}です".format(CRTDAMAGE=flr(AllCriticalDamage)))
