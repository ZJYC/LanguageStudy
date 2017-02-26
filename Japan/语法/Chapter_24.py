
import random
import time

#   0:normal Completion question
#   1:
#   2:
#
filename = "Chapter-24.txt"
Completion_question = [[0,"___ ___ ___:表示说话人的思考内容.",["小句（简体形）","と","おもいます"]],\
                       [0,"たなかさんは___ ___ ___:我想田中先生不回来了.",["こない","と","おもいます"]],\
                       [0,"このほんは___ ___ ___:我觉得这本书有意思.",["おもしろい","と","おもいます"]],\
                       [0,"にほんは___ ___ ___:我觉得日本很干净.",["きれいだ","と","おもいます"]],\
                       [0,"___ ___ ___ ___ ___:转述他人所说的话.",["名","は","小句（简体形）","と","いいました"]],\
                       [0,"もりさん は ちゆうごくご の しかん は ___ ___ ___:森先生说汉语考试很难.",["むずかしかつた","と","いいました"]],\
                       [0,"おのさんは りさんに ちようと ___ ___ ___:小野女士跟小李说想休息一下.",["やすみたい","と","いいました"]],\
                       
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





















