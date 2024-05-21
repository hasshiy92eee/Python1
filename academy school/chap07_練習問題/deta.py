import glob

file_paths = glob.glob('data/*.csv')
for file in file_paths:
    print(file.replace('data\\', ''))

