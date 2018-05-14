import json

filename = '/home/yzs/census0502/census_all_no_match_gen_0502_2000.json'
with open(filename) as fp:
    data = json.load(fp)
data_output = list()
i =0
for item in data:
    data_dict = dict ()
    if not item['ref']:
        continue
    data_dict['id'] = i
    data_dict['ref'] =item['ref']
    data_dict['m_city'] =item['m_city']
    data_dict['m_province'] =item['m_province']
    data_dict['m_county'] =item['m_county']
    data_dict['province_w'] =item['province_w']
    data_dict['city_w'] =item['city_w']
    data_dict['county_w'] =item['county_w']
    data_dict['write'] =item['write']
    data_dict['label_name'] =item['label_name']
    data_dict['asr'] =item['asr']
    i = i +1
    data_output.append(data_dict)
obj=json.dumps(data_output,ensure_ascii=False,indent=2)
file = open('/home/yzs/census_all_no_match_gen_0502_2000.json', 'w')
    # print(type(obj))  # dumps是将dict/list转化成str格式
file.write(obj)
file.close()
