#!/usr/bin/env python

from __future__ import print_function

"""
Note the big X, not a chi, in the class name.

It is possible that  {, " or $ need escaping with backslash ('\').
"""


class BibTeXWriter():
    def __init__(self, tag, data, entry_type='Misc'):
        self.entry_type = entry_type
        self.tag = tag
        self.data = data

    def str(self):
        lines = []
        for k in sorted(self.data):
            v = self.data[k]
            if isinstance(v, int):
                value = int(v)
            else:
                value = '{' + v + '}'
            lines.append('  {} = {}'.format(k, str(value)))
        return '@{0}{{{1},\n'.format(self.entry_type, self.tag,) + \
               ',\n'.join(lines) + '\n}'
