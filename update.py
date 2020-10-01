import os

id = int(input('Comic number: '))

while os.path.exists(os.path.join('_comics', f'{id}.md')):
    print('id already exists')
    id = int(input('Comic number: '))

title = input('Comic title: ')
text = input('Title text: ')

with open('_redirects', 'w') as redirects_file:
    redirects_file.write(f'/comics /comics/{id}.html')

navigation_text = '{% include navigation.html comic_id=page.comic_id %}'
comic_title_text = '{{ page.comic_title }}'

with open(os.path.join('_comics', f'{id}.md'), 'wb') as md_file:
    md_file.write('---\nlayout: default\ntitle: Random Tidbits | {1}\ncomic_title: {1}\ncomic_id: {0}\n---\n\n## {4}\n\n{3}\n\n![](/assets/images/{0}.png)\n\n{2}\n'.format(id, title, text, navigation_text, comic_title_text).encode('utf-8'))

nav_content = ['{% assign first_comic = site.comics | where: "comic_id", 1 | first %}\n', '{% assign num_comics = ' + str(id) + ' %}\n\n', '<div style="display: flex; justify-content: space-evenly;">\n', '  <a href="{{ first_comic.url }}"><i class="fas fa-angle-double-left"></i></a>\n', '  {% if include.comic_id == 1 %}\n', '  <a href="#"><i class="fas fa-angle-left"></i></a>\n', '  {% else %}\n', '  {% assign prev_comic_id = include.comic_id | minus: 1 %}\n', '  {% assign prev_comic = site.comics | where: "comic_id", prev_comic_id | first %}\n', '  <a href="{{ prev_comic.url }}"><i class="fas fa-angle-left"></i></a>\n', '  {% endif %}\n', '  {% if include.comic_id == num_comics %}\n', '  <a href="#"><i class="fas fa-angle-right"></i></a>\n', '  {% else %}\n', '  {% assign next_comic_id = include.comic_id | plus: 1 %}\n', '  {% assign next_comic = site.comics | where: "comic_id", next_comic_id | first %}\n', '  <a href="{{ next_comic.url }}"><i class="fas fa-angle-right"></i></a>\n', '  {% endif %}\n', '  {% assign most_recent_comic = site.comics | where: "comic_id", num_comics | first %}\n', '  <a href="{{ most_recent_comic.url }}"><i class="fas fa-angle-double-right"></i></a>\n', '</div>\n']

with open(os.path.join('_includes', 'navigation.html'), 'w') as nav_file:
    for line in nav_content:
        nav_file.write(line)
