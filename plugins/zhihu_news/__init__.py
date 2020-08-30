import requests
from nonebot import on_command,CommandSession

__plugin_name__ = '知乎日报'
__plugin_usage__ = r"""
！知乎日报 -- 可以查看每日知乎

"""

@on_command('知乎日报', only_to_me=False)
async def _(session:CommandSession):
    STORY_URL_FORMAT = 'https://daily.zhihu.com/story/{}'

    resp = requests.get(
        'https://news-at.zhihu.com/api/4/news/latest',
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
    )

    data = resp.json()
    stories = data.get('stories')

    if not stories:
        await session.send('暂时没有数据，或者服务无法访问')
        return

    reply = ''
    for story in stories:
        url = STORY_URL_FORMAT.format(story['id'])
        title = story.get('title', '未知内容')
        reply += f'\n{title}\n{url}\n'

    await session.send(reply)