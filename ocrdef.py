def fd(a): # 格式化日期,容错
    b=''
    for x in a:
        if x.isdigit():
            b+=x
    return b[:4]+'/'+b[4:6]+'/'+b[6:8]

def ft(a):# 格式化时间,容错
    b=''
    for x in a:
        if x.isdigit():
            b+=x
    return b[:2]+':'+b[2:]

def fid(a): # 格式化ID
    b=''
    for x in a:
        if x.isdigit():
            b+=x
    return b

def fscore(score): #分数修正
    try:
        if score[0]=='一' or score[0]=='-':
            score=int(score[1:])*-1
        else:
            score=int(score[1:])
    except:
        score='0'
        score=int(score)
    return score

def filltxt(txt): # 名字填充
    txt+=" "*(10-len(txt.encode('gbk')))
    return txt

def checkscore(score):
    check=0
    for x in score:
        check+=x
    if check !=0:
        return print('图片识别出错啦!请检查错误,手动更改')
    return print('[-战绩已通过验证-]')