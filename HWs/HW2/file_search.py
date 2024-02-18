import os
import sys

def file_search(target_file, current_dir=".") -> str:
    for root, dirs, files in os.walk(current_dir):
        if target_file not in files: continue
        
        file_path = root + "\\" + target_file
        with open(file_path) as f:
            s = ""
            for i in range(5):
                s += f.readline()
            return s
    return f"Файл {target_file} не найден"

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    print(file_search(sys.argv[1], current_directory))