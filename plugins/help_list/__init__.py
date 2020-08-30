from nonebot import on_command, CommandSession
import nonebot
__plugin_name__ = '联系咱'
__plugin_usage__ = r"""
！mysite查看咱的小站
！git可以看咱的lowbee github
！后花园可以加入咱的破群

"""


@on_command('mysite', aliases=['site', 'web', '网站'], only_to_me=False)
async def mysite(session: CommandSession):
    await session.send('天哥哥的lowbeeweb http://herrtian.top')


@on_command('github', aliases=['git'], only_to_me=False)
async def github(session: CommandSession):
    await session.send('天哥哥的lowbee github https://github.com/Herrtian')


@on_command('后花园', aliases=['群', '天哥群', '天哥后花园'], only_to_me=False)
async def qqqun(session: CommandSession):
    await session.send('天哥哥的后花园+群：1047533560')



