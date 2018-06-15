from gendata.inherit import *
from pyexcel import *
# pro_city_county = need_choose(0,'/home/yzs/Downloads/data_require/addressdetail/身份证签发机关.xls')
# a=need_choose(1,'/home/yzs/Downloads/data_require/addressdetail/身份证签发机关.xls')
# b=need_choose(2,'/home/yzs/Downloads/data_require/addressdetail/身份证签发机关.xls')

pro_city_county = reademptyexcel(0,'/home/yzs/Downloads/data_require/addressdetail/main身份证签发机关.xlsx')
a= reademptyexcel(1,'/home/yzs/Downloads/data_require/addressdetail/main身份证签发机关.xlsx')
b= reademptyexcel(2,'/home/yzs/Downloads/data_require/addressdetail/main身份证签发机关.xlsx')
# print(len(pro_city_county))
# print(len(a),len(b))

pro_city_county_other = reademptyexcel(0,'/home/yzs/Downloads/data_require/addressdetail/other身份证签发机关.xls')
a_other = reademptyexcel(1,'/home/yzs/Downloads/data_require/addressdetail/other身份证签发机关.xls')
b_other= reademptyexcel(2,'/home/yzs/Downloads/data_require/addressdetail/other身份证签发机关.xls')
print(len(pro_city_county_other))
print(len(a_other),len(b_other))
head=['','','','','','','','','身份证签发机关是','身份证发证机关是','发证机关是','签发机关是','机关是','是','好像是','身份证上写的是']
tail=['','','','','','','吧','签发的','发的']

def choicepcc():
    pro_city_county_chuan = []
    pro_city_county_yue = []
    pro_city_county_su = []
    pro_city_county_zhe = []
    for i,e in enumerate(pro_city_county):
        if e[0:3] in ['四川省']:#,'广东省','江苏省','浙江省']:
            pro_city_county_chuan.append(i)
        elif e[0:3] in ['广东省'] :
            pro_city_county_yue.append(i)
        elif e[0:3] in ['江苏省'] :
            pro_city_county_su.append(i)
        else:
            pro_city_county_zhe.append(i)
    return pro_city_county_chuan,pro_city_county_yue,pro_city_county_su,pro_city_county_zhe
pro_city_county_chuan,pro_city_county_yue,pro_city_county_su,pro_city_county_zhe = choicepcc()
def choiceissuing(issuing_list,a,b):
    choice_num = choice(issuing_list)
    print(choice_num)
    issuingauth = ''
    while issuingauth =='':
        issuingauth = choice([a[choice_num],b[choice_num]])
    return issuingauth

def choiceissuing_other():
    choice_num = randint(0,len(pro_city_county_other)-1)
    print(choice_num)
    c= a_other[choice_num]
    d= b_other[choice_num]
    print(c,d)
    if c ==''and d !='':
        issuingauth = d
    elif c !='' and d =='':
        issuingauth = c
    else:
        issuingauth= choice([c,d])
    return issuingauth

if __name__=="__main__":
    dataneed_data = list()
    num = 3000
    path = 'issuingauthority'
    for i in range(num):
        dataneed_dict = dict()
        isu = choiceissuing(pro_city_county_yue, a, b)
        # isu = choiceissuing_other()
        b_ref = choice(head)+isu+choice(tail)
        dataneed_dict['label_name'] = path
        dataneed_dict['id'] = i
        dataneed_dict['ref'] = b_ref
        dataneed_dict['write'] = isu
        dataneed_data.append(dataneed_dict)
    obj = json.dumps(dataneed_data, ensure_ascii=False, indent=2)
    file = open('/home/yzs/gendata/daqige/authority_10000/' + path + '_gen_' + str(datenow()) + '_yue_' + str(num) + '.json', 'w')
    file.write(obj)
    file.close()

