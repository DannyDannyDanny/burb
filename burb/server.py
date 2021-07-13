from pathlib import Path

# list dirs in current folder and write to file (files_in_here.txt)
mypath = '.'
mydirs = "\n".join([str(p) for p in Path(mypath).iterdir()])
myfilename = 'files_in_here.txt'
myfile = Path(myfilename)
mytext = f'testing dir: {mypath}' + mydirs
myfile.write_text(mytext)

# list dirs in parent folder and write to file (files_in_parent.txt)
mypath = '..'
mydirs = "\n".join([str(p) for p in Path(mypath).iterdir()])
myfilename = 'files_in_parent.txt'
myfile = Path(myfilename)
mytext = f'testing dir: {mypath}' + mydirs
myfile.write_text(mytext)

# write absolute file path to file (absolute.txt)
mypath = '..'
mydirs = "\n".join([str(p) for p in Path(mypath).iterdir()])
myfilename = 'absolute.txt'
myfile = Path(myfilename)
mytext = str(myfile.absolute())
myfile.write_text(mytext)
