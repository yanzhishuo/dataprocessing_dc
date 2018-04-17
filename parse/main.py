import jsonyzs
import pathlib
from pprint import pprint

import xmltojson


EVE_PATH = pathlib.Path('address0408')

LABEL = [
    's_loc',
    'e_loc',
    'year',
    'month',
    'day',
    'st',
    'et',
    'speed',
    'window',
    'part',
    'type',
]

ANAFORA = [
    '地址：a',
    '生日：b',
    '年：y',
    '月：m',
    '日：d',
    '起始时间：c',
    '终止时间：v',
    '播放速度：s',
    '窗格：w',
    '时间：p',
    '类型：t',
]

LABEL_TO_ANAFORA = dict(zip(LABEL, ANAFORA))
ANAFORA_TO_LABEL = dict(zip(ANAFORA, LABEL))



def load_data():
    with open('asr_1127_404_np.txt') as fp:
        asr_list = [i.strip() for i in fp.readlines()]
    with open('data_1127_404_np.txt') as fp:
        ref_list = [i.strip() for i in fp.readlines()]
    return asr_list, ref_list



if __name__ == '__main__':
    asr_list, ref_list = load_data()
    res_list = list()
    for i, ref in enumerate(ref_list):
        res_dict = dict()
        stem = 'case{:05d}'.format(i)
        patt = stem + '/' + stem + '*.xml'
        xml_path_list = list(EVE_PATH.glob(patt))
        if not xml_path_list:
            continue  # TODO: log why no xml file
        xml_path = xml_path_list[0]
        with xml_path.open() as fp:
            xml_string = fp.read()
        anafora = jsonyzs.loads(xmltojson.parse(xml_string))
        entities = anafora['data']['annotations']['entity']
        if isinstance(entities, dict):
            entities = [entities]
        for j, label in enumerate(entities):
            assert stem in label['id']
            res_label = ANAFORA_TO_LABEL[label['type']]
            span = list(map(int, label['span'].split(',')))
            res_dict[res_label] = asr_list[i][span[0]:span[1]]
        res_dict['case'] = stem
        res_dict['asr'] = asr_list[i]
        res_dict['ref'] = ref
        for label in LABEL:
            res_dict.setdefault(label, '')
        # res_list.append({'label': res_dict, 'case': stem, 'asr': asr_list[i], 'ref': ref})
        res_list.append(res_dict)
    print(jsonyzs.dumps(res_list, ensure_ascii=False, indent=2))
