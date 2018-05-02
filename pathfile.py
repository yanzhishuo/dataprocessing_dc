#该程序把所有的.V3文件改为.wav文件
import pathlib
from subprocess import run

p = pathlib.Path('.')

# for file in p.glob('*/*.V3'):
# for file in p.glob('*.V3'):
for file in p.glob('*/*/*.V3'):#当前目录下的两级子目录
    print(file.with_suffix('.wav'))
    run(['mv', str(file), str(file.with_suffix('.wav'))])
