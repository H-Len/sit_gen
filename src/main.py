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
    # possible_title = markdown[0: 3]
    # if possible_title == '<h1>':
    # print(f'markdown: {markdown}')
    title = ''
    split_md = markdown.split('\n')
    if block_to_block_type(markdown) == 'heading':
        for line in split_md:
            if line[0:2] == '# ':
                print(title = line[3:])
    return title




    
    

def main():
    copy_dir_rec('./static', './public')
    print(extract_title('content/index.md'))
main()
