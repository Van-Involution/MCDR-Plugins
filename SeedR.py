# -*- coding: UTF-8 -*-

from mcdreforged.api.types import ServerInterface
from mcdreforged.api.command import Literal
from mcdreforged.api.rtext import *

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
    seed_prefix = RTextTranslation(translation_key='commands.seed.success')
    seed_rtext = RText(text=seed, color=RColor.green) \
        .c(action=RAction.copy_to_clipboard, value=seed) \
        .h(RTextTranslation(translation_key='chat.copy.click'))
    seed_rtext_list = RTextList(seed_prefix, '[', seed_rtext, ']')
    return seed_rtext_list


def on_load(server: ServerInterface, old):
    server.register_help_message(prefix='!!seed', message='Get seed of server')
    server.register_command(
        Literal('!!seed').runs(lambda src: src.reply(get_seed(server)))
    )
