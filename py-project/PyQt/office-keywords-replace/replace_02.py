import os
import shutil
# replace_dir = r"D:\python-codes\py-project\PyQt\office-keywords-replace\test\replace"
# def recurse_transfer_file(path):
#     lsdir = os.listdir(path)
#     dirs = [i for i in lsdir if os.path.isdir(os.path.join(path, i))]
#     if dirs:
#         for i in dirs:
#             recurse_transfer_file(os.path.join(path, i))
#
#     files = [i for i in lsdir if os.path.isfile(os.path.join(path, i))]
#     for f in files:
#         if f.endswith(".doc") and not f.startswith('~$'):
#             print(os.path.join(path, f))
#
#
# recurse_transfer_file(replace_dir)

def del_dir(del_path):
    del_list = os.listdir(del_path)
    for f in del_list:
        file_path = os.path.join(del_path, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

replace_dir = r"D:\python-codes\py-project\PyQt\office-keywords-replace\test\replace"
del_dir(replace_dir)