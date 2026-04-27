import os

class FileManager:
    @staticmethod
    def read_file(filepath):
        """Reads integers from file"""
        if not os.path.exists(filepath):
            return []
        with open(filepath, 'r') as f:
            return [int(x) for x in f.read().split() if x.lstrip('-').isdigit()]

    @staticmethod
    def write_file(filepath, data):
        """Writes data to file"""
        with open(filepath, 'w') as f:
            for item in data:
                f.write(str(item) + '\n')
