import re
import os

def Class():
    tijiao = []
    cl_name = []
    file = ("./test")
    try:
        for names in os.walk(file):
            tijiao.append(names)
    except Exception as ret:
        print("出现%s异常错误" % ret)
        return

    new_data = []
    p = re.compile(r'[\u4e00-\u9fa5]')
    for i in range(len(tijiao)):
        data = re.findall(p, str(tijiao[i]))
        result = ''.join(data)
        new_data.append(result)
    box = []
    for i in range(len(new_data)):
        if new_data[i] != '':
            box.append(new_data[i])


    f = open("./class_name.txt", 'r')
    class_name = f.read()
    f.close()
    j = ''
    for i in class_name:

        if i == '\n':
            cl_name.append(j)
            j = ''
        else:
            j = j + i

            # print(type(i))
    for x in cl_name:
        result = re.search(str(x),str(box))
        if result == None:
            print(x)

    while True:
        pass



if __name__ == '__main__':
    Class()




