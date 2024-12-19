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
            "creator": self.content_opf
        }

        self.toc = xmltodict.parse(self.raw_file.read('OEBPS/toc.ncx'))

        print(self.toc)

        print(self.metadata)



