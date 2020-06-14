from docx import Document
import os,urllib,httplib2,requests,json,pyclbr



def makefiles():
    for i in range(2001):
        tex = '测' + str(i)
        document = Document()
        document.add_paragraph(tex+'.docx')
        document.save(tex+'.docx')

if __name__ == '__main__':
    makefiles()