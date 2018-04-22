# a =''
# if a:
#     print('exit')
#
# if not a:
#     print('not exit')
import pathlib

EVE_PATH = pathlib.Path('20180418')
line = '您'
stem = 'case{:05d}'.format(1)
sub_folder = EVE_PATH.joinpath(stem)
sub_folder.mkdir(mode=0o775)
file_path = sub_folder.joinpath(stem)
with file_path.open('w') as fp_o:
    fp_o.write(line)
#文件的格式 plain text document (text/plain)
