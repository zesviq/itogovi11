import zipfile
import xmltodict


class epub:
    def __init__(self, filename: str):
        self.raw_file = zipfile.ZipFile(filename, 'r')

        # Check mimetype
        if not self.raw_file.read("mimetype") == b"application/epub+zip":
            print("ЭТО НЕ ЕПУБ")
            return

        self.content_opf = xmltodict.parse(self.raw_file.read('OEBPS/content.opf'))

        self.metadata = {
            "title": self.content_opf["package"]["metadata"]["dc:title"],
            "creator": self.content_opf
        }

        self.toc = xmltodict.parse(self.raw_file.read('OEBPS/toc.ncx'))

        print(self.toc)

        print(self.metadata)

a = epub("./books/010000_000060_ART-01b88ec3-3cbf-4d58-ad38-085c28e2fe98-Пиковая_дама.epub")