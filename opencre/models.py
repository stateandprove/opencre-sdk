class CRE:
    def __init__(self, cre_raw):
        self.raw = cre_raw
        self.id = cre_raw["id"]
        self.name = cre_raw["name"]
        self.links = [Link(link_raw) for link_raw in cre_raw["links"]]
        self.doctype = cre_raw["doctype"]

    def __str__(self):
        return f'CRE {self.id}'


class Link:
    def __init__(self, link_raw):
        self.document = self.create_document_instance(link_raw)
        self.ltype = link_raw["ltype"]

    def create_document_instance(self, link_raw):
        document_raw = link_raw["document"]
        document = None

        if document_raw["doctype"] == "Standard":
            document = Standard(document_raw)

        if document_raw["doctype"] == "CRE":
            document = CRELink(document_raw)

        if document_raw["doctype"] == "Tool":
            document = Tool(document_raw)

        if document is None:
            raise NotImplementedError("Not implemented for this doctype")

        return document


class Document:
    def __init__(self, document_raw):
        self.doctype = document_raw["doctype"]
        self.name = document_raw["name"]


class Standard(Document):
    ...


class CRELink(Document):
    def __init__(self, document_raw):
        super().__init__(document_raw)
        self.id = document_raw["id"]


class Tool(Document):
    ...
