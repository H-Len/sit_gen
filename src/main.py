import os, shutil
from textnode import TextNode



def copy_dir_rec(source_dir, target_dir):
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    os.mkdir(target_dir)
    
    list = os.listdir(source_dir)
    for item in list:
        cur_path = f'{source_dir}/{item}'
        next_path = f'{target_dir}/{item}'
        if os.path.isdir(cur_path):
            copy_dir_rec(cur_path, next_path)
        else:
            shutil.copy(cur_path, next_path)
    




    
    

def main():
    copy_dir_rec('./static', './public')
main()