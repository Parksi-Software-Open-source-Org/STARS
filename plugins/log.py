import loguru

logger = loguru.logger
logger.add('./logs/bot.log', enqueue=True, rotation='10 MB', encoding='utf-8')

logger.info("欢迎使用 STARTS BOT")
with open('version', 'r') as f:
    logger.info("软件版本:" + f.read())
logger.info("关注项目:https://github.com/Parksi-Software-Open-source-Org/STARS")
