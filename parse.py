'''
   解析anafora平台
'''

import json
import pathlib
from pprint import pprint

import xmltojson


EVE_PATH = pathlib.Path('anafora/name0415')

LABEL = [
    'address',
    'birthday',
    'carnum',
    'census',
    'company',
    'idcard',
    'name',
    'phonenumber',
]

ANAFORA = [
    '地址：a',
    '生日：b',
    '车牌号：r',
    '户籍：c',
    '公司：o',
    '身份证后四位：i',
    '名字：n',
    '电话号码：p',
]

LABEL_TO_ANAFORA = dict(zip(LABEL, ANAFORA))
ANAFORA_TO_LABEL = dict(zip(ANAFORA, LABEL))
def load_data():
    with open('name_asr_0418_3000.json') as fp:
        data = json.load(fp)
    data_output = list()
    for item in data:
        if item['id'] in range(501):
            continue
        data_output.append(item)
    return data_output

if __name__ == '__main__':
    ref_list = load_data()
    res_list = list()
    for i, ref in enumerate(ref_list):
        res_dict = dict()
        stem = 'case{:05d}'.format(i + 501)
        patt = stem + '.Dialog.anafora.completed.xml'
        EVE_PATH_new=EVE_PATH.joinpath(stem)
        xml_path_list = list(EVE_PATH_new.glob(patt))
        asr_path_list=list(EVE_PATH_new.glob(stem))
        if not xml_path_list:
            continue  # TODO: log why no xml file
        xml_path = xml_path_list[0]
        with xml_path.open() as fp:
            xml_string = fp.read()
        with asr_path_list[0].open() as fp:
            asr_list = fp.read()
        anafora = json.loads(xmltojson.parse(xml_string))
        if not anafora['data']['annotations']:
            dfake = dict()
            dfake['name'] = '无'
            res_list.append(dfake)
        if anafora['data']['annotations']:
            entities = anafora['data']['annotations']['entity']
            if isinstance(entities, dict):
                entities = [entities]
            for j, label in enumerate(entities):
                assert stem in label['id']
                res_label = ANAFORA_TO_LABEL[label['type']]
                span = list(map(int, label['span'].split(',')))
                res_dict[res_label] = asr_list[span[0]:span[1]]
            for label in LABEL:
                res_dict.setdefault(label, '')
            for key in res_dict:
                #print(type(key))
                d = dict()
                if res_dict[key] != '':
                    d[key] = res_dict[key]
                    res_list.append(d)
    #print(res_list)
        #######将原json文件合并进来
    data_output = list()
    for i in range(len(res_list)):
        #print(i)
        z = dict()
        z = {**ref_list[i], **res_list[i]}#合并二个字典  或者 z = x.copy() z.update(y)
        #print(z)
        data_output.append(z)
    # #print(data_output)
    obj=json.dumps(data_output,ensure_ascii=False,indent=2)
    file = open('/home/yzs/name.json', 'w')
    print(type(obj))  # dumps是将dict/list转化成str格式
    file.write(obj)
    file.close()




