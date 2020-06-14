from docx import Document
import os,urllib,httplib2,requests,json,pyclbr



def makefile():
    for i in range(6):
        tex = '测试数据' + str(i)
        document = Document()
        document.add_paragraph(tex+'.docx')
        document.save(tex+'.docx')

if __name__ == '__main__':
    makefile()