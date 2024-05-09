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


def generate_page(from_path, template_path, dest_path):
    '''    Print a message to the console that says something like "Generating page from from_path to dest_path using template_path".
    -- Read the markdown file at from_path and store the contents in a variable.
    -- Read the template file at template_path and store the contents in a variable.
    -- Use your markdown_to_html_node function and .to_html() method to convert the markdown file to HTML.
    -- Use the extract_title function to grab the title of the page.
    -- Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated.
    -- Write the new HTML to a file at dest_path. Be sure to create any necessary directories if they don't exist.'''

    print(f'Generating page from {from_path} to {dest_path} using {template_path}')

    md_file = open(template_path)
    md_text = md_file.read()
    extract_title(md_text)


    
def main():
    copy_dir_rec('./static', './public')
    generate_page('../content/index.md', '../template.html', '../public/index.md')
    
main()
