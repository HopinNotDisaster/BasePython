# keyword
# random
# turtle
#
# 1.  导入请求模块
from urllib import request
import json
#
count = 1
# # 2. 发起请求 将请求结果赋予 res 变量
page = 1
while True:
    res = request.urlopen(
        f"https://image.baidu.com/search/albumsdata?pn={30 * page}&rn=30&tn=albumsdetail&word=%E5%AE%A0%E7%89%A9%E5%9B%BE%E7%89%87&album_tab=%E5%8A%A8%E7%89%A9&album_id=688&ic=0&curPageNum={page}")
    page += 1
    # 3. 获取请求返回值  解码  将类型转换为字典
    res = res.read().decode()
    res = json.loads(res)
    # 4. 解析数据
    datas = res["albumdata"]["linkData"]
    for data in datas:
        image_url = data["thumbnailUrl"]
        # 5. 请求图片
        res_image = request.urlopen(image_url)
        res_image = res_image.read()
        # print(res_image)
        # 6. 保存图片
        with open(f'./dogs/{count}.jpg','wb') as file:
            count += 1
            file.write(res_image)
    if len(datas) != 30:
        break
print(f"总共{count}张图片")

# keyword
# random
# turtle

# 1.  导入请求模块
# from urllib import request
# import json
#
# count = 0
# # 2. 发起请求 将请求结果赋予 res 变量
# page = 1
# res = request.urlopen(
#     f"https://image.baidu.com/search/acjson?tn=resultjson_com&logid=10859863601511598760&ipn=rj&ct"
#     f"=201326592&is=&fp=result&fr=&word=%E4%B8%89%E6%9C%88%E4%B8%83&queryWord=%E4%B8%89%E6%9C%88%E4"
#     f"%B8%83&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab="
#     f"&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn=30&rn=30&gsm=1e&1704872229412=")
# page += 1
# # 3. 获取请求返回值  解码  将类型转换为字典
# res = res.read().decode()
# res = json.loads(res)
# # 4. 解析数据
# print(res)
# datas = res["data"]
# for data in datas:
#     image_url = data["hoverURL"]
#     # 5. 请求图片
#     res_image = request.urlopen(image_url)
#     res_image = res_image.read()
#     # 6. 保存图片
#     count += 1
#     file = open(f"{count}.jpg", "wb")
#     file.write(res_image)
#     file.close()
#
# print(f"总共{count}张图片")
