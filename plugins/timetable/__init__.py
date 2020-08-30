import nonebot
from apscheduler.triggers.date import DateTrigger  # 一次性触发器
from apscheduler.triggers.cron import CronTrigger  # 定期触发器
from apscheduler.triggers.interval import IntervalTrigger  # 间隔触发器
from nonebot import on_command, scheduler

bot = nonebot.get_bot()


@nonebot.scheduler.scheduled_job(
    'cron',
    # year=None,
    # month=None,
    # day=None,
    # week=None,
    day_of_week="mon,tue,wed,thu,fri",
    hour=7,
    minute=50,
    # second=None,
    # start_date=None,
    # end_date=None,
    # timezone=None,
)
async def _():
    await bot.send_private_msg(user_id=3097079240, message="起床啦！")


@nonebot.scheduler.scheduled_job(
    'cron',
    # year=None,
    # month=None,
    # day=None,
    # week=None,
    day_of_week="mon,tue,wed,thu,fri",
    hour=8,
    minute=25,
    # second=None,
    # start_date=None,
    # end_date=None,
    # timezone=None,
)
async def _():
    await bot.send_private_msg(user_id=3097079240, message="呐呐呐，现在是gay率论时间咯")


@nonebot.scheduler.scheduled_job(
    'cron',
    # year=None,
    # month=None,
    # day=None,
    # week=None,
    day_of_week="mon,tue,wed,thu,fri",
    hour=10,
    minute=20,
    # second=None,
    # start_date=None,
    # end_date=None,
    # timezone=None,
)
async def _():
    await bot.send_private_msg(user_id=3097079240, message="主人最喜欢的数据结构来咯")


@nonebot.scheduler.scheduled_job(
    'cron',
    # year=None,
    # month=None,
    # day=None,
    # week=None,
    day_of_week="mon,tue,wed,thu,fri",
    hour=14,
    minute=25,
    # second=None,
    # start_date=None,
    # end_date=None,
    # timezone=None,
)
async def _():
    await bot.send_private_msg(user_id=3097079240, message="电子电路基础")


@nonebot.scheduler.scheduled_job(
    'cron',
    # year=None,
    # month=None,
    # day=None,
    # week=None,
    day_of_week="mon,tue,wed,thu,fri",
    hour=16,
    minute=10,
    # second=None,
    # start_date=None,
    # end_date=None,
    # timezone=None,
)
async def _():
    await bot.send_private_msg(user_id=3097079240, message="马哲~~马哲~~")
