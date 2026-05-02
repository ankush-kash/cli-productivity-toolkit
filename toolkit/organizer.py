from pathlib import Path
import shutil

def organize_folder(folder_path):

    folder = Path(folder_path)

    if not folder.exists():
        print('Folder does not exist')
        return
    
    for item in folder.iterdir():

        if item.is_file():

            extension = item.suffix.lower()[1:]

            if extension == "":
                extension = 'No extension'

            target_folder = folder/extension

            target_folder.mkdir(exist_ok=True)

            destination = target_folder/item.name

            shutil.move(str(item),str(destination))
    
    print('Files organized successfully.')

