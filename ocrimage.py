# 图像处理模块

from PIL import Image

# 参数配置
path = './cut/mm.jpg' #需要处理的图片
originposi=(72, 10) # 第一个坐标
roominfo={
    'club':(70,20,168,112), # (图片x,y.坐标x,y)
    'room':(70,20,298,111),
    'rnds':(25,20,424,112),
    'bits':(45,20,513,112),
    'type':(80,20,609,112),
    'date':(100,20,714,111),
    'time':(50,20,810,112)
}
playerinfo={
    'name':(100,22,145,162),
    # 'qiang':(20,20,165,190),
    # 'zhuang':(20,20,208,190),
    # 'tui':(20,20,250,190),
    'id':(78,12,105,218),
    'score':(135,40,90,234),
}

def readpic():
    setposi=originposi[1] # 粘贴图片y轴起始点
    im = Image.open(path) # 载入战绩图
    print('原始图像属性:', im.format, im.size, im.mode)
    im = im.resize((960, 540), Image.ANTIALIAS)
    tmp = Image.open('./cut/newtmp1.jpg') # 载入优化后图片

    for dictname,values in roominfo.items(): # 俱乐部信息优化
        imagebox= roominfo[dictname][2], roominfo[dictname][3], roominfo[dictname][2] + roominfo[dictname][0], roominfo[dictname][3] + roominfo[dictname][1]
        tmp.paste(im.crop(imagebox), (originposi[0], setposi))
        setposi+=roominfo[dictname][1]

    for row in range(0,2): # 玩家信息获取
        for p in range(0,4):
            for dictname,values in playerinfo.items():
                imagebox= playerinfo[dictname][2]+200*p, playerinfo[dictname][3]+row*134, playerinfo[dictname][2]+200*p + playerinfo[dictname][0], playerinfo[dictname][3]+row*134 + playerinfo[dictname][1]
                box=im.crop(imagebox)
                # box=box.resize((100, 25), Image.ANTIALIAS)
                tmp.paste(box, (originposi[0], setposi))
                setposi+=playerinfo[dictname][1]+10
                # setposi+=30

    tmp.save('./cut/newtmp.jpg') # 保存所有更改
    return

# 主程序
if __name__=='__main__':
    readpic()
    print('处理完毕')
    # pass

