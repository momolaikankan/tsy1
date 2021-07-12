import os
import shutil


path = r"C:\Users\admin\Desktop\ma_to_fbx"
to_path = r"C:\Users\admin\Desktop\fbx_file"
# maya = MayaHelp

for root, dirs, files in os.walk(path):
        for _file in files:
                if 'v1' in _file:
                    print(_file)
                    file = _file.split("___")
                    new_file = file[0].strip() + '.fbx'
                    # print(file[0]+'.fbx')
                    # new_file = _file.replace('.ma', '.ma.bk_2018')
                    print(new_file)
                    shutil.copyfile(os.path.join(root, _file), os.path.join(to_path, new_file))
                    # fp = os.path.join(root, _file).replace('\\', '/')
                    # print('save {} successfully'.format(fp))