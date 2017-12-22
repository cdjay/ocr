from PIL import Image
import ocrmod
import time
start = time.clock()

# 打开图片并resize原图.
path='./cut/wdnn1.jpg'
im = Image.open(path)
im=im.resize((960, 540),Image.ANTIALIAS)
print('图像属性:',im.format, im.size, im.mode)

# 俱乐部ID
x,y=70,20
box= (168, 112, 168+x, 112+y)
cuttools = im.crop(box)
tmp = Image.open('./cut/tmp.jpg')
tmp.paste(cuttools,(int((tmp.size[0]-70)/2),5))
tmp.save('./cut/tmp.jpg')
# 房间ID
x,y=70,20
box= (298, 112, 298+x, 112+y)
cuttools = im.crop(box)
tmp = Image.open('./cut/tmp.jpg')
tmp.paste(cuttools,(int((tmp.size[0]-70)/2),30))
tmp.save('./cut/tmp.jpg')
# 游戏日期
x,y=100,20
box= (711, 112, 711+x, 112+y)
cuttools = im.crop(box)
tmp = Image.open('./cut/tmp.jpg')
tmp.paste(cuttools,(int((tmp.size[0]-100)/2),55))
tmp.save('./cut/tmp.jpg')
# 游戏时间
x,y=50,20
box= (811, 112, 811+x, 112+y)
cuttools = im.crop(box)
tmp = Image.open('./cut/tmp.jpg')
tmp.paste(cuttools,(int((tmp.size[0]-50)/2),80))
tmp.save('./cut/tmp.jpg')


# 数据清理
class player(object):
    pass




gamedata=ocrmod.getdata('./cut/tmp.jpg')  # 调用百度ocr识别数据
# 数据赋值
player.club=gamedata['words_result'][0]['words']
player.room=gamedata['words_result'][1]['words']
player.date=gamedata['words_result'][2]['words']
player.time=gamedata['words_result'][3]['words']

# 数据输出
print()
print('开始识别数据>>>>>')
print()
print('俱乐部ID:  ',player.club) # 输出识别数据
print('房间ID:    ',player.room)
print('游戏日期:  ',player.date) # 输出识别数据
print('游戏时间:  ',player.time)
print()
print('本次耗时:  ',time.clock() - start,'秒')