import nonebot
from os import path
import config

if __name__ == '__main__':
    nonebot.init(config)

    # disable default logging
    # nonebot.logging.disable(logging.INFO)

    nonebot.load_plugin('plugins.log')
    # nonebot.load_plugins(
    #     path.join(path.dirname(__file__), 'plugins', 'core'),
    #     'plugins.core'
    # )
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'plugins', 'entertainment'),
        'plugins.entertainment'
    )

    nonebot.run(host='127.0.0.1', port=5867)
