#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
トーラムオンライン 安定率計算機
'''

from math import floor as math_floor
import sys

def One_handed_sword(): # 片手剣
    ALL_Equipment = int(input('装備の安定率の合計値: '))
    DEX = int(input('ステータスのDEX値: '))
    STR = int(input('ステータスのSTR値: '))
    Result = math_floor(ALL_Equipment + (DEX * 3 + STR) / 40)
    print('あなたの安定率は: {One_H_STabillity}%です。'.format(One_H_STabillity=Result))

def Tow_handed_sword(): # 両手剣
    ALL_Equipment = int(input('装備の安定率の合計値: '))
    DEX = int(input('ステータスのDEX値: '))
    Result = math_floor(ALL_Equipment + DEX / 10)
    print('あなたの安定率は: {Tow_H_STabillity}%です。'.format(Tow_H_STabillity=Result))

def Dual_sword(): # 双剣
    ALL_Equipment = int(input('装備の安定率の合計値: '))
    DEX = int(input('ステータスのDEX値: '))
    STR = int(input('ステータスのSTR値: '))
    Result = math_floor(ALL_Equipment + (DEX * 3 + STR) / 40)
    print('あなたの安定率は: {Dual_H_STabillity}%です。'.format(Dual_H_STabillity=Result))

def Knuckle(): # 拳
    ALL_Equipment = int(input('装備の安定率の合計値: '))
    DEX = int(input('ステータスのDEX値: '))
    Result = math_floor(ALL_Equipment + DEX / 40)
    print('あなたの安定率は: {Knuckle_STabillity}%です。'.format(Knuckle_STabillity=Result))
    
def Halberd(): # 旋風槍
    ALL_Equipment = int(input('装備の安定率の合計値: '))
    DEX = int(input('ステータスのDEX値: '))
    STR = int(input('ステータスのSTR値: '))
    Result = math_floor(ALL_Equipment + (DEX + STR) / 20)
    print('あなたの安定率は: {Halberd_STabillity}%です。'.format(Halberd_STabillity=Result))

def Katana(): # 刀
    ALL_Equipment = int(input('装備の安定率の合計値: '))
    DEX = int(input('ステータスのDEX値: '))
    STR = int(input('ステータスのSTR値: '))
    Result = math_floor(ALL_Equipment + (DEX + STR * 3) / 40)
    print('あなたの安定率は: {Katana_STabillity}%です。'.format(Katana_STabillity=Result))

def Staff(): # 杖
    ALL_Equipment = int(input('装備の安定率の合計値: '))
    STR = int(input('ステータスのSTR値: '))
    Result = math_floor(ALL_Equipment + STR / 20)
    print('あなたの安定率は: {Staff_STabillity}%です。'.format(Staff_STabillity=Result))

def Magic_Devices(): # 魔導具
    ALL_Equipment = int(input('装備の安定率の合計値: '))
    DEX = int(input('ステータスのDEX値: '))
    Result = math_floor(ALL_Equipment + DEX / 10)
    print('あなたの安定率は: {MD_STabillity}%です。'.format(MD_STabillity=Result))

def Bow(): # 弓
    ALL_Equipment = int(input('装備の安定率の合計値: '))
    Arrow_STabillity = int(input('矢の安定率: '))
    DEX = int(input('ステータスのDEX値: '))
    STR = int(input('ステータスのSTR値: '))
    Result = math_floor(ALL_Equipment + Arrow_STabillity + (DEX + STR) / 20)
    print('あなたの安定率は: {Bow_STabillity}%です。'.format(Bow_STabillity=Result))

def BowGun(): # 自動弓
    ALL_Equipment = int(input('装備の安定率の合計値: '))
    Arrow_STabillity = int(input('矢の安定率: '))
    STR = int(input('ステータスのSTR値: '))
    Result = math_floor(ALL_Equipment + Arrow_STabillity / 2 + STR / 20)
    print('あなたの安定率は: {Bowgun_STabillity}%です。'.format(Bowgun_STabillity=Result))
    
def Menu():
    Menus = """トーラム 安定率 計算機 v1.0
	1. 片手剣
	2. 両手剣
	3. 双剣
	4. 拳
	5. 槍
	6. 刀
	7. 杖
	8. 魔導具
	9. 弓
	10. 自動弓
(「装備の安定率の合計値」には武器についている「ATK (??%)」の()内の数値と装備で盛っている安定率を入れてください。)\n"""
    return Menus

def main():
    print(Menu())

    Selector = str(input('計算したい職の番号: '))

    if Selector == '1':
        print('片手剣を選択しました\n')
        One_handed_sword()
    elif Selector == '2':
        print('両手剣を選択しました\n')
        Tow_handed_sword()
    elif Selector == '3':
        print('双剣を選択しました\n')
        Dual_sword()
    elif Selector == '4':
        print('拳を選択しました\n')
        Knuckle()
    elif Selector == '5':
        print('旋風槍を選択しました\n')
        Halberd()
    elif Selector == '6':
        print('刀を選択しました\n')
        Katana()
    elif Selector == '7':
        print('杖を選択しました\n')
        Staff()
    elif Selector == '8':
        print('魔導具を選択しました\n')
        Magic_Devices()
    elif Selector == '9':
        print('弓を選択しました\n')
        Bow()
    elif Selector == '10':
        print('自動弓を選択しました\n')
        BowGun()
    else:
        print('番号を入力してください')
        sys.exit(0)

if __name__ == '__main__':
    main()