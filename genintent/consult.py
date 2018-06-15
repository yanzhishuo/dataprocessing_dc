from gendata.inherit import *
#consult

head = ['','你们']
demonstrative = ['这个','那个','这里','那里','这','']
tail = ['还要了解这么仔细吗','也要问吗','可以通过了吗','电话打不通会拒单吗',
        '需要多久能放款','款项什么时候可以到账户啊','没有手续吗','没有单子吗','不是应该有个手续什么的吗',
        '没有其他的那个吗','今天能下款吗','什么时候能放款',
        '如果没有通过的话我签的合同是不是不生效了']
#原本的consult.json
#repeat
yuqi = ['嗯','啊','啥','喂','什么','啥啊','什么啊','唉','等一下','怎么了','']
tingbujian = ['我没听清楚','我没听见','我听不见','我听不到','听不到','听不见','听不清','听不懂','我没听懂','不明白',
              '刚才没有听清楚','意思我没听清','声音咋听不太清杂音太大','你什么意思我没听明白','你说的话我没听明白啥意思',
              '我没听清','我这信号不太好','没听清','我这边有点吵','没听见','这下雨好吵听不到',
              '我这边有风我听不清','我不太听得清','刚刚没听清楚','没听清这里有点吵','这个手机听不太清楚']
shuo = ['你能再说一遍吗','你说啥','你说什么','你说的什么','你讲什么','你说用什么','你说什么呀','你再说一遍',
        '再说一遍','麻烦再说一遍','再说一下','你再说一下','你大点声','你再重复一遍怎么了','怎么了你说',
        '你能再说一下吗','你说慢一点','大声一点可以吗','你声音太小','稍微大声','说清楚一点',
        '你说话响一点','有什么事情啊','有什么事啊','你问吧','你要问什么','你说话响一点','你说','']
#交换tingbujian和shuo的位置
demonstrative_r =tingbujian
#quit
head_q = ['', '这个']
demonstrative_q =['', '我']
verb = ['真的忘记了','忘了','不想答','答不上来','不好说','不知道,','不确定','忘记了','不记得了','很难说','不了解']
tail_q=['','我看一下才知道','在手机里','存在手机上']
#stop
head_s = ['唉', '等一下', '你好', '那个', '']
demonstrative_s= ['我正在忙', '我有点事', '我不打算借钱了', '我不借了', '有个电话进来','我手机马上没电了',
         '我有个电话进来', '不用了', '我要考虑一下','我还要考虑一下做不做','我这里有点事'
         ,'我暂时就不放款了','我暂时就不贷款了','就不要放了你们这样子的话',
         '那你们就不要打了我不申请了可以吗','我想问下能不办了吗','那个我不申请了','我不申请了','那就算了吧']
stop = ['','','挂了吧', '先挂了', '有时间再打', '我先挂了', '']
tail_s = ['','','再见','']

if __name__=="__main__":
    #consult
    patternlist = [head,demonstrative,tail]
    length = '1'
    for i, item in enumerate(patternlist):
        print(len(item))
        length = int(length) * len(item)
    c = Gendata(patternlist,'consult',1,int(length)+100)
    c.genneed()
    # #quit
    # patternlist = [head_q, demonstrative_q,verb, tail_q]
    # length = '1'
    # for i, item in enumerate(patternlist):
    #     print(len(item))
    #     length = int(length) * len(item)
    # c = Gendata(patternlist, 'quit', 2, int(length) + 100)
    # c.genneed()
    #stop
    # patternlist = [head_s, demonstrative_s, stop, tail_s]
    # length = '1'
    # for i, item in enumerate(patternlist):
    #     print(len(item))
    #     length = int(length) * len(item)
    # c = Gendata(patternlist, 'stop', 1, int(length) + 100)
    # c.genneed()
    #repeat
    # dataneed_data = list()
    # num = len(yuqi)*len(tingbujian)*len(shuo)+200
    # path ='repeat'
    # for i in range(num):
    #     dataneed_dict = dict()
    #     a = choice(yuqi)
    #     b = choice(tingbujian)
    #     if b:
    #         c = choice(shuo)
    #     else:
    #         c = choice([choice(shuo),''])
    #         print(c)
    #     dataneed_dict['label_name'] = path
    #     dataneed_dict['id'] = i
    #     dataneed_dict['ref'] = a+b+c
    #     dataneed_data.append(dataneed_dict)
    # # print(dataneed_data)
    # obj = json.dumps(dataneed_data, ensure_ascii=False, indent=2)
    # file = open('/home/yzs/gendata/' + path + '_gen_' + str(datenow()) + '_2_' + str(num) + '.json', 'w')
    # file.write(obj)
    # file.close()
    # for i in range(num):
    #     dataneed_dict = dict()
    #     a = choice(yuqi)
    #     b = choice(shuo)
    #     if b:
    #         c = choice(tingbujian)
    #     else:
    #         c = choice([choice(tingbujian),''])
    #         print(c)
    #     dataneed_dict['label_name'] = path
    #     dataneed_dict['id'] = i
    #     dataneed_dict['ref'] = a+b+c
    #     dataneed_data.append(dataneed_dict)
    # # print(dataneed_data)
    # obj = json.dumps(dataneed_data, ensure_ascii=False, indent=2)
    # file = open('/home/yzs/gendata/' + path + '_gen_' + str(datenow()) + '_' + str(num) + '.json', 'w')
    # file.write(obj)
    # file.close()