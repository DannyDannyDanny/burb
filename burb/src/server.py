from pathlib import Path
import time
from loguru import logger
logger.add("log.txt", level="DEBUG")

logger.debug('')
while True:
    # list dirs in current folder and write to file (files_in_here.txt)
    mypath = '.'
    mydirs = "\n".join([str(p) for p in Path(mypath).iterdir()])
    logger.debug('files in current dir')
    logger.debug(mydirs)
    myfilename = 'files_in_here.txt'
    myfile = Path(myfilename)
    mytext = f'testing dir: {mypath}' + mydirs
    myfile.write_text(mytext)

    # list dirs in parent folder and write to file (files_in_parent.txt)
    mypath = '..'
    mydirs = "\n".join([str(p) for p in Path(mypath).iterdir()])
    logger.debug('files in parent')
    logger.debug(mydirs)
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
    logger.debug('absolute path')
    logger.debug(mydirs)
    myfile.write_text(mytext)

    time.sleep(60)
