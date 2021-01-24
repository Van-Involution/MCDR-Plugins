# -*- coding: UTF-8 -*-

from mcdreforged.api.types import ServerInterface
from mcdreforged.api.command import Literal
from mcdreforged.api.rtext import *

PLUGIN_METADATA = {
    'id': 'seed',
    'version': '1.0.0',
    'name': 'Seed',
    'description': 'rue',
    'author': [
        'Van_Involution',  # Reforged to  MCDR 1.0.0
        'White_Paper'  # Which  base
    ],
    'dependencies': {
        'mcdreforged': '>=1.0.0',
    }
}


def on_load(server: ServerInterface, old):
    server.logger.info('Rua!')
    help_message = RTextTranslation(translation_key='help.message.seed')
    server.register_help_message(prefix='!!seed', message=help_message)
    server_seed = get_seed(server)
    server.register_command(
        Literal('!!seed').runs(lambda src: src.reply(server_seed))
    )


def get_seed(server: ServerInterface):
    seed = server.rcon_query('/seed').split('[')[1].split(']')[0]
    seed_prefix = RTextTranslation(translation_key='commands.seed.success')
    seed_rtext = RText(text=seed, color=RColor.green) \
        .set_click_event(action=RAction.copy_to_clipboard, value=seed) \
        .set_hover_text(RTextTranslation(translation_key='chat.copy.click'))
    seed_rtext_list = RTextList(seed_prefix, '[', seed_rtext, ']')
    return seed_rtext_list
