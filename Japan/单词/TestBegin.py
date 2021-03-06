
import time

#---------------------------------------------------------
def get_uni_num():
    "获取随机数，确保本数字只出现一次"
    while True:
        if len(flag) == len(Japan):return None
        n = int(random.uniform(0,len(Japan)))
        if n in flag:pass
        else:
            flag.append(n)
            break
    #返回随机数
    return n
#---------------------------------------------------------
def LogError(num):
    "记录错误词条"
    "error 应由模块提供"
    #记录错误次数
    cnt[num] = cnt[num] + 1
    
    if num in error:return 1
    else:
        error.append(num)
        return None
#---------------------------------------------------------
def PrintError():
    "打印错误词条"
    global TimeStart
    global TimeEnd
    print("测试用时:%s"%time.strftime("%M-%S",time.localtime(TimeEnd-TimeStart)))
    print("本次测试分数：",str(GetScore()).center(10),"明细如下:")
    print("-----------------------------------------------------------------------------------------")
    for e in error:print(str(China[e]).ljust(30-len(China[e])),str(Japan[e]).ljust(30-len(Japan[e])),str(cnt[e]).ljust(5))
    print("-----------------------------------------------------------------------------------------")

#---------------------------------------------------------
def GetScore():
    "计算分数"
    Score = 100.0 - len(error) / len(Japan) * 100
    return round(Score,2)

#---------------------------------------------------------
def StorageError():
    
    "保存错误词条到文件"
    
    fo = open(filename,"a")
    try:
        fo.write("\r\n-----------------------------------------------------------------------------------------\r\n")
        fo.write(time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time())))
        fo.write("\r\n测试用时:%s"%time.strftime("%M-%S",time.localtime(TimeEnd-TimeStart)))
        fo.write("\r\n分数:" + str(GetScore()).center(10))
        fo.write("\r\n" + "Mode : " + str(mode) + "\r\n")
        for e in error:fo.write(str(China[e]).ljust(30-len(China[e])) + str(Japan[e]).ljust(30-len(Japan[e])) + str(cnt[e]).ljust(5) + "\r\n")
        fo.write("-----------------------------------------------------------------------------------------\r\n")
    finally:
        fo.close()

#---------------------------------------------------------
def TestOnce(num,mode):
    retry = 0
    if num == None:return 1
    if mode == 2:mode = int(random.uniform(0,2))
    if mode == 0:
        while True:
            print("日语单词是:",Japan[num])
            Input = input()
            if Input in China[num] and Input != "":
                if Input != China[num]:
                    print("完整的答案是:---",China[num],"---")
                print("!!正确!!","剩余词条数",len(Japan) - len(flag))
                input("按任意键继续...")
                break
            else:
                retry = retry + 1
                if retry < 4:pass
                else:
                    LogError(num)
                    print("!!!错误!!!","答案是:",China[num])
                    print("请照着抄写一边...")
                    while True:
                        Input = input()
                        if Input in China[num] and Input != "":
                            print("按任意键继续...")
                            break
                        else:print("!!ばかもの ですか!!")
                    Retry = 0
                    flag.remove(num)
                    break
    if mode == 1:
        while True:
            print("中文单词是:",China[num])
            Input = input()
            if Input in Japan[num] and Input != "":
                if Input != Japan[num]:
                    print("完整的答案是:---",Japan[num],"---")
                print("!!正确!!","剩余词条数",len(Japan) - len(flag))
                input("按任意键继续...")
                break
            else:
                retry = retry + 1
                if retry < 4:pass
                else:
                    LogError(num)
                    print("!!!错误!!!","答案是:",Japan[num])
                    print("请照着抄写一边...")
                    while True:
                        Input = input()
                        if Input in Japan[num] and Input != "":
                            print("按任意键继续...")
                            break
                        else:print("!!ばかもの ですか!!")
                    Retry = 0
                    flag.remove(num)
                    break
TimeStart,TimeEnd=0,0
if __name__ == "__main__":
    #global TimeStart
    #global TimeEnd
    TimeStart = time.time()
    chapter = int(input("请输入你要学习的章节(例如17)...\r\n"))
    #------------------------------------------------------
    if chapter == 0:from Card0 import *
    if chapter == 1:from Card1 import *
    if chapter == 2:from Card2 import *
    if chapter == 3:from Card3 import *
    if chapter == 4:from Card4 import *
    if chapter == 5:from Card5 import *
    if chapter == 6:from Card6 import *
    if chapter == 7:from Card7 import *
    if chapter == 8:from Card8 import *
    if chapter == 9:from Card9 import *
    if chapter == 10:from Card10 import *
    if chapter == 11:from Card11 import *
    if chapter == 12:from Card12 import *
    if chapter == 13:from Card13 import *
    if chapter == 14:from Card14 import *
    if chapter == 15:from Card15 import *
    if chapter == 16:from Card16 import *
    if chapter == 17:from Card17 import *
    if chapter == 18:from Card18 import *
    if chapter == 19:from Card19 import *
    if chapter == 20:from Card20 import *
    if chapter == 21:from Card21 import *
    if chapter == 22:from Card22 import *
    if chapter == 23:from Card23 import *
    if chapter == 24:from Card24 import *
    if chapter == 25:from Card25 import *
    if chapter == 26:from Card26 import *
    if chapter == 27:from Card27 import *
    if chapter == 28:from Card28 import *
    if chapter == 29:from Card29 import *
    if chapter == 30:from Card30 import *
    if chapter == 31:from Card31 import *
    if chapter == 32:from Card32 import *
    if chapter == 33:from Card33 import *
    if chapter == 34:from Card34 import *
    if chapter == 35:from Card35 import *
    if chapter == 36:from Card36 import *
    if chapter == 37:from Card37 import *
    if chapter == 38:from Card38 import *
    if chapter == 39:from Card39 import *
    if chapter == 40:from Card40 import *
    if chapter == 41:from Card41 import *
    if chapter == 42:from Card42 import *
    if chapter == 43:from Card43 import *
    if chapter == 44:from Card44 import *
    if chapter == 45:from Card45 import *
    if chapter == 46:from Card46 import *
    if chapter == 49:from Card49 import *
    
    #------------------------------------------------------
    if len(China) != len(Japan):
        print("中文单词与英文单词数目上存在出入,无法继续,请修正...")
        while True:input()
    #------------------------------------------------------
    print("|---------------------------------------|")
    print("|模式0:日->中                           |")
    print("|模式1:中->日                           |")
    print("|模式2:随机                             |")
    print("|请选择编号(例如1)....                  |")
    print("|---------------------------------------|")
    while True:
        try:
            mode = int(input())
            if mode in [0,1,2]:break
            else:print("模式选择错误,请重新输入...")
        except:
            mode = 0
            print("使用默认模式(0)...")
            break
    #------------------------------------------------------    
    while True:
        num = get_uni_num()
        res = TestOnce(num,mode)
        if res == 1:
            TimeEnd=time.time()
            if len(error) != 0:
                print("很好,您已经完成了本章测试...加油！！")
                PrintError()
                StorageError()
                input("本次测试完毕,按任意键退出...欢迎再来...")
            else:input("恭喜您完美完成测试,按任意键退出...欢迎再来...")
            print("测试用时:%s"%time.strftime("%M-%S",time.localtime(TimeEnd-TimeStart)))
            break
        else:
            pass







