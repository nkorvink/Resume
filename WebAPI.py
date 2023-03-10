from abc import ABC, abstractmethod

class WebAPI(ABC):

  def _download_url(self, url: str) -> dict:
    #TODO: Implement web api request code in a way that supports ALL types of web APIs
    pass
	
  def set_apikey(self, apikey:str) -> None:
    pass
	
  @abstractmethod
  def load_data(self):
    pass
	
  @abstractmethod
  def transclude(self, message:str) -> str:
    pass