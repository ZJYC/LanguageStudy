#---------------------------------------------------------
def get_uni_num(Max):
    '''
    ��ȡ�������ȷ��������ֻ����һ��
    flag��ģ���ṩ
    Max:�����
    '''
    while True:
        if len(flag) == Max:return None
        n = int(random.uniform(0,Max))
        if n in flag:pass
        else:
            flag.append(n)
            break
    #���������
    return n
#---------------------------------------------------------
def LogError(num):
    '''
    ��¼�������
    cnt,error��ģ���ṩ
    '''
    #��¼�������
    cnt[num] = cnt[num] + 1
    if num in error:return 1
    else:
        error.append(num)
        return None
#---------------------------------------------------------
def PrintError():
    "��ӡ�������"
    print("���β��Է�����",GetScore(),"��ϸ����:")
    print("-------------------------------------------------------")
    for e in error:print(China[e]," : ",English[e],"ERROR : ",cnt[e])
    print("-------------------------------------------------------")
#---------------------------------------------------------
def GetScore():
    "�������"
    return 100.0 - len(error) / len(English) * 100
#---------------------------------------------------------
def StorageError():
    "�������������ļ�"
    fo = open(filename,"a")
    try:
        fo.write("\r\n------------------------------------------------------------\r\n")
        fo.write(time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time())))
        fo.write("\r\n����:" + str(GetScore()) + "\r\n")
        fo.write("\r\n" + "Mode : " + str(mode) + "\r\n")
        for e in error:fo.write("      " + China[e] + " : " + English[e] + "ERROR : " + str(cnt[e]))
        fo.write("\r\n------------------------------------------------------------\r\n")
    finally:
        fo.close()

