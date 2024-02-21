# duptree.py: creates a directory tree from a list of files
# 2024-02-21, created

# bash> IFS=$'\n';for i in $(sort dup.txt | uniq | grep -v '\\$'| sed 's#\\\\#/#g' | sed 's#^...##'); do echo $i;mkdir -p "_3/$(dirname $i)" ;touch "_3/$i";done

import os
import re
import argparse

def test8():
    parser=argparse.ArgumentParser(description='creates a dummy directory tree')
    parser.add_argument('file',type=str,default='dup.txt',nargs='?',help='file (default=./dup.txt)')
    parser.add_argument('-o','--outdir',type=str,default='_dup',help='output base dir (default=./_dup)')
    parser.add_argument('-v','--verbose',action='store_true',help='more wordy output')
    args=parser.parse_args()
    args.verbose and print("Building %s from %s .." % (args.outdir,args.file))
    f=open(args.file,'r', encoding='UTF8')
    ar=set([li.strip() for li in f.readlines()] )    # discard trailing newlines
    ar=[re.sub(r'^.:', args.outdir, li) for li in ar if not li.endswith(r'\\')]  # discard dirs, and substitute the drive prefix with the output dir for the rest
    dirs=set([os.path.split(li)[0] for li in ar])   # use set to discard duplicates
#    print("\n".join(dirs))
    [os.path.exists(dir) or os.makedirs(dir) for dir in dirs]
#    [open(li,"w").close() for li in ar]
    [open(li,"w") for li in ar]     # FIXME no close()?
    args.verbose and print("\n".join(ar))


test8()
