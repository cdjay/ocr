# baiduai 模块
from aip import AipOcr
""" 你的 APPID AK SK """
APP_ID = '10532375'
API_KEY = 'k4Lucb2SnVotnYfnBgkWskKs'
SECRET_KEY = 'FO3DqnzcbYISjpFWipjKVK60NrZP6uVG'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def getdata(filename):
    # result = client.basicGeneral(get_file_content(filename)) #通用
    result = client.basicAccurate(get_file_content(filename)) #高精度
    return result