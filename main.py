import os

path = """insert folder path name"""
for file1 in os.listdir(path):
    file_name, ext = os.path.splitext(file1)
    print(path + file1)
    print(file_name)
    print(path + '\\' + file1)
    if 'tmp' in str(file1):
        os.rename(path + '\\' + file1, path + ' \\' + file_name)
        print('TMP found, renaming...')
    else:
        pass

