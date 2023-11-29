import os
from concurrent.futures import ThreadPoolExecutor

def sort_files_by_extension(folder_path):
    files_by_extension = {}
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            extension = os.path.splitext(file)[-1].lower()
            if extension not in files_by_extension:
                files_by_extension[extension] = []
            files_by_extension[extension].append(file_path)
    return files_by_extension

def process_folder(folder_path):
    with ThreadPoolExecutor() as executor:
        future = executor.submit(sort_files_by_extension, folder_path)
        result = future.result()
    return result

folder_path = '/шлях/до/папки/хлам'
sorted_files = process_folder(folder_path)
print(sorted_files)
