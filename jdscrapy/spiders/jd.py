import scrapy
from scrapy import Selector

from jdscrapy.items import JdscrapyItem


class JdSpider(scrapy.Spider):
    name = "jd"
    allowed_domains = ["jd.com"]
    start_urls = ["https://jd.com"]

    def parse(self, response, **kwargs):
        sel = Selector(response)
        goods_list = sel.css("ul#feedContent0 > li.more2_item.more2_item_good.hover-on")
        for item in goods_list:
            jd_item = JdscrapyItem()
            jd_item["src"] = item.css("a > div.lazyimg > img::attr(src)").extract_first() or ""
            jd_item["title"] = item.css("a::attr(title)").extract_first() or ''
            jd_item["price"] = item.css("a > div.more2_info > div > div > span::text").extract_first() + item.css(
                "a > div.more2_info > div > div > span > span::text").extract_first() or ''
            print(jd_item)
            yield jd_item
