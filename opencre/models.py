from __future__ import annotations
from requests import Response


class Link:
    def __init__(self, raw, ltype):
        self.raw = raw
        self.ltype = ltype

    @classmethod
    def parse_from_cre(cls, cre: CRE) -> list[Link]:
        links_raw = cre.raw.get("links")
        links = [cls(raw=link_raw, ltype=link_raw["ltype"]) for link_raw in links_raw]
        return links

    def get_document_class(self):
        document_parent = Document.parse_from_link(link=self)
        doctype = document_parent.doctype
        document_class = None

        if doctype == "Standard":
            document_class = Standard

        if doctype == "CRE":
            document_class = CRELink

        if doctype == "Tool":
            document_class = Tool

        if document_class is None:
            raise NotImplementedError("Not implemented for this doctype")

        return document_class

    @property
    def document(self):
        document_class = self.get_document_class()
        document = document_class.parse_from_link(self)
        return document


class CRE:
    def __init__(self, raw, cre_id, name, doctype):
        self.raw = raw
        self.id = cre_id
        self.name = name
        self.doctype = doctype

    @property
    def links(self):
        return Link.parse_from_cre(cre=self)

    @classmethod
    def parse_from_response(cls, response: Response, many: bool = False) -> CRE | list[CRE]:
        cres = []
        data = response.json().get("data")

        if not many:
            data = [data]

        for raw_cre in data:
            cre = cls(
                raw=raw_cre,
                cre_id=raw_cre["id"],
                name=raw_cre["name"],
                doctype=raw_cre["doctype"]
            )
            cres.append(cre)

        if not many:
            return cres[0]

        return cres

    def __str__(self):
        return f'CRE {self.id}'


class Document:
    def __init__(self, raw, doctype, name):
        self.raw = raw
        self.doctype = doctype
        self.name = name

    @classmethod
    def parse_from_link(cls, link: Link) -> Document:
        document_raw = link.raw.get("document")
        document = cls(
            raw=document_raw,
            doctype=document_raw["doctype"],
            name=document_raw["name"]
        )
        return document


class Standard(Document):
    ...


class Tool(Document):
    ...


class CRELink(Document):
    @property
    def id(self):
        return self.raw["id"]
