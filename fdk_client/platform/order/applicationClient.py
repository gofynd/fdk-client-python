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

    
    async def failedOrderLogs(self, page_no=None, page_size=None, search_type=None, search_value=None, request_headers:Dict={}):
        """Get failed order logs listing for filters based on order Id, user contact number, user email Id and sales channel Id.
        :param page_no : Page Number : type integer
        :param page_size : Page Size : type integer
        :param search_type : Search type for filter : type string
        :param search_value : Search value for filter : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if search_type is not None:
            payload["search_type"] = search_type
        if search_value is not None:
            payload["search_value"] = search_value

        # Parameter validation
        schema = OrderValidator.failedOrderLogs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/orders/failed", """{"required":[{"in":"path","name":"company_id","description":"Company ID","required":true,"schema":{"type":"integer","example":2}}],"optional":[{"in":"query","name":"application_id","description":"Application ID","required":false,"schema":{"type":"string","example":"64aed475db2cfb5b8a9f623d"}},{"in":"query","name":"page_no","required":false,"description":"Page Number","schema":{"type":"integer","example":1}},{"in":"query","name":"page_size","required":false,"description":"Page Size","schema":{"type":"integer","example":10}},{"in":"query","name":"search_type","required":false,"description":"Search type for filter","schema":{"type":"string","example":"email_id","x-not-enum":true}},{"in":"query","name":"search_value","required":false,"description":"Search value for filter","schema":{"type":"string","example":"employee@gofynd.com"}}],"query":[{"in":"query","name":"application_id","description":"Application ID","required":false,"schema":{"type":"string","example":"64aed475db2cfb5b8a9f623d"}},{"in":"query","name":"page_no","required":false,"description":"Page Number","schema":{"type":"integer","example":1}},{"in":"query","name":"page_size","required":false,"description":"Page Size","schema":{"type":"integer","example":10}},{"in":"query","name":"search_type","required":false,"description":"Search type for filter","schema":{"type":"string","example":"email_id","x-not-enum":true}},{"in":"query","name":"search_value","required":false,"description":"Search value for filter","schema":{"type":"string","example":"employee@gofynd.com"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company ID","required":true,"schema":{"type":"integer","example":2}}]}""", serverType="platform", page_no=page_no, page_size=page_size, search_type=search_type, search_value=search_value)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, search_type=search_type, search_value=search_value)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/orders/failed", page_no=page_no, page_size=page_size, search_type=search_type, search_value=search_value), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import FailedOrderLogs
            schema = FailedOrderLogs()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for failedOrderLogs")
                print(e)

        return response
    
    async def getRules(self, body="", request_headers:Dict={}):
        """Retrieves a comprehensive list of RMA (Return Merchandise Authorization) rules associated with  a specific company and application. These rules dictate the processes for handling returns,  including actions, reasons, quality control (QC) types, and associated questions.  The endpoint allows for filtering and pagination based on input conditions, providing a tailored set of rules that match the criteria specified.
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.getRules()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import RuleListRequestSchema
        schema = RuleListRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/rule_list", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/rule_list", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RuleListResponseSchema
            schema = RuleListResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getRules")
                print(e)

        return response
    
    async def getShipmentBagReasons(self, shipment_id=None, line_number=None, request_headers:Dict={}):
        """Allows users to retrieve a comprehensive list of reasons for cancellation  or returning a shipment. It provides both cancellation and return reasons, with an emphasis  on Quality Control (QC) evaluations.
        :param shipment_id : The unique identifier for the shipment : type string
        :param line_number : A unique identifier of the bag's line number. : type integer
        """
        payload = {}
        
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id
        if line_number is not None:
            payload["line_number"] = line_number

        # Parameter validation
        schema = OrderValidator.getShipmentBagReasons()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/shipments/{shipment_id}/line_number/{line_number}/reasons", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of a company on the platform.","required":true,"schema":{"type":"integer"}},{"in":"path","name":"application_id","description":"A unique identifier for the application on the platform","required":true,"schema":{"type":"string"}},{"in":"path","description":"The unique identifier for the shipment","name":"shipment_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"line_number","description":"A unique identifier of the bag's line number.","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of a company on the platform.","required":true,"schema":{"type":"integer"}},{"in":"path","name":"application_id","description":"A unique identifier for the application on the platform","required":true,"schema":{"type":"string"}},{"in":"path","description":"The unique identifier for the shipment","name":"shipment_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"line_number","description":"A unique identifier of the bag's line number.","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", shipment_id=shipment_id, line_number=line_number)
        query_string = await create_query_string()

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
        :param lane : Optional parameter to specify the lane for filtering results. : type string
        :param search_type : search_type refers to the field that will be used as the target for the search operation : type string
        :param search_id : Identifier used for the search operation based on the selected search type. : type string
        :param from_date : Date time in UTC timezone as per ISO format. : type string
        :param to_date : Date time in UTC timezone as per ISO format. : type string
        :param dp_ids : Comma-separated list of delivery partner IDs to filter results. : type string
        :param ordering_company_id : ID of the company placing the order, used for filtering results. : type string
        :param stores : Comma-separated list of store IDs to filter results. : type string
        :param sales_channel : The sales channel to filter results. : type string
        :param request_by_ext : Identifier for external requests. : type string
        :param page_no : The page number for pagination of results. : type integer
        :param page_size : The number of results to return per page for pagination. : type integer
        :param customer_id : ID of the customer to filter results related to specific customer. : type string
        :param is_priority_sort : Flag to determine if results should be sorted by priority. Defaults to true. : type boolean
        :param exclude_locked_shipments : Flag to exclude shipments that are currently locked from the results. : type boolean
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/shipments/", """{"required":[{"name":"company_id","in":"path","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}},{"name":"application_id","in":"path","required":true,"description":"A unique identifier for the application or system that is making the order request.","schema":{"type":"string"}}],"optional":[{"name":"lane","in":"query","required":false,"description":"Optional parameter to specify the lane for filtering results.","schema":{"type":"string"}},{"name":"search_type","in":"query","description":"search_type refers to the field that will be used as the target for the search operation","required":false,"schema":{"type":"string","enum":["shipment_id","order_id","channel_name","fynd_order_id"]}},{"name":"search_id","in":"query","required":false,"description":"Identifier used for the search operation based on the selected search type.","schema":{"type":"string"}},{"name":"from_date","in":"query","description":"Date time in UTC timezone as per ISO format.","required":false,"schema":{"type":"string","format":"date"}},{"name":"to_date","in":"query","description":"Date time in UTC timezone as per ISO format.","required":false,"schema":{"type":"string","format":"date"}},{"name":"dp_ids","in":"query","required":false,"description":"Comma-separated list of delivery partner IDs to filter results.","schema":{"type":"string"}},{"name":"ordering_company_id","in":"query","required":false,"description":"ID of the company placing the order, used for filtering results.","schema":{"type":"string"}},{"name":"stores","in":"query","required":false,"description":"Comma-separated list of store IDs to filter results.","schema":{"type":"string"}},{"name":"sales_channel","in":"query","required":false,"description":"The sales channel to filter results.","schema":{"type":"string"}},{"name":"request_by_ext","in":"query","description":"Identifier for external requests.","required":false,"schema":{"type":"string"}},{"name":"page_no","in":"query","required":false,"description":"The page number for pagination of results.","schema":{"type":"integer"}},{"name":"page_size","in":"query","required":false,"description":"The number of results to return per page for pagination.","schema":{"type":"integer"}},{"name":"customer_id","in":"query","required":false,"description":"ID of the customer to filter results related to specific customer.","schema":{"type":"string"}},{"name":"is_priority_sort","in":"query","required":false,"description":"Flag to determine if results should be sorted by priority. Defaults to true.","schema":{"type":"boolean","default":true}},{"name":"exclude_locked_shipments","in":"query","required":false,"description":"Flag to exclude shipments that are currently locked from the results.","schema":{"type":"boolean","default":true}}],"query":[{"name":"lane","in":"query","required":false,"description":"Optional parameter to specify the lane for filtering results.","schema":{"type":"string"}},{"name":"search_type","in":"query","description":"search_type refers to the field that will be used as the target for the search operation","required":false,"schema":{"type":"string","enum":["shipment_id","order_id","channel_name","fynd_order_id"]}},{"name":"search_id","in":"query","required":false,"description":"Identifier used for the search operation based on the selected search type.","schema":{"type":"string"}},{"name":"from_date","in":"query","description":"Date time in UTC timezone as per ISO format.","required":false,"schema":{"type":"string","format":"date"}},{"name":"to_date","in":"query","description":"Date time in UTC timezone as per ISO format.","required":false,"schema":{"type":"string","format":"date"}},{"name":"dp_ids","in":"query","required":false,"description":"Comma-separated list of delivery partner IDs to filter results.","schema":{"type":"string"}},{"name":"ordering_company_id","in":"query","required":false,"description":"ID of the company placing the order, used for filtering results.","schema":{"type":"string"}},{"name":"stores","in":"query","required":false,"description":"Comma-separated list of store IDs to filter results.","schema":{"type":"string"}},{"name":"sales_channel","in":"query","required":false,"description":"The sales channel to filter results.","schema":{"type":"string"}},{"name":"request_by_ext","in":"query","description":"Identifier for external requests.","required":false,"schema":{"type":"string"}},{"name":"page_no","in":"query","required":false,"description":"The page number for pagination of results.","schema":{"type":"integer"}},{"name":"page_size","in":"query","required":false,"description":"The number of results to return per page for pagination.","schema":{"type":"integer"}},{"name":"customer_id","in":"query","required":false,"description":"ID of the customer to filter results related to specific customer.","schema":{"type":"string"}},{"name":"is_priority_sort","in":"query","required":false,"description":"Flag to determine if results should be sorted by priority. Defaults to true.","schema":{"type":"boolean","default":true}},{"name":"exclude_locked_shipments","in":"query","required":false,"description":"Flag to exclude shipments that are currently locked from the results.","schema":{"type":"boolean","default":true}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}},{"name":"application_id","in":"path","required":true,"description":"A unique identifier for the application or system that is making the order request.","schema":{"type":"string"}}]}""", serverType="platform", lane=lane, search_type=search_type, search_id=search_id, from_date=from_date, to_date=to_date, dp_ids=dp_ids, ordering_company_id=ordering_company_id, stores=stores, sales_channel=sales_channel, request_by_ext=request_by_ext, page_no=page_no, page_size=page_size, customer_id=customer_id, is_priority_sort=is_priority_sort, exclude_locked_shipments=exclude_locked_shipments)
        query_string = await create_query_string(lane=lane, search_type=search_type, search_id=search_id, from_date=from_date, to_date=to_date, dp_ids=dp_ids, ordering_company_id=ordering_company_id, stores=stores, sales_channel=sales_channel, request_by_ext=request_by_ext, page_no=page_no, page_size=page_size, customer_id=customer_id, is_priority_sort=is_priority_sort, exclude_locked_shipments=exclude_locked_shipments)

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
            from .models import ShipmentInternalPlatformViewResponseSchema
            schema = ShipmentInternalPlatformViewResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getApplicationShipments")
                print(e)

        return response
    
    async def trackShipmentPlatform(self, shipment_id=None, request_headers:Dict={}):
        """Track shipment by shipment Id for an application
        :param shipment_id : The unique identifier for the shipment : type string
        """
        payload = {}
        
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id

        # Parameter validation
        schema = OrderValidator.trackShipmentPlatform()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/shipments/{shipment_id}/track", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of a company on the platform.","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"A unique identifier for the application on the platform","required":true,"schema":{"type":"string"}},{"in":"path","name":"shipment_id","description":"The unique identifier for the shipment","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of a company on the platform.","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","description":"A unique identifier for the application on the platform","required":true,"schema":{"type":"string"}},{"in":"path","name":"shipment_id","description":"The unique identifier for the shipment","required":true,"schema":{"type":"string"}}]}""", serverType="platform", shipment_id=shipment_id)
        query_string = await create_query_string()

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
            from .models import ShipmentReasonsResponseSchema
            schema = ShipmentReasonsResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPlatformShipmentReasons")
                print(e)

        return response
    