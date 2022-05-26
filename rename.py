from __future__ import with_statement
import os

PATH = "."
original_phrase = 'friendlyreminder'
new_phrase = 'booklandingpage'

for path, dirs, files in os.walk(PATH):
    for filename in files:
        if filename != os.path.basename(__file__):
            fullpath = os.path.join(path, filename)
            with open(fullpath, 'r', encoding='iso-8859-15') as f:
                data = f.read()
                if original_phrase in data:
                    with open(fullpath, 'w') as f:
                        f.write(data.replace(original_phrase, new_phrase))
                        print('Ocurrence replaced on file: ', fullpath)

    for folder in dirs:
        if folder == original_phrase:
            current_fullpath = os.path.join(path, folder)
            new_fullpath = os.path.join(path, new_phrase)
            os.rename(current_fullpath, new_fullpath)
            print(f'Folder {os.path.basename(current_fullpath)} renamed to {new_fullpath}')
