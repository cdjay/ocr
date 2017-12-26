# 主程序

from PIL import Image
import ocrmod
import time
import ocrdef
# import itchat

# itchat.auto_login(True,enableCmdQR=True)
start = time.clock()

# 打开图片并resize原图.
path = './cut/mm.jpg'
im = Image.open(path)
print('原始图像属性:', im.format, im.size, im.mode)
im = im.resize((960, 540), Image.ANTIALIAS)


def pastepic(x, y, sx, sy, s):
    box = (sx, sy, sx + x, sy + y)
    cuttools = im.crop(box)
    tmp = Image.open('./cut/tmp.jpg')
    tmp.paste(cuttools, (int((tmp.size[0] - x) / 2), s))
    tmp.save('./cut/tmp.jpg')


pastepic(70, 20, 168, 112, 5)  # 俱乐部ID
pastepic(70, 20, 298, 112, 30)  # 房间ID
pastepic(100, 20, 711, 112, 55)  # 日期
pastepic(50, 20, 811, 112, 80)  # 时间
pastepic(80, 24, 142, 161, 105)  # 名字1
pastepic(100, 18, 88, 214, 134)  # IDa
pastepic(138, 40, 88, 233, 157)  # scorea
pastepic(80, 24, 342, 161, 203)  # 名字2
pastepic(100, 18, 288, 214, 232)  # IDa
pastepic(138, 40, 288, 233, 255)  # scorea
pastepic(80, 24, 542, 161, 304)  # 名字3
pastepic(100, 18, 488, 214, 333)  # IDa
pastepic(138, 40, 488, 233, 356)  # scorea
pastepic(80, 24, 742, 161, 401)  # 名字4
pastepic(100, 18, 688, 214, 430)  # IDa
pastepic(138, 40, 688, 233, 453)  # scorea
pastepic(80, 24, 142, 295, 498)  # 名字5
pastepic(100, 18, 88, 350, 527)  # IDa
pastepic(138, 40, 88, 367, 550)  # scorea
pastepic(80, 24, 342, 295, 595)  # 名字6
pastepic(100, 18, 288, 350, 624)  # IDa
pastepic(138, 40, 288, 367, 647)  # scorea
pastepic(80, 24, 542, 295, 692)  # 名字7
pastepic(100, 18, 488, 350, 721)  # IDa
pastepic(138, 40, 488, 367, 744)  # scorea
pastepic(80, 24, 742, 295, 789)  # 名字8
pastepic(100, 18, 688, 350, 818)  # IDa
pastepic(138, 40, 688, 367, 841)  # scorea


# 数据清理
class player(object):
    pass


gamedata = ocrmod.getdata('./cut/tmp.jpg')  # 调用百度ocr识别数据
# 数据赋值
player.club = ocrdef.fid(gamedata['words_result'][0]['words'])
player.room = ocrdef.fid(gamedata['words_result'][1]['words'])
player.date = ocrdef.fd(gamedata['words_result'][2]['words'])
player.time = ocrdef.ft(gamedata['words_result'][3]['words'])
player.name1 = gamedata['words_result'][4]['words'][2:]
player.id1 = ocrdef.fid(gamedata['words_result'][5]['words'])
player.score1 = ocrdef.fscore(gamedata['words_result'][6]['words'])
player.name2 = gamedata['words_result'][7]['words'][2:]
player.id2 = ocrdef.fid(gamedata['words_result'][8]['words'])
player.score2 = ocrdef.fscore(gamedata['words_result'][9]['words'])
player.name3 = gamedata['words_result'][10]['words'][2:]
player.id3 = ocrdef.fid(gamedata['words_result'][11]['words'])
player.score3 = ocrdef.fscore(gamedata['words_result'][12]['words'])
player.name4 = gamedata['words_result'][13]['words'][2:]
player.id4 = ocrdef.fid(gamedata['words_result'][14]['words'])
player.score4 = ocrdef.fscore(gamedata['words_result'][15]['words'])
player.name5 = gamedata['words_result'][16]['words'][2:]
player.id5 = ocrdef.fid(gamedata['words_result'][17]['words'])
player.score5 = ocrdef.fscore(gamedata['words_result'][18]['words'])
player.name6 = gamedata['words_result'][19]['words'][2:]
player.id6 = ocrdef.fid(gamedata['words_result'][20]['words'])
player.score6 = ocrdef.fscore(gamedata['words_result'][21]['words'])
player.name7 = gamedata['words_result'][22]['words'][2:]
player.id7 = ocrdef.fid(gamedata['words_result'][23]['words'])
player.score7 = ocrdef.fscore(gamedata['words_result'][24]['words'])
player.name8 = gamedata['words_result'][25]['words'][2:]
player.id8 = ocrdef.fid(gamedata['words_result'][26]['words'])
player.score8 = ocrdef.fscore(gamedata['words_result'][27]['words'])
# 数据输出
print()
print('开始识别数据>>>>>')
print()
print('俱乐部ID: {}   房间ID: {}   游戏时间: {} {}'.format(player.club, player.room, player.date, player.time))
print('-' * 60)
print('玩家1:{} \n   ID:{}  分数: {:5}  倍数:0.5  税率:5%  税后:￥{:10.2f}  大赢家'.format(player.name1, player.id1, player.score1,player.score1 * 0.95))
print('玩家2:{} \n   ID:{}  分数: {:5}  倍数:0.5  税率:5%  税后:￥{:10.2f}'.format(player.name2, player.id2, player.score2,player.score2))
print('玩家3:{} \n   ID:{}  分数: {:5}  倍数:0.5  税率:5%  税后:￥{:10.2f}'.format(player.name3, player.id3, player.score3,player.score3))
print('玩家4:{} \n   ID:{}  分数: {:5}  倍数:0.5  税率:5%  税后:￥{:10.2f}'.format(player.name4, player.id4, player.score4,player.score4))
print('玩家5:{} \n   ID:{}  分数: {:5}  倍数:0.5  税率:5%  税后:￥{:10.2f}'.format(player.name5, player.id5, player.score5,player.score5))
print('玩家6:{} \n   ID:{}  分数: {:5}  倍数:0.5  税率:5%  税后:￥{:10.2f}'.format(player.name6, player.id6, player.score6,player.score6))
print('玩家7:{} \n   ID:{}  分数: {:5}  倍数:0.5  税率:5%  税后:￥{:10.2f}'.format(player.name7, player.id7, player.score7,player.score7))
print('玩家8:{} \n   ID:{}  分数: {:5}  倍数:0.5  税率:5%  税后:￥{:10.2f}  土豪'.format(player.name8, player.id8, player.score8,player.score8))
print('-' * 60)
print('本次耗时:  ', time.clock() - start, '秒')




# wxmsg = ''
# wxmsg += '俱乐部ID: {}   \n房间编号: {}   \n游戏时间: {} {}\n\n'.format(player.club, player.room, player.date, player.time)
# wxmsg += player.name1 + '  ' + str(player.score1) + '\n'
# wxmsg += player.name2 + '  ' + str(player.score2) + '\n'
# wxmsg += player.name3 + '  ' + str(player.score3) + '\n'
# wxmsg += player.name4 + '  ' + str(player.score4) + '\n'
# wxmsg += player.name5 + '  ' + str(player.score5) + '\n'
# wxmsg += player.name6 + '  ' + str(player.score6) + '\n'
# wxmsg += player.name7 + '  ' + str(player.score7) + '\n'
# wxmsg += player.name8 + '  ' + str(player.score8) + '\n'
#
# itchat.send(wxmsg, 'filehelper')
