from abc import ABCMeta, abstractmethod


class ApiModel(metaclass=ABCMeta):
    """Abstract class for defining a new API object"""
    service_url: str

    def __init__(self, infusionsoft):
        self.infusionsoft = infusionsoft
        self.base_payload = {'access_token': self.infusionsoft.token.access_token}

    @abstractmethod
    def get_service_url(self):
        pass
