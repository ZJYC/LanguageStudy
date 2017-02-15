

import random

Japan = [   "しゆうまつ",\
            "スケート",\
            "あじ",\
            "まいかい",\
            "つうきん",\
            "ふね",\
            "きじ",\
            "へいてんじこく",\
            "そつぎようしき",\
            "ちがいます",\
            "こみます",\
            "きまります",\
            "しらせます",\
            "たしかめます",\
            "こい",\
            "うすい",\
            "はやい",\
            "おそい",\
            "たぶん",\
            "とうきようえき"]
China = [   "周末",\
            "滑冰",\
            "味道",\
            "每次",\
            "通勤",\
            "船",\
            "布料",\
            "关门时间",\
            "毕业典礼",\
            "不同",\
            "拥挤",\
            "决定",\
            "告诉",\
            "弄清",\
            "口味重浓",\
            "轻薄",\
            "早",\
            "晚慢",\
            "可能",\
            "东京站"]
#The Correct index
Correct = []
n = 0
Retry = 0

print("Japan vocabulary chapter 23 --primary")
mode = input("Please select test mode...")
#日文到中文
if mode in ["JC"]:
    print ("Japan --> China")
    input()
    while 1 :
        while 1 :
            print("\r\n"*100)
            if len(Correct) == len(Japan):
                break
            n = int(random.uniform(0,len(Japan)))
            if n in Correct:
                pass
            else:
                Correct.append(n)
                break
        while 1 :
            print("Jppan is : ",Japan[n])
            Input = input()
            if Input == China[n]:
                print ("!!!Right!!!")
                print("Remain....",len(Japan) - len(Correct))
                input()
                break
            else:
                Retry = Retry + 1
                if Retry < 4:
                    pass
                else:
                    print("!!!Error!!!!")
                    print(China[n])
                    input("Remember??????")
                    Retry = 0
                    Correct.remove(n)
                    break
        if len(Correct) == len(Japan):
            print("!!!You finished..!!!!")
            break
else:
    print ("China --> Japan")
    input()
    while 1 :
        while 1 :
            print("\r\n"*100)
            if len(Correct) == len(Japan):
                break
            n = int(random.uniform(0,len(Japan)))
            if n in Correct:
                pass
            else:
                Correct.append(n)
                break
        while 1 :
            print("China is : ",China[n])
            Input = input()
            if Input == Japan[n]:
                print ("!!!Right!!!")
                print("Remain....",len(Japan) - len(Correct))
                input()
                break
            else:
                Retry = Retry + 1
                if Retry < 4:
                    pass
                else:
                    print("!!!Error!!!!")
                    print(Japan[n])
                    input("Remember??????")
                    Retry = 0
                    Correct.remove(n)
                    break
        if len(Correct) == len(Japan):
            print("!!!You finished..!!!!")
            break













































