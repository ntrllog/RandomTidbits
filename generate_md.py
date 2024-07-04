import csv, os

gifs = [56]

i = 0
with open('comics.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='|')
    for row in csv_reader:
        i += 1
        with open(os.path.join('_comics', f'{row[0]}.md'), 'wb') as md_file:
            if i in gifs:
                extension = "gif"
            else:
                extension = "png"
            md_file.write('---\nlayout: comic\ntitle: Random Tidbits | {1}\ncomic_id: {0}\ncomic_title: {1}\n---\n\n## {1}\n\n<img id="img{0}" class="img-fluid" src="/assets/images/{0}.{3}">\n\n{2}\n'.format(row[0], row[1], row[2], extension).encode('utf-8'))
