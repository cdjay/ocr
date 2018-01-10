import os
from PIL import Image

rpath = 'test.jpg' # 读取原始战绩图片设置
wpath = 'read.jpg' # 写入识别图片设置
originposi=[8, 0] # 第一个坐标
# 房间信息坐标集合
roominfo={
    'club':(85,25,227,150), # (图片x,y.坐标x,y)
    'room':(85,25,400,148),
    # 'rnds':(25,20,424,112),
    # 'bits':(45,20,513,112),
    # 'type':(80,20,609,112),
    'date':(129,25,950,148),
    'time':(65,25,1081,148)
}
#用户信息坐标(第一个玩家)
playerinfo={
    # 'name':(100,22,145,162),
    # 'qiang':(20,20,165,190),
    # 'zhuang':(20,20,208,190),
    # 'tui':(20,20,250,190),
    'id':(82,20,140,288),
    'score':(180,50,117,311),
}

im = Image.open(rpath) # 载入战绩图
im = im.resize((1280, 720), Image.ANTIALIAS) # 更改图标大小

count=1
for dictname,values in roominfo.items(): # 俱乐部信息获取
    x,y,sx,sy=roominfo[dictname][0],roominfo[dictname][1],roominfo[dictname][2],roominfo[dictname][3]
    imagebox= sx, sy, sx+x, sy+y
    tmp=im.crop(imagebox)
    tmp.save('{}.png'.format(count))
    count+=1

for row in range(0,2): # 玩家信息获取
    for p in range(0,4):
        for dictname,values in playerinfo.items():
            x,y,sx,sy=playerinfo[dictname][0],playerinfo[dictname][1],playerinfo[dictname][2],playerinfo[dictname][3]
            imagebox= sx+266*p, sy+row*178, sx+266*p+x, sy+row*178+y
            tmp=im.crop(imagebox)
            tmp.save('{}.png'.format(count))
            count+=1

background = Image.open(wpath)
for file in range(1,21):# 调整图片到合适大小
    im = Image.open('{}.png'.format(file))
    x,y=im.size
    x=int(x*(25/y))
    y=int(y*(25/y))
    im = im.resize((x, y), Image.ANTIALIAS) # 更改图片大小
    os.remove('{}.png'.format(file))
    background.paste(im, (56, 25*file-25))
background.save(wpath)