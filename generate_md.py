import csv, os

with open('comics.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\\')
    for row in csv_reader:
        with open(os.path.join('_comics', f'{row[0]}.md'), 'wb') as md_file:
            md_file.write('---\nlayout: comic\ntitle: Random Tidbits | {1}\ncomic_id: {0}\ncomic_title: {1}\n---\n\n## {1}\n\n![](/assets/images/{0}.png)\n\n{2}\n'.format(row[0], row[1], row[2]).encode('utf-8'))
