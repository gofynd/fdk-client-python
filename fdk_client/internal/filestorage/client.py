

"""FileStorage Internal Client"""

from urllib.parse import urlparse

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import FileStorageValidator

class FileStorage:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "generateBulkPdf": "/___/internal/assets/v1.0/bulk/generate-shipment"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def generateBulkPdf(self, body=""):
        """Generate single PDFs for bulk shipments for invoices, label's and Delivery challan
        """
        payload = {}
        
        # Parameter validation
        schema = FileStorageValidator.generateBulkPdf()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GenerateShipmentRequestBody
        schema = GenerateShipmentRequestBody()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["generateBulkPdf"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {}
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["generateBulkPdf"]).netloc, "get", await create_url_without_domain("/___/internal/assets/v1.0/bulk/generate-shipment", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GenerateShipment200
            schema = GenerateShipment200()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for generateBulkPdf")
                print(e)

        

        return response
    

