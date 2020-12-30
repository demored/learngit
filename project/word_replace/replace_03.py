from win32com.client import Dispatch
import time

# def tihuan(before,content):
#     word = Dispatch('Word.Application')
#     doc = word.Documents.Open(r"E:\sxx\test2.docx")
#     word.Selection.Find.Execute(before, False, False, False, False, False, True, 1, True, content, 2)

word = Dispatch('kwps.Application')
doc = word.Documents.Open(r"D:\python-codes\project\word_replace\替换结果\[CM-IM-001-V1.0]信息安全管理手册.docx")
word.Selection.Find.Execute("蝉鸣科技（西安）有限公司", False, False, False, False, False, True, 1, True, "证优客", 2)
doc.SaveAs(r"D:\python-codes\project\word_replace\替换结果\[CM-IM-001-V1.0]信息安全管理手册.docx")
doc.Close()
