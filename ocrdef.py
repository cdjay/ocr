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
    if '+' in score:return int(fid(score))
    else:return int(fid(score))*-1
