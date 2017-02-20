
import random
import time

#   0:normal Completion question
#   1:
#   2:
#
filename = "Chapter-22.txt"
Completion_question = [[0,"___  ___  ___：表示过去的经历",["动词た型","ことが","あります"]],\
                       [0,"た型的变换方式是て型的て->___ で->___",["た","だ"]],\
                       [0,"わたしは すきやきを___ ___ ___：我吃过日式牛肉火锅",["たべた","ことが","あります"]],\
                       [0,"ベキン へ ___ ___ ___か：你去过北京吗？",["いつた","ことが","あります"]],\
                       [0,"いいえ いちども ___ ___ ___せん：没有，一次也没去过",["いつた","ことが","あります"]],\
                       [0,"___ ___:一个动作在另一个动作之后发生",["动词た型","あとで"]],\
                       [0,"かいしやが ___ ___ のみに いきます:公司下班后去喝酒",["おわつた","あとで"]],\
                       [0,"えいが を ___  ___,しよくじを しました:看完电影后吃了饭",["みた","あとで"]],\
                       [0,"___ ___ ___:在两种食物中进行选择时。",["动词た型","ほうが","いいです"]],\
                       [0,"もつと やさいを ___ ___ ___よ:还是多吃点蔬菜好啊",["たべた","ほうが","いいです"]],\
                       [0,"そんなに ___ ___ ___よ:别那么慌张啊",["あわてない","ほうが","いいです"]],\
                       [0,"なにか たべ_____:吃点什么吗",["ましようか"]],\
                       [0,"にもつを まち____:我来帮你拿行李吧",["ましようか"]],\
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





















