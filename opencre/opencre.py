import requests

from dataclasses import dataclass
from .models import CRE


@dataclass
class OpenCREConfig:
    HOST_URL: str = "https://www.opencre.org/"
    API_PREFIX: str = "rest/v1/"


class OpenCRE:
    def __init__(self):
        self.conf = OpenCREConfig()

    def get_endpoint_url(self, endpoint_title: str):
        host_url = self.conf.HOST_URL
        api_prefix = self.conf.API_PREFIX
        endpoint_url = f'{host_url}{api_prefix}{endpoint_title}'
        return endpoint_url

    def perform_api_get_request(self, endpoint_title: str):
        endpoint_url = self.get_endpoint_url(endpoint_title=endpoint_title)
        response = requests.get(url=endpoint_url)

        if response.status_code == 404:
            return None

        return response

    def root_cres(self) -> list[CRE]:
        endpoint_title = "root_cres"
        root_cres_response = self.perform_api_get_request(endpoint_title)
        cres = CRE.parse_from_response(response=root_cres_response, many=True)
        return cres

    def cre(self, cre_id: str) -> CRE | None:
        endpoint_title = f"id/{cre_id}"

        if not isinstance(cre_id, str):
            raise TypeError("Expected type str")

        cre_response = self.perform_api_get_request(endpoint_title)

        if cre_response is None:
            return None

        cre = CRE.parse_from_response(response=cre_response)
        return cre
