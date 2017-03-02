
import random
import time

#   0:normal Completion question
#   1:
#   2:
#
filename = "Chapter-18.txt"
Completion_question = [[0,"___ ___ :表示性质或状态的变化，一类形词尾的い变为___再加___",["一类形","なります","く","なります"]],\
                       [0,"だんだん あたたか ___ ___:天气渐渐转暖",["く","なります"]],\
                       [0,"けいたいでんわ は ちいさ___ ___:手机变小了",["く","なります"]],\
                       [0,"パソコン は やす ___ ___:个人电脑便宜了",["く","なります"]],\
                       [0,"一类形 ___:因主语的意志性动作而引起食物发生变化，い变为___再加___",["します","く","します"]],\
                       [0,"テレビの おとを おおき ___ ___:把电视机的声音开大一些",["く","します"]],\
                       [0,"ジユースを つめた ___ ___:把果汁冰镇一下",["く","します"]],\
                       [0,"二类形/名 ___ ___:性质或状态的变化",["に","なります"]],\
                       [0,"もう げんき___ ___:已经恢复健康了",["に","なります"]],\
                       [0,"らいねん しやかいじん ___ ___:来年将成为社会的一员",["に","なります"]],\
                       [0,"二类形/名 ___ ___:因主语的意志性动作而引起的变化",["に","します"]],\
                       [0,"へやを きれい ___ ___:请把房间打扫干净",["に","してください"]],\
                       [0,"かいぎしつを きんえん ___ ___:会议室里禁烟",["に","します"]],\
                       [0,"一类形/二类形 ___ ___:对两个以上的事物的性质进行比较之后，认为其中一个比较好时",["ほうが","いいです"]],\
                       [0,"りよこうのにもつは かるい ___ ___:旅行行李还是轻点好",["ほうが","いいです"]],\
                       [0,"へやは ひろい ___ ___:房子还是宽敞一点好",["ほうが","いいです"]],\
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





















