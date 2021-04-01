green = "\033[0;33m"
red = "\033[0;31m"
blue = "\033[0;34m"


maxLen = 99999
inputMaxlen = input("Info: 输入要下载的组数，默认为不限制: ")
if inputMaxlen != '':
    print('非空')
    maxLen = int(inputMaxlen)


print(green, "超过设定最大下载数 %d 进程结束" % int(maxLen))
