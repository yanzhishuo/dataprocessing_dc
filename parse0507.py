import json
import pathlib
from pprint import pprint

import xmltojson


EVE_PATH = pathlib.Path('all_no_match')

LABEL = [
    'province',
    'city',
    'county',
    'empty',
]

ANAFORA = [
    '省：a',
    '市：s',
    '县：d',
    '空：f',
]

LABEL_TO_ANAFORA = dict(zip(LABEL, ANAFORA))
ANAFORA_TO_LABEL = dict(zip(ANAFORA, LABEL))

def load_data(filename):
        with open(filename) as fp:
            data = json.load(fp)
        data_output = list()
        for item in data:
        #    if item['id'] in range(501):
         #       continue
            data_output.append(item)
        return data_output

if __name__ == '__main__':
    filename = '/home/yzs/census0502/census_all_no_match_gen_0502_2000.json'
    ref_list = load_data(filename)
    res_list = list()
    for i, ref_dict in enumerate(ref_list):
        print(ref_dict['ref'])
        print(i)
        res_dict = dict()
        stem = 'case{:05d}'.format(i)
        patt = stem + '.census.anafora.completed.xml'
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
        print(asr_list)
        anafora = json.loads(xmltojson.parse(xml_string))
        entities = anafora['data']['annotations']['entity']
        if isinstance(entities, dict):
            entities = [entities]
        # for j, label in enumerate(entities):
        #     print(ANAFORA_TO_LABEL[label['type']])
        for j, label in enumerate(entities):
            assert stem in label['id']
            res_label = ANAFORA_TO_LABEL[label['type']]
            span = list(map(int, label['span'].split(',')))
            # print(asr_list[i])
            # print(span[0],span[1])
            # print(asr_list[span[0]:span[1]])
            res_dict[res_label] = asr_list[span[0]:span[1]]
        for label in LABEL:
            res_dict.setdefault(label, '')
            # print(res_dict)
        # res_list.append({'label': res_dict, 'case': stem, 'asr': asr_list[i], 'ref': ref})
        res_list.append(res_dict)
    data_output = list()
    for i in range(len(res_list)):
                #print(i)
        z = dict()
        z = {**ref_list[i], **res_list[i]}#合并二个字典  或者 z = x.copy() z.update(y)
                    #print(z)
        data_output.append(z)
                                # #print(data_output)
    obj=json.dumps(data_output,ensure_ascii=False,indent=2)
    file = open('/home/yzs/census_all_no_match_gen_0502_2000.json', 'w')
    # print(type(obj))  # dumps是将dict/list转化成str格式
    file.write(obj)
    file.close()
