import json
from datetime import datetime
from gendata.inherit import *

def open_json(path):
    with open(path) as f:
        data = json.load(f)
    return data

class Combinejson():
    '''path1,path2是要合并的两个json文件的路径，path3是合并后的json文件保存的路径'''
    def __init__(self,path1,path2,path3):
        self.path1=path1
        self.path2 = path2
        self.path3 = path3
        self.data1 = list()

    def combine(self):
        data,data1=open_json(self.path1),open_json(self.path2)
        self.data1 = data
        for item in data1:
            self.data1.append(item)
        return self.data1

    def merge(self):
        i = 0
        l = []
        self.combine()
        for item in self.data1:
            item['id'] = i
            i = i + 1
            l.append(item)
        obj=json.dumps(l,ensure_ascii=False,indent=2)
        file=open(self.path3,'w')
        print(type(obj))#dumps是将dict/list转化成str格式
        file.write(obj)
        file.close()

def cutjson(path,num,path2,number):
    '''全切分（把一个json文件全部切分）'''
    with open(path) as f:
        data = json.load(f)
    for i in range(num):
        data_output = list()
        for item in data:
            print(i)
            if item['id'] in range(number*i,number*(i+1)):
                data_output.append(item)
            if i == num-1:
                if item['id'] in range(number * (i + 1)+1,len(data)):
                    data_output.append(item)
        # print(data_output)
        obj=json.dumps(data_output,ensure_ascii=False,indent=2)
        file=open('/home/yzs/gendata/'+path2+'_gen_'+str(datenow())+'_'+str(number)+'_'+str(i+1)+'.json','w')
        print(type(obj))#dumps是将dict/list转化成str格式
        file.write(obj)
        file.close()

def cutpartjson(path,num,path2,number):
    '''部分切分（把一个json文件取出部分并切分）'''
    with open(path) as f:
        data = json.load(f)
    for i in range(num):
        data_output = list()
        for item in data:
            print(i)
            if item['id'] in range(number*i,number*(i+1)):
                data_output.append(item)
        obj=json.dumps(data_output,ensure_ascii=False,indent=2)
        file=open('/home/yzs/gendata/'+path2+'_gen_'+str(datenow())+'_'+str(number)+'_'+str(i+1)+'.json','w')
        print(type(obj))#dumps是将dict/list转化成str格式
        file.write(obj)
        file.close()

if __name__ == '__main__':
    # print('1')
    # cutpartjson('/home/yzs/gendata/intent/repeat_gen_0527_5098_1.jso()
    # c = Combinejson('/home/yzs/gendata/loanperiod_gen_0613_463.json','/home/yzs/gendata/loanperiod_gen_0613_30.json'
    #                 ,'/home/yzs/gendata/loanperiod_gen_0613_493.json')
    # c.merge()
    # class Merge(Combinejson):
    #     def __init__(self,path1,path2,path3,path4):#,path5):
    #         Combinejson.__init__(self,path1,path2,path3)
    #         self.path4 = path4
    #         #self.path5 = path5
    #
    #     def combine(self):
    #         # data, data1,data2,data3 = open_json(self.path1), open_json(self.path2),open_json(self.path4)#, open_json(self.path5)
    #         data, data1,data2 = open_json(self.path1), open_json(self.path2),open_json(self.path4)#, open_json(self.path5)
    #         self.data1 = data
    #         for item in data1:
    #             self.data1.append(item)
    #         for item in data2:
    #             self.data1.append(item)
    #         # for item in data3:
    #         #     self.data1.append(item)
    #         return self.data1
    #
    # c =Merge('/home/yzs/gendata/intent/consult_gen_0527_132.json',
    #          '/home/yzs/gendata/intent/quit_gen_0527_140.json',
    #          '/home/yzs/gendata/intent/intent_gen_0610.json',
    #          '/home/yzs/gendata/intent/stop_gen_0527_778.json')#,'/home/yzs/gendata/intent/chuan/census_procc_gen_0530_400.json')
    # # c = Merge('./address_right_gen_0609_1000_1.json',
    # #           './address_right_gen_0609_1000_2.json',
    # #           './address_gen_0610_2100.json',
    # #           './address_right_gen_0609_100_3.json')
    # c.merge()
    # class Merge(Combinejson):
    #     def __init__(self,path1,path2,path3,path4,path5,path6):
    #         Combinejson.__init__(self,path1,path2,path3)
    #         self.path4 = path4:
    #         self.path5 = path5
    #         self.path6 = path6
    #
    #     def combine(self):
    #         data, data1,data2,data3,data4 = open_json(self.path1), open_json(self.path2),open_json(self.path4), open_json(self.path5), open_json(self.path6)
    #         self.data1 = data
    #         for item in data1:
    #             self.data1.append(item)
    #         for item in data2:
    #             self.data1.append(item)
    #         for item in data3:
    #             self.data1.append(item)
    #         for item in data4:
    #             self.data1.append(item)
    #         return self.data1
    #
    # c =Merge('/home/yzs/gendata/5_phone_address/census_gen_0530_suzhe_1200.json',
    #          '/home/yzs/gendata/5_phone_address/other/other/census_county_gen_0530_300.json',
    #          '/home/yzs/gendata/5_phone_address/census_gen_0603_3000.json',
    #          '/home/yzs/gendata/5_phone_address/other/other/census_proc_gen_0530_600.json',
    #          '/home/yzs/gendata/5_phone_address/other/other/census_procounty_gen_0530_600.json',
    #          '/home/yzs/gendata/5_phone_address/other/other/census_pro_gen_0530_300.json',
    #          )
    # c.merge()
    # cutjson('/home/yzs/gendata/5_phone_address/census_gen_0603_3000.json', 3, '5_phone_address/census', 1000)
    # class Merge(Combinejson):
    #     def __init__(self,path1,path2,path3,path4,path5):
    #         Combinejson.__init__(self,path1,path2,path3)
    #         self.path4 = path4
    #         self.path5 = path5
    #
    #     def combine(self):
    #         data, data1,data2,data3 = open_json(self.path1), open_json(self.path2),open_json(self.path4), open_json(self.path5)
    #         self.data1 = data
    #         for item in data1:
    #             self.data1.append(item)
    #         for item in data2:
    #             self.data1.append(item)
    #         for item in data3:
    #             self.data1.append(item)
    #         return self.data1
    #
    # c =Merge('/home/yzs/gendata/5_phone_address/other/census_city_county_gen_0530_300.json','/home/yzs/gendata/5_phone_address/other/census_city_gen_0530_300.json','/home/yzs/gendata/5_phone_address/census_gen_0530_1000_4.json',
    #          '/home/yzs/gendata/5_phone_address/mu_tai/census_gen_0530_100_1.json','/home/yzs/gendata/5_phone_address/mu_tai/census_mu4_gen_0530_300_1.json')
    # c.merge()
    class Merge(Combinejson):
        def __init__(self,path1,path2,path3,path4,path5,path6,path7):
            Combinejson.__init__(self,path1,path2,path3)
            self.path4 = path4
            self.path5 = path5
            self.path6 = path6
            self.path7 = path7

        def combine(self):
            data, data1,data2,data3 = open_json(self.path1), open_json(self.path2),open_json(self.path4), open_json(self.path5)
            data5,  data4 = open_json(self.path7), open_json(self.path6)
            self.data1 = data
            for item in data1:
                self.data1.append(item)
            for item in data2:
                self.data1.append(item)
            for item in data3:
                self.data1.append(item)
            for item in data4:
                self.data1.append(item)
            for item in data5:
                self.data1.append(item)
            return self.data1

    c =Merge('/home/yzs/gendata/occupation_gen_0614_label1_53.json','/home/yzs/gendata/occupation_gen_0614_label2_30.json','/home/yzs/gendata/occupation_gen_0614.json',
             '/home/yzs/gendata/occupation_gen_0614_label3_26.json','/home/yzs/gendata/occupation_gen_0614_label4_29.json','/home/yzs/gendata/occupation_gen_0614_label5_841.json',
             '/home/yzs/gendata/occupation_gen_0614_label6_1278.json')
    c.merge()
    # class Merge(Combinejson):
    #     def __init__(self,path1,path2,path3,path4,path5,path6,path7,path8):
    #         Combinejson.__init__(self,path1,path2,path3)
    #         self.path4 = path4
    #         self.path5 = path5
    #         self.path6 = path6
    #         self.path7 = path7
    #         self.path8 = path8
    #
    #     def combine(self):
    #         data, data1,data2,data3 = open_json(self.path1), open_json(self.path2),open_json(self.path4), open_json(self.path5)
    #         data5,  data4,data6 = open_json(self.path7), open_json(self.path6), open_json(self.path8)
    #         self.data1 = data
    #         for item in data1:
    #             self.data1.append(item)
    #         for item in data2:
    #             self.data1.append(item)
    #         for item in data3:
    #             self.data1.append(item)
    #         for item in data4:
    #             self.data1.append(item)
    #         for item in data5:
    #             self.data1.append(item)
    #         for item in data6:
    #             self.data1.append(item)
    #         return self.data1
    #
    # c =Merge('/home/yzs/gendata/5_phone_address/yue/census_city_county_gen_0530_300.json',
    #          '/home/yzs/gendata/5_phone_address/yue/census_city_gen_0530_300.json',
    #          '/home/yzs/gendata/5_phone_address/census_gen_0603_3000.json',
    #          '/home/yzs/gendata/5_phone_address/yue/census_county_gen_0530_300.json',
    #          '/home/yzs/gendata/5_phone_address/yue/census_procc_gen_0530_600.json',
    #          '/home/yzs/gendata/5_phone_address/yue/census_proc_gen_0530_600.json',
    #          '/home/yzs/gendata/5_phone_address/yue/census_procounty_gen_0530_600.json',
    #          '/home/yzs/gendata/5_phone_address/yue/census_pro_gen_0530_300.json',
    #          )
    # c.merge()
    # class Merge(Combinejson):
    #     def __init__(self,path1,path2,path3,path4,path5,path6,path7,path8,path9):
    #         Combinejson.__init__(self,path1,path2,path3)
    #         self.path4 = path4
    #         self.path5 = path5
    #         self.path6 = path6
    #         self.path7 = path7
    #         self.path8 = path8
    #         self.path9 = path9
    #
    #     def combine(self):
    #         data, data1,data2,data3,data4 = open_json(self.path1), open_json(self.path2),open_json(self.path4), open_json(self.path5), open_json(self.path6)
    #         data5,data6,data7 = open_json(self.path7), open_json(self.path8), open_json(self.path9)
    #         self.data1 = data1
    #         for item in data:
    #             self.data1.append(item)
    #         for item in data2:
    #             self.data1.append(item)
    #         for item in data3:
    #             self.data1.append(item)
    #         for item in data4:
    #             self.data1.append(item)
    #         for item in data5:
    #             self.data1.append(item)
    #         for item in data6:
    #             self.data1.append(item)
    #         for item in data7:
    #             self.data1.append(item)
    #         return self.data1
    # c =Merge('/hd4T/dialog_data_stage_2_variation/xj/tag/xj.json','/hd4T/dialog_data_stage_2_variation/xj/tag/xj1.json','/home/yzs/gendata/10_phone_carbrand_out/10_phone_carbrand_out/carbrand_gen_0530_1000_1.json',
    #           '/hd4T/dialog_data_stage_2_variation/xj/tag/xj2.json','/hd4T/dialog_data_stage_2_variation/xj/tag/xj3.json','/hd4T/dialog_data_stage_2_variation/xj/tag/xj4.json',
    #           '/hd4T/dialog_data_stage_2_variation/xj/tag/xj5.json','/hd4T/dialog_data_stage_2_variation/xj/tag/xj6.json','/hd4T/dialog_data_stage_2_variation/xj/tag/xj7.json')
    # c.merge()