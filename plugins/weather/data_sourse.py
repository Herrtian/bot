import requests
import json
import os

async def get_weather_of_city(city: str) -> str:
    url = 'http://t.weather.sojson.com/api/weather/city/'
    citys = city
    # 读取json文件
    with open(file='../../data/citys.json') as f:

    # 使用json模块的load方法加载json数据，返回一个字典
        cities = json.load(f)

        # 通过城市的中文获取城市代码
        citys = cities.get(citys)

        # 网络请求，传入请求api+城市代码
        response = requests.get(url + citys)

        # 将数据以json形式返回，这个d就是返回的json数据
        d = response.json()

    print("温度：", d["data"]["forecast"][0]["high"], d["data"]["forecast"][0]["low"])
    print("天气：", d["data"]["forecast"][0]["type"])

    return f'{city}的天气:' \
           f'温度:{d["data"]["forecast"][0]["high"]},{d["data"]["forecast"][0]["low"]}'

