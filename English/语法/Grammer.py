
import random
import time

#   0:normal Completion question
#   1:
#   2:
#
filename = "Grammer.txt"
Completion_question = [[0,"现在完成进行时:S+___+___+____",["have","been","Ving"]],\
                       [0,"过去完成进行时:S+___+___+____",["had","been","Ving"]],\
                       [0,"将来完成进行时:S+___+___+___+____",["will","have","been","Ving"]],\
                       [0,"现在完成时:S+___+___",["have","过去分词"]],\
                       [0,"过去完成时:S+___+___",["had","过去分词"]],\
                       [0,"将来完成时:S+___+___+___",["will","have","过去分词"]],\
                       [0,"现在进行时:S+___+___(am/is/are)",["be","Ving"]],\
                       [0,"过去进行时:S+___+___(was/were)",["be","Ving"]],\
                       [0,"将来进行时:S+___+___+___",["will","be","Ving"]],\
                       [0,"将来时:S+___+___",["will/shall","V"]],\
                       [0,"虚拟-于现在事实相反:if+___,主语+___+___",["一般过去时","would","V"]],\
                       [0,"虚拟-于过去事实相反:if+___,主语+___+___",["过去完成时","would","have-pp"]],\
                       [0,"虚拟-于将来事实相反(几乎不可能发生):if+___,主语+___+___",["一般过去时","would","V"]],\
                       [0,"虚拟-于将来事实相反(含有万一之意  ):if+___+___,主语+___+___",["should","V","would","V"]],\
                       #例句
                       [0,"he ___ ___ ___ car for 200 years:他造车200年-_-",["has","been","making"]],\
                       [0,"he ___ ___ ___ games before you got home:在你回家之前他一直在玩游戏",["had","been","playing"]],\
                       [0,"he ___ ___ ___ waiting for you since you keeping talking to like this way:你一直这样说话我就不会等你了",["won't","have","been"]],\
                       [0,"he ___ ___ his hoseworks:他已经完成了作业",["have","finished"]],\
                       [0,"he ___ ___ his hoseworks before you visit me:在你看我之前，他已经完成了作业",["had","finished"]],\
                       [0,"They ___ ___ ___ the meeting by now:到现在，他们或许已经完成了会议",["will","have","finished"]],\
                       [0,"I ___ ___ to pick you up:我正过去接你",["am","coming"]],\
                       [0,"I ___ ___ a novel this morning:今天造成我在读报纸",["was","reading"]],\
                       [0,"At this time tommorrow,I ___ ___ ___ at home:明天的这个时候，我正在睡觉",["will","be","sleeping"]],\
                       [0,"If I ___ you,I ___ ___ his suggestion:如果我是你，我会接受他的建议",["were","would","accept"]],\
                       [0,"If you ___ ___ here yesteday,you ___ ___ ___ her:如果昨天你在这里，你会见到他的",["had","been","would","have","seen"]],\
                       [0,"If the sun ___ to disapper,you ___ win this game:如果太阳消失，你就会赢得此游戏",["were","would"]],\
                       [0,"If mike ___ ___ tommorrow,I ___ ___ him to the best restaurant:如果mike明天来，我将会带它去最好的餐馆",["would","come","will","bring"]],\
                       #[0,"If the sun ___ to disapper,you ___ win this game:如果太阳消失，你就会赢得此游戏",["were","would"]],\
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
                print("--------------------------------RIGHT--------------------------------")
                break
            else:
                retry = retry + 1
                if retry >= 4:
                    print("--------------------------------ERROR--------------------------------")
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





















