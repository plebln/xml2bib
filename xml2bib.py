#!/usr/bin/env python

from __future__ import print_function
import sys
import xml.etree.ElementTree as ET

"""
Note the big X, not a chi, in the class name.

It is possible that  {, " or $ need escaping with backslash ('\').
"""


class BibTeXWriter():
    def __init__(self, tag, data, entry_type='Misc'):
        self.entry_type = entry_type
        self.tag = tag
        self.data = data

    def __str__(self):
        lines = []
        for k in sorted(self.data):
            v = self.data[k]
            if v is None:
                continue
            try:
                value = int(v)
            except ValueError:
                value = '{' + str(v) + '}'
            lines.append('  {} = {}'.format(k, str(value)))
        return '@{0}{{{1},\n'.format(self.entry_type, self.tag,) + \
               ',\n'.join(lines) + '\n}'


class XMLReader():
    def __init__(self, filename):
        tree = ET.parse(filename)
        self.root = tree.getroot()


def xml2dict(x):
    """
    Keys of the dictionary are the fields conventionally used by bibtex.
    """

    r = x.root
    #print('DEBUG', r.attrib)

    xmlfields = ('creator', 'identifier', 'title', 'publisher',
                 'publicationYear', 'resourceType')
    #nsd = {'dc': 'http://datacite.org/schema/kernel-4'}
    ns = '{http://datacite.org/schema/kernel-4}'

    dc = dict.fromkeys(xmlfields)
    for field in xmlfields:
        #for n in r.findall('dc:' + field, nsd):
        for n in r.iter(ns + field):
            v = n.text
            if field == 'creator':
                v = n.find(ns + 'creatorName').text
            #print('Found', field, v)
            if n is not None:
                if dc[field] is None:
                    dc[field] = v
                else:
                    dc[field] = dc[field] + ' and ' + v

    #print('DEBUG dc=', dc)

    d = dict()
    dc_to_bib = {'author': 'creator',
                 'year': 'publicationYear',
                 'DOI': 'identifier',
                 'howpublished': 'resourceType',
                 'publisher': 'publisher',
                 'title': 'title',
                 }

    for x in dc_to_bib:
        d[x] = dc[dc_to_bib[x]]
    return d

if __name__ == '__main__':
    # Process all input files given on command line
    for k in range(1, len(sys.argv)):
        f = sys.argv[k]
        x = XMLReader(f)
        y = xml2dict(x)
        print(str(BibTeXWriter('ref%i' % (k,), y)))
        print()
