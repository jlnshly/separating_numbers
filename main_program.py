from file_manager import FileManager
from functionalities import NumberSeparator
import time

def run_transmuter():
    source = 'integers.txt'
    even_numbers = 'double.txt'
    odd_numbers = 'triple.txt'
    print('Welcome...')
    time.sleep(1)
    raw_data = FileManager.read_file(source)
    if not raw_data:
        print(f'No data available, {source} might be missing/empty!')
        return
    engine = NumberSeparator(raw_data)
    squared


