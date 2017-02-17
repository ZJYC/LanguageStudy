

import random

Japan = [   "ハイキング",\
            "おわかれ",\
            "はなし",\
            "みおくり",\
            "あいだ",\
            "ほうりつ",\
            "おもいます",\
            "いいます",\
            "さがします",\
            "わらいます",\
            "やめます",\
            "きめます",\
            "ねぼうします",\
            "がいしゆつします",\
            "けんきゆうします",\
            "おかしい",\
            "いつぱい",\
            "すごい",\
            "とうとう",\
            "かならず",\
            "ぜつたいに",\
            "ば",\
            "おせわになりました",\
            "よろしくおつたえください",\
            "おげんきで",\
            "おきをつけて",\
            "さようなら",\
            "どうやつて",\
            "やくにたちます",\
            "おなかがいつぱいです"]
China = [   "郊游",\
            "分别",\
            "说话",\
            "送行",\
            "期间",\
            "法律",\
            "思考",\
            "说讲",\
            "寻找",\
            "笑",\
            "停止",\
            "决定",\
            "睡懒觉",\
            "外出",\
            "研究",\
            "滑稽",\
            "满",\
            "了不起",\
            "终究",\
            "一定",\
            "绝对",\
            "马",\
            "承蒙照顾",\
            "请代问好",\
            "请多保重",\
            "小心点",\
            "再见",\
            "怎样",\
            "有用",\
            "吃饱"]
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













































