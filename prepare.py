#!/usr/bin/env python3

"""
How to use:

./main.py <input_file> --EVE=<number>

"""
import argparse
import os
import pathlib

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('in_path', type=str)
    parser.add_argument('--EVE', type=int)
    parser.add_argument('--case', type=int)
    args = parser.parse_args()
    if args.EVE is None:
        args.EVE = 0
    if args.case is None:
        args.case = 0
    if args.EVE > 999:
        raise ValueError
    folder = pathlib.Path('EVE{:03d}'.format(args.EVE))
    if not folder.exists():
        folder.mkdir(mode=0o775)
    in_path = pathlib.Path(args.in_path)
    with in_path.open('r') as fp_in:
        for i, line in enumerate(fp_in):
            stem = 'case{:05d}'.format(i)
            sub_folder = folder.joinpath(stem)
            sub_folder.mkdir(mode=0o775)
            file_path = sub_folder.joinpath(stem)
            with file_path.open('w') as fp_o:
                fp_o.write(line)
