
import random
import time

#   0:normal Completion question
#   1:
#   2:
#
filename = "Chapter-19.txt"
Completion_question = [[0,"动___ ___:表示否定的命令",["ないで","ください"]],\
                       [0,"へやの かぎ を ___ ___:请别忘了房间钥匙",["わすれないで","ください"]],\
                       [0,"むりを し ___ ___:请不要勉强",["ないで","ください"]],\
                       [0,"动___ ___:表示必须,把ない替换成___ ___",["なければ","なりません","なければ","なりません"]],\
                       [0,"りさんは きよう はやく かえら ___ ___:小李今天必须早点回家",["なければ","なりません"]],\
                       [0,"この くすりは まいにち のま ___ ___:这个要必须每天吃",["なければ","なりません"]],\
                       [0,"动___ ___:表示不做某事也可以,将ない替换成___ ___",["なくても","いいです","なくても","いいです"]],\
                       [0,"あした は ざんぎようし ___ ___:明天不加班也行",["なくても","いいです"]],\
                       [0,"あわて ___ ___:不要慌慌张张的！",["なくても","いいですよ"]],\
                       
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





















