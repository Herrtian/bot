# this plugin is to handle msg
from nonebot import on_command, CommandSession
import nonebot
from time import strftime, gmtime
bot = nonebot.get_bot()


@bot.on_message('private')
async def save_msg(context):
    msg = context["message"]
    s_msg = str(msg)
    qq = context["user_id"]

    ctx = f'用户:{qq} 发送了以下内容\n' \
          f'{msg}'
    if qq ==  3097079240:
        pass
    else:
        await bot.send_private_msg(user_id=3097079240, message=ctx)


# sm is to send message to a group
# sb is to send message to someone

bot = nonebot.get_bot()


@on_command('sm')
async def send_message(session:CommandSession):
    sentence = session.get('sentence')
    param = sentence
    userid = session.ctx["user_id"]
    aim = param[0]
    time_01 = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    message = f'用户 {userid} 在 {time_01} 发送了以下内容\n' + param[1]

    if userid == 3097079240 or 1020116397:
        if aim == "你群":
            aim = 55563398

        elif aim == "舰狗":
            aim = 484784241

        elif aim == "宿舍":
            aim = 878373471

        elif aim == "测试":
            aim = 887412693

        elif aim == "学校":
            aim = 473610271

        await bot.send_msg(group_id=int(aim), message=message)
        await bot.send_msg(user_id=userid, message="发送成功了哦")

@send_message.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.split()
    session.state['sentence'] = stripped_arg


@on_command('sb')
async def send_message(session:CommandSession):
    sentence = session.get('sentence')
    param = sentence
    userid = session.ctx["user_id"]
    aim = param[0]
    time_01 = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    message = f'用户 {userid} 在 {time_01} 发送了以下内容\n' + param[1]

    if userid == 3097079240 or 1020116397:

        await bot.send_msg(user_id=int(aim), message=message)
        await bot.send_msg(user_id=userid, message="发送成功了哦")


@send_message.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.split()
    session.state['sentence'] = stripped_arg

