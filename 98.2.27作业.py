import json
import pprint
import re
from urllib import request

# datas = [
#
# ]
#
# res = request.urlopen('https://tieba.baidu.com/hottopic/browse/topicList?res_type=1')
# res = res.read().decode()
# topics = re.findall(r's="topic-text">(.*?)</a>', res)
# talk_numbers = re.findall(r'<span class="topic-num">(.*?)</span>', res)
# texts = re.findall(r'"topic-top-item-desc">(.*?)</p>', res)
# # print(len(topics))
# # print(topics)
# # imags = re.findall(r'pic-top-item"><img src="(.*?)" clas', res)
# # websites = re.findall(r'topic_id=(.*?)&amp;topic_name=', res)
# # print(imags)
# # print(len(imags))
# # print(res)
# # print(websites)
# for i in range(len(topics)):
#     #     web_res = request.urlopen(f'https://tieba.baidu.com/hottopic/browse/hottopic?topic_id={websites[i]}')
#     #     web_res = web_res.read().decode()
#     #     # print(web_res)
#     dic = {
#         "topic": topics[i],
#         "talk_number": talk_numbers[i],
#         "text": texts[i]
#     }
#     datas.append(dic)
# #     web_titles = re.findall(r'="title track-thread-title">(.*?)</a>', web_res)
# #     print(web_titles)
# #     break
# # for data in datas:
# #     print(data)
# # pretty_dict = json.dumps(datas, indent=4, sort_keys=True, )
# # print(pretty_dict)
# pprint.pprint(datas, width=30, indent=4, depth=3, compact=True)

datas = [

]

res = request.urlopen(
    'https://tieba.baidu.com/f/index/forumpark?cn=&ci=0&pcn=%E4%BD%93%E8%82%B2%E8%BF%B7&pci=275&ct=&st=new&pn=3')
res = res.read().decode()
ba_cintents = re.findall(r'ass="ba_name">(.*?)</p><p class', res)
ba_m_nums = re.findall(r'"ba_m_num">(.*?)</span', res)
ba_p_nums = re.findall(r'"ba_p_num">(.*?)</span', res)
desces = re.findall(r'="ba_desc">(.*?)</p>', res)
for i in range(len(ba_cintents)):
    dic = {
        "ba_cintent": ba_cintents[i],
        "ba_m_num": ba_m_nums[i],
        "ba_p_num": ba_p_nums[i],
        "desc": desces[i]
    }
    datas.append(dic)

pprint.pprint(datas, width=30, indent=4, depth=3, compact=True)
