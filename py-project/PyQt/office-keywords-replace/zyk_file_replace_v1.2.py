from win32com.client import Dispatch
import time
import os
import shutil
import sys
# 定义文件目录为当前目录
work_dir = os.path.abspath('.')
replace_dir = work_dir+"\\test\\替换目录\\"
result_dir = work_dir+"\\替换结果\\"

word = Dispatch('kwps.Application')

#获取目录下所有doc文件
def get_dir_doc_files(filepath):
    # doc文件列表
    doc_files = []
    # #读取文件夹中文件列表
    for file in os.listdir(filepath):
        if file.endswith(".doc") and not file.startswith('~$'):
            doc_files.append(file)
    return doc_files

#获取目录中所有docx文件
def get_dir_docx_files(filepath):
    # 获取目录下所有doc文件
    # docx文件列表
    docx_files = []
    # #读取文件夹中文件列表
    for file in os.listdir(filepath):
        if file.endswith(".docx") and not file.startswith('~$'):
            docx_files.append(file)
    return docx_files


#将old_path中的docx，xls,xlsx文件复制到new_path中
def mv_file_result_dir(old_path, new_path):
    for file in os.listdir(old_path):
        # if file.endswith(".xls") and not file.startswith('~$'):
        #     shutil.copyfile(old_path+file, new_path+file)
        # elif file.endswith(".xlsx") and not file.startswith('~$'):
        #     shutil.copyfile(old_path + file, new_path + file)
        if file.endswith(".docx") and not file.startswith('~$'):
            shutil.copyfile(old_path + file, new_path + file)

# #将doc替换成docx
def doSaveAas(files_arr):
    for i in files_arr:
        temp = replace_dir+'{}'.format(i)
        doc = word.Documents.Open(temp)  #目标路径下的文件
        rename = os.path.splitext(i)
        print("转换【"+result_dir+i+"】")
        doc.SaveAs(result_dir + rename[0] + '.docx', 12)  # 12表示docx格式
        doc.Close()
    word.Quit()

if __name__ == '__main__':
    # print("证优客咨询师文件替换工具V1.2")
    print('''+----------------------------------------------------------------------
| 证优客咨询师文件替换工具V1.2
+----------------------------------------------------------------------
| Copyright (c) 2020 ZYK rights reserved.
+----------------------------------------------------------------------''')
    # 创建需要替换的目录
    if not os.path.exists(replace_dir):
        os.makedirs(replace_dir)

    # 创建替换后的目录
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)

    print(result_dir);
    # 如果存在doc文件则将doc转换成docx
    doc_files = get_dir_doc_files(replace_dir)
    if len(doc_files) > 0:
        print("##############开始文件格式转换##############")
        doSaveAas(doc_files)

    #将replace中的不需要转换的文件复制到result目录
    mv_file_result_dir(replace_dir, result_dir)

    # word = Dispatch('kwps.Application')
    # doc = word.Documents.Open(r"D:\python-codes\project\word_replace\替换结果\[CM-IM-001-V1.0]信息安全管理手册.docx")
    # word.Selection.Find.Execute("蝉鸣科技（西安）有限公司", False, False, False, False, False, True, 1, True, "证优客", 2)
    # doc.SaveAs(r"D:\python-codes\project\word_replace\替换结果\[CM-IM-001-V1.0]信息安全管理手册.docx")
    # doc.Close()
    #
    # sys.exit()

    print("##############开始关键词替换##############")
    #获取需要替换的文件
    replace_files = os.listdir(result_dir)
    ##读取配置文件
    config_text = work_dir +"\\" +"config.txt"

    if not os.path.exists(config_text):
        print("配置文件不存在")
        sys.exit()

    word = Dispatch('kwps.Application')
    for i in replace_files:
        #加上绝对路径
        file = result_dir + i
        print("进行【"+file+"】关键字替换")
        origin_file_name = file_name = os.path.splitext(i)[0]

        doc = word.Documents.Open(file)
        f = open(config_text, encoding='utf-8')
        while True:
            line = f.readline()
            if line:
                split_list = line.split('|')
                old_word = split_list[0].replace('\r','').replace('\n','').replace('\t','')
                new_word = split_list[1].replace('\r','').replace('\n','').replace('\t','')
                word.Selection.Find.Execute(old_word, False, False, False, False, False, True, 1, True, new_word, 2)
                file_name = file_name.replace(old_word, new_word)
            else:
                break
        f.close()
        # doc.SaveAs(file)
        # print("{0}{1}.docx".format(result_dir, file_name))

        doc.SaveAs(r"{0}{1}.docx".format(result_dir, file_name))
        if origin_file_name != file_name:
            os.remove(file)

        doc.Close()
    print("##############操作结束##############")
    os.system("pause")

