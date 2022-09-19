'''
Author: CalmCapK
Date: 2022-09-20 01:11:01
LastEditors: CalmCapK
LastEditTime: 2022-09-20 01:59:58
'''
import numpy as np
import shutil

from file_op import *

################################# 将图像文件夹写成list形式，再划分，再分别导出 #####################################
#把文件划分训练、验证、测试集
def split_dataset(files_list):
    ratio_train = 0.8 #训练集比例
    ratio_val = 0 #验证集比例
    ratio_test = 0.2 #测试集比例
    np.random.shuffle(files_list) ##打乱文件列表
    cnt_test = round(len(files_list) * ratio_test, 0)
    cnt_val = round(len(files_list) * ratio_val, 0)
    cnt_train = len(files_list) - cnt_val - cnt_test
    
    train_list = []
    val_list = []
    test_list = []
    for i in range(int(cnt_train)):
        train_list.append(files_list[i])
    for i in range(int(cnt_train), int(cnt_train + cnt_val)):
        val_list.append(files_list[i])
    for i in range(int(cnt_train + cnt_val), int(cnt_train + cnt_val + cnt_test)):
        test_list.append(files_list[i])
    
    print("train Sample:", cnt_train, len(train_list))
    print("val Sample:", cnt_val, len(val_list))
    print("test Sample:", cnt_test, len(test_list))
    return train_list, val_list, test_list
    
#处理单一类别文件，得到标注文件
def process_single(path, label):
    '''
    path: xxx.jpg
    label: ,1,3
    '''
    files = get_files(path)
    print("files:", len(files))
    
    files_label = []
    for f in files:
        files_label.append(f+label)
    
    train_list, val_list, test_list = split_dataset(files_label)
    
    path = 'D:\\myfile\\code\\toolkit\\test_file_op'
    train_path = path+'\\train.list'
    write_file(train_path, train_list)
    test_path = path+'\\test.list'
    write_file(test_path, test_list)

################################# test #####################################
def test_fun(op):
    if op == 1:
        path = 'D:\\myfile\\code\\toolkit\\test_file_op\\change_name'
        process_single(path, ',3,4\n')

if __name__=="__main__":    
    op = 1
    test_fun(op)