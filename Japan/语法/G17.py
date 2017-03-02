
import random
import time

#   0:normal Completion question
#   1:
#   2:
#
filename = "Chapter-17.txt"
Completion_question = [[0,"___ ___ ___:表示愿望",["名","が","ほしいです"]],\
                       [0,"わたしは あたらしい ___ ___:我想有套新西服",["ようふくが","ほしいです"]],\
                       [0,"あなたは ___ ___:你想要什么",["なにが","ほしいですか"]],\
                       [0,"___ ___ ____ ____:相当于汉语的想的意思",["名","を","动","たいです"]],\
                       [0,"わたしは ___ ___:我想看电影",["えいがを","みたいです"]],\
                       [0,"きようは ___ ___:今天不想喝酒",["おさけを","のみたくないです"]],\
                       [0,"___ ___:表示提议:**好吗,,**怎么样,,",["动","ませんか"]],\
                       [0,"いつしよに おちやを___:一起喝茶好吗",["のみませんか"]],\
                       [0,"すこし ___:休息一下怎么样",["やすみませんか"]],\
                       [0,"___ ___:表示提议:**吧",["动","ましよう"]],\
                       [0,"ちようと ___:休息一下吧",["やすみましよう"]],\
                       [0,"そろそろ ___:咱们快走吧",["いきましよう"]],\
                       [0,"疑问词+___:表示在任何情况下事态都相同",["でも"]],\
                       [0,"A:りさん なにを たべたいですかB:なに___いいです:什么都行",["でも"]],\
                       [0,"だれ___わかります:谁都明白",["でも"]],\
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
    chapter = int(input("Input the chapter you wanted..."))
    if chapter == 17:from Card17 import *
    if chapter == 18:from Card18 import *
    if chapter == 19:from Card19 import *
    if chapter == 20:from Card20 import *
    if chapter == 21:from Card21 import *
    if chapter == 22:from Card22 import *
    if chapter == 23:from Card23 import *
    if chapter == 24:from Card24 import *
    Completion()





















