class Documento:
    def leer(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

class PDFDocumento(Documento):
    def leer(self):
        return "Leyendo documento PDF."

class WORDDocumento(Documento):
    def leer(self):
        return "Leyendo documento WORD."

class TXTDocumento(Documento):
    def leer(self):
        return "Leyendo documento TXT."