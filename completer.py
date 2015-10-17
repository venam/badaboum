# -*- coding: UTF-8 -*-

import re
import os
import readline
# ---complete the path or commands--- #


class Completer(object):
    def __init__(self, default_mode, commands):
        self.re_space = re.compile('.*\s+$', re.M)
        self.mode = default_mode
        self.commands = commands

    def _listdir(self, root):
        res = []
        for name in os.listdir(root):
            path = os.path.join(root, name)
            if os.path.isdir(path):
                name += os.sep
            res.append(name)
        return res

    def _complete_path(self, path=None):
        if not path:
            return self._listdir('.')
        dirname, rest = os.path.split(path)
        tmp = dirname if dirname else '.'
        res = [
            os.path.join(dirname, p)
            for p in self._listdir(tmp) if p.startswith(rest)]
        if len(res) > 1 or not os.path.exists(path):
            return res
        if os.path.isdir(path):
            return [os.path.join(path, p) for p in self._listdir(path)]
        return [path + '']

    def complete_extra(self, args):
        if not args:
            return self._complete_path('.')
        return self._complete_path(args[-1])

    def complete(self, text, state):
        buffer = readline.get_line_buffer()
        line = readline.get_line_buffer().split()
        if not line:
            return [c + ' 'for c in self.commands[self.mode].keys()][state]
        if self.re_space.match(buffer):
            line.append('')
        cmd = line[0].strip()
        if cmd in self.commands[self.mode].keys():
            impl = getattr(self, 'complete_%s' % "extra")
            args = line[1:]
            if args:
                return (impl(args) + [None])[state]
            return [cmd + ''][state]
        if cmd.startswith('/'):
            impl = getattr(self, 'complete_%s' % "extra")
            args = line[0:]
            if args:
                return (impl(args) + [None])[state]
            return [cmd + ''][state]
        results = [
            c + ''
            for c in self.commands[self.mode].keys()
            if c.startswith(cmd)] + [None]

        return results[state]
