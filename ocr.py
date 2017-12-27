# 纯OCR
import time
import image
import ocrdef
from aip import AipOcr

start = time.clock()

""" APPID AK SK """
APP_ID = '10532375'
API_KEY = 'k4Lucb2SnVotnYfnBgkWskKs'
SECRET_KEY = 'FO3DqnzcbYISjpFWipjKVK60NrZP6uVG'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def gt(filename):
    # result = client.basicGeneral(get_file_content(filename)) #通用
    result = client.basicAccurate(get_file_content(filename))  # 高精度
    return result

image.readpic()
listjson = gt('./cut/newtmp.jpg')
print('ID({})'.format(listjson['log_id']))
print('识别数量: {}\n'.format(listjson['words_result_num']))
listjson = list(listjson['words_result'])

# print('获取的json:\n',listjson)

# 数据分类存放以供使用
room=[]
pname=[]
pid=[]
ps=[]
# 房间信息赋值
for i in listjson[0:7]:
    room.append(i['words'][3:])
# 姓名,ID,分数
for i in listjson[7::3]:
    txt=ocrdef.filltxt(i['words'][3:])
    pname.append(txt)
for i in listjson[8::3]:
    txt=ocrdef.fid(i['words'][3:])
    pid.append(txt[:8])
for i in listjson[9::3]:
    txt=i['words'][3:]
    ps.append(txt)

# 格式化输出
outputmsg='俱乐部: {}  \n房间号: {}  \n时  间: {} {}\n'.format(room[0],room[1],room[5],room[6])
outputmsg+='-'*40
outputmsg+='\n'
for roll in range(0,8):
    outputmsg+='{} [ {} ]   Score:  {}\n'.format(pid[roll],pname[roll],ps[roll])
    # print('{} [ {} ]   Score:  {}'.format(pid[roll],pname[roll],ps[roll]))
outputmsg+='-'*40

print(outputmsg)

print('\n耗时:', time.clock() - start, '秒')
