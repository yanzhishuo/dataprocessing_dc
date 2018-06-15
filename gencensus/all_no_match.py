from gendata.inherit import *
from pyexcel import *
from weight_choice import *

# refdeduplication('census_mu_all_no_match_gen_0523_2000','ref')
def refdeempty(path):
    '''去重：因为生成数据时候容易出现重复，后续会造成人力浪费，故去重
    input:
          文件路径，想去重的标签名字
    output：
          去掉重复的json文件'''
    with open('/home/yzs/gendata/'+path+'.json') as f:
        data_output = json.load(f)
    l4 = []
    for item in data_output:
        if item["m_city"]==2 and item["m_county"]==2:
            continue
        else:
            l4.append(item)
    l = []
    i = 0
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

refdeempty('census_mu_all_no_match_gen_0523_1782')
# #type 1
# Modal = ['', '啊', '哦']
# title_pattern = ['', '我', '我的']
# pronounce = ['那个', '']
# feature = ['户籍', '户籍地', '户籍地址', '老家']
# verb = ['是', '就是', '在', '']
# attribute = ['的', '']
#
# #type 2
# title_pattern2 = ['', '我']
# verb2 = ['是', '']
# tail = ['人', '']
# city_county = readexcel(9, '../provincecc.xlsx')
# county_mu = readexcel(8, '../provincecc.xlsx')
# municipalities = readexcel(7, '../provincecc.xlsx')
# # print(city_county,county_mu,municipalities)

# def cut_mu(data):
#     pro1 = re.match('(.*市)?(.*[县|区])', data)
#     pcc = list()
#     for x in pro1.groups():
#         if x != None:
#             pcc.append(x)
#     return pcc[0], pcc[1]
#
# def census_type1():
#     census_raw1_verb = verb[windex([4,1,2,3])]
#     census_address1 = choice(city_county)
#     census_c, census_county= cut_mu(census_address1)
#     census_city_choice = choice(municipalities)
#     census_county_choice = choice(county_mu)
#     census_fcity = [census_city_choice, '']
#     census_cfcity = census_fcity[windex([1, 0.1])]
#     census_fc = [census_county_choice, '']
#     census_cfc = census_fc[windex([1, 0.1])]
#     if census_cfcity == '' or census_cfcity == census_c:
#         m_city = 2
#         if census_cfc == census_county or census_cfc == ''  :
#            m_county=2
#            census_add1 =''
#         else:
#             census_add1 = census_county_choice
#             m_county = 0
#     else:
#         census_add1 = census_city_choice
#         m_city = 0
#         if census_cfc == census_county or census_cfc == ''  :
#             m_county = 2
#         else:
#             census_add1 = census_add1 + census_county_choice
#             m_county = 0
#     census_raw1 = Modal[windex([9,0.5,0.5])]+choice(title_pattern) +pronounce[windex([1,9])] +feature[windex([3,3,3,1])] +census_raw1_verb + census_add1
#     if census_raw1_verb == '在':
#         census_raw1 = census_raw1 + ''
#     else:
#         census_raw1 = census_raw1 + attribute[windex([1,9])]
#     return census_raw1, census_address1, census_c, census_county,m_city,m_county
#
# def census_type2():
#     census_address1 = choice(city_county)
#     census_c, census_county = cut_mu(census_address1)
#     census_city_choice = choice(municipalities)
#     census_county_choice = choice(county_mu)
#     census_fcity = [census_city_choice, '']
#     census_cfcity = census_fcity[windex([1, 0.1])]
#     census_fc = [census_county_choice, '']
#     census_cfc = census_fc[windex([1, 0.1])]
#     if census_cfcity == '' or census_cfcity == census_c:
#         m_city = 2
#         if census_cfc == census_county or census_cfc == '':
#             m_county=2
#             census_add1 =''
#         else:
#             census_add1 = census_county_choice
#             m_county = 0
#     else:
#         census_add1 = census_city_choice
#         m_city = 0
#         if census_cfc == census_county or census_cfc == '':
#             m_county = 2
#         else:
#             census_add1 = census_add1 + census_county_choice
#             m_county = 0
#     census_raw2 = Modal[windex([9.5,0.3,0.2])]+title_pattern2[windex([7,3])]+verb2[windex([3,7])]+census_add1+tail[windex([3,7])]
#     return census_raw2, census_address1, census_c, census_county, m_city,m_county
#
# def gen_census():
#     index = choice([0,1])
#     census_list =[census_type1(), census_type2()]
#     census_ref, census_write, census_city,census_county, m_city,m_county=census_list[index]
#     return census_ref, census_write, census_city,census_county, m_city,m_county
#
# if __name__ =="__main__":
#     num_data = 2000
#     census_data = list()
#     for i in range(num_data):
#         census_dict = dict()
#         census_dict['label_name'] = 'census'
#         census_dict['id'] = i
#         census_dict['ref'],census_dict['write'], census_dict['city'], census_dict['county'],census_dict['m_city'],census_dict['m_county']= gen_census()
#         census_dict['province']=''
#         census_dict['m_province']=''
#         census_data.append(census_dict)
#     # print(census_data)
#     obj = json.dumps(census_data, ensure_ascii=False, indent=2)
#     file = open('/home/yzs/gendata/census_mu_all_no_match_gen_0523_2000.json', 'w')
#     file.write(obj)
#     file.close()