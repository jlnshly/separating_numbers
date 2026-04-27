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
    squared_evens = engine.transmute_even()
    cubed_odds = engine.transmute_odd()
    FileManager.write_file(even_numbers, squared_evens)
    FileManager.write_file(odd_numbers, cubed_odds)
    print('Transmutation successful!')
    print(f'{len(squared_evens)} squared evens were transmitted to {even_numbers}!')
    print(f'{len(cubed_odds)} squared evens were transmitted to {odd_numbers}!')

if __name__ == '__main__':
    run_transmuter()


