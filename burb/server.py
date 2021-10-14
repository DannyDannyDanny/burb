from pathlib import Path
import time
from loguru import logger
import os
logger.add("output/log.txt", level="DEBUG")

AUDIO_FILES_DIR = os.environ['AUDIO_FILES_DIR']
logger.debug(f'{AUDIO_FILES_DIR = }')

logger.debug(f'{list(Path(".").iterdir()) = }')
for p in Path('.').iterdir():
    if p.is_dir():
        logger.debug(f'{str(p)} -> {len(list(p.iterdir()))} files')
    else:
        logger.debug(f'{str(p)} is file')

logger.debug(f'{list(Path(AUDIO_FILES_DIR).iterdir()) = }')
# TODO: bring while back with sleep
# while True:

# list dirs in audio folder
mydirs = [p.name for p in Path(AUDIO_FILES_DIR).iterdir()]
logger.debug('files in audio dir:\n' + "\n\t".join(mydirs))

# myfilename = 'output/files_in_parent.txt'
# myfile = Path(myfilename)
# mytext = f'testing dir: {mypath}' + mydirs
# myfile.write_text(mytext)

# TODO: bring sleep back with while
# time.sleep(60*60)
