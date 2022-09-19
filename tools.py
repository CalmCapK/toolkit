'''
Author: CalmCapK
Date: 2022-09-11 17:49:49
LastEditors: CalmCapK
LastEditTime: 2022-09-18 21:32:25
'''

#文件操作
def change_file_name(folder_path):
    '''
    功能：修改目录下所有文件的名字
    '''
    import os
    files = os.listdir(folder_path)
    cnt = 0
    for file in files:
        print(file)
        os.rename(os.path.join(folder_path, file), os.path.join(folder_path, str(cnt)+'.jpg'))
        cnt += 1


#读写
#csv方式
def write_csv(path, data):
    '''
    输入：
        data是list格式
    '''
    import csv
    with open(path, 'a+', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(data)
        

if __name__=="__main__":    
    path = 'D:\myfile\code\\blog\source\\assets\img\cook\process\w9'
    change_file_name(path)