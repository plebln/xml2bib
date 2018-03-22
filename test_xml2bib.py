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

if __name__ == '__main__':
    unittest.main()
