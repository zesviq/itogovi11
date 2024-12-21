import zipfile
import xmltodict


def delta_list(arg):
    t = type(arg)
    if t == list:
        return arg
    elif t == dict:
        return [arg]


# contributor docs: https://idpf.org/epub/20/spec/OPF_2.0_final_spec.html#Section2.2.6

_epub_contributor_roles = [
    "adp", "ann", "arr", "art", "asn",
    "aut", "aqt", "aft", "aui", "ant",
    "bkp", "clb", "cmm", "dsr", "edt",
    "ill", "lyr", "mdc", "mus", "nrt",
    "oth", "pht", "prt", "red", "rev",
    "spn", "ths", "trc", "trl"
]


class Contributor:
    def __init__(self, name: str, role: str):
        self.name = name

        if role in _epub_contributor_roles:
            self.role = role
        else:
            self.role = "oth"


def contributors_roles(cont_list: list):
    ret = []
    for cont in cont_list:
        ret.append(Contributor(cont["#text"], cont["@opf:role"]))
    return ret


class epub:
    def __init__(self, filename: str):
        try:
            self.filename = filename
            self.raw_file = zipfile.ZipFile(filename, 'r')

            # Check mimetype
            if not self.raw_file.read("mimetype") == b"application/epub+zip":
                raise KeyError("ItsNoEPUB")

            self.content_opf = xmltodict.parse(self.raw_file.read('OEBPS/content.opf'))
            metadata = self.content_opf["package"]["metadata"]

            self.metadata = {
                "title": metadata["dc:title"],
                "authors": contributors_roles(delta_list(metadata["dc:creator"])),
                # "authors": [i["#text"] for i in delta_list(metadata["dc:creator"])],
                "language": metadata["dc:language"],
                "publisher": metadata["dc:publisher"],
                "rights": metadata["dc:rights"],
                "contributors": contributors_roles(delta_list(metadata["dc:contributor"])),
                "dates": {},  # Filled with for
                "cover_path": "",
                "description": metadata["dc:description"]
            }

            # Set dates
            for i in delta_list(metadata["dc:date"]):
                self.metadata["dates"][i["@opf:event"]] = i["#text"]

            for i in delta_list(metadata["meta"]):
                typ = i["@name"]
                if typ == "cover":
                    self.metadata["cover_path"] = str("OEBPS/Images/" + i["@content"])

            for i in delta_list(metadata["dc:identifier"]):
                scheme = i["@opf:scheme"]
                if scheme == "UUID" and i["@id"] == "BookId":
                    self.metadata["BookId"] = i["#text"]
                elif scheme == "ISBN":
                    self.metadata["ISBN"] = i["#text"]

            # Set
            print("\n\n", self.metadata)
            self.toc = xmltodict.parse(self.raw_file.read('OEBPS/toc.ncx'))

        # print(self.toc)

        # print(self.metadata)
        except KeyError:
            raise KeyError("ItsNoEPUB")

    def get_metadata(self):
        return self.metadata


# a = epub("./books/010000_000060_ART-fe85f208-ab88-41cc-bb63-ec52e7811146-Преступление_отпавшего_листа.epub")
