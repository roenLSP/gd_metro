# -*- coding: utf-8 -*-
import json

import scrapy

from shenzhen_metro.items import GaodeItem


class SzdtSpider(scrapy.Spider):
    name = 'szdt'
    allowed_domains = ['https://www.amap.com/search?']
    start_urls = ['http://https://www.amap.com/search?/']
    def start_requests(self):
        url1 = 'https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=12&city=440300&geoobj=113.959604%7C22.461044%7C114.322153%7C22.63924&keywords=%E5%9C%B0%E9%93%811%E5%8F%B7%E7%BA%BF(%E7%BD%97%E5%AE%9D%E7%BA%BF)'
        # url2 = 'https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=12&city=440300&geoobj=113.873655%7C22.493729%7C114.038467%7C22.671894&keywords=%E5%9C%B0%E9%93%812%E5%8F%B7%E7%BA%BF(%E8%9B%87%E5%8F%A3%E7%BA%BF)'
        # url3 = 'https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=11&city=440300&geoobj=113.806526%7C22.496821%7C114.136132%7C22.8529&keywords=%E5%9C%B0%E9%93%813%E5%8F%B7%E7%BA%BF(%E9%BE%99%E5%B2%97%E7%BA%BF)'
        # url4 = 'https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=10&city=440300&geoobj=113.976076%7C22.202853%7C114.63527%7C22.915592&keywords=%E5%9C%B0%E9%93%814%E5%8F%B7%E7%BA%BF(%E9%BE%99%E5%8D%8E%E7%BA%BF)'
        # url5 =  'https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=12&city=440300&geoobj=113.948591%7C22.503969%7C114.113402%7C22.68212&keywords=%E5%9C%B0%E9%93%815%E5%8F%B7%E7%BA%BF(%E7%8E%AF%E4%B8%AD%E7%BA%BF)'
        # url6 = 'https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=11&city=440300&geoobj=113.832177%7C22.410478%7C114.161783%7C22.76678&keywords=%E5%9C%B0%E9%93%815%E5%8F%B7%E7%BA%BF%E5%8D%97%E5%BB%B6%E7%BA%BF'
        # url7 = 'https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=13.95&city=440300&geoobj=113.891746%7C22.487664%7C113.934416%7C22.53381&keywords=%E5%9C%B0%E9%93%817%E5%8F%B7%E7%BA%BF'
        # url8 = 'https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=11&city=440300&geoobj=113.744041%7C22.479057%7C114.073647%7C22.835182&keywords=%E5%9C%B0%E9%93%812%E5%8F%B7%E7%BA%BF%E4%B8%9C%E5%BB%B6%E7%BA%BF'
        # url9 = 'https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=11&city=440300&geoobj=113.863707%7C22.384363%7C114.193313%7C22.740732&keywords=%E5%9C%B0%E9%93%819%E5%8F%B7%E7%BA%BF'
        # url10 = 'https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=12&city=440300&geoobj=113.960209%7C22.459293%7C114.12502%7C22.637502&keywords=%E5%9C%B0%E9%93%819%E5%8F%B7%E7%BA%BF%E8%A5%BF%E5%BB%B6%E7%BA%BF'
        # url11 = 'https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=13&city=440300&geoobj=113.887079%7C22.476574%7C113.969494%7C22.565703&keywords=%E5%9C%B0%E9%93%8111%E5%8F%B7%E7%BA%BF'
        # url12 = 'https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=14&city=440300&geoobj=114.138934%7C22.534448%7C114.180151%7C22.579008&keywords=%E5%9C%B0%E9%93%813%E5%8F%B7%E7%BA%BF%E4%B8%9C%E5%BB%B6%E7%BA%BF'

        yield scrapy.Request(url1, callback=self.parse)
        # yield scrapy.Request(url2, callback=self.parse)
        # yield scrapy.Request(url3, callback=self.parse)
        # yield scrapy.Request(url4, callback=self.parse)
        # yield scrapy.Request(url5, callback=self.parse)
        # yield scrapy.Request(url6, callback=self.parse)
        # yield scrapy.Request(url7, callback=self.parse)
        # yield scrapy.Request(url8, callback=self.parse)
        # yield scrapy.Request(url9, callback=self.parse)
        # yield scrapy.Request(url10, callback=self.parse)
        # yield scrapy.Request(url11, callback=self.parse)
        # yield scrapy.Request(url12, callback=self.parse)

    def parse(self, response):
        html = json.loads(response.text)
        item = GaodeItem()
        if 'data' in html.keys():
            name = html.get('data').get('busline_list')[0].get('name')
            stations = html.get('data').get('busline_list')[0].get('stations')

            for station in stations:
                item['name'] = name
                item['station_name'] = station.get('name')
                item['station_num'] = station.get('station_num')
                item['longitude'] = station.get('poiid2_xy')[:10]
                item['latitude'] = station.get('poiid2_xy')[11:20]
                yield item