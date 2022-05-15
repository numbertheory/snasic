import os
from snasic.argument_parse import collect


class Config:
    def __init__(self, args_file):
        path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
        self.args = path + '/snasic/' + args_file
        self.filename = collect.Arguments(self.args).value("filename")
        self.list = collect.Arguments(self.args).value("list")
        self.debug = collect.Arguments(self.args).value("debug")
        self.explore = collect.Arguments(self.args).value("explore")
