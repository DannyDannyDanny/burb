from pathlib import Path
import time
from loguru import logger
logger.add("output/log.txt", level="DEBUG")

logger.debug('')
while True:
    # list dirs in current folder and write to file (files_in_here.txt)
    mypath = '.'
    mydirs = "\n".join([str(p) for p in Path(mypath).iterdir()])
    logger.debug('files in current dir')
    logger.debug(mydirs)
    myfilename = 'output/files_in_here.txt'
    myfile = Path(myfilename)
    mytext = f'testing dir: {mypath}' + mydirs
    myfile.write_text(mytext)

    # list dirs in parent folder and write to file (files_in_parent.txt)
    mypath = '..'
    mydirs = "\n".join([str(p) for p in Path(mypath).iterdir()])
    logger.debug('files in parent')
    logger.debug(mydirs)
    myfilename = 'output/files_in_parent.txt'
    myfile = Path(myfilename)
    mytext = f'testing dir: {mypath}' + mydirs
    myfile.write_text(mytext)

    # write absolute file path to file (absolute.txt)
    mypath = '..'
    mydirs = "\n".join([str(p) for p in Path(mypath).iterdir()])
    myfilename = 'output/absolute.txt'
    myfile = Path(myfilename)
    mytext = str(myfile.absolute())
    logger.debug('absolute path')
    logger.debug(mydirs)
    myfile.write_text(mytext)

    #TODO: read list of new files (from db)
    if False:
        # reading file from directory
        filepath = '.' # TODO: get a file from db
        file_to_read = Path(filepath)
        logger.debug(f'reading file {file_to_read.absolute()}')
        logger.debug(f'file size: {file_to_read.stat().st_size}')

    time.sleep(60*60)
