from gendata.inherit import *
import time
from random import *
from weight_choice import *

road = readexcel(0,'/home/yzs/genXJ/xjdata.xlsx')
yearxj=['今年','2018年','']

def ymdxj():
    a=choice(yearxj)
    b=choice(['1', '2', '3', '4', '5'])
    if b in ['1', '3', '5']:
        c = str(randint(1,31))
    elif b ==2:
        c = str(randint(1, 28))
    else:
        c = str(randint(1,30))
    return a+b+'月'+c+'日',a,b,c

def datexj(index):
    if index ==1:
        ref,year,month,day=ymdxj()
    else:
        a =choice(['昨天','今天'])
        ref,year,month,day=a,'','',a
    return ref,year,month,day

def zao():
    a = '早上'
    b = choice(['06', '07', '08', '09']) + ':' + choice([str(randint(10, 59)),'00'])
    return a,b
def zhong():
    a = '中午'
    c=str(randint(1, 59))
    if len(c)==1:
        c='0'+c
    b = '12:' + choice([c,'00'])
    return a,b
def xiawu():
    a = '下午'
    b = str(choice([1, 2, 3, 4, 5, 6])) + ':' + choice([str(randint(10, 59)),'00'])
    return a,b
def wan():
    a = '晚上'
    b = str(choice([7, 8, 9, 10, 11, 12])) + ':' + choice([str(randint(10, 59)),'00'])
    return a,b

def twelve():
    b = choice(['00','01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12']) + ':' + choice([str(randint(10, 59)),'00'])
    return '',b
def twentyfour():
    b = str(choice([13, 14, 15, 16, 17, 18, 19, 20, 21, 22,23])) + ':' + choice([str(randint(10, 59)),'00'])
    return '',b

def moment():
    a = choice(['早上','中午','下午',''])
    if a=='早上':
       a1,b1=zao()
       a2,b2=choice([zhong(),xiawu(),wan(),twentyfour()])
    elif a=='中午':
       a1,b1=zhong()
       x =xiawu()
       w =wan()
       t = twentyfour()
       a2,b2=choice([x,w,t])
    elif a=='下午':
        a1, b1 = xiawu()
        a2, b2 = wan()
    else:
        a1, b1 = twelve()
        x = xiawu()
        w = wan()
        t = twentyfour()
        a2, b2 = choice([x, w, t])
    return a1,a2,b1,b2
if __name__=="__main__":
    # print(ymdxj())
    # print(gendate_time())
    # num_data = 200
    # xj_data = list
    # ()
    # for i in range(num_data):
    #     xj_dict = dict()
    #     a = choice(road)
    #     xj_dict['part'] = ''
    #     xj_dict['year'] = ''
    #     xj_dict['month'] = ''
    #     xj_dict['day'] = ''
    #     xj_dict['id'] ：%= i
    #     xj_dict['ref']='打开'+a+'摄像机实况'
    #     xj_dict['asr'] = ''
    #     xj_dict['sloc'] = a
    #     xj_dict['eloc'] = ''
    #     xj_dict['date'] = ''
    #     xj_dict['st'] = ''
    #     xj_dict['et'] = ''
    #     xj_dict['speed'] =''
    #     xj_dict['windownormal'] =''
    #     xj_dict['part'] = ''
    #     xj_dict['type'] = '实况'
    #     xj_dict['cmd_type'] = 'normal'
    #     xj_data.append(xj_dict)
    # # print(xj_data)
    # obj = json.dumps(xj_data, ensure_ascii=False, indent=2)
    # file = open('/home/yzs/genXJ/xj_gen_0529_200.json', 'w')
    # file.write(obj)
    # file.close()
#打开xxx摄像机实况
    num_data = 800
    xj_data = list()
    for i in range(num_data):
        xj_dict = dict()
        a = choice(road)
        # l=[1,2]
        ref, year, month, day =  datexj(choice([1,2]))
        a1,a2,b1,b2 = moment()
        xj_dict['year'] = year
        xj_dict['month'] = month
        xj_dict['day'] = day
        xj_dict['id'] = i
        xj_dict['ref']='打开'+a+'摄像机'+ref+a1+b1+'到'+a2+b2+'的录像'
        xj_dict['asr'] = ''
        xj_dict['sloc'] = a
        xj_dict['eloc'] = ''
        xj_dict['st'] = b1
        xj_dict['et'] = b2
        xj_dict['speed'] =''
        xj_dict['windownormal'] =''
        xj_dict['part'] = ''
        xj_dict['type'] = '录像'
        xj_dict['cmd_type'] = 'normal'
        xj_data.append(xj_dict)
    # print(xj_data)
    obj = json.dumps(xj_data, ensure_ascii=False, indent=2)
    file = open('/home/yzs/genXJ/xj_gen_0529_vide0_800.json', 'w')
    file.write(obj)
    file.close()
#打开xxx摄像机+【昨天/今天/*月*日/*年*月*日】+【早上/中午/下午/晚上/‘’]+*点/*点*+到+[早上/中午/下午/晚上/'']+*点/*点*分（12/24时）的录像
