import os
from urllib.parse import quote

template_head = '''# LightNovels 轻小说

> **建议使用<kbd>Ctrl</kbd> + <kbd>F</kbd>来搜索你想看的小说**

<!-- Authors tables -->
## 作者列表
'''

template_tail = '''
'''

rendered = ''''''

if __name__ == '__main__':
    origin_dirs = os.listdir('./temp')
    dirs = os.listdir('./temp')
    dirs.remove('.git')
    origin_dirs.remove('.git')
    for i in range(len(dirs)):
        dirs[i] = f'[{dirs[i]}](#user-content-{dirs[i]})'
    if len(dirs) > 5:
        rendered += f'| {dirs[0]} | {dirs[1]} | {dirs[2]} | {dirs[3]} | {dirs[4]} |\n| :--: | :--: | :--: | :--: | :--: |\n'
        for num in len(5, len(dirs), 5):
            try:
                tmp = str(dirs[num:num+5]).replace('[', '| ').replace(']',
                                                                      ' |\n').replace("'", '').replace(', ', ' | ')
                rendered += tmp
            except IndexError:
                tmp = str(dirs[num]).replace('[', '| ').replace(
                    ']', ' |\n\n').replace("'", '').replace(', ', ' | ')
                rendered += tmp
    else:
        authors = {}
        tmp= str(dirs).replace('\'','')
        tmp = str(dirs).replace('[\'', '| ').replace(
            '\']', ' |').replace("'", '').replace(', ', ' | ')
        tmp += ' |' * (5 - tmp.count(' |')) + '\n'
        rendered += tmp
        rendered += '| :--: | :--: | :--: | :--: | :--: |\n| | | | | |\n\n'
    novels = {} 
    for dir in origin_dirs:
        rendered += f'\n## {dir}\n\n| 序号 | 书名 |\n| ---- | ---- |\n'
        # rendered.replace(dir, f'[{dir}](#{dir})')
        for root, _, fs in os.walk(f'./temp/{dir}'):
            count = 1
            for book in fs:
                if book.endswith('.pdf'):
                    booklink = f'https://lightnovels.github.io/?file=https://cdn.bilicdn.tk/gh/LightNovels/Home@novels/{quote(dir)}/{quote(book)}'
                    bookname = book.replace(f'{dir} - ', '')
                    rendered += f'| {count} | [{bookname}]({booklink}) |\n'
                    count += 1

    with open('README.md', 'wt', encoding='utf8') as f:
        f.write(template_head + rendered + template_tail)
