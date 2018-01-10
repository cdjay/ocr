import time
from ocrapi import readimg

imgpath='./pil/read.jpg'
start = time.clock()
listjson = readimg(imgpath)
for x in listjson['words_result']:
    print(x['words'][2:])
print('\n[耗时: {} 毫秒 ({:.2f}秒)]'.format(int((time.clock() - start)*1000),time.clock() - start))
