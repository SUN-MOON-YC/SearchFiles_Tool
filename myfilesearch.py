#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：yangchao  albert time:2020/9/5
"""
   说明：按指定路径，关键字，后缀进行需求文件查找，结果写入文件并 复制1份文件到指定路径
   source_dir 为指定查找的路径，
   file_types 为后缀组成的list
   key_strs 为设定查找包含的关键字list
"""
import os
import subprocess
import shutil


# 递归查询指定后缀文件的方法
def new_search_file_by_file_type(source_dir, file_types, tar_list):
    if os.path.exists (source_dir):
        result = os.walk (source_dir)
        for pardir, childdir, filenames in result:
            for n in filenames:
                name, type = os.path.splitext (n)
                if type in file_types:
                    tar_list.append (os.path.join (pardir, n))
    else:
        print('查找的目录错误或不存在！')
    tar_list = list (set (tar_list))
    return tar_list

def new_search_file_by_key_str(source_dir, key_strs, tar_list):
    if os.path.exists (source_dir):
        result = os.walk (source_dir)
        for pardir, childdir, filenames in result:
            for n in filenames:
                name, type = os.path.splitext (n)
                for key in key_strs:
                    if key in name:
                        tar_list.append (os.path.join (pardir, n))
    else:
        print('查找的目录错误或不存在！')
    tar_list = list (set (tar_list))
    return tar_list

def new_search_file_by_all(source_dir, key_strs, file_types, tar_list):
    if os.path.exists (source_dir):
        result = os.walk (source_dir)
        for pardir, childdir, filenames in result:
            for n in filenames:
                name, type = os.path.splitext (n)
                for key in key_strs:
                    if (key in name) and (type in file_types):
                        tar_list.append (os.path.join (pardir, n))
    else:
        print('查找的目录错误或不存在！')
    tar_list = list (set (tar_list))
    return tar_list

# 递归查询指定后缀文件的方法
def search_file_by_file_type(source_dir, file_type, tar_list):
    names = []
    if os.path.exists (source_dir):
        os.chdir (source_dir)
        filenames = os.listdir (os.curdir)
        for f in filenames:
            if os.path.isfile (f):
                ext = os.path.splitext (f)[1]
                if ext in file_type:
                    tar_list.append (os.path.join (os.getcwd (), f))
                    names.append (f)
            else:
                search_file_by_file_type (f, file_type, tar_list)
                os.chdir (os.pardir)
    else:
        print ('查找的目录错误或不存在！')
    return tar_list, names


# 查询包含关键字的文件 key_strs
def search_file_by_key_str(source_dir, key_strs, tar_list):
    names = []
    if os.path.exists (source_dir):
        os.chdir (source_dir)
        filenames = os.listdir (os.curdir)
        for f in filenames:
            if os.path.isfile (f):
                n = os.path.splitext (f)[0]
                for key_str in key_strs:
                    if key_str in n:
                        tar_list.append (os.path.join (os.getcwd (), f))
            else:
                search_file_by_key_str (f, key_strs, tar_list)
                os.chdir (os.pardir)
    else:
        print ('查找的目录错误或不存在！')
        tar_list = list (set (tar_list))
    return tar_list, names


# 综合查询
def search_file_by_all(source_dirs, key_strs, file_type, tar_list):
    all_names = []
    for p in source_dirs:
        if os.path.exists (p):
            tar_list_by_keystr, names = search_file_by_key_str (p, key_strs, tar_list)
            tar_list.extend (tar_list_by_keystr)
            all_names.extend (names)
    for n in all_names:
        hz = os.path.splitext (n)[1]
        if hz not in file_type:
            all_names.remove (n)
    for li in tar_list:
        val = os.path.split (li)[1]
        if val not in all_names:
            tar_list.remove (val)
    return tar_list, all_names


# 判定目录存在的方法
def is_dir_exists(dir):
    if os.path.exists (dir):
        pass
    else:
        os.makedirs (dir)


# 写文件路径信息到txt文件的方法
def write_info_txt(tar_list, data_dir, name):
    is_dir_exists (data_dir)
    file = open (os.path.join (data_dir, name), 'a')
    for p in tar_list:
        file.writelines (p + '\n')
    file.flush ()
    file.close ()
    msg = 'find {} files，dir path for save file is: {}'.format (len (tar_list), data_dir)
    return msg


# 复制文件方法1- subprocess.call(cmd,shell=True)
def subprocess_copy_files(tar_list, dst):
    is_dir_exists (dst)
    for file in tar_list:
        src = file
        cmd = 'copy "%s" "%s"' % (src, dst)
        subprocess.call (cmd, shell=True)
    status = 'OK,total copy {} files'.format (len (tar_list))
    return status


# 复制文件方法2-  shutil.copy(src,dst)
def shutil_copy_files(tar_list, dst):
    is_dir_exists (dst)
    for file in tar_list:
        src = file
        shutil.copy (src, dst)
    status = 'OK, copied {} files'.format (len (tar_list))
    return status


if __name__ == '__main__':
    # dir=r'C:\Users'
    # p1=r'C:\Users\Administrator\Desktop\MyPic'
    # dir=os.path.normpath(dir)
    # p1 = os.path.normpath (p1)
    # data=os.walk(dir)
    # flag=''
    # for dirs,childdirs,childfiles in data:
    #     for d in childdirs:
    #         if p1 in d:
    #             flag='OK'
    #         else:
    #             flag='NG'
    # print('flag:',flag)
    # if os.path.exists(dir):
    #     os.chdir(dir)
    #     files=os.listdir(os.curdir)
    #     print(files)
    # flag='C:\\'
    # os.path.exists(flag)
    # example_source_dir = 'D:/python/mydata'
    #
    # # print ('待查找的目录--示例：{}'.format (example_source_dir))
    # # source_dir = input ('请输入待查找的目录：')
    p1=r'C:\Users\Administrator\Desktop\MyPic'

    p2='E:/'
    source_dirs=[p1]
    file_types = ['.png', '.jpg']  # 根据需要可以更改或增加
    key_strs=['mango','mongo','yc']
    tar_list = []  # 存放查找到文件的绝对路径
    # # #
    # # for dir in source_dirs:
    # #      tar_list,names=search_file_by_file_type (dir, file_types, tar_list)
    # # # key_strs = ['第10章', '第16章', '第20章']
    for p in source_dirs:
        new_search_file_by_all (p, key_strs, file_types, tar_list)

    print (tar_list)
