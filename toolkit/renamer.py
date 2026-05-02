from pathlib import Path

def bulk_rename(folder_path,prefix):

    folder = Path(folder_path)

    if not folder.exists():
        print('Folder does not exists.')
        return
    
    files = [file for file in folder.iterdir() if file.is_file()]

    if not files:
        print('No files found.')
        return
    
    for index,file in enumerate(files,start=1):

        new_name = f'{prefix}_{index}{file.suffix}'

        new_path = folder/new_name

        file.rename(new_path)

        print(f"{file.name} → {new_name}")
    
    print("Bulk rename completed!")

