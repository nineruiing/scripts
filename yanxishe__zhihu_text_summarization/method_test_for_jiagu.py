# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import jiagu
import pandas as pd
from tqdm import tqdm

test_df = pd.read_csv(r'D:\data\61\data\test.csv')

texts = test_df['article'].values
res = []

for text in tqdm(texts):
    text = text.replace('<Paragraph>', ' ')
    summarize = jiagu.summarize(text, 1)
    print(summarize)
    res.append(summarize[0])

sub = pd.DataFrame()
sub['sum'] = res
sub.head()

sub.to_csv('sub_jiagu.csv', header=False)

# fin = open('input.txt', 'r')
# text = fin.read()
# fin.close()
# if __name__ == '__main__':
#     text = '(临湘“12·10”强奸杀人案嫌犯一审被判死刑)红网临湘8月21日讯（通讯员 彭勇 胡莎）8月21日上午10点15分，由临湘市人民检察院起诉的湖南临湘“12·10”强奸杀人案的嫌犯邓某，被临湘市人民法院判处死刑，剥夺政治权利终身。邓某，男，1990年9月5日出生于湖南省临湘市，租住在该市饲料公司院内，在五里牌某发廊工作。近两年，因失恋、经商亏损等原因让他产生以强奸、杀人等极端方式报复社会的想法。2014年12月10日晚上9点左右，邓某携带胶带、美工刀等作案工具，在临湘市城区寻找作案目标。在临湘市五中门口，他发现了晚自习后回家的刘小美（化名，本案被害人，女，在校高中学生，殁年16岁）。邓某尾随小美回家，至一条偏僻小路时，乘其不备，用右手勒住她脖子，迅速将她拖至旁边的菜地其掐至昏迷，对她实施了两次强奸行为。事后逃离时，他发现小美尚有气息，又用双手用力掐住其颈部直至其死亡后，再次逃离了作案现场。2014年12月17日，邓某被公安机关在其租住房中抓获。临湘市人民检察院提前介入该案，并全程参与犯罪嫌疑人对犯罪现场及作案过程的指认。审讯过程中，邓某还交代了其曾犯盗窃罪，并在2013年曾强奸杀人的事实。原来，2013年8月10日晚上10点左右，已经产生报复社会想法的邓某携带作案工具绳索，骑自行车在临湘市城区寻找作案目标，发现赵月（化名，本案被害人，女，在校大学生，殁年20岁）独自一人在长安三桥附近的河边路上行走。邓某见周围人烟稀少，于是尾随其后，用右手勒住其脖子将其拖至路边将其掐死。在确认赵月死亡后，对尸体实施了奸淫，并将她包内50多元现金偷走，其他身份证等物品丢弃至长安河中。为防止被人发现，邓某用事先准备的绳索将路边的水泥块绑在尸体上，将尸体抛入长安河中，再逃离了作案现场。'
#
#     summarize = jiagu.summarize(text, 5)  # 摘要
#     print(summarize)
