import os,datetime
file_dir = r'E:\untitled\test\777'


def file():
    for root,dirs,filrs in os.walk(file_dir):
        pass
    print(filrs[1])

    print(datetime.datetime.now())
    os.system('python 66.py')
    print(datetime.datetime.now())
    # os.system('python 1托尔斯泰.py')


if __name__ == '__main__':
    file()
