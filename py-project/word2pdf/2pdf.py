#coding:utf8

'''
    python将word doc、docx格式转换成pdf
'''

from win32com.client import gencache
from win32com.client import constants, gencache

input = 'E:/python-codes/word2pdf/tmp/02.docx'
output = 'E:/python-codes/word2pdf/tmp/02.pdf'


def createPdf(wordPath, pdfPath):
    """
    word转pdf
    :param wordPath: word文件路径
    :param pdfPath:  生成pdf文件路径
    """
    word = gencache.EnsureDispatch('Word.Application')
    doc = word.Documents.Open(wordPath, ReadOnly=1)
    doc.ExportAsFixedFormat(pdfPath,
                            constants.wdExportFormatPDF,
                            Item=constants.wdExportDocumentWithMarkup,
                            CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
    word.Quit(constants.wdDoNotSaveChanges)

createPdf(input, output)