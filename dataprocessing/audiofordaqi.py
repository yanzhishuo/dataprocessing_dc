import json
import pathlib

with open('/home/yzs/workspace/dataprocessing/validperiod_gen_0508_2000.json') as f:
    data=json.load(f)
_json=dict()
dest_json = pathlib.Path('/home/yzs/gendata').joinpath('ref.json')
for indx in range(2000):
    _json['{:>05}.wav'.format(indx)] = dict(
            ref= data[indx]['ref'],
            tsinghua_asr=data[indx]['id'],
        )
dest_json.write_text(json.dumps(_json, ensure_ascii=False, indent=4))