from gendata.inherit import *
#
labelist1 = excel2label(0,'/home/yzs/Downloads/data_require/银行.xls')
labelist2=excel2label(1,'/home/yzs/Downloads/data_require/银行.xls')
# labelist = dict(labelist1, **labelist2)
labelist = {}
print(len(labelist1))
for k,v in labelist1.items():
    labelist[k] = v
for k,v in labelist2.items():
    if v:
        l=labelist[k]
        labelist[k]=list()
        labelist[k].append(l)
        labelist[k].append(v)
    # print(labelist)
labelist3=excel2label(2,'/home/yzs/Downloads/data_require/银行.xls')
labelist4=excel2label(3,'/home/yzs/Downloads/data_require/银行.xls')
labelist5=excel2label(4,'/home/yzs/Downloads/data_require/银行.xls')
for k,v in labelist3.items():
    if v:
        labelist[k].append(v)
for k,v in labelist4.items():
    if v:
        labelist[k].append(v)
for k,v in labelist5.items():
    if v:
        labelist[k].append(v)
# print(labelist)
print(len(labelist))

modal = ['','','','','','','是','我本笔贷款的收款银行是','我银行卡是','贷款的收款银行是','收款银行是','恩','那个','啊','是','应该是','好像是','本次贷款的收款银行是']
tail = ['','','','','','的','的','的','卡','嘛','吧','啊']

banklist =[]
for k,v in labelist.items():
    if isinstance(labelist[k], str):
        bankdict = {}
        bankdict['label'] = k
        bankdict['write'] = v
        banklist.append(bankdict)
    else:
        for e in v:
            bankdict = {}
            bankdict['label'] = k
            bankdict['write'] =e
            # print(bankdict)
            banklist.append(bankdict)
print(len(banklist))
print(banklist)

dataneed_data = list()
num = 5000
path = 'bank'
for i in range(num):
    C = randint(0,len(banklist)-1)
    a =  banklist[C]['write']
    dataneed_dict = dict()
    dataneed_dict['label_name'] = path
    dataneed_dict['id'] = i
    dataneed_dict['ref'] = choice(modal)+a+choice(tail)
    dataneed_dict['write'] = a
    dataneed_dict['label'] = banklist[C]['label']
    dataneed_data.append(dataneed_dict)
obj = json.dumps(dataneed_data, ensure_ascii=False, indent=2)
file = open('/home/yzs/gendata/'+path+'_gen_'+str(datenow())+'_'+str(num)+'.json', 'w')
file.write(obj)
file.close()

# refdeduplication('bank_gen_0613_5000','ref')