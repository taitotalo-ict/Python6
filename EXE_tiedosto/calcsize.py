from pathlib import Path
# import sys
import argparse
import logging


# logger = logging.getLogger(__name__)
logging.basicConfig(filename='calcsize.log', format='{asctime} - {levelname}:{message}', style='{', level=logging.INFO)
logging.info('Starting script')

parser = argparse.ArgumentParser(prog='calcsize', description='Calculates the size of a folder (with subdirectories)')
parser.add_argument('folder', type=str, help='Path to the folder to calculate size for', default=Path('.'))
args = parser.parse_args()

folder = Path(args.folder)
logging.info(f'Folder to calculate size: {folder.absolute()}')

# folder = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')

summa = sum(item.stat().st_size for item in folder.rglob('*') if item.is_file())
print(f'\nTotal size: {summa} bytes ({summa/1024/1024:.2f}MB)')
logging.info('Ending script')