# 筛选出小于 3M 的 epub 文件
# 然后根据元数据重命名
import os
import re
from ebooklib import epub

filepath = 'D:\\Document\\Books\\temp\\'
limit = 3 * 1024 * 1000

for filename in os.listdir(filepath):
    file = filepath + filename
    print(filename, os.path.getsize(file))
    if (file.endswith(".epub") and os.path.getsize(file) < limit):
        book = epub.read_epub(file)
        title = book.get_metadata('DC', 'title')
        creator = book.get_metadata('DC', 'creator')
        if len(title) == 0:
            title = "未知"
        else:
            title = title[0][0]
        if len(creator) == 0:
            creator = "未知"
        else:
            creator = creator[0][0]
        raw_name = title.strip() + '-' + creator.strip()
        new_name = re.sub("\s|:|》|《|，|。|！|、|：|、|”|“", "", raw_name) + '.epub'
        if (not os.path.exists(filepath + new_name)):
            os.rename(file, filepath + new_name)
