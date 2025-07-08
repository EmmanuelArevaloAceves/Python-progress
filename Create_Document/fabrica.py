from documento import *
from contador import *

class DocumentFactory:
    @staticmethod
    def create_document(doc_type):
        counter = DocumentCounter()

        if doc_type.lower() == "pdf":
            counter.increment()
            return PDFDocumento()
        elif doc_type.lower() == "word":
            counter.increment()
            return WORDDocumento()
        elif doc_type.lower() == "txt":
            counter.increment()
            return TXTDocumento()
        else:
            raise ValueError("doc_type must be 'pdf', 'word' or 'txt'")