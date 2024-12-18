# Package EPUB

import zipfile
import xmltodict


class EPUB:
    def __init__(self, filename: str):
        self.raw_file = zipfile.ZipFile(filename, 'r')

        # Check mimetype
        self.mimetype = self.raw_file.read("mimetype")

        self.content_opf = xmltodict.parse(self.raw_file.read('OEBPS/content.opf'))

        self.metadata = {
            "title": self.content_opf["package"]["metadata"]["dc:title"],
            "creator": ""
        }

        self.toc = xmltodict.parse(self.raw_file.read('OEBPS/toc.ncx'))

        print(self.toc)

        print(self.metadata)

    def get_mimetype(self, chapter):
        return self.raw_file.read(f'OEBPS/Text/chapter{chapter}.xhtml').decode("UTF-8")


S = EPUB("D:\github\itogovi11\prest.epub")
