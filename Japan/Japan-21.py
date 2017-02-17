

import random

Japan = [   "ことば"\
            "メールアドレス"\
            "れんきゆう"\
            "ゴールデンウイーク"\
            "おわり"\
            "きゆうけいじかん"\
            "きようげき"\
            "きつぷ"\
            "からだ"\
            "じしん"\
            "どろぼう"\
            "ちゆうしやじよう"\
            "わたします"\
            "おくれます"\
            "かんがえます"\
            "しらべます"\
            "きます"\
            "よやくします"\
            "かんしやします"\
            "うんどうします"\
            "せんたくします"\
            "ほうこくします"\
            "あぶない"\
            "それとも"\
            "とうきようタワー"\
            "そんなに"]
China = [   "语言"\
            "邮件地址"\
            "连休"\
            "黄金周"\
            "结束"\
            "休息时间"\
            "京剧"\
            "票"\
            "身体"\
            "地震"\
            "盗贼"\
            "停车场"\
            "交给"\
            "迟到"\
            "考虑"\
            "调查"\
            "穿"\
            "预定"\
            "感谢"\
            "运动"\
            "洗涤"\
            "报告"\
            "危险"\
            "或者"\
            "东京塔"\
            "那么"]
#The Correct index
Correct = []
n = 0
Error = 0
Retry = 0

print("Japan vocabulary chapter 23 --primary")
if len(Japan) != len(China) : 
    print("China != Japan....")
    while True : input()
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
                Retry = 0
                input()
                break
            else:
                Retry = Retry + 1
                if Retry < 4:
                    pass
                else:
                    Error = Error + 1
                    print("!!!Error!!!!")
                    print(China[n])
                    input("Remember??????")
                    Retry = 0
                    Correct.remove(n)
                    break
        if len(Correct) == len(Japan):
            print("!!!You finished..!!!!")
            print("Error times is : ",Error)
            print("\r\n"*15)
            input()
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
                Retry = 0
                input()
                break
            else:
                Retry = Retry + 1
                if Retry < 4:
                    pass
                else:
                    Error = Error + 1
                    print("!!!Error!!!!")
                    print(Japan[n])
                    input("Remember??????")
                    Retry = 0
                    Correct.remove(n)
                    break
        if len(Correct) == len(Japan):
            print("!!!You finished..!!!!")
            print("Error times is : ",Error)
            print("\r\n"*15)
            input()
            break













































