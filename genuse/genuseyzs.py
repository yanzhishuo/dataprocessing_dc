from gendata.inherit import *
from random import *

use ={1:'日常消费',2:'购车',3:'装修',4:'资金周转',5:'旅游',6:'教育',7:'医疗',8:'企业经营',9:'其他'}
use_label = ['日常消费','购车','装修','资金周转','旅游','教育','医疗','企业经营','其他']
modal =['','','','恩']
# head = ['','我贷款用途是','用途就是','用途是','借款用途是','就是','为了','想','用作','用来','主要就是']
head = ['','','','','用途就是','贷款用途是','用来','主要就是','就是','是']
person = ['','我','我','自己']
tail = ['','用']
modal_tail = ['','','','','嘛','啊','呀']

label1 = ['日常消费','消费购物','消费','私房钱','有点急用生活消费','日常消费或备用','个人消费','生活上的',
          '生活开支','生活消费','购物','数码消费','房租','生活费','交房租','加油','租房',
          '买衣服','赡养老人','抚养儿女','人情往来','娱乐消费','物业费','水电费','炉灶费','消费开支','日常开销','衣食住行']
label2 = ['购车','换车','购买汽车','买家电','买东西','买数码产品','买电子产品','买手机','买电脑',
          '买珠宝','买玉石','买电动车','买摩托车','买卡车','买货车','买车打算',
          '做一些家用补贴家具','买家具','买房','买健身器材','添置设备','买空调','买冰箱','买洗衣机']
label3 = ['装修','装修房子','家里装修','家里厕所装修','房屋装修','盖房子','盖养殖房子','家具装修','要扩充一下店面',
          '店面装修','店铺装修','家居装修','室内装修','地板装修','购买原材料','房子装修需要点钱','我准备我这装修']
label4 = ['资金周转','日常周转','周转','日常周转消费','做周转','应急应急','做下资金周转',
          '加工这块周转一下','消费周转','周转一下','购物周转','公司资金周转','店里周转','短期周转']
label5 = ['旅游','准备出去逛一圈去','出去玩一趟','旅游与购物','去泰国旅游一趟','出去玩','出国玩']
label6 = ['教育','给小孩报英语班','教育学习','买课外书','辅导班','买学习用品','学付费课程',
          '教育培训','出国留学','出国','日常消费教育','考学历文凭','上培训班']
label7 = ['医疗','交医疗费','交住院费','老人住院','买保健品','作医疗检查','检查身体']
label8 = ['公司运营','企业经营','做生意','开早餐店','企业运营','公司经营','工厂运营','扩大经营面积','再开个店','店铺资金','再扩大一下工作规模',
          '发展企业','买门面地皮需要钱','定一些广告材料','买材料']
label9 = ['做点投资','投资股票','购买股票','购买基金','养殖','种植业','买债券','美容','结婚','买保险','做婚庆','垫款','投机搞项目','还信用卡']
# label2 = ['','','','','','','','','','','','','','','','','','','']

class Genuse(Gendata):
    def __init__(self,patternlist,path,indexchoose,num,label):
        Gendata.__init__(self,patternlist,path,indexchoose,num)
        self.label = label
    def genneed(self):
        dataneed_data = list()
        for i in range(self.num):
            C = Appendneed(self.patternlist,self.indexchoose)
            ref,write=C.choose_append()
            dataneed_dict = dict()
            dataneed_dict['label_name'] = self.path
            dataneed_dict['id'] = i
            dataneed_dict['ref'] = ref
            dataneed_dict['write'] = write
            dataneed_dict['label'] = self.label
            dataneed_data.append(dataneed_dict)
        obj = json.dumps(dataneed_data, ensure_ascii=False, indent=2)
        file = open('/home/yzs/gendata/'+self.path+'_gen_'+str(datenow())+'_label'+str(self.label)+'_'+str(self.num)+'.json', 'w')
        file.write(obj)
        file.close()

if __name__ =="__main__":
    # patternlist = [modal,head,person,use_label,tail,modal_tail]
    # patternlist = [modal,head,person,label7,tail,modal_tail]
    # length = '1'
    # for i, item in enumerate(patternlist):
    #     print(len(item))
    #     length  = int(length)*len(item)
    # u = Genuse(patternlist,'test_use',3,length,'医疗')
    # u.genneed()
    # u = Gendata(patternlist,'use',3,2000)
    # u.genneed()
    refdeduplication('test_use_gen_0615_label医疗_15680','ref')