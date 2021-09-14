#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 10:39:26 2021

@author: stefan
"""
# This script uses the following character frequency list by Jun DA
# Combined character frequency list of Classical and Modern Chinese
# Obtained from: https://lingua.mtsu.edu/chinese-computing/statistics/

from icrawler.builtin import GoogleImageCrawler
import pandas as pd
data=pd.read_csv("s_charfreq.csv")

for hanzi in data['汉字']:
    google_crawler = GoogleImageCrawler(
    feeder_threads=1,
    parser_threads=1,
    downloader_threads=4,
    storage={'root_dir': 's_img/'+hanzi})

    google_crawler.crawl(keyword=hanzi+'书法', offset=0, max_num=4,
                     min_size=None, max_size=(400,400), file_idx_offset=0)
