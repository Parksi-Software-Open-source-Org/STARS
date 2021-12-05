from nonebot import on_command, CommandSession
from plugins.log import logger


@on_command('re-read', aliases=('re_read', 'reread', 're'), only_to_me=False)
def re_read(session: CommandSession):
    logger.info(f"BOT 向 {session.event.user_id} ({session.event.sender['nickname']})发送了: {session.current_arg_text}")
    session.finish(f"你发送了: {session.current_arg_text}")
