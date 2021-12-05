from nonebot import on_command, CommandSession, permission

on_command('show_log', permission=permission.SUPERUSER, only_to_me=False)


async def show_log(session: CommandSession):
    if session.current_arg_text is None:
        with open('./logs/bot.log', 'r') as f:
            log = f.readline()
