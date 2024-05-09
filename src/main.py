import os, shutil
from block_markdown import block_to_block_type



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
    

def extract_title(markdown):
    title = ''
    split_md = markdown.split('\n')
    for line in split_md:
        if line[0:2] == '# ':
            title = line[2:]
            print(title)
            return title
    raise Exception('No H1 header')



    
    

def main():
    copy_dir_rec('./static', './public')

    md_file = open('../content/index.md')
    md_text = md_file.read()
    extract_title(md_text)
main()
