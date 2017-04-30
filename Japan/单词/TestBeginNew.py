
import time
import random
#-----------------------------------------------------------------------------------#
class Calculate():
    def __init__(self,NumOfWords):
        self.TimeStart,self.TimeEnded,self.RandomPool=0,0,list(range(0,NumOfWords))
        self.ErrorCounter=0
    def Score(self,ErrorMap):        
        for i in ErrorMap:self.ErrorCounter+=i
        return round((len(ErrorMap)-self.ErrorCounter)/len(ErrorMap),2)*100
    def TimeConsume(self):
        return self.TimeEnded-self.TimeStart
    def TimeBegin(self):
        self.TimeStart=time.time()
    def TimeEnd(self):
        self.TimeEnded=time.time()
    def GetUniqueRandom(self):
        if len(self.RandomPool) > 0:
            RandomNum=random.choice(self.RandomPool)
            self.RandomPool.remove(RandomNum)
            return RandomNum
        else:
            return None
    def ReturnToPool(self,ReturnedValue):
        self.RandomPool.append(ReturnedValue)
    def GetRemain(self):
        return len(self.RandomPool)

#-----------------------------------------------------------------------------------#
class Error(Calculate):
    def __init__(self,NumOfWords,FileNameToStorage):
        self.ErrorMap=[0]*NumOfWords
        self.FileNameToStorage=FileNameToStorage
        Calculate.__init__(self,NumOfWords)
    def Log(self,IndexOfWords):
        self.ErrorMap[IndexOfWords]+=1
    def Show(self):
        for i,e in enumerate(self.ErrorMap):
            if e != 0:
                SplitedStr=str(Words[i]).split(".")
                PianJia,PingJia,HanZi=0,0,0
                if len(SplitedStr) == 2:
                    PianJia=SplitedStr[0]
                    PingJia=None
                    HanZi=SplitedStr[1]
                if len(SplitedStr) == 3:
                    PianJia=SplitedStr[0]
                    PingJia=SplitedStr[1]
                    HanZi=SplitedStr[2]
                print(str(PianJia).ljust(40),str(PingJia).ljust(40-len(PingJia)),str(HanZi).ljust(40-len(HanZi)),str(e).center(5))
    def ShowAll(self):
        print("Time consume:%s"%time.strftime("%M-%S",time.localtime(self.TimeConsume())))
        print("Score:%s"%str(self.Score(self.ErrorMap)).center(10),"明细如下:")
        print("-----------------------------------------------------------------------------------------")
        self.Show()
        print("-----------------------------------------------------------------------------------------")
    def Storage(self,TestMode):
        fo=open(self.FileNameToStorage,"a")
        try:
            fo.write("\r\n-----------------------------------------------------------------------------------------\r\n")
            fo.write(time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time())))
            fo.write("\r\n测试用时:%s"%time.strftime("%M-%S",time.localtime(self.TimeConsume())))
            fo.write("\r\n分数:" + str(self.Score(self.ErrorMap)).center(10))
            fo.write("\r\n" + "Mode : " + str(TestMode) + "\r\n")
            for i,e in enumerate(self.ErrorMap):fo.write(str(Words[i]).ljust(40)+str(e).center(5) + "\r\n")
            fo.write("-----------------------------------------------------------------------------------------\r\n")
        finally:
            fo.close()
#-----------------------------------------------------------------------------------#
class Test(Error):
    def __init__(self):
        Error.__init__(self,len(Words),filename)
    def SelectMode(self):
        print("|---------------------------------------|")
        print("|模式0:片-平-中                         |")
        print("|模式1:中-平-片                         |")
        print("|模式2:随机                             |")
        print("|请选择编号(例如1)....                  |")
        print("|---------------------------------------|")
        while True:
            try:
                self.TestMode = int(input())
                if self.TestMode in [0,1,2]:break
                else:print("模式选择错误,请重新输入...")
            except:
                self.TestMode = 0
                print("使用默认模式(0)...")
                break
    def TestOnce(self,IndexOfWords,TestMode):
        SplitedStr=str(Words[IndexOfWords]).split(".")
        PianJia,PingJia,HanZi=0,0,0
        if len(SplitedStr) == 2:
            PianJia=SplitedStr[0]
            PingJia=None
            HanZi=SplitedStr[1]
        if len(SplitedStr) == 3:
            PianJia=SplitedStr[0]
            PingJia=SplitedStr[1]
            HanZi=SplitedStr[2]
        if TestMode == 2:TestMode=random.choice([0,1])
        if TestMode == 0:
            if PingJia != None:print("\r\n"+"PianJia:{%s},Please input HanZi".center(60,'-')%PianJia)
            else:print("\r\n"+"PianJia:{%s},Please Inpute HanZi".center(60,'-')%PianJia)
            for i in list(range(1,4)):
                Input=str(input())
                if Input in HanZi and len(Input) != 0:
                    print("You do a good work".center(60,'*'));
                    print("\r\n"+"PianJia:{%s} PingJia:{%s} HanZi:{%s}".center(60,'-')%(PianJia,PingJia,HanZi))
                    print("Remain...%s"%GetRemain())
                    return True
                else:
                    print("Try again".center(60,'*'))
            else:
                print("\r\n"+"You need to work harder".center(60,'*'));
                print("\r\n"+"PianJia:{%s} PingJia:{%s} HanZi:{%s}".center(60,'-')%(PianJia,PingJia,HanZi))
                while True:
                    Input=str(input("Input again..."))
                    if Input in HanZi and len(Input) != 0:
                        return False
                    else:
                        print("WTF")
                return False
        if TestMode == 1:
            if PingJia != None:print("\r\n"+"HanZi:{%s},Please input PianJia and PingJia".center(60,'-')%HanZi)
            else:print("\r\n"+"HanZi:{%s},Please input PianJia".center(60,'-')%PianJia)
            for i in list(range(0,4)):
                Input=str(input())
                if Input in PianJia+PingJia and len(Input) != 0:
                    print("You do a good work".center(60,'*'));
                    print("Remain...%s"%GetRemain())
                    return True
                else:
                    print("Try again".center(60,'*'))
            else:
                print("\r\n"+"You need to work harder".center(60,'*'));
                print("\r\n"+"PianJia:{%s} PingJia:{%s} HanZi:{%s}".center(60,'-')%(PianJia,PingJia,HanZi))
                return False
    def TestAll(self):
        self.SelectMode()
        self.TimeBegin()
        while True:
            IndexOfWords=self.GetUniqueRandom()
            if IndexOfWords == None:
                self.TimeEnd()
                self.ShowAll()
                self.Storage(self.TestMode)
                return
            Res=self.TestOnce(IndexOfWords,self.TestMode)
            if Res == False:
                self.Log(IndexOfWords)
                self.ReturnToPool(IndexOfWords)
#---------------------------------------------------------

                
if __name__ == "__main__":
    Chapter=int(input("请输入你要学习的章节(例如17)...\r\n"))
    if Chapter == 29:from CardNew29 import *
    if len(Words)==0:
        print("Zero Length...Please check again...");
        while(True):input()
    test=Test()
    test.TestAll()




