
import random
import time

#   0:normal Completion question
#   1:
#   2:
#
filename = "Chapter-23.txt"
Completion_question = [[0,"___ ___ ___します:表示列举若干种有代表性的动作时.",["动词たり","动词たり","します"]],\
                       [0,"おのさん は 休みのひ ___ ___ ___:休息日，小野女士有时去散步，有时去买东西.",["さんぽしたり","かいものにいつたり","します"]],\
                       [0,"ひこうき の チケツト は ___ ___ ___:飞机票有时贵有时便宜.",["たかかつたり","やすかつたり","です"]],\
                       [0,"この こうえん は じかんに よつて ___ ___ ___:根据时间，这个公园有时寂静，有时热闹.",["しずかだつたり","にぎやかだつたり","です"]],\
                       [0,"にほんご の せんせい は ___ ___ ___:日语老师既有中国人，也有日本人",["ちゆうごくじんだつたり","にほんじんだつたり","です"]],\
                       [0,"小句+___:表示某种不确定的内容",["か"]],\
                       [0,"将不包含疑问词的疑问句作为一个长句中的一部分时，将动词、一类形容词的敬体形变为简体型，并在其后面加上___ ___",["か","どうか"]],\
                       [0,"わたしは ことしのなつ ぺキン へ ___ ___ わかりません:我今年去不去北京还不知道",["いくか","どうか"]],\
                       [0,"わたしは このりようりが ___ ___ しりません:我不知道这道菜辣不辣",["からいか","どうか"]],\
                       [0,"将包含なに、だれ、どこ等的疑问句，作为一个长句中的一部分使用时，须将疑问词小句的动词、一类形容词的敬体形变为简体形，再加___",["か"]],\
                       [0,"どの りようりが ___ しりません:不知道那道菜辣",["からいか"]],\
                       [0,"基本意思相当于汉语的“根据。。。”",["～に","よつて"]],\
                       [0,"けつこんしき のやりかた は くに___ ___ ちがいます:结婚典礼的形式因国而异",["に","よつて"]],\
                       [0,"___ ___:突然想起某事或突然想起某事时的表达",["あつ","そうだ"]],\
        ]
#------------------------------------------------------------------------------------
flag = []
def GetUniNum():
    while True:
        if len(flag) == len(Completion_question):
            return "OVER"
        n = int(random.uniform(0,len(Completion_question)))
        if n in flag:
            pass
        else:
            flag.append(n)
            return n
#------------------------------------------------------------------------------------
def CompletionOnce(j):
    "Test a Completion question,return the result to the caller..."
    if Completion_question[j][0] == 0:
        print("-------------------------------------------------------------------")
        print(Completion_question[j][1])
        print("-------------------------------------------------------------------")
        answer = input("Your answer(splited by space):\r\n")
        if Completion_question[j][2] == answer.split():
            return True
        else:
            return False
#------------------------------------------------------------------------------------
error = []
def Completion():
    while True:
        #Get random number
        n = GetUniNum()
        if n == "OVER":break
        retry = 0
        while True:
            #test
            if CompletionOnce(n) == True:
                print("----RIGHT----")
                break
            else:
                retry = retry + 1
                if retry >= 4:
                    print("----ERROR----")
                    print(Completion_question[n])
                    error.append(Completion_question[n])
                    break
                
    print("Test finished...The following needed to reinforce...")
    for e in error:print(e)
    fo = open(filename,"a")
    try:
        fo.write(time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time())))
        fo.write("\r\n")
        for e in error:fo.write(str(e) + "\r\n")
        fo.write("\r\n")
    finally:
        fo.close()
        input()

#------------------------------------------------------------------------------------
if __name__ == "__main__":
    Completion()





















