# -*- coding: utf-8 -*-

import sys, math

defCRT = int("25")

# ユーザー入力
try:
	Device = input("◇ご使用端末は？iOS(1) 又は Android(2)? : ")
except:
	Device = "1"

print('\n\t\t\t[キャラのステータス]\n')
try:
	StatusCRT = int(input("◇ステータス(CRT) : "))
except:
	StatusCRT = int("1")
try:
	SkillCRT = int(input("◇クリティカルUp Lv : "))
except:
	SkillCRT = int("1")
print('\n\t\t\t[装備による補正]\n')
try:
	EQCRT = int(input("◇クリティカル率+ : "))
except:
	EQCRT = int("0")
try:
	EQsCRT = int(input("◇クリティカル率(%)+ : "))
except:
	EQsCRT = int("0")

# クリティカルUp のスキル毎のクリティカル率判定

if SkillCRT == 1:
	SCr = 1
if SkillCRT == 2:
	SCr = 1
if SkillCRT == 3:
	SCr = 2
if SkillCRT == 4:
	SCr = 2
if SkillCRT == 5:
	SCr = 3
if SkillCRT == 6:
	SCr = 3
if SkillCRT == 7:
	SCr = 4
if SkillCRT == 8:
	SCr = 4
if SkillCRT == 9:
	SCr = 5
if SkillCRT == 10:
	SCr = 5

# iOSとAndroidで分けた計算式

if Device == "1":
	DeviceCals = int(math.floor((defCRT+math.floor(StatusCRT/3.3999))*((1+0.01*EQsCRT)*100)/100)+EQCRT+SCr)
else:
	if Device == "2":
		DeviceCals = int(math.floor((defCRT+math.floor(StatusCRT/3.4001))*((1+0.01*EQsCRT)*100)/100)+EQCRT+SCr) 
	else:
		sys.exit('入力エラーです')

Criticals = str(DeviceCals)


print("\n◇あなたのクリティカル率は" + Criticals + "%です")
input()