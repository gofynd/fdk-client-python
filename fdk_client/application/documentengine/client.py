

"""DocumentEngine Application Client"""

import base64
import ujson
from urllib.parse import urlparse

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import DocumentEngineValidator

class DocumentEngine:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "getInvoiceByShipmentId": "/service/application/document/v1.0/orders/shipments/{shipment_id}/invoice",
            "getCreditNoteByShipmentId": "/service/application/document/v1.0/orders/shipments/{shipment_id}/credit-note"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getInvoiceByShipmentId(self, shipment_id=None, parameters=None, body=""):
        """Use this API to generate Presigned URLs for downloading Invoice
        :param shipment_id : Shiment ID : type string
        :param parameters :  : type 
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        if parameters:
            payload["parameters"] = parameters
        
        # Parameter validation
        schema = DocumentEngineValidator.getInvoiceByShipmentId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getInvoiceByShipmentId"], proccessed_params="""{"required":[{"in":"path","name":"shipment_id","required":true,"description":"Shiment ID","schema":{"type":"string"}}],"optional":[{"in":"query","name":"parameters","required":false,"schema":{"$ref":"#/components/schemas/invoiceParameter"},"style":"form","explode":true}],"query":[{"in":"query","name":"parameters","required":false,"schema":{"$ref":"#/components/schemas/invoiceParameter"},"style":"form","explode":true}],"headers":[],"path":[{"in":"path","name":"shipment_id","required":true,"description":"Shiment ID","schema":{"type":"string"}}]}""", shipment_id=shipment_id, parameters=parameters)
        query_string = await create_query_string(shipment_id=shipment_id, parameters=parameters)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getInvoiceByShipmentId"]).netloc, "get", await create_url_without_domain("/service/application/document/v1.0/orders/shipments/{shipment_id}/invoice", shipment_id=shipment_id, parameters=parameters), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getCreditNoteByShipmentId(self, shipment_id=None, parameters=None, body=""):
        """Use this API to generate Presigned URLs for downloading Invoice
        :param shipment_id : Shiment ID : type string
        :param parameters :  : type 
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        if parameters:
            payload["parameters"] = parameters
        
        # Parameter validation
        schema = DocumentEngineValidator.getCreditNoteByShipmentId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCreditNoteByShipmentId"], proccessed_params="""{"required":[{"in":"path","name":"shipment_id","required":true,"description":"Shiment ID","schema":{"type":"string"}}],"optional":[{"in":"query","name":"parameters","required":false,"schema":{"$ref":"#/components/schemas/creditNoteParameter"},"style":"form","explode":true}],"query":[{"in":"query","name":"parameters","required":false,"schema":{"$ref":"#/components/schemas/creditNoteParameter"},"style":"form","explode":true}],"headers":[],"path":[{"in":"path","name":"shipment_id","required":true,"description":"Shiment ID","schema":{"type":"string"}}]}""", shipment_id=shipment_id, parameters=parameters)
        query_string = await create_query_string(shipment_id=shipment_id, parameters=parameters)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCreditNoteByShipmentId"]).netloc, "get", await create_url_without_domain("/service/application/document/v1.0/orders/shipments/{shipment_id}/credit-note", shipment_id=shipment_id, parameters=parameters), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    

