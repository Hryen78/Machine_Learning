from icrawler.builtin import BingImageCrawler

classess=['water bottle images']
number = 10

for i in classess:
    bing_crawler=BingImageCrawler(storage={'root_dir':f'C:/SGU/Python/Trash_detection_AI/Img/water_bottle'})
    bing_crawler.crawl(keyword=i, filters=None, max_num=number, offset=0)