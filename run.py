import subprocess
import os, sys
import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument('-f',dest='fname',help='Name of the rnw and other files',
                    default = 'example_under_construction')
parser.add_argument('-c', dest = 'cleanup' , help='Removes old files from this name')
parser.add_argument('-o',dest='old_file',help='Override the filename for cleanup')
args = parser.parse_args()
cwd = os.getcwd()

if args.cleanup == 'True':
    ignore_files = [args.fname+'.R', args.fname+'.rnw', 'run.py']
    files = set(os.listdir()) - set(ignore_files)
    dirname = 'backup'+str(random.randint(1,100))
    os.mkdir(dirname,755)
    for file in files:
        new_file = os.path.join(dirname, file)
        os.rename(file, new_file)
    sys.exit()

fname = args.fname
cmd1 = 'R CMD BATCH '+fname+'.R'
cmd2 = 'pdflatex '+fname+'.tex'
cmd3 = 'biber '+fname
cmd4 = 'pdflatex '+fname+'.tex'
cmd5 = 'xdg-open '+fname+'.pdf'
cmds = [cmd1,cmd2,cmd3,cmd4,cmd5]
for cmd in cmds:
	subprocess.call(cmd,shell='True')
