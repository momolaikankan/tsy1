import os


def get_ma_config_files(dir=os.getcwd()):
    file_lists = os.listdir(dir)
    files = [file for file in file_lists if file.endswith('.ma')]
    config_file = [file for file in file_lists if file.endswith('.txt')]
    return files, config_file


def write_to_new_file(files, config_file):
    if not os.path.exists('new'):
        os.makedirs('new')
    for file in files:
        with open(file, 'r') as old_flie, open('new\\' + file, 'w') as new_file, open(config_file, 'r') as config:
            for line in config:
                old, new = line.split()
                for file_line in old_flie:
                    new_file.write(file_line.replace(old, new))


def write_to_new_file1(files, config_file):
    if not os.path.exists('new'):
        os.makedirs('new')
    for file in files:
        with open(file, 'r') as old_flie, open('new\\' + file, 'w') as new_file, open(config_file, 'r') as config:
            for file_line in old_flie:
                for line in config:
                    old, new = line.split()
                    file_line.replace(old, new)
                new_file.write(file_line)


def convert(ma_files, config_file, out_dir):
    # read config <= config_file
    for ma_file in ma_files:
        new_ma_file = join out_dir, ma_file.filename
        convert_one(ma_file, config, new_ma_file)

def convert_one(ma_file, config, new_ma_file):
    read content from ma_file
    for every src,dst from config
        replace content src to dst
    write content to new_ma_file
def func():
    pass

def main():
    # get ma files <= ma/
    # get config file <= ./config.txt
    # get out_dir <= new/
    convert(ma_files, config_file)


if __name__ == '__main__':
    # files, config_file = get_ma_config_files()
    # write_to_new_file(files, config_file[0])
    main()
