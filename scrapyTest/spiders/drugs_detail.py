import scrapy
import json


class DrugsInfoSpider(scrapy.Spider):
    name = 'drugs_detail'
    start_urls = []
    # start_urls = ['https://irc.fda.gov.ir//NFI/Detail/12413']

    with open('scrapyTest/drugs_info.json', 'r', encoding='utf-8') as file:
        drugs_info = json.loads(file.read())

        # print(drugs_info)

        for drug in drugs_info:
            drug_url = drug['drug_link']
            start_urls.append(drug_url)

    # for i, link in enumerate(link_list):
    #     # print(link)
    #     try:
    #         link_list[i] = json.loads(link)
    #         start_urls.append(str(link_list[i]['drug_link']))
    #         # print(link_list[i]['drug_link'])
    #     except:
    #         pass
    counter = -1

    # print('we were here')
    # print(link_list[1]['drug_link'])
    def parse(self, response, **kwargs):
        # for drug in response.css('div.col-lg-12.col-md-12.col-sm-12.col-xs-12.padding0.RowSearchSty'):
        self.counter += 1
        try:
            yield {
                "drug_name": response.css(
                    'div.col-lg-5.col-md-5.col-sm-6.col-xs-12 span.txtAlignLTR::text').get().strip(),
                "generic_code": self.drugs_info[self.counter]['generic_code'],
                "global_name": response.css(
                    "div.col-lg-7.col-md-7.col-sm-12.col-xs-12 bdo.txtAlignLTR::text").get().strip(),
                "drug_type": response.css("div.col-lg-5.col-md-5.col-sm-6.col-xs-12 span.txtAlignLTR::text")[
                    1].get().strip(),
                "how_to_use": response.css("div.col-lg-5.col-md-5.col-sm-6.col-xs-12 bdo.txtAlignLTR::text")[
                    0].get().strip(),
                "license_owner": response.css("div.col-lg-5.col-md-5.col-sm-6.col-xs-12 span.txtAlignLTR::text")[
                    2].get().strip(),
                "license_expire": response.css("div.col-lg-5.col-md-5.col-sm-6.col-xs-12 span.txtAlignLTRFa::text")[
                    0].get().strip(),
                "price": response.css("div.col-lg-5.col-md-5.col-sm-6.col-xs-12 span.txtAlignLTRFa::text")[
                    1].get().strip(),
                "unit_price":
                    response.css("div.col-lg-5.col-md-5.col-sm-12.col-xs-12 span.txtAlignLTRFa.priceTxt::text")[
                        0].get().strip(),
                "GTIN": response.css("div.col-lg-5.col-md-5.col-sm-6.col-xs-12 span.txtAlignLTRFa::text")[
                    2].get().strip(),
                "IRC": response.css("div.col-lg-5.col-md-5.col-sm-6.col-xs-12 span.txtAlignLTRFa::text")[
                    3].get().strip(),
                "count_per_package": response.css("div.col-lg-5.col-md-5.col-sm-6.col-xs-12 bdo.txtAlignLTR::text")[
                    1].get().strip(),
                "package_image": f"https://irc.fda.gov.ir/{response.css('div.gallery-page-inner1.pull-right.padding-right10 a::attr(href)').get()}",
                "drug_image": f"https://irc.fda.gov.ir/{response.css('div.gallery-page-inner1.pull-right.padding-right10 a::attr(href)').get()}",
                "usage": response.css(
                    'div.col-lg-12.col-md-12.col-sm-12.col-xs-12.paddingSearchTXT span.txtSearch1::text').get().strip(),
                "effect_process":
                    response.css('div.col-lg-12.col-md-12.col-sm-12.col-xs-12.paddingSearchTXT span.txtSearch1::text')[
                        1].get().strip(),
                "farmakokintik":
                    response.css('div.col-lg-12.col-md-12.col-sm-12.col-xs-12.paddingSearchTXT span.txtSearch1::text')[
                        2].get().strip(),
                "warnings":
                    response.css('div.col-lg-12.col-md-12.col-sm-12.col-xs-12.paddingSearchTXT span.txtSearch1::text')[
                        3].get().strip(),
                "side_effects":
                    response.css('div.col-lg-12.col-md-12.col-sm-12.col-xs-12.paddingSearchTXT span.txtSearch1::text')[
                        4].get().strip(),
                "Interference":
                    response.css('div.col-lg-12.col-md-12.col-sm-12.col-xs-12.paddingSearchTXT span.txtSearch1::text')[
                        5].get().strip(),
                "advices": response.css(
                    'div.col-lg-5.col-md-5.col-sm-6.col-xs-12.paddingSearchTXT span.txtSearch1::text').get().strip(),
                "drug_url": response.url
            }
            # yield {self.counter: {
            #     "drug_name": response.css(
            #         'div.col-lg-5.col-md-5.col-sm-6.col-xs-12 span.txtAlignLTR::text').get().strip(),
            #     "global_name": response.css(
            #         "div.col-lg-7.col-md-7.col-sm-12.col-xs-12 bdo.txtAlignLTR::text").get().strip(),
            #     "drug_type": response.css("div.col-lg-5.col-md-5.col-sm-6.col-xs-12 span.txtAlignLTR::text")[
            #         1].get().strip(),
            #     "how_to_use": response.css("div.col-lg-5.col-md-5.col-sm-6.col-xs-12 bdo.txtAlignLTR::text")[
            #         0].get().strip(),
            #     "license_owner": response.css("div.col-lg-5.col-md-5.col-sm-6.col-xs-12 span.txtAlignLTR::text")[
            #         2].get().strip(),
            #     "license_expire": response.css("div.col-lg-5.col-md-5.col-sm-6.col-xs-12 span.txtAlignLTRFa::text")[
            #         0].get().strip(),
            #     "price": response.css("div.col-lg-5.col-md-5.col-sm-6.col-xs-12 span.txtAlignLTRFa::text")[
            #         1].get().strip(),
            #     "unit_price":
            #         response.css("div.col-lg-5.col-md-5.col-sm-12.col-xs-12 span.txtAlignLTRFa.priceTxt::text")[
            #             0].get().strip(),
            #     "GTIN": response.css("div.col-lg-5.col-md-5.col-sm-6.col-xs-12 span.txtAlignLTRFa::text")[
            #         2].get().strip(),
            #     "IRC": response.css("div.col-lg-5.col-md-5.col-sm-6.col-xs-12 span.txtAlignLTRFa::text")[
            #         3].get().strip(),
            #     "count_per_package": response.css("div.col-lg-5.col-md-5.col-sm-6.col-xs-12 bdo.txtAlignLTR::text")[
            #         1].get().strip(),
            #     "package_image": f"https://irc.fda.gov.ir/{response.css('div.gallery-page-inner1.pull-right.padding-right10 a::attr(href)').get()}",
            #     "drug_image": f"https://irc.fda.gov.ir/{response.css('div.gallery-page-inner1.pull-right.padding-right10 a::attr(href)').get()}",
            #     "usage": response.css(
            #         'div.col-lg-12.col-md-12.col-sm-12.col-xs-12.paddingSearchTXT span.txtSearch1::text').get().strip(),
            #     "effect_process":
            #         response.css('div.col-lg-12.col-md-12.col-sm-12.col-xs-12.paddingSearchTXT span.txtSearch1::text')[
            #             1].get().strip(),
            #     "farmakokintik":
            #         response.css('div.col-lg-12.col-md-12.col-sm-12.col-xs-12.paddingSearchTXT span.txtSearch1::text')[
            #             2].get().strip(),
            #     "warnings":
            #         response.css('div.col-lg-12.col-md-12.col-sm-12.col-xs-12.paddingSearchTXT span.txtSearch1::text')[
            #             3].get().strip(),
            #     "side_effects":
            #         response.css('div.col-lg-12.col-md-12.col-sm-12.col-xs-12.paddingSearchTXT span.txtSearch1::text')[
            #             4].get().strip(),
            #     "Interference":
            #         response.css('div.col-lg-12.col-md-12.col-sm-12.col-xs-12.paddingSearchTXT span.txtSearch1::text')[
            #             5].get().strip(),
            #     "advices": response.css(
            #         'div.col-lg-5.col-md-5.col-sm-6.col-xs-12.paddingSearchTXT span.txtSearch1::text').get().strip(),
            #     "drug_url": response.url
            # }}


        except:
            {'status': 'not ok'}

    # page_num = 2
    # from ScrapyTest.make_link_dict import link_list
    # next_page = link_list[page_num]
    # page_num += 1
    # if next_page is not None:
    #     yield response.follow(next_page, callback=self.parse)
