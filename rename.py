# (probably) only works when only 1 comic has been deleted at a time

import os

deleted = input('Have you deleted the comic and png yet? (y/n): ')

if deleted != 'y':
    print('What are you doing?! Go delete them!')
    exit()

missing_number = 0
for path in ['assets/images', 'Krita Comics']:
    image_files = os.listdir(path)
    existing_numbers = [int(file.split(".")[0]) for file in image_files if file.split(".")[0].isdigit()]
    existing_numbers.sort()

    confirmation = ''
    for i, num in enumerate(existing_numbers):
        if num != i + 1:
            confirmation = input(f"{i + 1} in {path} has been deleted. Is that correct? (y/n): ")
            if confirmation == 'y':
                missing_number = i + 1
                break
            else:
                print("Yeah, something's wrong. You should check it out.")
                exit()

    if not confirmation:
        print(f"No deleted file in {path} has been detected")
        exit()

    for file in image_files:
        parts = file.split('.')
        file_number = int(parts[0])
        extension = parts[1]
        if file_number >= missing_number:
            new_name = f"{file_number-1}.{extension}"
            os.rename(f"{path}/{file}", f"{path}/{new_name}")