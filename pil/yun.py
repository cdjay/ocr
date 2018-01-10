import time
from textocr import readimg
import pil

start = time.clock()

if __name__=='__main__':
    roominfo=[]
    imgpath='read.jpg'
    listjson = readimg(imgpath)
    for x in listjson['words_result']:
        roominfo.append(x['words'][2:])
    for x in roominfo:
        print(x)
    print('\n[耗时: {} 毫秒 ({:.2f}秒)]'.format(int((time.clock() - start)*1000),time.clock() - start))


