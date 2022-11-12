'''
Author: CalmCapK
Date: 2022-09-20 00:25:06
LastEditors: Please set LastEditors
LastEditTime: 2022-11-09 08:33:08
'''
import os
import shutil

################################# 介绍1：file #####################################
def file_ext(filename, level=1):
    return filename.split('.')[-level]

def get_files(path, is_recursive=False):
    files = []
    # get files in current path
    if not is_recursive:
        for name in os.listdir(path):
            fullname = os.path.join(path, name)
            if os.path.isfile(fullname):
                files.append(fullname)
        return files
    # get files recursively
    for main_dir, _, sub_file_list in os.walk(path):
        for filename in sub_file_list:
            fullname = os.path.join(main_dir, filename)
            files.append(fullname)
    return files
    
def get_folders(path, is_recursive=False):
    folders = []
    # get folders in current path
    if not is_recursive:
        for name in os.listdir(path):
            fullname = os.path.join(path, name)
            if os.path.isdir(fullname):
                folders.append(fullname)
        return folders
    # get folders recursively
    for main_dir, _, _ in os.walk(path):
        folders.append(main_dir)
    return folders

def change_file_name(folder_path):
    '''
    功能：修改目录下所有文件的名字
    '''
    files = os.listdir(folder_path)
    cnt = 0
    #wenti= [str(i)+'.jpg' for i in range(70, 99)]
    files = sorted(files)
    for file in files:
        #if file in wenti:
        print(file) 
        os.rename(os.path.join(folder_path, file), os.path.join(folder_path, str(cnt)+'.jpg'))
        cnt += 1

def move_dir(path, new_path):
    shutil.move(path, new_path)

def copy_dir(path, new_path):
    shutil.copytree(path, new_path)

def remove_dir(path):
    os.remove(path)

def create_dir(path):
    os.makedirs(path)

################################# 介绍2：xml #####################################
from xml.etree.ElementTree import ElementTree

def read_xml(in_path):
    tree = ElementTree()
    tree.parse(in_path)
    return tree

def write_xml(tree, out_path):
    tree.write(out_path, encoding="utf-8", xml_declaration=False)

def find_nodes(tree, path):
    '''
    查找某个路径匹配的所有节点
    tree: xml树
    path: 节点路径
    '''
    return tree.findall(path)
    
def change_node_text(nodelist, text, is_add=False, is_delete=False):
    '''
       改变/增加/删除一个节点的文本
       nodelist:节点列表
       text : 更新后的文本
    '''
    for node in nodelist:
        if is_add:
            node.text += text
        elif is_delete:
            node.text = ""
        else:
            node.text = text

################################# 介绍3：txt #####################################
def read_file(filename):
    datas = []
    file = open(filename,'r+')
    for line in file: # 遍历file文件
        #data = line.split(',')
        datas.append(line)
    file.close()# 关闭文件
    return datas

def write_file(filename, data):
    with open(filename,'w+') as fw: # 打开文件  #write和writelines都不会自动换行
        for d in data:
            fw.writelines(d)

################################# 介绍4：csv #####################################
import csv

def write_csv(path, data):
    with open(path, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        for d in data:
            spamwriter.writerow(d)
    
################################# 介绍5：xlsx #####################################
# import pandas as pd

def read_xlsx_row_by_index(path, index):
    hdr = pd.read_excel(path, index_col=0) #index_col=0 不读首列序号
    r = hdr.iloc[index].tolist() #行 首行/第0行 不含序号
    return r

def read_xlsx_col_by_index(path, index):
    hdr = pd.read_excel(path, index_col=0) #index_col=0 不读首列序号
    l = hdr.iloc[:,index].tolist() #列 首列/第0列 不含序号
    return l

def write_xlsx(path, data):
    df = pd.DataFrame(data)
    df.to_excel(path)

# from openpyxl import load_workbook

def read_xlsx_by_sheetindex(path, sheet_index):
    wb = load_workbook(path)
    sheet_names = wb.sheetnames
    sheet = wb.get_sheet_by_name(sheet_names[sheet_index])
    rows = sheet.rows
    data = []
    for row in rows:
        col_value = [col.value for col in row]
        data.append(col_value)
    return data

################################# 介绍6：yml #####################################
# import yaml

def read_yml(path):
    with open(path, "r", encoding='utf-8') as cd:
        _cf = yaml.load(cd, Loader=yaml.FullLoader)
    return _cf

################################# 介绍7：py #####################################
import json

def read_json(path):
    with open(path,'r', encoding='utf8')as fp:
        json_data = json.load(fp)
    return json_data

def write_json(data, path):
    json_str = json.dumps(data)
    with open(path, 'w') as json_file:
        json_file.write(json_str)

################################# 介绍8：py #####################################
import importlib

def read_py(path):
    cfg = importlib.import_module(path.replace('.py', '').replace('/','.'))
    return cfg

################################# test #####################################
def test_fun(op):
    if op == 1: #file op
        path = '/d/myfile/code/toolkit/test.py'
        print(file_ext(path))
    if op == 2: #file op
        path = 'D:\\myfile\\code\\toolkit\\test_directory_structure'
        f = get_files(path, is_recursive=True)
        print(f)
    if op == 3: #file op
        path = 'D:\\myfile\\code\\toolkit\\test_directory_structure'
        f = get_folders(path, is_recursive=True)
        print(f)
    if op == 4: #xml
        path = 'D:\\myfile\\code\\toolkit\\test_file_op\\a.xml'
        out_path = 'D:\\myfile\\code\\toolkit\\test_file_op\\b.xml'
        tree = read_xml(path)
        nodelist= find_nodes(tree, 'b')
        change_node_text(nodelist, '5', is_add=False, is_delete=False)
        write_xml(tree, out_path)
    if op == 5: #txt
        in_path = 'D:\\myfile\\code\\toolkit\\test_file_op\\a.txt'
        out_path = 'D:\\myfile\\code\\toolkit\\test_file_op\\b.txt'
        data = read_file(in_path)
        write_file(out_path, data)
    if op == 6: #csv
        in_path = 'D:\\myfile\\code\\toolkit\\test_file_op\\a.csv'
        out_path = 'D:\\myfile\\code\\toolkit\\test_file_op\\b.csv'
        data = [[1,2,"4"],[5,8,9]]
        write_csv(out_path, data)
    if op == 7: #xlsx
        in_path = 'D:\\myfile\\code\\toolkit\\test_file_op\\a.xlsx'
        out_path = 'D:\\myfile\\code\\toolkit\\test_file_op\\pb.xlsx'
        # data = [[1,2,"4"],[5,8,9]]
        # write_xlsx(out_path, data)
        d = read_xlsx_row_by_index(out_path, 0)
        print(d)
        d = read_xlsx_col_by_index(out_path, 0)
        print(d)
        win_path = 'D:\\myfile\\code\\toolkit\\test_file_op\\win.xlsx'
        wind = read_xlsx_by_sheetindex(win_path, 1)
        print(wind)
    if op == 8: #yml
        in_path = 'D:\\myfile\\code\\toolkit\\test_file_op\\a.yml'
        out_path = 'D:\\myfile\\code\\toolkit\\test_file_op\\b.yml'
        cfg = read_yml(in_path)
        print(cfg)
    if op == 9: #py
        in_path = 'test_file_op/a.py'
        out_path = 'D:\\myfile\\code\\toolkit\\test_file_op\\b.py'
        cfg = read_py(in_path)
        print(cfg.a)
    if op == 10: #json
        data = {'a':{1:"23", "12":34},'b':{3:4}}
        path = 'D:\\myfile\\code\\toolkit\\test_file_op\\a.json'
        write_json(data, path)
        data = read_json(path)
        print(data)
    if op == 11: #厨房笔记
        #folder_path = 'D:\\myfile\\code\\toolkit\\test_file_op\\change_name'
        #folder_path = 'D:\myfile\code\\blog\source\\assets\img\cook\process\w13'
        folder_path = 'D:\myfile\code\\blog\source\\assets\img\cook\process\w14_'
        change_file_name(folder_path)
    if op == 12:
        old_dir = 'D:\\myfile\\code\\toolkit\\test_file_op'
        new_dir = 'D:\\myfile\\code\\toolkit\\test_file_op2'
        #move_dir(old_dir, new_dir) 
        #copy_dir(old_dir, new_dir)
        path = './1/2/3'
        create_dir(path)
        remove_dir(path)
        

if __name__=="__main__":    
    op = 11
    test_fun(op)