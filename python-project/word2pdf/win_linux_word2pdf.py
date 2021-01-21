import subprocess
import os
import sys
'''
使用python将word文件转换成pdf
实际项目中通过预览PDF，达到预览word文件目的
项目中运用成功，环境为Win
安装的模块：
pip install pywin32
pip install comtypes
'''
try:
    from comtypes import client
except ImportError:
    client = None

try:
    from win32com.client import constants, gencache
except ImportError:
    constants = None
    gencache = None


def doc2pdf(docPath, pdfPath):
    """
        convert a doc/docx document to pdf format
        :param doc: path to document
        """
    docPathTrue = os.path.abspath(docPath)  # bugfix - searching files in windows/system32
    pdfPath = os.path.abspath(pdfPath)

    if client is None:  # 判断环境，linux环境这里肯定为None
        return doc2pdf_linux(docPathTrue, pdfPath)

    word = gencache.EnsureDispatch('kwps.Application')
    doc = word.Documents.Open(docPathTrue, ReadOnly=1)
    doc.ExportAsFixedFormat(pdfPath,
                            constants.wdExportFormatPDF,
                            Item=constants.wdExportDocumentWithMarkup,
                            CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
    word.Quit(constants.wdDoNotSaveChanges)


def doc2pdf_linux(docPath, pdfPath):
    """
    convert a doc/docx document to pdf format (linux only, requires libreoffice)
    :param doc: path to document
    """
    cmd = 'libreoffice6.2 --headless --convert-to pdf'.split() + [docPath] + ['--outdir'] + [pdfPath]
    p = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    p.wait(timeout=30)
    stdout, stderr = p.communicate()
    if stderr:
        raise subprocess.SubprocessError(stderr)


if __name__ == '__main__':
    doc2pdf(sys.argv[1], sys.argv[2])
    # print("运行执行");