import os

path = '/mnt/c/My Drive/Obsidian/SCRIPTURES/'
book_to_process = 'DOCTRINE_AND_COVENANTS'

def file_path_list(book_name)-> str:
    file_list = []
    for dir_, _, files in os.walk(path):
        for file_name in files:
            if '.md' in file_name and 'README.md' not in file_name and '_index.md' not in file_name:
                rel_dir = os.path.relpath(dir_, path)
                rel_file = os.path.join(rel_dir, file_name)
                if f'{book_name}' in rel_file:
                    file_list.append(rel_file)
    
    return file_list


def create_header(chapter_path, prev_chapter_path, next_chapter_path):
    # Current Chapter
    items = chapter_path.split('/')
    book_name = items[0]
    chapter = items[-1].replace('.md', '').replace('_', ' ') # Used to be 2
    
    # Previous Chapter
    prev_items = prev_chapter_path.split('/')
    prev_chapter = prev_items[-1].replace('.md', '').replace('_', ' ') # used to be 2
    
    # Next Chapter
    next_items = next_chapter_path.split('/')
    next_chapter = next_items[-1].replace('.md', '').replace('_', ' ') # Used to be 2
    
    header = f'''---
Tags: SCRIPTURE, {book_name}
---

[<< {prev_chapter}]({prev_chapter_path}) | [{next_chapter} >>]({next_chapter_path})

# {chapter}

'''
    
    return header
    

def edit_file(file_path, header):
    with open(file_path, 'r') as file:
        first_line = file.readline()
        all_lines = file.readlines()
    if 'Chapter' in first_line:
        with open(file_path, 'w') as file:
            file.write(header)
            for line in all_lines:
                verse_split = line.split('.', maxsplit=1)
                verse_num = verse_split[0]
                # print(repr(verse_num)=='\n')
                if verse_num != '\n':
                    verse_header = f'##### {verse_num}\n'
                    line_sin_verse = verse_split[1]
                    file.write(verse_header)
                # linked_line = line.replace('\n', f' ^{verse}\n')
                # if linked_line != '^\n':
                    file.write(line_sin_verse)
                # print(line)


def process_book_list(book_name):
    chapter_list = file_path_list(book_name)
    chapter_list_length = len(chapter_list)
    
    for chapter in chapter_list:
        position = chapter_list.index(chapter)
        current_chapter_index = position
        previous_chapter_index = position - 1
        next_chapter_index = position + 1 if position < chapter_list_length - 2 else chapter_list_length - 1

        current_chapter = chapter_list[current_chapter_index]
        previous_chapter = chapter_list[previous_chapter_index] 
        next_chapter = chapter_list[next_chapter_index]

        new_header = create_header(current_chapter, previous_chapter, next_chapter)
        edit_file(chapter, new_header)
    


print(process_book_list(book_to_process))


# TODO: Create a function that opens the files that have the word chapter on the first line.


    
def edit_file2(file_path, header):
    with open(file_path, 'r') as file:
        first_line = file.readline()
        all_lines = file.readlines()
    if 'Chapter' in first_line:
        with open(file_path, 'w') as file:
            file.write(header)
            for line in all_lines:
                verse_split = line.split('.', maxsplit=1)
                verse_num = verse_split[0]
                # print(repr(verse_num)=='\n')
                if verse_num != '\n':
                    verse_header = f'##### {verse_num}\n'
                    line_sin_verse = verse_split[1]
                    file.write(verse_header)
                # linked_line = line.replace('\n', f' ^{verse}\n')
                # if linked_line != '^\n':
                    file.write(line_sin_verse)
                print(line)
        # return f'{}'

multi_line_text = '''---
NEW TEST HEADER
---

'''

    
# print(edit_file2('BOOK_OF_MORMON/15_Moroni/Moroni_08.md', multi_line_text))