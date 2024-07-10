from scrapy.crawler import CrawlerProcess
import scrapy


class NaverSpider(scrapy.Spider):
    name="Naver"

    # 처음 크롤링을 시작하는 함수
    def start_requests(self):
        # '포르투 여행 추천'으로 검색한 네이버 결과 링크
        url = "https://search.naver.com/search.naver?sm=tab_hty.top&ssc=tab.blog.all&query=%ED%8F%AC%EB%A5%B4%ED%88%AC+%EC%97%AC%ED%96%89+%EC%B6%94%EC%B2%9C&oquery=%ED%95%B4%EC%99%B8+%EC%97%AC%ED%96%89%EC%A7%80+%EC%B6%94%EC%B2%9C&tqi=ioJEnlqVOswssFVdANdssssssbl-070288"

        yield scrapy.Request(url=url, callback=self.parse)

    # 크롤링 결과를 받는 callback 함수
    def parse(self, response):
        result = response.css('.api_txt_lines').xpath('string(.)').get()
        print(result)

if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(NaverSpider)
    process.start()