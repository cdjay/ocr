import itchat

itchat.auto_login(True)
a=itchat.search_chatrooms(name='小')
# a=itchat.search_friends(name='Jaxen')
print(a)
# itchat.send('机器人 ','@@6735805cc959d434d3ad8884b93bd579cd1a94d05b4da0956020c7d155b929dc')
# itchat.send('机器人 ','filehelper')
# print()
# print('昵称: {}'.format(a[0]['PYInitial']))
# print('ID:   {}'.format(a[0]['UserName']))
# print('地区: {}'.format(a[0]['Province']))
# print('城市: {}'.format(a[0]['City']))

for i in range(1,100):
    sendmsg='数到100就停止.看封号不呢? 数 {:20}'.format(i)
    itchat.send(sendmsg,'@@d9bc945e60b63255f826babb45c40b493236e476e8a2cf4f166649729189361a')