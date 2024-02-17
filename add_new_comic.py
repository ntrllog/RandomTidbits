import os

comic_id = int(input('Comic number: '))

while os.path.exists(os.path.join('_comics', f'{comic_id}.md')):
    print('id already exists')
    comic_id = int(input('Comic number: '))

comic_title = input('Comic title: ')
title_text = input('Title text: ')

with open('_redirects', 'w') as redirects_file:
    redirects_file.write(f'/comics /comics/{comic_id}')

with open(os.path.join('_comics', f'{comic_id}.md'), 'wb') as md_file:
    md_file.write('---\nlayout: comic\ntitle: Random Tidbits | {1}\ncomic_id: {0}\ncomic_title: {1}\n---\n\n## {1}\n\n<img id="img{0}" src="/assets/images/{0}.png">\n\n{2}\n'.format(comic_id, comic_title, title_text).encode('utf-8'))

with open('comics.txt', 'a') as db:
    db.write(f'\n{comic_id}|{comic_title}|{title_text}')
