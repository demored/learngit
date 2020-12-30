import os
import sys
import zipfile
def docx_replace(old_file,new_file,rep):
    zin = zipfile.ZipFile (old_file, 'r')
    zout = zipfile.ZipFile (new_file, 'w')
    for item in zin.infolist():
        buffer = zin.read(item.filename)
        if (item.filename == 'word/document.xml' or 'header' in item.filename):
            res = buffer.decode("utf-8")
            for r in rep:
                res = res.replace(r,rep[r])
            buffer = res.encode("utf-8")
        zout.writestr(item, buffer)
    zout.close()
    zin.close()


old_name = os.path.abspath('.') +"\\" + "[CM-IM-001-V1.0]信息安全管理手册.docx"
zip_list = os.path.splitext(old_name)
zip_name = zip_list[0]+".zip"
if os.path.exists(old_name):
    os.rename(old_name, zip_name)


new_name = os.path.abspath('.') +"\\" +"02.docx"
# print(zip_name)
# print(new_name)
# sys.exit()
dict = {
    "蝉鸣科技（西安）有限公司":"证优客"
}
docx_replace(zip_name , new_name , dict)
