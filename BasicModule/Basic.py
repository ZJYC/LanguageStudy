#---------------------------------------------------------
def get_uni_num(Max):
    '''
    获取随机数，确保本数字只出现一次
    flag由模块提供
    Max:最大数
    '''
    while True:
        if len(flag) == Max:return None
        n = int(random.uniform(0,Max))
        if n in flag:pass
        else:
            flag.append(n)
            break
    #返回随机数
    return n
#---------------------------------------------------------
def LogError(num):
    '''
    记录错误词条
    cnt,error由模块提供
    '''
    #记录错误次数
    cnt[num] = cnt[num] + 1
    if num in error:return 1
    else:
        error.append(num)
        return None
#---------------------------------------------------------
def PrintError():
    "打印错误词条"
    print("本次测试分数：",GetScore(),"明细如下:")
    print("-------------------------------------------------------")
    for e in error:print(China[e]," : ",English[e],"ERROR : ",cnt[e])
    print("-------------------------------------------------------")
#---------------------------------------------------------
def GetScore():
    "计算分数"
    return 100.0 - len(error) / len(English) * 100
#---------------------------------------------------------
def StorageError():
    "保存错误词条到文件"
    fo = open(filename,"a")
    try:
        fo.write("\r\n------------------------------------------------------------\r\n")
        fo.write(time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time())))
        fo.write("\r\n分数:" + str(GetScore()) + "\r\n")
        fo.write("\r\n" + "Mode : " + str(mode) + "\r\n")
        for e in error:fo.write("      " + China[e] + " : " + English[e] + "ERROR : " + str(cnt[e]))
        fo.write("\r\n------------------------------------------------------------\r\n")
    finally:
        fo.close()

