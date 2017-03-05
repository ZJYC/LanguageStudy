
import random
import time
#------------------------------------------------------------------------------------
def GetUniNum():
    "获取唯一随机数"
    while True:
        if len(flag) == len(Completion_question):
            return None
        n = int(random.uniform(0,len(Completion_question)))
        if n in flag:
            pass
        else:
            flag.append(n)
            return n
#------------------------------------------------------------------------------------
def CompletionOnce(j):
    if Completion_question[j][0] == 0:
        print("-------------------------------------------------------------------")
        print(Completion_question[j][1])
        print("-------------------------------------------------------------------")
        answer = input("你的答案是(用空格区分):\r\n")
        if Completion_question[j][2] == answer.split():return True
        else:return False
#------------------------------------------------------------------------------------
error = []
def Completion():
    while True:
        #Get random number
        n = GetUniNum()
        if n == None:break
        retry = 0
        while True:
            if CompletionOnce(n) == True:
                print("正确...")
                break
            else:
                retry = retry + 1
                if retry >= 4:
                    print("错误...")
                    print(Completion_question[n])
                    error.append(Completion_question[n])
                    break
                
    print("测试完成,如下需要加强...")
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
    if chapter == 17:from G17 import *
    if chapter == 18:from G18 import *
    if chapter == 19:from G19 import *
    if chapter == 20:from G20 import *
    if chapter == 21:from G21 import *
    if chapter == 22:from G22 import *
    if chapter == 23:from G23 import *
    if chapter == 24:from G24 import *
    Completion()





















