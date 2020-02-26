import requests
import os
from PIL import Image
from io import BytesIO


def one_chapter(url, number):   # 地址,章节数
    for i in range(1, 60):         # 单张图片下载
        url1 = url+str(i)+'.jpg-mht.middle.webp'    # 单张图片地址
        try:                   # 下载过程
            img = requests.get(url1, timeout=30)
            img.raise_for_status()
        except requests.exceptions.ConnectTimeout:  # 自身网络问题
            print(url1+'网络连接失败')
            continue
        except requests.exceptions.HTTPError:       # 检测章节下载是否正常结束
            if i == 1:
                return 0
            else:
                return 1
        # 保存图片
        root = 'D:/entertainment/comics/斗破苍穹/'+str(number)+'话/'
        img_name = root+str(i)+'页.png'
        img = Image.open(BytesIO(img.content))
        try:
            if not os.path.exists(root):    #检测路径是否存在
                os.mkdir(root)
            img.save(img_name)
        except Exception as e:
            print(e)


def main():
    url_head = 'https://mhpic.manhualang.com/comic/D/%E6%96%97%E7%A0%B4%E8%8B%8D%E7%A9%B9%E6%8B%86%E5%88%86%E7%89%88/'
    url_tail = '%E8%AF%9DGQV/'
    tag1 = 1
    tag2 = 1
    i = 820
    while tag1:
        url = url_head + str(i) + url_tail
        tag1 = one_chapter(url, i)
        i += 1
    i -= 1
    url_tail = url_tail.replace('V/', '/')         # 根据实际变动替换
    while tag2:
        url = url_head + str(i) + url_tail
        tag2 = one_chapter(url, i)
        i += 1
    print('终止章节数'+str(i))


if __name__ == '__main__':
    main()
