
def get_uni_num():
    "获取随机数，确保本数字只出现一次"
    while True:
        if len(flag) == len(Japan):
            return "OVER"
        n = int(random.uniform(0,len(Japan)))
        if n in flag:
            pass
        else:
            flag.append(n)
            break
    return n

def Display(num,mode):
    "mode:0   J->C  mode:1   C->J   mode:2  Random"
    retry = 0
    if num == "OVER":return 1
    if mode == 2:
        mode = int(random.uniform(0,2))
    if mode == 0:
        while True:
            print("Jppan is : ",Japan[num])
            Input = input()
            if Input == China[num]:
                print("!!!Right!!!","Remain....",len(Japan) - len(flag))
                input("Keep going...")
                break
            else:
                retry = retry + 1
                if retry < 4:
                    pass
                else:
                    error.append(num)
                    print("!!!Error!!!!",China[num])
                    print("-----------------Spell it now--------------------")
                    while True:
                        Input = input()
                        if Input == China[num]:
                            print("Keep on......")
                            break
                        else:
                            print("!!!!idiot!!!!")
                    Retry = 0
                    flag.remove(num)
                    break
    if mode == 1:
        while True:
            print("China is : ",China[num])
            Input = input()
            if Input == Japan[num]:
                print("!!!Right!!!","Remain....",len(Japan) - len(flag))
                input("Keep going...")
                break
            else:
                retry = retry + 1
                if retry < 4:
                    pass
                else:
                    error.append(num)
                    print("!!!Error!!!!",Japan[num])
                    print("-----------------Spell it now--------------------")
                    while True:
                        Input = input()
                        if Input == Japan[num]:
                            print("Keep on......")
                            break
                        else:
                            print("!!!!idiot!!!!")
                    Retry = 0
                    flag.remove(num)
                    break

if __name__ == "__main__":
    chapter = int(input("Input the chapter you wanted..."))
    if chapter == 20:from Card20 import *
    if chapter == 21:from Card21 import *
    if chapter == 22:from Card22 import *
    if chapter == 23:from Card23 import *
    if chapter == 24:from Card24 import *
    #------------------------------------------------------
    if len(China) != len(Japan):
        print("China != Japan....")
        while True:
            input()
    #------------------------------------------------------
    print("mode:0   J->C  mode:1   C->J   mode:2  Random")
    while True:
        mode = int(input("Input Mode you wanted..."))
        if mode in [0,1,2]:
            break
        else:
            print("Please input the right number...[0,1,2]")
    #------------------------------------------------------    
    while True:
        num = get_uni_num()
        res = Display(num,mode)
        if res == 1:
            if len(error) != 0:
                print("Good,You had finished this test,The following need to reinforce")
                for e in error:print(China[e]," : ",Japan[e])
            fo = open(filename,"a")
            try:
                fo.write(time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time())))
                fo.write("\r\n" + "Mode : " + str(mode) + "\r\n")
                for e in error:fo.write("      " + China[e] + " : " + Japan[e] + "\r\n")
            finally:
                fo.close() 
                input()
            break
        else:
            pass
