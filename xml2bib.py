#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function
import sys
import xml.etree.ElementTree as ET

"""
Need to convert some accented Unicode characters to their LaTeX forms.

Note the big X, not a chi, in the class name BibTeXWriter.

It is possible that  {, " or $ need escaping with backslash ('\').
"""


class BibTeXWriter():
    def __init__(self, tag, data, entry_type='Misc', encoding='UTF-8'):
        self.entry_type = entry_type
        self.tag = tag
        self.data = data
        self.enc = encoding

    def __str__(self):
        # LaTex makes accented chars differently.
        replacements = {
            u'ä': u'\\"{a}', u'Ä': u'\"{A}',
            u'ö': u'\\"{o}', u'Ö': u'\"{O}',
            u'ü': u'\\"{u}', u'Ü': u'\"{U}',
            }
        lines = []
        for k in sorted(self.data):
            v = self.data[k]
            if v is None:
                continue
            try:
                value = int(v)
            except ValueError:
                for x in replacements:
                    v = v.replace(x, replacements[x])
                value = '{' + v.encode(self.enc) + '}'
            lines.append('  {} = {}'.format(k, value))
        return '@{0}{{{1},\n'.format(self.entry_type, self.tag,) + \
               ',\n'.join(lines) + '\n}'


class XMLReader():
    def __init__(self, filename):
        try:
            tree = ET.parse(filename)
        except ET.ParseError:
            print('ParseError while processing', filename, file=sys.stderr)
            raise
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
            v = v.strip()
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
