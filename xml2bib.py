#!/usr/bin/env python

from __future__ import print_function


class BibTeXWriter():
    def __init__(self, data=dict()):
        self.data = data

    def str(self):
        lines = []
        for k in self.data.keys():
            lines.append('  {} = {}'.format(k, self.data[k]))
        return '@Misc[{}]\{' + ',\n'.join(lines) + '\}'

