import scrapy


class DrugsInfoSpider(scrapy.Spider):
    name = 'drugs_info'
    start_urls = [
        'https://irc.fda.gov.ir/NFI/Search?Term=%20&PageNumber=1&PageSize=9000',
    ]

    def parse(self, response, **kwargs):
        page_num = 1
        for drug in response.css('div.col-lg-12.col-md-12.col-sm-12.col-xs-12.padding0.RowSearchSty'):
            try:
                yield {
                    # 'drug_name': drug.css(
                    #     'span.col-lg-12.col-md-12.col-sm-12.col-xs-12.titleSearch-Link-RtlAlter a::text').get(),
                    # 'brand_owner': drug.css(
                    #     'div.col-lg-4.col-md-4.col-sm-6.col-xs-12 span.txtSearch1::text').get().strip(),
                    # 'license_owner': drug.css(
                    #     "div.col-lg-4.col-md-4.col-sm-6.col-xs-12 span.txtSearch1::text").get().strip(),
                    # 'price': drug.css(
                    #     "div.col-lg-4.col-md-4.col-sm-6.col-xs-12 span.txtAlignLTRFa.priceTxt::text").get().strip(),
                    # 'generic_code': drug.css("div.row div.col-lg-4.col-md-4.col-sm-6.col-xs-12 span.txtSearch1::text")[
                    #     3].get().strip(),
                    'drug_link':
                        f"https://irc.fda.gov.ir/{drug.css('span.col-lg-12.col-md-12.col-sm-12.col-xs-12.titleSearch-Link-RtlAlter a').attrib['href']}",
                }
            except:
                {}
        # page_num += 1
        # next_page = response.css('ul.pagination li')[page_num]
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)
