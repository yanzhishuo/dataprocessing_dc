import json
from random import *
from weight_choice import *
from genuse.genuseyzs import Genuse
from gendata.inherit import refdeduplication
head = ['','','','','我', '我是','就是','我现在','我目前', '我的职业身份是','我的职业是']
opt = {1:'自己做生意',2:'在职人员',3:'待业',4:'学生',5:'在工地工作',6:'其他'}
modal = ['','','','','','啊','呀','嘛']

# label1 = ['自己做生意','做生意','做小本生意','个体经营户','私营老板','自己开店']
label1 = ['自己做生意','做生意']
#label2 = ['在职人员','在职','职业人']
label2 = ['在职人员']
#label3 = ['待业','没工作','正在找工作','待业人员','等待工作机会']
label3 = ['待业']
label4 = ['学生']
#label4 = ['学生','在上学','在读书']
label5 = ['在工地工作','在工地搬砖','农民工','搞工程车的','搞工程的','做这个工程生意的',
          '在工地干活','工地上干活','挖掘机','做工程','自己做工程','那个做工程的','干工程','包工程',
          '在工地上铲斗车','在建筑工地上面','在高速做工程','在工地上','做建筑自己承包',
          '建筑包工头','承包工程','整工地','施工建造','建筑工程','工地监工','农机操作人员','建筑工人',
          '工程建设','工程管理','工地的工程包活的','矿工','工地看守员','砌墙'
          '在那个建筑上面包点那个水电','建筑运沙']
label6 = ['种植业者','司机','木匠','电工','退休','开饺子馆','爆破','当房东','教舞蹈的'
          ,'承包家具安装','房屋装修','自由职业','快递员','汽车美容','做食材的','养殖'
          ,'做宝石的','自己干农业这块饲料','个体开的洗车行','做销售','做经销商','送原料'
          ,'股权咨询','开长途货车','开小车','做玻璃行业','家里是卖猪肉的','给别人打工的',
          '项目负责人','做美发','物业保险','上班','蔬菜运输','小生意','工程机械租赁','跑滴滴'
          ,'电商','务农','种地','农民种水稻','果农','放牧人员','教师','园丁','木匠'
          ,'装潢人员','警察','教练','运动员','家庭主妇','记者','厨师','保安','下岗']

# def opt_type():
#     opt_c = choice(opt)
#     opt_raw = choice(head) +opt_c + modal[windex([5,1,1,1])]
#     return opt_raw, opt_c
#
# if __name__ =="__main__":
#     num_data = 1000
#     # num_data = 2
#     occupation_data = list()
#     for i in range(num_data):
#         occupation_dict = dict()
#         occupation_dict['label_name'] = 'occupation'
#         occupation_dict['id'] = i
#         occupation_dict['ref'],occupation_dict['write'] = opt_type()
#         occupation_data.append(occupation_dict)
#     # print(occupation_data)
#     obj = json.dumps(occupation_data, ensure_ascii=False, indent=2)
#     file = open('/home/yzs/occupation_gen_0508_1000.json', 'w')
#     file.write(obj)
#     file.close()

if __name__ =="__main__":
    patternlist = [head,label6,modal]
    length = '1'
    for i, item in enumerate(patternlist):
        print(len(item))
        length  = int(length)*len(item)
    u = Genuse(patternlist,'occupation',1,int(length)+100,'其他')
    u.genneed()
    # refdeduplication('occupation_gen_0614_label6_4852', 'ref')
