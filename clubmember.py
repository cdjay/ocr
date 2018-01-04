import time
from PIL import Image
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

listjson=[]
for file in range(1,3):

    path='./club/{}.jpg'.format(file)

    background = Image.open(path)
    background=background.resize((960, 540), Image.ANTIALIAS)
    foreground = Image.open('./club/mask.png')
    # 粘贴蒙版
    background.paste(foreground, (0, 0), foreground)


    background.save('./club/p{}.jpg'.format(file))

    json = gt('./club/p{}.jpg'.format(file))
    json = list(json['words_result'])
    listjson=listjson+json

for x in listjson:
    print(x['words'][2:])

# for x in range(0,8):
#     for file in listjson[x::8]:
#         print(file['words'][2:])
# for x in range(4,8):
#     for file in listjson[x::8]:
#         print(file['words'][2:])

