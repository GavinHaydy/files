import os,multiprocessing

file_dir = r'E:\untitled\test\新建文件夹'
url =''
def files():
    for root,dirs,files in os.walk(file_dir):
        pass
    print(files)
    exec('E:\untitled\test\新建文件夹\66.py')

if __name__ == '__main__':
    files()