import requests

from .models import CRE


class OpenCRE:
    def __init__(self):
        self.settings = {
            "HOST_URL": "https://www.opencre.org/",
            "API_PREFIX": "rest/v1/"
        }

    def change_settings(self, new_settings: dict) -> bool:
        if not isinstance(new_settings, dict):
            raise TypeError("Expected type dict")

        for key in new_settings:
            if self.settings.get(key) is None:
                continue
            self.settings[key] = new_settings[key]

        return True

    def get_endpoint_url(self, endpoint_title):
        host_url = self.settings['HOST_URL']
        api_prefix = self.settings['API_PREFIX']
        endpoint_url = f'{host_url}{api_prefix}{endpoint_title}'
        return endpoint_url

    def perform_api_get_request(self, endpoint_title):
        endpoint_url = self.get_endpoint_url(endpoint_title=endpoint_title)
        response = requests.get(url=endpoint_url)

        if response.status_code == 404:
            return None

        data = response.json().get("data")
        return data

    def root_cres(self) -> list[CRE]:
        endpoint_title = "root_cres"
        root_cres_raw = self.perform_api_get_request(endpoint_title)
        cres = [CRE(root_cre_raw) for root_cre_raw in root_cres_raw]
        return cres

    def cre(self, cre_id: str) -> CRE | None:
        endpoint_title = f"id/{cre_id}"

        if not isinstance(cre_id, str):
            raise TypeError("Expected type str")

        cre_raw = self.perform_api_get_request(endpoint_title)

        if cre_raw is None:
            return cre_raw

        cre_instance = CRE(cre_raw)
        return cre_instance
