import json

def jsonfilew(num_data, label_name, list_type):
    list_data = list()
    for i in range(num_data):
        list_dict = dict()
        list_dict['label_name'] = label_name
        list_dict['id'] = i
        list_dict['ref'], list_dict['write'] = list_type
        list_data.append(list_dict)
    obj = json.dumps(list_data, ensure_ascii=False, indent=2)
    file = open('/home/yzs/'+label_name+'_gen_0424_50000.json', 'w')
    file.write(obj)
    file.close()