# -*- coding: utf-8 -*-
import ranger.api
from ranger.api.commands import Command


HOOK_INIT_OLD = ranger.api.hook_init


class hello_world(Command):
    def execute(self):
        self.fm.notify("Hellow World!")


def hook_init(fm):
    fm.execute_console('map hw eval fm.notify("Hello World!")')
    return HOOK_INIT_OLD(fm)


ranger.api.hook_init = hook_init
