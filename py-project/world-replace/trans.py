# coding=utf-8

import os
from docx import Document

old_file_path = "F:\\replace\\docx\\"
new_file_path = "F:\\replace\\new_docx\\"

replace_dict = {
    "你妈的": "我草",
}

def check_and_change(document, replace_dict):
    """
    遍历word中的所有 paragraphs，在每一段中发现含有key 的内容，就替换为 value 。
    （key 和 value 都是replace_dict中的键值对。）
    """
    for para in document.paragraphs:
        for i in range(len(para.runs)):
            for key, value in replace_dict.items():
                if key in para.runs[i].text:
                    print(key+"-->"+value)
                    para.runs[i].text = para.runs[i].text.replace(key, value)
    return document


def main():
    for name in os.listdir(old_file_path):
        print(name)
        old_file = old_file_path + name

        new_file = new_file_path + name
        # print(new_file)
        if old_file.split(".")[1] == 'docx':
            document = Document(old_file)
            document = check_and_change(document, replace_dict)
            document.save(new_file)
        print("^"*30)


if __name__ == '__main__':
    main()