from PySide6 import QtCore, QtWidgets, QtGui, QtUiTools
import sources.file_extension.epub_class
from si import lang


def gen_html_p_property(item, value, typeq: str = "Normal"):
    if typeq == "Normal":
        return f'<p class="property"><span style="font-weight: 800">{item}</span>: <span>{value}</span></p>'
    elif typeq == "Authors":
        return " ".join([i.name for i in value])
    elif typeq == "Contributors":
        return f'<p class="property"><span style="font-weight: 800">{item}</span>:</p><ul>{
            "".join([
                f"<li><span style='font-weight: 500'>{i.name}</span> <span class='inrpct'>&#183;</span> <span class='role'>{
                    lang.epub_contributor_roles[i.role]
                }</span></li>" for i in value
            ])
        }</ul>'
        pass


class BookInfo:
    def __init__(self, book: sources.file_extension.epub_class.epub):
        loader = QtUiTools.QUiLoader()
        ui_file = QtCore.QFile("./sources/interface/ui/book_info.ui")
        ui_file.open(QtCore.QFile.ReadOnly)
        self.ui = loader.load(ui_file, None)
        ui_file.close()


        with open("./sources/interface/html/book_info.html", encoding="UTF-8") as f:
            q = f.read()
            ret = []
            q = q.replace("$title", book.metadata["title"])
            q = q.replace("$authors", str(gen_html_p_property(", ", book.metadata["authors"], "Authors")))
            q = q.replace("$description", book.metadata["description"])

            ret.append(gen_html_p_property(lang.epub_metadata["language"], book.metadata["language"]))
            ret.append(gen_html_p_property(lang.epub_metadata["publisher"], book.metadata["publisher"]))
            ret.append(gen_html_p_property(lang.epub_metadata["rights"], book.metadata["rights"]))
            ret.append(gen_html_p_property(lang.epub_metadata["ISBN"], book.metadata["ISBN"]))
            ret.append(gen_html_p_property(lang.epub_metadata["BookId"], book.metadata["BookId"]))
            ret.append(gen_html_p_property(lang.epub_metadata["contributors"], book.metadata["contributors"], "Contributors"))

            q = q.replace("$additional", "".join(ret))

            self.ui.cover.setHtml(f"<img src='{book.init_temp_cover()}' width='350'")
            self.ui.textBrowser.setHtml(q)

        QtGui.QShortcut('Esc', self.ui).activated.connect(self.ui.close)

        # self.ui.
        self.ui.setWindowTitle(lang.win_book_info + ": " + book.metadata["title"])
        self.ui.setWindowOpacity(0.97)
        book.get_metadata()

        # self.ui.setFixedSize(530, 200)

    def open(self):
        self.ui.show()
