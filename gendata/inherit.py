from random import *
import re
import json
# from weight_choice import *
# from genpassword import *
from pyexcel import *
from datetime import datetime
import string
import xlrd

class Appendneed():
    '''实现对模式的相加
    input:
    iterable:组成模式的列表
    indexchoose:所需要的回答在列表中的位置（比如：我今年21岁，21就是'write',所需要的回答)
    output:
    我今年21岁,21:分别对应'ref','write'
    '''
    def __init__(self,iterable,indexchoose):
        self.items_list = str()
        self.items_choice = str()
        self.iterable = iterable
        self.indexchoose = indexchoose

    def choose_append(self):
        a = ''
        for i, item in enumerate(self.iterable):
            item1 = choice(item)
            self.items_list = self.items_list + item1
            if i == self.indexchoose:
                a = item1
        return self.items_list, a

class excel2list():
    '''读取excel表格全部内容（每一行的单元格相加），要求表格的表单名字是Sheet1'''
    def __init__(self,index,path):
        self.index = index
        self.path = path
    def getlist(self):
        data = xlrd.open_workbook(self.path)
        sheet_1_by_name=data.sheet_by_name('Sheet1')
        n_of_rows=sheet_1_by_name.nrows
        excel_list = list()
        for i in range(1,n_of_rows):
            cell_list = str()
            for j in range(self.index):
                cell = sheet_1_by_name.row(i)[j].value
                # print(cell)
                cell_list = cell_list +cell
            excel_list.append(cell_list)
        return excel_list

def need_choose(index,path):
    '''读取excel表格第index列内容，path是excel文件的路径，要求表格的表单名字是Sheet1'''
    brand = readexcel(index, path)
    return brand

def datenow():
    '''output：今天的日期（月日）如0521'''
    daten = datetime.now().strftime('%m%d')
    return daten

class Gendata():
    '''生成数据的核心函数（主要看这个）
    input：patternlist:模式列表（组成结构）
    path：json文件名称（如age）
    indexchoose：选取所需的write在patternlist的位置
    num：json文件的条数
    output：生成的一个json文件
    说明：需要改动的地方file = open('/home/yzs/gendata/'+self.path+'_gen_'+str(datenow())+'_'+str(self.num)+'.json', 'w')
         改成自己电脑想保存文件的地址
    '''
    def __init__(self,patternlist,path,indexchoose,num):
        self.patternlist = patternlist
        self.path = path
        self.indexchoose = indexchoose
        self.num = num

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
            dataneed_data.append(dataneed_dict)
        obj = json.dumps(dataneed_data, ensure_ascii=False, indent=2)
        file = open('/home/yzs/gendata/'+self.path+'_gen_'+str(datenow())+'_'+str(self.num)+'.json', 'w')
        file.write(obj)
        file.close()

def refdeduplication(path,label):
    '''去重：因为生成数据时候容易出现重复，后续会造成人力浪费，故去重
    input:
          文件路径，想去重的标签名字
    output：
          去掉重复的json文件'''
    with open('/home/yzs/gendata/'+path+'.json') as f:
        data_output = json.load(f)
    # #ref有没有重复
    l4 = []
    l4.append(data_output[0])
    # print(l4)
    for dict in data_output:
        k = 0
        for item in l4:
            if dict[label] != item[label]:
                k = k + 1
            else:
                #print(dict[label])
                break
            if k == len(l4):
                l4.append(dict)
    print(len(l4))
    l = []
    # i = 0
    i = l4[0]["id"]
    for item in l4:
        item['id'] = i
        i = i + 1
        l.append(item)
    print(len(l))
    obj = json.dumps(l, ensure_ascii=False, indent=2)
    file = open('/home/yzs/gendata/'+path+str(len(l))+'.json', 'w')
    print(type(obj))  # dumps是将dict/list转化成str格式
    file.write(obj)
    file.close()

class gennum():
    '''生成随机数字
    分两种情况：
    input1：输入是想要数据的位数
           比如length=2，输出是10/99...
    input2：输入数据范围,比如a=1,b=20,
           输出是15
    '''
    def __init__(self,length,a,b):
        self.len =length
        self.a =a
        self.b =b
    def gennumpassword(self):
        slcNum = [random.choice(string.digits) for i in range(self.len)]
        random.shuffle(slcNum)
        genpwd = ''.join(i for i in slcNum)
        return genpwd
    def gennum(self):
        result = random.randint(self.a, self.b)
        return result

def excel2label(index,path):
    '''给excel的数据加上label标签'''
    excelabel = dict()
    data = xlrd.open_workbook(path)
    sheets = data.sheets()
    sheet_1_by_name=data.sheet_by_name('Sheet1')
    n_of_rows=sheet_1_by_name.nrows
    for i in range(1,n_of_rows):
        cell_A=sheet_1_by_name.row(i)[index].value
        excelabel[i] = cell_A
    return excelabel


if __name__ =="__main__":
    #亲属关系
    # kinship = need_choose(0,'/home/yzs/gendata/kinship.xlsx')
    # kinship_name = need_choose(7,'/home/yzs/Downloads/data_require/final_new.xlsx')
    # kinship_relation = need_choose(1,'/home/yzs/gendata/kinship.xlsx')[:20]
    # # print(kinship_relation)
    # modal_head =['那个','那','恩','啊','']
    # # name_choice = [name_index,'']
    # head = ['是我','是我的','我','他是我','他是我的','这是我','']
    # head_relation =['','是']
    # tail = ['','关系']
    # Modal = ['', '啊','唉','嘛','呐']
    # name = Gendata([modal_head,head,kinship,Modal],'kinship',2,6000)
    # name.genneed()
    # # name_yes = Gendata([kinship_name, head, kinship], 'kinship', 2, 1000)
    # # name_yes.genneed()
    # name_rl = Gendata([head_relation, kinship_relation, tail], 'kinship', 1, 300)
    # name_rl.genneed()
    #贷款期限
    answer =['本次申请的','我这次申请的','我申请的','','','']
    head =['','贷款','还款','借款','','']
    time_a = ['期限','期限的话','','','']
    attribute = ['是','为','']
    day_need =['六','十二']
    month_need = ['个月','个月的','个月']
    #type2
    answer2 = ['','','','是分','分期']
    month2 = ['个月']
    tail =['付清','还完','付清的','还完的','']
    # lp = Gendata([answer,head,time_a,attribute,day_need,month_need],'loanperiod',4,2000)
    # lp.genneed()
    lp2 = Gendata([answer2,day_need,month2,tail],'loanperiod',1,2001)
    lp2.genneed()
    # n = gennum(2, 1, 2000)
    # print(n.gennum())
    # print(n.gennumpassword())
