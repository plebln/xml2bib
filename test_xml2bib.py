#!/usr/bin/env python

from __future__ import print_function
import xml2bib
import unittest


class TestBibTeXWrite(unittest.TestCase):
    verbose = False

    def test_empty(self):
        w = xml2bib.BibTeXWriter('', dict())
        x = str(w)
        self.assertTrue(len(x) > 0)

    def test_basic(self):
        d = {'creator': 'A. Einstein',
             'year': 1905,
             'title': 'The photo-electric effect',
             'journal': 'Phys. Rev.'}
        w = xml2bib.BibTeXWriter('AE05', d)
        x = str(w)
        self.assertTrue(len(x) > 0)
        if (self.verbose):
            print('testBasic:', x)


class TestXMLReader(unittest.TestCase):
    def test_one(self):
        f = 'xmlfiles/_10.14470_6t569239.xml'
        x = xml2bib.XMLReader(f)
        d = xml2bib.xml2dict(x)

        c_names = ('Th, H.',
                   'Ba, N.',
                   'Ma, V.',
                   'Ri, J.',
                   'Ti, F.',)
        c = ' and '.join(c_names)
        self.assertEqual(d['author'], c)


if __name__ == '__main__':
    unittest.main()
