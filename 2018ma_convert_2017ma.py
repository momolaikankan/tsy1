# coding:utf-8
from __future__ import print_function
import os

def convert():
    origin_path = raw_input(u'please input 2018ma folder path:')
    target_path = raw_input(u'please input 2017ma folder path:')
    for root, dirs, files in os.walk(origin_path):
        for file in files:
            if file.endswith('.ma'):
                try:
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as f:
                            ma_file_content = f.readlines()
                    for index, line in enumerate(ma_file_content):
                            if line.find('requires maya "2018ff09"') != -1:
                                    ma_file_content[index] = line.replace('requires maya "2018ff09"', 'requires maya "2017ff05"')
                                    break
                    if os.path.dirname(file_path) == origin_path:
                        target_file_path = os.path.join(target_path, file)
                    else:
                        target_file_path =os.path.join(target_path, file_path.split(origin_path)[1].lstrip('\\'))
                        if not os.path.exists(os.path.dirname(target_file_path)):
                            os.makedirs(os.path.dirname(target_file_path))
                    with open(target_file_path, 'w') as f1:
                            f1.writelines(ma_file_content)
                    print(u'{}文件转换完成'.format(file))
                except Exception as e:
                    print(u'{}文件转换失败,错误原因{}'.format(file, e))


if __name__ == '__main__':
    if not os.path.exists(r'W:\xmov\bin\Python27'):
        raise(u'请挂在W盘，双击"S:/acg-xmov/Xuhui_Public/tools/mount/mount_W.bat"脚本')
    convert()
