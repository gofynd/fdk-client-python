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

    
    async def getQuestions(self, page_no=None, page_size=None, q=None, is_active=None, request_headers:Dict={}):
        """Get all questions of that cluster
        :param page_no :  : type integer
        :param page_size :  : type integer
        :param q : To search questions using query : type string
        :param is_active : To get active questions : type boolean
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if q is not None:
            payload["q"] = q
        if is_active is not None:
            payload["is_active"] = is_active

        # Parameter validation
        schema = OrderValidator.getQuestions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/question", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"page_no","required":false,"schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer","default":10}},{"in":"query","name":"q","description":"To search questions using query","schema":{"type":"string","default":"None"}},{"in":"query","name":"is_active","description":"To get active questions","schema":{"type":"boolean","default":"None"}}],"query":[{"in":"query","name":"page_no","required":false,"schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer","default":10}},{"in":"query","name":"q","description":"To search questions using query","schema":{"type":"string","default":"None"}},{"in":"query","name":"is_active","description":"To get active questions","schema":{"type":"boolean","default":"None"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, q=q, is_active=is_active)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q, is_active=is_active)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/question", page_no=page_no, page_size=page_size, q=q, is_active=is_active), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def getRuleLaneConfig(self, search_value=None, request_headers:Dict={}):
        """Retrieve rule lane configurations
        :param search_value :  : type string
        """
        payload = {}
        
        if search_value is not None:
            payload["search_value"] = search_value

        # Parameter validation
        schema = OrderValidator.getRuleLaneConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/rule-lane-config", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"search_value","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"search_value","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", search_value=search_value)
        query_string = await create_query_string(search_value=search_value)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/rule-lane-config", search_value=search_value), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RuleLaneConfigResponse
            schema = RuleLaneConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getRuleLaneConfig")
                print(e)

        return response
    
    async def createRule(self, body="", request_headers:Dict={}):
        """Create a new rule
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.createRule()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import RuleRequest
        schema = RuleRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/rule", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/rule", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RuleSuccessResponse
            schema = RuleSuccessResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createRule")
                print(e)

        return response
    
    async def getRuleById(self, rule_id=None, request_headers:Dict={}):
        """Get a specific rule by ID
        :param rule_id :  : type string
        """
        payload = {}
        
        if rule_id is not None:
            payload["rule_id"] = rule_id

        # Parameter validation
        schema = OrderValidator.getRuleById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/rule/{rule_id}", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"rule_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"rule_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", rule_id=rule_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/rule/{rule_id}", rule_id=rule_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RuleResponse
            schema = RuleResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getRuleById")
                print(e)

        return response
    
    async def updateRule(self, rule_id=None, body="", request_headers:Dict={}):
        """Update a specific rule by ID
        :param rule_id :  : type string
        """
        payload = {}
        
        if rule_id is not None:
            payload["rule_id"] = rule_id

        # Parameter validation
        schema = OrderValidator.updateRule()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import RuleUpdateRequest
        schema = RuleUpdateRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/rule/{rule_id}", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"rule_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"rule_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", rule_id=rule_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/rule/{rule_id}", rule_id=rule_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RuleSuccessResponse
            schema = RuleSuccessResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateRule")
                print(e)

        return response
    
    async def deleteRule(self, rule_id=None, request_headers:Dict={}):
        """Delete a specific rule by ID
        :param rule_id :  : type string
        """
        payload = {}
        
        if rule_id is not None:
            payload["rule_id"] = rule_id

        # Parameter validation
        schema = OrderValidator.deleteRule()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/rule/{rule_id}", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"rule_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"rule_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", rule_id=rule_id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/rule/{rule_id}", rule_id=rule_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RuleSuccessResponse
            schema = RuleSuccessResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteRule")
                print(e)

        return response
    
    async def updateRulePosition(self, body="", request_headers:Dict={}):
        """Update the position of a rule
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.updateRulePosition()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateRulePositionRequest
        schema = UpdateRulePositionRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/rule-position", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/rule-position", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RuleListResponse
            schema = RuleListResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateRulePosition")
                print(e)

        return response
    
    async def getRuleParameters(self, request_headers:Dict={}):
        """Get available rule parameters
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.getRuleParameters()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/rule-parameters", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/rule-parameters", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RuleParametersResponse
            schema = RuleParametersResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getRuleParameters")
                print(e)

        return response
    
    async def getRuleList(self, body="", request_headers:Dict={}):
        """Get a list of rules
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.getRuleList()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import RuleListRequest
        schema = RuleListRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/rule_list", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/rule_list", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RuleListResponse
            schema = RuleListResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getRuleList")
                print(e)

        return response
    
    async def getShipmentBagReasons(self, shipment_id=None, line_number=None, bag_id=None, request_headers:Dict={}):
        """Use this API to retrieve the issues that led to the cancellation of bags within a shipment.
        :param shipment_id : ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        :param line_number : line number of bag. : type integer
        :param bag_id : The ID of the bag. : type string
        """
        payload = {}
        
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id
        if line_number is not None:
            payload["line_number"] = line_number
        if bag_id is not None:
            payload["bag_id"] = bag_id

        # Parameter validation
        schema = OrderValidator.getShipmentBagReasons()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/shipments/{shipment_id}/line_number/{line_number}/reasons", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}},{"in":"path","name":"application_id","description":"Application ID of company","required":true,"schema":{"type":"string"}},{"in":"path","description":"ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"shipment_id","required":true,"schema":{"type":"string"}},{"in":"path","description":"line number of bag.","name":"line_number","required":true,"schema":{"type":"integer"}},{"name":"bag_id","in":"query","description":"The ID of the bag.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"bag_id","in":"query","description":"The ID of the bag.","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}},{"in":"path","name":"application_id","description":"Application ID of company","required":true,"schema":{"type":"string"}},{"in":"path","description":"ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"shipment_id","required":true,"schema":{"type":"string"}},{"in":"path","description":"line number of bag.","name":"line_number","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", shipment_id=shipment_id, line_number=line_number, bag_id=bag_id)
        query_string = await create_query_string(bag_id=bag_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/shipments/{shipment_id}/line_number/{line_number}/reasons", shipment_id=shipment_id, line_number=line_number, bag_id=bag_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ShipmentBagReasons
            schema = ShipmentBagReasons()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getShipmentBagReasons")
                print(e)

        return response
    
    async def getApplicationShipments(self, lane=None, search_type=None, search_id=None, search_value=None, from_date=None, to_date=None, dp_ids=None, ordering_company_id=None, stores=None, sales_channel=None, request_by_ext=None, page_no=None, page_size=None, customer_id=None, is_priority_sort=None, exclude_locked_shipments=None, request_headers:Dict={}):
        """Get cross selling platform shipments
        :param lane :  : type string
        :param search_type :  : type string
        :param search_id :  : type string
        :param search_value :  : type string
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
        if search_value is not None:
            payload["search_value"] = search_value
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/shipments", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string"}}],"optional":[{"name":"lane","in":"query","required":false,"schema":{"type":"string"}},{"name":"search_type","in":"query","required":false,"schema":{"type":"string"}},{"name":"search_id","in":"query","required":false,"schema":{"type":"string"}},{"name":"search_value","in":"query","required":false,"schema":{"type":"string"}},{"name":"from_date","in":"query","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","required":false,"schema":{"type":"string"}},{"name":"dp_ids","in":"query","required":false,"schema":{"type":"string"}},{"name":"ordering_company_id","in":"query","required":false,"schema":{"type":"string"}},{"name":"stores","in":"query","required":false,"schema":{"type":"string"}},{"name":"sales_channel","in":"query","required":false,"schema":{"type":"string"}},{"name":"request_by_ext","in":"query","required":false,"schema":{"type":"string"}},{"name":"page_no","in":"query","required":false,"schema":{"type":"integer"}},{"name":"page_size","in":"query","required":false,"schema":{"type":"integer"}},{"name":"customer_id","in":"query","required":false,"schema":{"type":"string"}},{"name":"is_priority_sort","in":"query","required":false,"schema":{"type":"boolean"}},{"name":"exclude_locked_shipments","in":"query","required":false,"schema":{"type":"boolean"}}],"query":[{"name":"lane","in":"query","required":false,"schema":{"type":"string"}},{"name":"search_type","in":"query","required":false,"schema":{"type":"string"}},{"name":"search_id","in":"query","required":false,"schema":{"type":"string"}},{"name":"search_value","in":"query","required":false,"schema":{"type":"string"}},{"name":"from_date","in":"query","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","required":false,"schema":{"type":"string"}},{"name":"dp_ids","in":"query","required":false,"schema":{"type":"string"}},{"name":"ordering_company_id","in":"query","required":false,"schema":{"type":"string"}},{"name":"stores","in":"query","required":false,"schema":{"type":"string"}},{"name":"sales_channel","in":"query","required":false,"schema":{"type":"string"}},{"name":"request_by_ext","in":"query","required":false,"schema":{"type":"string"}},{"name":"page_no","in":"query","required":false,"schema":{"type":"integer"}},{"name":"page_size","in":"query","required":false,"schema":{"type":"integer"}},{"name":"customer_id","in":"query","required":false,"schema":{"type":"string"}},{"name":"is_priority_sort","in":"query","required":false,"schema":{"type":"boolean"}},{"name":"exclude_locked_shipments","in":"query","required":false,"schema":{"type":"boolean"}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"}},{"name":"application_id","in":"path","required":true,"schema":{"type":"string"}}]}""", serverType="platform", lane=lane, search_type=search_type, search_id=search_id, search_value=search_value, from_date=from_date, to_date=to_date, dp_ids=dp_ids, ordering_company_id=ordering_company_id, stores=stores, sales_channel=sales_channel, request_by_ext=request_by_ext, page_no=page_no, page_size=page_size, customer_id=customer_id, is_priority_sort=is_priority_sort, exclude_locked_shipments=exclude_locked_shipments)
        query_string = await create_query_string(lane=lane, search_type=search_type, search_id=search_id, search_value=search_value, from_date=from_date, to_date=to_date, dp_ids=dp_ids, ordering_company_id=ordering_company_id, stores=stores, sales_channel=sales_channel, request_by_ext=request_by_ext, page_no=page_no, page_size=page_size, customer_id=customer_id, is_priority_sort=is_priority_sort, exclude_locked_shipments=exclude_locked_shipments)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/shipments", lane=lane, search_type=search_type, search_id=search_id, search_value=search_value, from_date=from_date, to_date=to_date, dp_ids=dp_ids, ordering_company_id=ordering_company_id, stores=stores, sales_channel=sales_channel, request_by_ext=request_by_ext, page_no=page_no, page_size=page_size, customer_id=customer_id, is_priority_sort=is_priority_sort, exclude_locked_shipments=exclude_locked_shipments), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

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
        """Track Shipment by shipment id, for application based on application Id
        :param shipment_id : Shipment Id : type string
        """
        payload = {}
        
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id

        # Parameter validation
        schema = OrderValidator.trackShipmentPlatform()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/shipments/{shipment_id}/track", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}},{"in":"path","name":"application_id","description":"Id of application","required":true,"schema":{"type":"string"}},{"in":"path","name":"shipment_id","description":"Shipment Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}},{"in":"path","name":"application_id","description":"Id of application","required":true,"schema":{"type":"string"}},{"in":"path","name":"shipment_id","description":"Shipment Id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", shipment_id=shipment_id)
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
        """Using action, get reasons behind full or partial cancellation of a shipment
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
    