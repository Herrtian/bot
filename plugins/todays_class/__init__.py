from nonebot import on_command, CommandSession
import nonebot
from time import strftime, gmtime

bot = nonebot.get_bot()
from nonebot.permission import *
from datetime import datetime

SUPERUSERS = [3097079240, 1020116397]

Monday = ['08:30-gay率论@B-414\n', '10:25-数据结构@B-511\n',
          '14:30-电路与电子基础@B-106\n', '16:10-马克思主义基本原理论@B-419\n']


@on_command('today', only_to_me=False)
async def todays_course(session: CommandSession):
    dayOfWeek = datetime.now().isoweekday()

    if dayOfWeek == 1:
        course = Monday[0] + Monday[1] + Monday[2] + Monday[3]

    elif dayOfWeek == 2:
        course = ''

    else:
        course = ''

    content = f'亲爱的主人大人，今天有{course}' \
              f'这些课要上呢，打起精神来吧！加油哦！！'

    if session.ctx["user_id"] in SUPERUSERS:
        await session.send(content)

    else:
        await session.send('您不是我的主人，但我也为你加油！')
