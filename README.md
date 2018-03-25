# xml2bib

This is xml2bib, a quick tool for producing BibTeX entries from DataCite XML.

Begun by Peter L. Evans in Berlin, Germany, March 2018.

Bibliographic chaos may ensue if it is not used correctly.

Use under Gnu Public License (GPL) Version 3.0. http://www.gnu.org/licenses/

    xml2bib is Copyright (C) 2018 Peter L. Evans.
    This software comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions; see `LICENSE` for details.

BibTeX is a widely-used format for references, introduced by Oren
Patashnik in the late 20th century. Despite its age, it is still
widely used, serving in particular as an important part of the LaTeX
software ecosystem.
http://www.bibtex.org/Format/

DataCite is ... the provider and maintainer of DataCite XML,
a schema for metadata about digital objects.
http://datacite.org


Using xml2bib
-------------

1. Standalone.

	python xml2bib file1.xml [ file2.xml ... ]

    e.g. python xml2bib.py xmlfiles/*  runs xml2bib on all the files listed on the command line.

2. As a Python module. Load your XML, then call xml2dict, and the str() method of BibTeXWriter.

        import xml2bib

        x = xml2bib.XMLReader('mydatacitefile.xml')
        d = xml2bib.xml2dict(x)
        print(str(BibTeXWriter('mytagname', d)))

