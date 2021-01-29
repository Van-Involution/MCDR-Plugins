# -*- coding: UTF-8 -*-

from mcdreforged.api.types import ServerInterface
from mcdreforged.api.command import Literal
from mcdreforged.api.rtext import RText, RTextTranslation, RTextList, RColor, RAction

PLUGIN_METADATA = {
    'id': 'seed_reforged',
    'version': '1.0.0',
    'name': 'SeedR',
    'description': 'For "non-op", use command "!!seed" to get seed of server',
    'author': [
        'Van_Involution',  # Reforged to fit MCDR 1.x
        'White_Paper'  # Source of inspiration
    ],
    'link': 'https://github.com/Van-Involution/SeedR',
    'dependencies': {
        'mcdreforged': '>=1.0.0',
    }
}


def get_seed(server: ServerInterface):
    seed = server.rcon_query('/seed').split('[')[1].split(']')[0]
    return RTextList(
        RTextTranslation('commands.seed.success'),
        '[',
        RText(seed, RColor.green)
        .c(RAction.copy_to_clipboard, seed)
        .h(RTextTranslation('chat.copy.click')),
        ']'
    )


def on_load(server: ServerInterface, prev):
    server.register_help_message('!!seed', 'Get seed of server')
    server.register_command(
        Literal('!!seed').runs(lambda src: src.reply(get_seed(server)))
    )
