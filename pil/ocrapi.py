# baiduai 模块
from aip import AipOcr

# 百度AI参数----------------------------------
""" APPID AK SK """
APP_ID = '10532375'
API_KEY = 'k4Lucb2SnVotnYfnBgkWskKs'
SECRET_KEY = 'FO3DqnzcbYISjpFWipjKVK60NrZP6uVG'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def readimg(filename):
    with open(filename, 'rb') as fp:
        # result = client.basicGeneral(fp.read()) #通用
        result = client.basicAccurate(fp.read())  # 高精度
    return result