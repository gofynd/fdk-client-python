"""Order Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .applicationValidator import OrderValidator

class Order:
    def __init__(self, config: PlatformConfig, applicationId: str):
        self._conf = config
        self.applicationId = applicationId

    
    async def getShipmentBagReasons(self, shipment_id=None, line_number=None, request_headers:Dict={}):
        """Get reasons to perform full or partial cancellation of a shipment
        :param shipment_id : ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        :param line_number : line number of bag. : type integer
        """
        payload = {}
        
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id
        if line_number is not None:
            payload["line_number"] = line_number

        # Parameter validation
        schema = OrderValidator.getShipmentBagReasons()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/shipments/{shipment_id}/line_number/{line_number}/reasons", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer","example":37}},{"in":"path","name":"application_id","description":"Application ID of company","required":true,"schema":{"type":"string","example":"5d63686df2a4f7806b76bb32"}},{"in":"path","description":"ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"shipment_id","required":true,"schema":{"type":"string"}},{"in":"path","description":"line number of bag.","name":"line_number","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer","example":37}},{"in":"path","name":"application_id","description":"Application ID of company","required":true,"schema":{"type":"string","example":"5d63686df2a4f7806b76bb32"}},{"in":"path","description":"ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"shipment_id","required":true,"schema":{"type":"string"}},{"in":"path","description":"line number of bag.","name":"line_number","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", shipment_id=shipment_id, line_number=line_number)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/shipments/{shipment_id}/line_number/{line_number}/reasons", shipment_id=shipment_id, line_number=line_number), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ShipmentBagReasons
            schema = ShipmentBagReasons()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getShipmentBagReasons")
                print(e)

        return response
    
    async def getApplicationShipments(self, lane=None, search_type=None, search_id=None, from_date=None, to_date=None, dp_ids=None, ordering_company_id=None, stores=None, sales_channel=None, request_by_ext=None, page_no=None, page_size=None, customer_id=None, is_priority_sort=None, exclude_locked_shipments=None, request_headers:Dict={}):
        """Get shipments of a particular sales channel based on the filters provided
        :param lane :  : type string
        :param search_type :  : type string
        :param search_id :  : type string
        :param from_date :  : type string
        :param to_date :  : type string
        :param dp_ids :  : type string
        :param ordering_company_id :  : type string
        :param stores :  : type string
        :param sales_channel :  : type string
        :param request_by_ext :  : type string
        :param page_no :  : type integer
        :param page_size :  : type integer
        :param customer_id :  : type string
        :param is_priority_sort :  : type boolean
        :param exclude_locked_shipments :  : type boolean
        """
        payload = {}
        
        if lane is not None:
            payload["lane"] = lane
        if search_type is not None:
            payload["search_type"] = search_type
        if search_id is not None:
            payload["search_id"] = search_id
        if from_date is not None:
            payload["from_date"] = from_date
        if to_date is not None:
            payload["to_date"] = to_date
        if dp_ids is not None:
            payload["dp_ids"] = dp_ids
        if ordering_company_id is not None:
            payload["ordering_company_id"] = ordering_company_id
        if stores is not None:
            payload["stores"] = stores
        if sales_channel is not None:
            payload["sales_channel"] = sales_channel
        if request_by_ext is not None:
            payload["request_by_ext"] = request_by_ext
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if customer_id is not None:
            payload["customer_id"] = customer_id
        if is_priority_sort is not None:
            payload["is_priority_sort"] = is_priority_sort
        if exclude_locked_shipments is not None:
            payload["exclude_locked_shipments"] = exclude_locked_shipments

        # Parameter validation
        schema = OrderValidator.getApplicationShipments()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/shipments/", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string"}}],"optional":[{"name":"lane","in":"query","required":false,"schema":{"type":"string"}},{"name":"search_type","in":"query","required":false,"schema":{"type":"string"}},{"name":"search_id","in":"query","required":false,"schema":{"type":"string"}},{"name":"from_date","in":"query","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","required":false,"schema":{"type":"string"}},{"name":"dp_ids","in":"query","required":false,"schema":{"type":"string"}},{"name":"ordering_company_id","in":"query","required":false,"schema":{"type":"string"}},{"name":"stores","in":"query","required":false,"schema":{"type":"string"}},{"name":"sales_channel","in":"query","required":false,"schema":{"type":"string"}},{"name":"request_by_ext","in":"query","required":false,"schema":{"type":"string"}},{"name":"page_no","in":"query","required":false,"schema":{"type":"integer"}},{"name":"page_size","in":"query","required":false,"schema":{"type":"integer"}},{"name":"customer_id","in":"query","required":false,"schema":{"type":"string"}},{"name":"is_priority_sort","in":"query","required":false,"schema":{"type":"boolean","default":true}},{"name":"exclude_locked_shipments","in":"query","required":false,"schema":{"type":"boolean","default":true}}],"query":[{"name":"lane","in":"query","required":false,"schema":{"type":"string"}},{"name":"search_type","in":"query","required":false,"schema":{"type":"string"}},{"name":"search_id","in":"query","required":false,"schema":{"type":"string"}},{"name":"from_date","in":"query","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","required":false,"schema":{"type":"string"}},{"name":"dp_ids","in":"query","required":false,"schema":{"type":"string"}},{"name":"ordering_company_id","in":"query","required":false,"schema":{"type":"string"}},{"name":"stores","in":"query","required":false,"schema":{"type":"string"}},{"name":"sales_channel","in":"query","required":false,"schema":{"type":"string"}},{"name":"request_by_ext","in":"query","required":false,"schema":{"type":"string"}},{"name":"page_no","in":"query","required":false,"schema":{"type":"integer"}},{"name":"page_size","in":"query","required":false,"schema":{"type":"integer"}},{"name":"customer_id","in":"query","required":false,"schema":{"type":"string"}},{"name":"is_priority_sort","in":"query","required":false,"schema":{"type":"boolean","default":true}},{"name":"exclude_locked_shipments","in":"query","required":false,"schema":{"type":"boolean","default":true}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string"}}]}""", serverType="platform", lane=lane, search_type=search_type, search_id=search_id, from_date=from_date, to_date=to_date, dp_ids=dp_ids, ordering_company_id=ordering_company_id, stores=stores, sales_channel=sales_channel, request_by_ext=request_by_ext, page_no=page_no, page_size=page_size, customer_id=customer_id, is_priority_sort=is_priority_sort, exclude_locked_shipments=exclude_locked_shipments)
        query_string = await create_query_string(lane=lane, search_type=search_type, search_id=search_id, from_date=from_date, to_date=to_date, dp_ids=dp_ids, ordering_company_id=ordering_company_id, stores=stores, sales_channel=sales_channel, request_by_ext=request_by_ext, page_no=page_no, page_size=page_size, customer_id=customer_id, is_priority_sort=is_priority_sort, exclude_locked_shipments=exclude_locked_shipments)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/shipments/", lane=lane, search_type=search_type, search_id=search_id, from_date=from_date, to_date=to_date, dp_ids=dp_ids, ordering_company_id=ordering_company_id, stores=stores, sales_channel=sales_channel, request_by_ext=request_by_ext, page_no=page_no, page_size=page_size, customer_id=customer_id, is_priority_sort=is_priority_sort, exclude_locked_shipments=exclude_locked_shipments), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ShipmentInternalPlatformViewResponse
            schema = ShipmentInternalPlatformViewResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getApplicationShipments")
                print(e)

        return response
    
    async def trackShipmentPlatform(self, shipment_id=None, request_headers:Dict={}):
        """Track shipment by shipment Id for an application
        :param shipment_id : Shipment Id : type string
        """
        payload = {}
        
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id

        # Parameter validation
        schema = OrderValidator.trackShipmentPlatform()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/shipments/{shipment_id}/track", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Id of application","required":true,"schema":{"type":"string"}},{"in":"path","name":"shipment_id","description":"Shipment Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"Id of application","required":true,"schema":{"type":"string"}},{"in":"path","name":"shipment_id","description":"Shipment Id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", shipment_id=shipment_id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/shipments/{shipment_id}/track", shipment_id=shipment_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PlatformShipmentTrack
            schema = PlatformShipmentTrack()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for trackShipmentPlatform")
                print(e)

        return response
    
    async def getPlatformShipmentReasons(self, action=None, request_headers:Dict={}):
        """Get reasons to perform full or partial cancellation of a shipment
        :param action :  : type string
        """
        payload = {}
        
        if action is not None:
            payload["action"] = action

        # Parameter validation
        schema = OrderValidator.getPlatformShipmentReasons()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/shipments/reasons/{action}", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"action","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"action","required":true,"schema":{"type":"string"}}]}""", serverType="platform", action=action)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/shipments/reasons/{action}", action=action), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ShipmentReasonsResponse
            schema = ShipmentReasonsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPlatformShipmentReasons")
                print(e)

        return response
    