from PIL import Image
import time
start = time.clock()
im = Image.open("new3.jpg")
im=im.resize((960, 540),Image.ANTIALIAS)
print('原始图像属性:',im.format, im.size, im.mode)
box = (67, 162, 265, 300)
region = im.crop(box)

#第一个坐标
x1,x2,x3,x4=67+40,162+100,265-45,300

# 切割所有玩家
for x in range(0,4):
    box = (x1+209*x, x2, x3+209*x, x4)
    region = im.crop(box)
    region.save('p'+str(x+1)+'.jpg', 'jpeg')
x2=x2+154
x4=x4+154
for x in range(0,4):
    box = (x1+209*x, x2, x3+209*x, x4)
    region = im.crop(box)
    region.save('p'+str(x+5)+'.jpg', 'jpeg')

#百度ocr
#参数设置
from aip import AipOcr
""" 你的 APPID AK SK """
APP_ID = '10532375'
API_KEY = 'k4Lucb2SnVotnYfnBgkWskKs'
SECRET_KEY = 'FO3DqnzcbYISjpFWipjKVK60NrZP6uVG'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 识别图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
def gt(filename):
#    result = client.basicGeneral(get_file_content(filename)) #通用
    result = client.basicAccurate(get_file_content(filename)) #高精度
    return result

# 调用通用文字识别接口
try:
    ps=[]
    for i in range(1,9):
        filename='p'+str(i)+'.jpg'
        soc=gt(filename)
        # ps[i]=soc['words_result']
        # print(soc['words_result'][0]['words'])
        ps.append(int((soc['words_result'][0]['words'])))
        # print('成绩表为:',ps)
except:
    print('oqs超出限制!')



# 清洗数据
# ps=[760, 440, 320, 260, 20, 0,-540,1240]
for i in range(0,7):
    if ps[i+1]>ps[i]:
        ps[i+1]=abs(ps[i+1])*-1
    else:
        pass

# 判断数据正确性
jieguo=0
for i in ps:
    jieguo+=i
if jieguo == 0:
    print('数据已通过正确性验证,清洗结果:',ps)
    print('耗时:',time.clock() - start,'秒')
else:
    print('无法识别,请检查!')