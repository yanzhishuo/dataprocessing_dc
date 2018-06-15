from gendata.inherit import *
from pyexcel import *
from weight_choice import *

# refdeduplication('census_municipalities_county_gen_0523_2000','ref')
#type 1
Modal = ['', '啊', '哦']
title_pattern = ['', '我', '我的']
pronounce = ['那个', '']
feature = ['户籍', '户籍地', '户籍地址', '老家']
verb = ['是', '就是', '在', '']
attribute = ['的', '']

#type 2
title_pattern2 = ['', '我']
verb2 = ['是', '']
tail = ['人', '']
city_county = readexcel(9, '../provincecc.xlsx')
county_mu = readexcel(8, '../provincecc.xlsx')
municipalities = readexcel(7, '../provincecc.xlsx')
# print(city_county,county_mu,municipalities)

def cut_mu(data):
    pro1 = re.match('(.*市)?(.*[县|区])', data)
    pcc = list()
    for x in pro1.groups():
        if x != None:
            pcc.append(x)
    return pcc[0], pcc[1]
# print(cut_mu('北京市密云县'))
# #only city match
#
def census_type1():
    census_raw1_verb = verb[windex([4,1,2,3])]
    census_address1= choice(city_county)
    print(census_address1 +'1')
    census_c, census_county = cut_mu(census_address1)
    census_city_choice = choice(municipalities)
    census_fc = [census_city_choice, '']
    census_cfc = census_fc[windex([1,3])]
    if census_cfc == census_c or census_cfc == ''  :
            m_city = 2
            census_add1 = census_county
    else:
            census_add1 = census_city_choice+census_county
            m_city  = 0
    census_raw1 = Modal[windex([9,0.5,0.5])]+choice(title_pattern) +pronounce[windex([1,9])] +feature[windex([3,3,3,1])] +census_raw1_verb + census_add1
    if census_raw1_verb == '在':
        census_raw1 = census_raw1 + ''
    else:
        census_raw1 = census_raw1 + attribute[windex([1,9])]
    return census_raw1, census_address1, m_city,census_c, census_county

def census_type2():
    census_address1 = choice(city_county)
    print(census_address1 + '1')
    census_c, census_county = cut_mu(census_address1)
    census_city_choice = choice(municipalities)
    census_fc = [census_city_choice, '']
    census_cfc = census_fc[windex([1, 3])]
    if census_cfc == census_c or census_cfc == '':
        m_city = 2
        census_add1 = census_county
    else:
        census_add1 = census_city_choice + census_county
        m_city = 0
    census_raw2 = Modal[windex([9.5,0.3,0.2])]+title_pattern2[windex([7,3])]+verb2[windex([3,7])]+census_add1+tail[windex([3,7])]
    return census_raw2, census_address1,m_city, census_c, census_county

def gen_census():
    index = choice([0,1])
    census_list =[census_type1(), census_type2()]
    census_ref, census_write,m_county, census_c, census_county = census_list[index]
    return census_ref, census_write,m_county, census_c, census_county

if __name__ =="__main__":
    num_data = 2000
    # num_data = 2
    census_data = list()
    for i in range(num_data):
        census_dict = dict()
        census_dict['label_name'] = 'census'
        census_dict['id'] = i
        census_dict['ref'],census_dict['write'],census_dict['m_city'], census_dict['city'], census_dict['county']  = gen_census()
        census_dict['m_county'] = 1
        census_dict['province']=''
        census_dict['m_province'] = ''
        census_data.append(census_dict)
    # print(census_data)
    obj = json.dumps(census_data, ensure_ascii=False, indent=2)
    file = open('/home/yzs/gendata/census_county_gen_0523_2000.json', 'w')
    file.write(obj)
    file.close()
