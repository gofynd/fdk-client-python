"""Order Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .validator import OrderValidator

class Order:
    def __init__(self, config: PlatformConfig):
        self._conf = config

    
    async def invalidateShipmentCache(self, body="", request_headers:Dict={}):
        """Clear the existing shipment cache data stored in Redis  and serialize the updated data for subsequent use.
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.invalidateShipmentCache()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import InvalidateShipmentCachePayload
        schema = InvalidateShipmentCachePayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/update-cache", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/update-cache", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import InvalidateShipmentCacheResponse
            schema = InvalidateShipmentCacheResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for invalidateShipmentCache")
                print(e)

        return response
    
    async def postRefundStateConfiguration(self, app_id=None, body="", request_headers:Dict={}):
        """Refund State Configuration
        :param app_id :  : type string
        """
        payload = {}
        
        if app_id is not None:
            payload["app_id"] = app_id

        # Parameter validation
        schema = OrderValidator.postRefundStateConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PostRefundStateConfiguration
        schema = PostRefundStateConfiguration()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/refund/states/config", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"query","name":"app_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"in":"query","name":"app_id","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", app_id=app_id)
        query_string = await create_query_string(app_id=app_id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/refund/states/config", app_id=app_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PostRefundStateConfigurationResponse
            schema = PostRefundStateConfigurationResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for postRefundStateConfiguration")
                print(e)

        return response
    
    async def getRefundStateConfiguration(self, app_id=None, request_headers:Dict={}):
        """Refund State Configuration
        :param app_id :  : type string
        """
        payload = {}
        
        if app_id is not None:
            payload["app_id"] = app_id

        # Parameter validation
        schema = OrderValidator.getRefundStateConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/refund/states/config", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"query","name":"app_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"in":"query","name":"app_id","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", app_id=app_id)
        query_string = await create_query_string(app_id=app_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/refund/states/config", app_id=app_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetRefundStateConfigurationResponse
            schema = GetRefundStateConfigurationResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getRefundStateConfiguration")
                print(e)

        return response
    
    async def getRefundEnableStateList(self, request_headers:Dict={}):
        """refund configuration.
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.getRefundEnableStateList()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/refund/states", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/refund/states", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetRefundStates
            schema = GetRefundStates()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getRefundEnableStateList")
                print(e)

        return response
    
    async def postRefundConfiguration(self, app_id=None, body="", request_headers:Dict={}):
        """refund configuration.
        :param app_id :  : type string
        """
        payload = {}
        
        if app_id is not None:
            payload["app_id"] = app_id

        # Parameter validation
        schema = OrderValidator.postRefundConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import RefundStateConfigurationManualSchema
        schema = RefundStateConfigurationManualSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/refund/config", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"query","name":"app_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"in":"query","name":"app_id","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", app_id=app_id)
        query_string = await create_query_string(app_id=app_id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/refund/config", app_id=app_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RefundStateConfigurationManualSchemaResponse
            schema = RefundStateConfigurationManualSchemaResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for postRefundConfiguration")
                print(e)

        return response
    
    async def getRefundConfiguration(self, app_id=None, request_headers:Dict={}):
        """refund configuration.
        :param app_id :  : type string
        """
        payload = {}
        
        if app_id is not None:
            payload["app_id"] = app_id

        # Parameter validation
        schema = OrderValidator.getRefundConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/refund/config", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"query","name":"app_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"in":"query","name":"app_id","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", app_id=app_id)
        query_string = await create_query_string(app_id=app_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/refund/config", app_id=app_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RefundStateConfigurationManualSchemaResponse
            schema = RefundStateConfigurationManualSchemaResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getRefundConfiguration")
                print(e)

        return response
    
    async def reassignLocation(self, body="", request_headers:Dict={}):
        """Change the assigned location for an order or shipment.
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.reassignLocation()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import StoreReassign
        schema = StoreReassign()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/store/reassign-internal", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/store/reassign-internal", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import StoreReassignResponse
            schema = StoreReassignResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for reassignLocation")
                print(e)

        return response
    
    async def getRefundOptions(self, shipment_id=None, bag_ids=None, state=None, optin_app_id=None, optin_company_id=None, status=None, request_headers:Dict={}):
        """This API can be used for giving the refund amount with available option of MOPs.
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        :param bag_ids : It is the bag_id of the bags with comma separated. : type string
        :param state : It is the desired state at which refund amount needs to be calculated. : type string
        :param optin_app_id : It is affiliate id of the order in case of cross selling. : type string
        :param optin_company_id : It is company id of the order in case of cross selling. : type integer
        :param status : It specifies the desired status to which the shipment should be updated. It represents the next step in the shipment's lifecycle,  such as being cancelled by the customer or moved to another status in the shipping process. : type string
        """
        payload = {}
        
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id
        if bag_ids is not None:
            payload["bag_ids"] = bag_ids
        if state is not None:
            payload["state"] = state
        if optin_app_id is not None:
            payload["optin_app_id"] = optin_app_id
        if optin_company_id is not None:
            payload["optin_company_id"] = optin_company_id
        if status is not None:
            payload["status"] = status

        # Parameter validation
        schema = OrderValidator.getRefundOptions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/shipment/{shipment_id}/refund-options", """{"required":[{"in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"shipment_id","required":true,"schema":{"type":"string"}},{"in":"path","description":"This is the company_id for the sales channel.","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","description":"It is the bag_id of the bags with comma separated.","name":"bag_ids","required":false,"schema":{"type":"string"}},{"in":"query","description":"It is the desired state at which refund amount needs to be calculated.","name":"state","required":false,"schema":{"type":"string"}},{"in":"query","description":"It is affiliate id of the order in case of cross selling.","name":"optin_app_id","required":false,"schema":{"type":"string"}},{"in":"query","description":"It is company id of the order in case of cross selling.","name":"optin_company_id","required":false,"schema":{"type":"integer"}},{"in":"query","description":"It specifies the desired status to which the shipment should be updated. It represents the next step in the shipment's lifecycle,  such as being cancelled by the customer or moved to another status in the shipping process.","name":"status","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","description":"It is the bag_id of the bags with comma separated.","name":"bag_ids","required":false,"schema":{"type":"string"}},{"in":"query","description":"It is the desired state at which refund amount needs to be calculated.","name":"state","required":false,"schema":{"type":"string"}},{"in":"query","description":"It is affiliate id of the order in case of cross selling.","name":"optin_app_id","required":false,"schema":{"type":"string"}},{"in":"query","description":"It is company id of the order in case of cross selling.","name":"optin_company_id","required":false,"schema":{"type":"integer"}},{"in":"query","description":"It specifies the desired status to which the shipment should be updated. It represents the next step in the shipment's lifecycle,  such as being cancelled by the customer or moved to another status in the shipping process.","name":"status","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"shipment_id","required":true,"schema":{"type":"string"}},{"in":"path","description":"This is the company_id for the sales channel.","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", shipment_id=shipment_id, bag_ids=bag_ids, state=state, optin_app_id=optin_app_id, optin_company_id=optin_company_id, status=status)
        query_string = await create_query_string(bag_ids=bag_ids, state=state, optin_app_id=optin_app_id, optin_company_id=optin_company_id, status=status)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/shipment/{shipment_id}/refund-options", shipment_id=shipment_id, bag_ids=bag_ids, state=state, optin_app_id=optin_app_id, optin_company_id=optin_company_id, status=status), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RefundOptionsSchemaResponse
            schema = RefundOptionsSchemaResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getRefundOptions")
                print(e)

        return response
    
    async def getAnnouncements(self, date=None, request_headers:Dict={}):
        """Retrieve announcements related to orders fulfilment configured by platform or company admin
        :param date : Date On which the announcement is Active (Date should in ISO Datetime format IST Time) : type string
        """
        payload = {}
        
        if date is not None:
            payload["date"] = date

        # Parameter validation
        schema = OrderValidator.getAnnouncements()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/announcements", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"date","required":false,"description":"Date On which the announcement is Active (Date should in ISO Datetime format IST Time)","schema":{"type":"string"}}],"query":[{"in":"query","name":"date","required":false,"description":"Date On which the announcement is Active (Date should in ISO Datetime format IST Time)","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", date=date)
        query_string = await create_query_string(date=date)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/announcements", date=date), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AnnouncementsResponse
            schema = AnnouncementsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAnnouncements")
                print(e)

        return response
    
    async def click2Call(self, caller=None, receiver=None, bag_id=None, caller_id=None, method=None, request_headers:Dict={}):
        """Click to call. 
        :param caller : Call Number : type string
        :param receiver : Receiver Number : type string
        :param bag_id : Bag Id for the query : type string
        :param caller_id : Caller Id : type string
        :param method : Provider Method to Call : type string
        """
        payload = {}
        
        if caller is not None:
            payload["caller"] = caller
        if receiver is not None:
            payload["receiver"] = receiver
        if bag_id is not None:
            payload["bag_id"] = bag_id
        if caller_id is not None:
            payload["caller_id"] = caller_id
        if method is not None:
            payload["method"] = method

        # Parameter validation
        schema = OrderValidator.click2Call()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/ninja/click2call", """{"required":[{"in":"query","name":"caller","required":true,"description":"Call Number","schema":{"type":"string"}},{"in":"query","name":"receiver","required":true,"description":"Receiver Number","schema":{"type":"string"}},{"in":"query","name":"bag_id","required":true,"description":"Bag Id for the query","schema":{"type":"string"}},{"in":"path","name":"company_id","required":true,"description":"Company Id","schema":{"type":"integer"}}],"optional":[{"in":"query","name":"caller_id","required":false,"description":"Caller Id","schema":{"type":"string"}},{"in":"query","name":"method","required":false,"description":"Provider Method to Call","schema":{"type":"string","example":"dial.click2call"}}],"query":[{"in":"query","name":"caller","required":true,"description":"Call Number","schema":{"type":"string"}},{"in":"query","name":"receiver","required":true,"description":"Receiver Number","schema":{"type":"string"}},{"in":"query","name":"bag_id","required":true,"description":"Bag Id for the query","schema":{"type":"string"}},{"in":"query","name":"caller_id","required":false,"description":"Caller Id","schema":{"type":"string"}},{"in":"query","name":"method","required":false,"description":"Provider Method to Call","schema":{"type":"string","example":"dial.click2call"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Company Id","schema":{"type":"integer"}}]}""", serverType="platform", caller=caller, receiver=receiver, bag_id=bag_id, caller_id=caller_id, method=method, )
        query_string = await create_query_string(caller=caller, receiver=receiver, bag_id=bag_id, caller_id=caller_id, method=method, )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/ninja/click2call", caller=caller, receiver=receiver, bag_id=bag_id, caller_id=caller_id, method=method), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Click2CallResponse
            schema = Click2CallResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for click2Call")
                print(e)

        return response
    
    async def updateShipmentStatus(self, body="", request_headers:Dict={}):
        """Shipment state transition or Shipment data update or both.
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.updateShipmentStatus()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateShipmentStatusRequest
        schema = UpdateShipmentStatusRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/shipment/status-internal", """{"required":[{"in":"path","name":"company_id","description":"company id from where are transitioning the shipment state or data","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"company id from where are transitioning the shipment state or data","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/shipment/status-internal", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdateShipmentStatusResponseBody
            schema = UpdateShipmentStatusResponseBody()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateShipmentStatus")
                print(e)

        return response
    
    async def getShipmentHistory(self, shipment_id=None, bag_id=None, request_headers:Dict={}):
        """Retrieve the shipment history.
        :param shipment_id : Shipment Id : type string
        :param bag_id : Bag/Product Id : type integer
        """
        payload = {}
        
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id
        if bag_id is not None:
            payload["bag_id"] = bag_id

        # Parameter validation
        schema = OrderValidator.getShipmentHistory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/shipment/history", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Company Id","schema":{"type":"integer"}}],"optional":[{"in":"query","name":"shipment_id","description":"Shipment Id","required":false,"schema":{"type":"string"}},{"in":"query","name":"bag_id","description":"Bag/Product Id","required":false,"schema":{"type":"integer"}}],"query":[{"in":"query","name":"shipment_id","description":"Shipment Id","required":false,"schema":{"type":"string"}},{"in":"query","name":"bag_id","description":"Bag/Product Id","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Company Id","schema":{"type":"integer"}}]}""", serverType="platform", shipment_id=shipment_id, bag_id=bag_id)
        query_string = await create_query_string(shipment_id=shipment_id, bag_id=bag_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/shipment/history", shipment_id=shipment_id, bag_id=bag_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ShipmentHistoryResponse
            schema = ShipmentHistoryResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getShipmentHistory")
                print(e)

        return response
    
    async def postShipmentHistory(self, body="", request_headers:Dict={}):
        """Add history records for a shipment.
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.postShipmentHistory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PostShipmentHistory
        schema = PostShipmentHistory()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/shipment/history", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/shipment/history", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ShipmentHistoryResponse
            schema = ShipmentHistoryResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for postShipmentHistory")
                print(e)

        return response
    
    async def sendSmsNinja(self, body="", request_headers:Dict={}):
        """Send SMS to customer based on the template that is selected
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.sendSmsNinja()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SendSmsPayload
        schema = SendSmsPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/ninja/send-sms", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Company Id","schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Company Id","schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/ninja/send-sms", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SendSmsResponse
            schema = SendSmsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for sendSmsNinja")
                print(e)

        return response
    
    async def updatePackagingDimensions(self, body="", request_headers:Dict={}):
        """Modify the dimensions of packaging.
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.updatePackagingDimensions()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdatePackagingDimensionsPayload
        schema = UpdatePackagingDimensionsPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/update-packaging-dimension", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/update-packaging-dimension", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdatePackagingDimensionsResponse
            schema = UpdatePackagingDimensionsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePackagingDimensions")
                print(e)

        return response
    
    async def orderUpdate(self, body="", request_headers:Dict={}):
        """Used to update an order's meta information. These meta information can be accessed via order or shipment details API.
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.orderUpdate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PlatformOrderUpdate
        schema = PlatformOrderUpdate()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/order/validation", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/order/validation", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ResponseDetail
            schema = ResponseDetail()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for orderUpdate")
                print(e)

        return response
    
    async def getStateTransitionMap(self, request_headers:Dict={}):
        """Retrieve a map of state transitions for orders
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.getStateTransitionMap()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/bag/state/transition", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/bag/state/transition", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BagStateTransitionMap
            schema = BagStateTransitionMap()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getStateTransitionMap")
                print(e)

        return response
    
    async def getAllowedStateTransition(self, ordering_channel=None, status=None, request_headers:Dict={}):
        """Retrieve next possible states based on logged in user.
        :param ordering_channel : Ordering channel : type string
        :param status : current status of a shipment : type string
        """
        payload = {}
        
        if ordering_channel is not None:
            payload["ordering_channel"] = ordering_channel
        if status is not None:
            payload["status"] = status

        # Parameter validation
        schema = OrderValidator.getAllowedStateTransition()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/allowed/state/transition", """{"required":[{"in":"path","name":"company_id","description":"Company ID","required":true,"schema":{"type":"integer"}},{"in":"query","name":"ordering_channel","description":"Ordering channel","required":true,"schema":{"type":"string"}},{"in":"query","name":"status","description":"current status of a shipment","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"in":"query","name":"ordering_channel","description":"Ordering channel","required":true,"schema":{"type":"string"}},{"in":"query","name":"status","description":"current status of a shipment","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company ID","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", ordering_channel=ordering_channel, status=status)
        query_string = await create_query_string(ordering_channel=ordering_channel, status=status)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/allowed/state/transition", ordering_channel=ordering_channel, status=status), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RoleBaseStateTransitionMapping
            schema = RoleBaseStateTransitionMapping()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAllowedStateTransition")
                print(e)

        return response
    
    async def fetchCreditBalanceDetail(self, body="", request_headers:Dict={}):
        """Retrieve details about credit balance on the basis of customer mobile number
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.fetchCreditBalanceDetail()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import FetchCreditBalanceRequestPayload
        schema = FetchCreditBalanceRequestPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/customer-credit-balance", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/customer-credit-balance", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import FetchCreditBalanceResponsePayload
            schema = FetchCreditBalanceResponsePayload()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for fetchCreditBalanceDetail")
                print(e)

        return response
    
    async def fetchRefundModeConfig(self, body="", request_headers:Dict={}):
        """Get list of refund modes to trigger refunds
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.fetchRefundModeConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import RefundModeConfigRequestPayload
        schema = RefundModeConfigRequestPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/refund-mode-config", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/refund-mode-config", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RefundModeConfigResponsePayload
            schema = RefundModeConfigResponsePayload()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for fetchRefundModeConfig")
                print(e)

        return response
    
    async def attachOrderUser(self, body="", request_headers:Dict={}):
        """Attach order User
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.attachOrderUser()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AttachOrderUser
        schema = AttachOrderUser()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/user/attach", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/user/attach", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AttachOrderUserResponse
            schema = AttachOrderUserResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for attachOrderUser")
                print(e)

        return response
    
    async def sendUserMobileOTP(self, body="", request_headers:Dict={}):
        """Send a one-time OTP to a users mobile device.
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.sendUserMobileOTP()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SendUserMobileOTP
        schema = SendUserMobileOTP()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/user/send/otp/mobile", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/user/send/otp/mobile", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SendUserMobileOtpResponse
            schema = SendUserMobileOtpResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for sendUserMobileOTP")
                print(e)

        return response
    
    async def verifyMobileOTP(self, body="", request_headers:Dict={}):
        """Verify Mobile OTP
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.verifyMobileOTP()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import VerifyMobileOTP
        schema = VerifyMobileOTP()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/user/verify/otp", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/user/verify/otp", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import VerifyOtpResponse
            schema = VerifyOtpResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for verifyMobileOTP")
                print(e)

        return response
    
    async def downloadLanesReport(self, body="", request_headers:Dict={}):
        """Downloads shipments/orders present in the provided lane
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.downloadLanesReport()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkReportsDownloadRequest
        schema = BulkReportsDownloadRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/reports/lanes/download", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/reports/lanes/download", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkReportsDownloadResponse
            schema = BulkReportsDownloadResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for downloadLanesReport")
                print(e)

        return response
    
    async def bulkStateTransistion(self, body="", request_headers:Dict={}):
        """Performs State Transisiton in Bulk for the given shipments in the excel/csv file url.
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.bulkStateTransistion()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkStateTransistionRequest
        schema = BulkStateTransistionRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/jobs/state-transition", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/jobs/state-transition", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkStateTransistionResponse
            schema = BulkStateTransistionResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for bulkStateTransistion")
                print(e)

        return response
    
    async def bulkListing(self, page_size=None, page_no=None, start_date=None, end_date=None, status=None, bulk_action_type=None, search_key=None, request_headers:Dict={}):
        """Fetches of previous or running  bulk jobs.

        :param page_size : page size : type integer
        :param page_no : page number : type integer
        :param start_date : UTC start date in ISO format : type string
        :param end_date : UTC end date in ISO format : type string
        :param status : status for which to fetch the jobs. : type string
        :param bulk_action_type : job type. : type string
        :param search_key : search_key. : type string
        """
        payload = {}
        
        if page_size is not None:
            payload["page_size"] = page_size
        if page_no is not None:
            payload["page_no"] = page_no
        if start_date is not None:
            payload["start_date"] = start_date
        if end_date is not None:
            payload["end_date"] = end_date
        if status is not None:
            payload["status"] = status
        if bulk_action_type is not None:
            payload["bulk_action_type"] = bulk_action_type
        if search_key is not None:
            payload["search_key"] = search_key

        # Parameter validation
        schema = OrderValidator.bulkListing()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/jobs", """{"required":[{"in":"path","name":"company_id","description":"Company ID","required":true,"schema":{"type":"integer"}},{"in":"query","name":"page_size","description":"page size","required":true,"schema":{"type":"integer"}},{"in":"query","name":"page_no","description":"page number","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"start_date","description":"UTC start date in ISO format","schema":{"type":"string","format":"date-time"}},{"in":"query","name":"end_date","description":"UTC end date in ISO format","schema":{"type":"string","format":"date-time"}},{"in":"query","name":"status","description":"status for which to fetch the jobs.","schema":{"type":"string"}},{"in":"query","name":"bulk_action_type","description":"job type.","schema":{"type":"string"}},{"in":"query","name":"search_key","description":"search_key.","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_size","description":"page size","required":true,"schema":{"type":"integer"}},{"in":"query","name":"page_no","description":"page number","required":true,"schema":{"type":"integer"}},{"in":"query","name":"start_date","description":"UTC start date in ISO format","schema":{"type":"string","format":"date-time"}},{"in":"query","name":"end_date","description":"UTC end date in ISO format","schema":{"type":"string","format":"date-time"}},{"in":"query","name":"status","description":"status for which to fetch the jobs.","schema":{"type":"string"}},{"in":"query","name":"bulk_action_type","description":"job type.","schema":{"type":"string"}},{"in":"query","name":"search_key","description":"search_key.","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company ID","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", page_size=page_size, page_no=page_no, start_date=start_date, end_date=end_date, status=status, bulk_action_type=bulk_action_type, search_key=search_key)
        query_string = await create_query_string(page_size=page_size, page_no=page_no, start_date=start_date, end_date=end_date, status=status, bulk_action_type=bulk_action_type, search_key=search_key)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/jobs", page_size=page_size, page_no=page_no, start_date=start_date, end_date=end_date, status=status, bulk_action_type=bulk_action_type, search_key=search_key), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkListingResponse
            schema = BulkListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for bulkListing")
                print(e)

        return response
    
    async def jobDetails(self, batch_id=None, request_headers:Dict={}):
        """Fetches details for the job of the provided batch_id
        :param batch_id :  : type string
        """
        payload = {}
        
        if batch_id is not None:
            payload["batch_id"] = batch_id

        # Parameter validation
        schema = OrderValidator.jobDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/jobs/{batch_id}", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"path","name":"batch_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"path","name":"batch_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", batch_id=batch_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/jobs/{batch_id}", batch_id=batch_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import JobDetailsResponse
            schema = JobDetailsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for jobDetails")
                print(e)

        return response
    
    async def getFileByStatus(self, batch_id=None, status=None, file_type=None, report_type=None, request_headers:Dict={}):
        """Get the file download URL used for performing bulk operation
        :param batch_id :  : type string
        :param status :  : type string
        :param file_type :  : type string
        :param report_type :  : type string
        """
        payload = {}
        
        if batch_id is not None:
            payload["batch_id"] = batch_id
        if status is not None:
            payload["status"] = status
        if file_type is not None:
            payload["file_type"] = file_type
        if report_type is not None:
            payload["report_type"] = report_type

        # Parameter validation
        schema = OrderValidator.getFileByStatus()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/jobs/{batch_id}/file", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"path","name":"batch_id","required":true,"schema":{"type":"string"}},{"in":"query","name":"status","required":true,"schema":{"type":"string"}},{"in":"query","name":"file_type","required":true,"schema":{"type":"string","default":"xlsx","enum":["xlsx","csv"]}}],"optional":[{"in":"query","name":"report_type","schema":{"type":"string","default":"generation_report","enum":["generation_report","invoice_report"]}}],"query":[{"in":"query","name":"status","required":true,"schema":{"type":"string"}},{"in":"query","name":"file_type","required":true,"schema":{"type":"string","default":"xlsx","enum":["xlsx","csv"]}},{"in":"query","name":"report_type","schema":{"type":"string","default":"generation_report","enum":["generation_report","invoice_report"]}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"path","name":"batch_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", batch_id=batch_id, status=status, file_type=file_type, report_type=report_type)
        query_string = await create_query_string(status=status, file_type=file_type, report_type=report_type)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/jobs/{batch_id}/file", batch_id=batch_id, status=status, file_type=file_type, report_type=report_type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import JobFailedResponse
            schema = JobFailedResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getFileByStatus")
                print(e)

        return response
    
    async def getManifestfilters(self, view=None, request_headers:Dict={}):
        """get Manifest Filters.
        :param view : Name of View : type string
        """
        payload = {}
        
        if view is not None:
            payload["view"] = view

        # Parameter validation
        schema = OrderValidator.getManifestfilters()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/filter/listing", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}},{"in":"query","name":"view","description":"Name of View","required":true,"schema":{"type":"string","default":"manifest","enum":["my_orders","bulk_action","manifest","bulk_invoice"]}}],"optional":[],"query":[{"in":"query","name":"view","description":"Name of View","required":true,"schema":{"type":"string","default":"manifest","enum":["my_orders","bulk_action","manifest","bulk_invoice"]}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", view=view)
        query_string = await create_query_string(view=view)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/filter/listing", view=view), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ManifestFiltersResponse
            schema = ManifestFiltersResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getManifestfilters")
                print(e)

        return response
    
    async def eInvoiceRetry(self, body="", request_headers:Dict={}):
        """Retry e-invoice after failure
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.eInvoiceRetry()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EInvoiceRetry
        schema = EInvoiceRetry()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/einvoice/retry/irn", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/einvoice/retry/irn", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EInvoiceRetryResponse
            schema = EInvoiceRetryResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for eInvoiceRetry")
                print(e)

        return response
    
    async def trackShipment(self, shipment_id=None, awb=None, page_no=None, page_size=None, request_headers:Dict={}):
        """Retrieve courier partner tracking details for a given shipment id or awb no.
        :param shipment_id : Shipment ID : type string
        :param awb : AWB number : type string
        :param page_no : Page number : type integer
        :param page_size : Page size : type integer
        """
        payload = {}
        
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id
        if awb is not None:
            payload["awb"] = awb
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = OrderValidator.trackShipment()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/tracking", """{"required":[{"description":"Company ID","in":"path","name":"company_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"Shipment ID","example":"16908065964581066182","in":"query","name":"shipment_id","required":false,"schema":{"type":"string"}},{"description":"AWB number","example":"581066182","in":"query","name":"awb","required":false,"schema":{"type":"string"}},{"description":"Page number","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Page size","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}}],"query":[{"description":"Shipment ID","example":"16908065964581066182","in":"query","name":"shipment_id","required":false,"schema":{"type":"string"}},{"description":"AWB number","example":"581066182","in":"query","name":"awb","required":false,"schema":{"type":"string"}},{"description":"Page number","in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"description":"Page size","in":"query","name":"page_size","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"description":"Company ID","in":"path","name":"company_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", shipment_id=shipment_id, awb=awb, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(shipment_id=shipment_id, awb=awb, page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/tracking", shipment_id=shipment_id, awb=awb, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierPartnerTrackingResponse
            schema = CourierPartnerTrackingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for trackShipment")
                print(e)

        return response
    
    async def updateShipmentTracking(self, body="", request_headers:Dict={}):
        """Modify courier partner tracking details for a given shipment id or awb no.
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.updateShipmentTracking()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CourierPartnerTrackingDetails
        schema = CourierPartnerTrackingDetails()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/tracking", """{"required":[{"in":"path","description":"Company ID","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","description":"Company ID","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/tracking", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierPartnerTrackingDetails
            schema = CourierPartnerTrackingDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateShipmentTracking")
                print(e)

        return response
    
    async def getFailedOrderLogs(self, page_no=None, page_size=None, search_type=None, search_value=None, request_headers:Dict={}):
        """This endpoint allows users to get failed order logs listing for filters based on order id, user contact number, user email id and sales channel id.
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
        schema = OrderValidator.getFailedOrderLogs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/orders/failed", """{"required":[{"in":"path","name":"company_id","description":"Company ID","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"page_no","required":false,"description":"Page Number","schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"description":"Page Size","schema":{"type":"integer"}},{"in":"query","name":"search_type","required":false,"description":"Search type for filter","schema":{"type":"string","example":"email_id"}},{"in":"query","name":"search_value","required":false,"description":"Search value for filter","schema":{"type":"string","example":"employee@gofynd.com"}}],"query":[{"in":"query","name":"page_no","required":false,"description":"Page Number","schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"description":"Page Size","schema":{"type":"integer"}},{"in":"query","name":"search_type","required":false,"description":"Search type for filter","schema":{"type":"string","example":"email_id"}},{"in":"query","name":"search_value","required":false,"description":"Search value for filter","schema":{"type":"string","example":"employee@gofynd.com"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company ID","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, search_type=search_type, search_value=search_value)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, search_type=search_type, search_value=search_value)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/orders/failed", page_no=page_no, page_size=page_size, search_type=search_type, search_value=search_value), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import FailedOrderLogs
            schema = FailedOrderLogs()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getFailedOrderLogs")
                print(e)

        return response
    
    async def failedOrderLogDetails(self, log_id=None, request_headers:Dict={}):
        """This endpoint allows users to get the exact error trace from the log id provided
        :param log_id : Log Error ID : type string
        """
        payload = {}
        
        if log_id is not None:
            payload["log_id"] = log_id

        # Parameter validation
        schema = OrderValidator.failedOrderLogDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/orders/failed/logs/{log_id}", """{"required":[{"in":"path","name":"company_id","description":"Company ID","required":true,"schema":{"type":"integer"}},{"in":"path","name":"log_id","description":"Log Error ID","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company ID","required":true,"schema":{"type":"integer"}},{"in":"path","name":"log_id","description":"Log Error ID","required":true,"schema":{"type":"string"}}]}""", serverType="platform", log_id=log_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/orders/failed/logs/{log_id}", log_id=log_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import FailedOrderLogDetails
            schema = FailedOrderLogDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for failedOrderLogDetails")
                print(e)

        return response
    
    async def getRoleBasedActions(self, request_headers:Dict={}):
        """Retrieve permissible actions based on user roles such as company_admin,  company_operation, customer_care, and read_only.
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.getRoleBasedActions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/roles", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/roles", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetActionsResponse
            schema = GetActionsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getRoleBasedActions")
                print(e)

        return response
    
    async def checkOrderStatus(self, body="", request_headers:Dict={}):
        """Verify the current status of an order.
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.checkOrderStatus()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OrderStatus
        schema = OrderStatus()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/debug/order_status", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/debug/order_status", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OrderStatusResult
            schema = OrderStatusResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for checkOrderStatus")
                print(e)

        return response
    
    async def updateShipmentLock(self, body="", request_headers:Dict={}):
        """Modify shipment/bag lock and check status.
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.updateShipmentLock()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateShipmentLockPayload
        schema = UpdateShipmentLockPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/entity/lock-manager", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/entity/lock-manager", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdateShipmentLockResponse
            schema = UpdateShipmentLockResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateShipmentLock")
                print(e)

        return response
    
    async def createOrder(self, body="", request_headers:Dict={}):
        """Create order.
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.createOrder()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateOrderAPI
        schema = CreateOrderAPI()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/create-order", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"},"description":"Id of the company."}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"},"description":"Id of the company."}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/create-order", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateOrderResponse
            schema = CreateOrderResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createOrder")
                print(e)

        return response
    
    async def updateShipment(self, body="", request_headers:Dict={}):
        """Shipment action transition or Shipment data update or both.
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.updateShipment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateShipmentActionRequest
        schema = UpdateShipmentActionRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/shipment/update", """{"required":[{"in":"path","name":"company_id","description":"company id from where are transitioning the shipment state or data","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"company id from where are transitioning the shipment state or data","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/shipment/update", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdateShipmentStatusResponseBody
            schema = UpdateShipmentStatusResponseBody()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateShipment")
                print(e)

        return response
    
    async def updateOrder(self, order_id=None, body="", request_headers:Dict={}):
        """Enables the updating of various order properties, including tax_details, meta, and more, providing flexibility and precision in order adjustments.
        :param order_id :  : type string
        """
        payload = {}
        
        if order_id is not None:
            payload["order_id"] = order_id

        # Parameter validation
        schema = OrderValidator.updateOrder()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OrderUpdatePayload
        schema = OrderUpdatePayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/order/{order_id}", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"path","name":"order_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"path","name":"order_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", order_id=order_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/order/{order_id}", order_id=order_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OrderUpdateResponseDetail
            schema = OrderUpdateResponseDetail()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateOrder")
                print(e)

        return response
    
    async def getShipments(self, lane=None, bag_status=None, status_override_lane=None, time_to_dispatch=None, search_type=None, search_value=None, from_date=None, to_date=None, start_date=None, end_date=None, dp_ids=None, stores=None, sales_channels=None, page_no=None, page_size=None, fetch_active_shipment=None, allow_inactive=None, exclude_locked_shipments=None, payment_methods=None, channel_shipment_id=None, channel_order_id=None, custom_meta=None, ordering_channel=None, company_affiliate_tag=None, my_orders=None, platform_user_id=None, sort_type=None, show_cross_company_data=None, tags=None, customer_id=None, order_type=None, operational_status=None, financial_status=None, logistics_status=None, parent_view_slug=None, child_view_slug=None, lock_status=None, group_entity=None, request_headers:Dict={}):
        """Get Shipments Listing for the company id
        :param lane : Name of lane for which data is to be fetched : type string
        :param bag_status : Comma separated values of bag statuses : type string
        :param status_override_lane : Use this flag to fetch by bag_status and override lane : type boolean
        :param time_to_dispatch :  : type integer
        :param search_type : Search type key : type string
        :param search_value : Search type value : type string
        :param from_date : Start Date in DD-MM-YYYY format : type string
        :param to_date : End Date in DD-MM-YYYY format : type string
        :param start_date : UTC Start Date in ISO format : type string
        :param end_date : UTC End Date in ISO format : type string
        :param dp_ids : Comma separated values of delivery partner ids : type string
        :param stores : Comma separated values of store ids : type string
        :param sales_channels : Comma separated values of sales channel ids : type string
        :param page_no : Page number for paginated data : type integer
        :param page_size : Page size of data received per page : type integer
        :param fetch_active_shipment : flag to fetch active shipments : type boolean
        :param allow_inactive : Flag to allow inactive shipments : type boolean
        :param exclude_locked_shipments : flag to fetch locked shipments : type boolean
        :param payment_methods : Comma separated values of payment methods : type string
        :param channel_shipment_id : App Shipment Id : type string
        :param channel_order_id : App Order Id : type string
        :param custom_meta :  : type string
        :param ordering_channel :  : type string
        :param company_affiliate_tag :  : type string
        :param my_orders :  : type boolean
        :param platform_user_id :  : type string
        :param sort_type : Sort the result data on basis of input : type string
        :param show_cross_company_data : Flag to view cross & non-cross company order : type boolean
        :param tags : Comma separated values of tags : type string
        :param customer_id :  : type string
        :param order_type :  : type string
        :param operational_status : Statuses relating to shipment transition in order processing journey. Comma separated values of operational statuses. : type string
        :param financial_status : Statuses relating to finance related operations in the order processing journey. Comma separated values of financial statuses. : type string
        :param logistics_status : Statuses relating to delivery and pickup related operations in the order processing journey. Comma separated values of logistics statuses. : type string
        :param parent_view_slug : Parent view is used for grouping of child views. Slug of parent view. : type string
        :param child_view_slug : Child view is user configured view which has filters added by the user on which shipments/orders are fetched. Slug of child view. : type string
        :param lock_status : Flag to identify if a shipment is locked or not. : type string
        :param group_entity : Defines the grouping criterion for retrieving shipments or orders. It specifies whether the results should be organized based on shipment groups or order groups.  For example, using 'shipments' groups results by shipment, while an invalid value like 'abcd' may not be recognized, leading to errors or default behavior. : type string
        """
        payload = {}
        
        if lane is not None:
            payload["lane"] = lane
        if bag_status is not None:
            payload["bag_status"] = bag_status
        if status_override_lane is not None:
            payload["status_override_lane"] = status_override_lane
        if time_to_dispatch is not None:
            payload["time_to_dispatch"] = time_to_dispatch
        if search_type is not None:
            payload["search_type"] = search_type
        if search_value is not None:
            payload["search_value"] = search_value
        if from_date is not None:
            payload["from_date"] = from_date
        if to_date is not None:
            payload["to_date"] = to_date
        if start_date is not None:
            payload["start_date"] = start_date
        if end_date is not None:
            payload["end_date"] = end_date
        if dp_ids is not None:
            payload["dp_ids"] = dp_ids
        if stores is not None:
            payload["stores"] = stores
        if sales_channels is not None:
            payload["sales_channels"] = sales_channels
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if fetch_active_shipment is not None:
            payload["fetch_active_shipment"] = fetch_active_shipment
        if allow_inactive is not None:
            payload["allow_inactive"] = allow_inactive
        if exclude_locked_shipments is not None:
            payload["exclude_locked_shipments"] = exclude_locked_shipments
        if payment_methods is not None:
            payload["payment_methods"] = payment_methods
        if channel_shipment_id is not None:
            payload["channel_shipment_id"] = channel_shipment_id
        if channel_order_id is not None:
            payload["channel_order_id"] = channel_order_id
        if custom_meta is not None:
            payload["custom_meta"] = custom_meta
        if ordering_channel is not None:
            payload["ordering_channel"] = ordering_channel
        if company_affiliate_tag is not None:
            payload["company_affiliate_tag"] = company_affiliate_tag
        if my_orders is not None:
            payload["my_orders"] = my_orders
        if platform_user_id is not None:
            payload["platform_user_id"] = platform_user_id
        if sort_type is not None:
            payload["sort_type"] = sort_type
        if show_cross_company_data is not None:
            payload["show_cross_company_data"] = show_cross_company_data
        if tags is not None:
            payload["tags"] = tags
        if customer_id is not None:
            payload["customer_id"] = customer_id
        if order_type is not None:
            payload["order_type"] = order_type
        if operational_status is not None:
            payload["operational_status"] = operational_status
        if financial_status is not None:
            payload["financial_status"] = financial_status
        if logistics_status is not None:
            payload["logistics_status"] = logistics_status
        if parent_view_slug is not None:
            payload["parent_view_slug"] = parent_view_slug
        if child_view_slug is not None:
            payload["child_view_slug"] = child_view_slug
        if lock_status is not None:
            payload["lock_status"] = lock_status
        if group_entity is not None:
            payload["group_entity"] = group_entity

        # Parameter validation
        schema = OrderValidator.getShipments()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/shipments-listing", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"lane","description":"Name of lane for which data is to be fetched","required":false,"schema":{"type":"string","enum":["new","confirmed","to_be_packed","ready_for_dispatch","in_transit","handed_over_to_customer","delivered","cancelled","return_initiated","return_in_transit","return_delivered","return_accepted"]}},{"in":"query","name":"bag_status","description":"Comma separated values of bag statuses","required":false,"schema":{"type":"string"}},{"in":"query","name":"status_override_lane","description":"Use this flag to fetch by bag_status and override lane","required":false,"schema":{"type":"boolean","default":false}},{"in":"query","name":"time_to_dispatch","required":false,"schema":{"type":"integer"}},{"in":"query","name":"search_type","description":"Search type key","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_value","description":"Search type value","required":false,"schema":{"type":"string"}},{"in":"query","name":"from_date","description":"Start Date in DD-MM-YYYY format","required":false,"schema":{"type":"string","format":"date"}},{"in":"query","name":"to_date","description":"End Date in DD-MM-YYYY format","required":false,"schema":{"type":"string","format":"date"}},{"in":"query","name":"start_date","description":"UTC Start Date in ISO format","required":false,"schema":{"type":"string","format":"date-time"}},{"in":"query","name":"end_date","description":"UTC End Date in ISO format","required":false,"schema":{"type":"string","format":"date-time"}},{"in":"query","name":"dp_ids","description":"Comma separated values of delivery partner ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","description":"Comma separated values of store ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channels","description":"Comma separated values of sales channel ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","description":"Page number for paginated data","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","description":"Page size of data received per page","required":false,"schema":{"type":"integer"}},{"in":"query","name":"fetch_active_shipment","description":"flag to fetch active shipments","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"allow_inactive","description":"Flag to allow inactive shipments","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"exclude_locked_shipments","description":"flag to fetch locked shipments","required":false,"schema":{"type":"boolean","default":true}},{"in":"query","name":"payment_methods","description":"Comma separated values of payment methods","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_shipment_id","description":"App Shipment Id","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_order_id","description":"App Order Id","required":false,"schema":{"type":"string"}},{"in":"query","name":"custom_meta","required":false,"schema":{"type":"string","format":"json"}},{"in":"query","name":"ordering_channel","required":false,"schema":{"type":"string"}},{"in":"query","name":"company_affiliate_tag","required":false,"schema":{"type":"string"}},{"in":"query","name":"my_orders","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"platform_user_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"sort_type","description":"Sort the result data on basis of input","required":false,"schema":{"type":"string","enum":["sla_asc","created_date_asc","created_date_desc"],"default":"sla_asc"}},{"in":"query","name":"show_cross_company_data","description":"Flag to view cross & non-cross company order","required":false,"schema":{"type":"boolean","default":false}},{"in":"query","name":"tags","description":"Comma separated values of tags","required":false,"schema":{"type":"string"}},{"in":"query","name":"customer_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"order_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"operational_status","description":"Statuses relating to shipment transition in order processing journey. Comma separated values of operational statuses.","required":false,"schema":{"type":"string"}},{"in":"query","name":"financial_status","description":"Statuses relating to finance related operations in the order processing journey. Comma separated values of financial statuses.","required":false,"schema":{"type":"string"}},{"in":"query","name":"logistics_status","description":"Statuses relating to delivery and pickup related operations in the order processing journey. Comma separated values of logistics statuses.","required":false,"schema":{"type":"string"}},{"in":"query","name":"parent_view_slug","description":"Parent view is used for grouping of child views. Slug of parent view.","required":false,"schema":{"type":"string"}},{"in":"query","name":"child_view_slug","description":"Child view is user configured view which has filters added by the user on which shipments/orders are fetched. Slug of child view.","required":false,"schema":{"type":"string"}},{"in":"query","name":"lock_status","description":"Flag to identify if a shipment is locked or not.","required":false,"schema":{"type":"string"}},{"in":"query","name":"group_entity","description":"Defines the grouping criterion for retrieving shipments or orders. It specifies whether the results should be organized based on shipment groups or order groups.  For example, using 'shipments' groups results by shipment, while an invalid value like 'abcd' may not be recognized, leading to errors or default behavior.","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"lane","description":"Name of lane for which data is to be fetched","required":false,"schema":{"type":"string","enum":["new","confirmed","to_be_packed","ready_for_dispatch","in_transit","handed_over_to_customer","delivered","cancelled","return_initiated","return_in_transit","return_delivered","return_accepted"]}},{"in":"query","name":"bag_status","description":"Comma separated values of bag statuses","required":false,"schema":{"type":"string"}},{"in":"query","name":"status_override_lane","description":"Use this flag to fetch by bag_status and override lane","required":false,"schema":{"type":"boolean","default":false}},{"in":"query","name":"time_to_dispatch","required":false,"schema":{"type":"integer"}},{"in":"query","name":"search_type","description":"Search type key","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_value","description":"Search type value","required":false,"schema":{"type":"string"}},{"in":"query","name":"from_date","description":"Start Date in DD-MM-YYYY format","required":false,"schema":{"type":"string","format":"date"}},{"in":"query","name":"to_date","description":"End Date in DD-MM-YYYY format","required":false,"schema":{"type":"string","format":"date"}},{"in":"query","name":"start_date","description":"UTC Start Date in ISO format","required":false,"schema":{"type":"string","format":"date-time"}},{"in":"query","name":"end_date","description":"UTC End Date in ISO format","required":false,"schema":{"type":"string","format":"date-time"}},{"in":"query","name":"dp_ids","description":"Comma separated values of delivery partner ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","description":"Comma separated values of store ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channels","description":"Comma separated values of sales channel ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","description":"Page number for paginated data","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","description":"Page size of data received per page","required":false,"schema":{"type":"integer"}},{"in":"query","name":"fetch_active_shipment","description":"flag to fetch active shipments","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"allow_inactive","description":"Flag to allow inactive shipments","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"exclude_locked_shipments","description":"flag to fetch locked shipments","required":false,"schema":{"type":"boolean","default":true}},{"in":"query","name":"payment_methods","description":"Comma separated values of payment methods","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_shipment_id","description":"App Shipment Id","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_order_id","description":"App Order Id","required":false,"schema":{"type":"string"}},{"in":"query","name":"custom_meta","required":false,"schema":{"type":"string","format":"json"}},{"in":"query","name":"ordering_channel","required":false,"schema":{"type":"string"}},{"in":"query","name":"company_affiliate_tag","required":false,"schema":{"type":"string"}},{"in":"query","name":"my_orders","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"platform_user_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"sort_type","description":"Sort the result data on basis of input","required":false,"schema":{"type":"string","enum":["sla_asc","created_date_asc","created_date_desc"],"default":"sla_asc"}},{"in":"query","name":"show_cross_company_data","description":"Flag to view cross & non-cross company order","required":false,"schema":{"type":"boolean","default":false}},{"in":"query","name":"tags","description":"Comma separated values of tags","required":false,"schema":{"type":"string"}},{"in":"query","name":"customer_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"order_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"operational_status","description":"Statuses relating to shipment transition in order processing journey. Comma separated values of operational statuses.","required":false,"schema":{"type":"string"}},{"in":"query","name":"financial_status","description":"Statuses relating to finance related operations in the order processing journey. Comma separated values of financial statuses.","required":false,"schema":{"type":"string"}},{"in":"query","name":"logistics_status","description":"Statuses relating to delivery and pickup related operations in the order processing journey. Comma separated values of logistics statuses.","required":false,"schema":{"type":"string"}},{"in":"query","name":"parent_view_slug","description":"Parent view is used for grouping of child views. Slug of parent view.","required":false,"schema":{"type":"string"}},{"in":"query","name":"child_view_slug","description":"Child view is user configured view which has filters added by the user on which shipments/orders are fetched. Slug of child view.","required":false,"schema":{"type":"string"}},{"in":"query","name":"lock_status","description":"Flag to identify if a shipment is locked or not.","required":false,"schema":{"type":"string"}},{"in":"query","name":"group_entity","description":"Defines the grouping criterion for retrieving shipments or orders. It specifies whether the results should be organized based on shipment groups or order groups.  For example, using 'shipments' groups results by shipment, while an invalid value like 'abcd' may not be recognized, leading to errors or default behavior.","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", lane=lane, bag_status=bag_status, status_override_lane=status_override_lane, time_to_dispatch=time_to_dispatch, search_type=search_type, search_value=search_value, from_date=from_date, to_date=to_date, start_date=start_date, end_date=end_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, page_no=page_no, page_size=page_size, fetch_active_shipment=fetch_active_shipment, allow_inactive=allow_inactive, exclude_locked_shipments=exclude_locked_shipments, payment_methods=payment_methods, channel_shipment_id=channel_shipment_id, channel_order_id=channel_order_id, custom_meta=custom_meta, ordering_channel=ordering_channel, company_affiliate_tag=company_affiliate_tag, my_orders=my_orders, platform_user_id=platform_user_id, sort_type=sort_type, show_cross_company_data=show_cross_company_data, tags=tags, customer_id=customer_id, order_type=order_type, operational_status=operational_status, financial_status=financial_status, logistics_status=logistics_status, parent_view_slug=parent_view_slug, child_view_slug=child_view_slug, lock_status=lock_status, group_entity=group_entity)
        query_string = await create_query_string(lane=lane, bag_status=bag_status, status_override_lane=status_override_lane, time_to_dispatch=time_to_dispatch, search_type=search_type, search_value=search_value, from_date=from_date, to_date=to_date, start_date=start_date, end_date=end_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, page_no=page_no, page_size=page_size, fetch_active_shipment=fetch_active_shipment, allow_inactive=allow_inactive, exclude_locked_shipments=exclude_locked_shipments, payment_methods=payment_methods, channel_shipment_id=channel_shipment_id, channel_order_id=channel_order_id, custom_meta=custom_meta, ordering_channel=ordering_channel, company_affiliate_tag=company_affiliate_tag, my_orders=my_orders, platform_user_id=platform_user_id, sort_type=sort_type, show_cross_company_data=show_cross_company_data, tags=tags, customer_id=customer_id, order_type=order_type, operational_status=operational_status, financial_status=financial_status, logistics_status=logistics_status, parent_view_slug=parent_view_slug, child_view_slug=child_view_slug, lock_status=lock_status, group_entity=group_entity)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/shipments-listing", lane=lane, bag_status=bag_status, status_override_lane=status_override_lane, time_to_dispatch=time_to_dispatch, search_type=search_type, search_value=search_value, from_date=from_date, to_date=to_date, start_date=start_date, end_date=end_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, page_no=page_no, page_size=page_size, fetch_active_shipment=fetch_active_shipment, allow_inactive=allow_inactive, exclude_locked_shipments=exclude_locked_shipments, payment_methods=payment_methods, channel_shipment_id=channel_shipment_id, channel_order_id=channel_order_id, custom_meta=custom_meta, ordering_channel=ordering_channel, company_affiliate_tag=company_affiliate_tag, my_orders=my_orders, platform_user_id=platform_user_id, sort_type=sort_type, show_cross_company_data=show_cross_company_data, tags=tags, customer_id=customer_id, order_type=order_type, operational_status=operational_status, financial_status=financial_status, logistics_status=logistics_status, parent_view_slug=parent_view_slug, child_view_slug=child_view_slug, lock_status=lock_status, group_entity=group_entity), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ShipmentInternalPlatformViewResponse
            schema = ShipmentInternalPlatformViewResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getShipments")
                print(e)

        return response
    
    async def getShipmentById(self, channel_shipment_id=None, shipment_id=None, fetch_active_shipment=None, request_headers:Dict={}):
        """Retrieve detailed information about a specific shipment.
        :param channel_shipment_id : App Shipment Id : type string
        :param shipment_id : Shipment Id : type string
        :param fetch_active_shipment : flag to fetch active or deactivated shipments : type boolean
        """
        payload = {}
        
        if channel_shipment_id is not None:
            payload["channel_shipment_id"] = channel_shipment_id
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id
        if fetch_active_shipment is not None:
            payload["fetch_active_shipment"] = fetch_active_shipment

        # Parameter validation
        schema = OrderValidator.getShipmentById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/shipment-details", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"channel_shipment_id","description":"App Shipment Id","required":false,"schema":{"type":"string"}},{"in":"query","name":"shipment_id","description":"Shipment Id","required":false,"schema":{"type":"string"}},{"in":"query","name":"fetch_active_shipment","description":"flag to fetch active or deactivated shipments","required":false,"schema":{"type":"boolean"}}],"query":[{"in":"query","name":"channel_shipment_id","description":"App Shipment Id","required":false,"schema":{"type":"string"}},{"in":"query","name":"shipment_id","description":"Shipment Id","required":false,"schema":{"type":"string"}},{"in":"query","name":"fetch_active_shipment","description":"flag to fetch active or deactivated shipments","required":false,"schema":{"type":"boolean"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", channel_shipment_id=channel_shipment_id, shipment_id=shipment_id, fetch_active_shipment=fetch_active_shipment)
        query_string = await create_query_string(channel_shipment_id=channel_shipment_id, shipment_id=shipment_id, fetch_active_shipment=fetch_active_shipment)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/shipment-details", channel_shipment_id=channel_shipment_id, shipment_id=shipment_id, fetch_active_shipment=fetch_active_shipment), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ShipmentInfoResponse
            schema = ShipmentInfoResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getShipmentById")
                print(e)

        return response
    
    async def getOrderById(self, order_id=None, my_orders=None, allow_inactive=None, request_headers:Dict={}):
        """Retrieve detailed information about a specific order.
        :param order_id : Flag for order id : type string
        :param my_orders :  : type boolean
        :param allow_inactive : Flag to allow inactive shipments : type boolean
        """
        payload = {}
        
        if order_id is not None:
            payload["order_id"] = order_id
        if my_orders is not None:
            payload["my_orders"] = my_orders
        if allow_inactive is not None:
            payload["allow_inactive"] = allow_inactive

        # Parameter validation
        schema = OrderValidator.getOrderById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/order-details", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}},{"in":"query","name":"order_id","description":"Flag for order id","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"my_orders","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"allow_inactive","description":"Flag to allow inactive shipments","required":false,"schema":{"type":"boolean"}}],"query":[{"in":"query","name":"order_id","description":"Flag for order id","required":true,"schema":{"type":"string"}},{"in":"query","name":"my_orders","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"allow_inactive","description":"Flag to allow inactive shipments","required":false,"schema":{"type":"boolean"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", order_id=order_id, my_orders=my_orders, allow_inactive=allow_inactive)
        query_string = await create_query_string(order_id=order_id, my_orders=my_orders, allow_inactive=allow_inactive)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/order-details", order_id=order_id, my_orders=my_orders, allow_inactive=allow_inactive), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OrderDetailsResponse
            schema = OrderDetailsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOrderById")
                print(e)

        return response
    
    async def getLaneConfig(self, super_lane=None, group_entity=None, from_date=None, to_date=None, start_date=None, end_date=None, dp_ids=None, stores=None, sales_channels=None, payment_mode=None, bag_status=None, search_type=None, search_value=None, tags=None, time_to_dispatch=None, payment_methods=None, my_orders=None, show_cross_company_data=None, order_type=None, request_headers:Dict={}):
        """Get lane config for the order and shipment
        :param super_lane : Name of lane for which data is to be fetched : type string
        :param group_entity : Name of group entity : type string
        :param from_date : Start Date in DD-MM-YYYY format : type string
        :param to_date :  : type string
        :param start_date : UTC Start Date in ISO format : type string
        :param end_date : UTC End Date in ISO format : type string
        :param dp_ids : Comma separated values of delivery partner ids : type string
        :param stores : Comma separated values of store ids : type string
        :param sales_channels :  : type string
        :param payment_mode : Comma separated values of payment modes : type string
        :param bag_status : Comma separated values of bag statuses : type string
        :param search_type :  : type string
        :param search_value :  : type string
        :param tags :  : type string
        :param time_to_dispatch :  : type integer
        :param payment_methods :  : type string
        :param my_orders :  : type boolean
        :param show_cross_company_data : Flag to view cross & non-cross company order : type boolean
        :param order_type :  : type string
        """
        payload = {}
        
        if super_lane is not None:
            payload["super_lane"] = super_lane
        if group_entity is not None:
            payload["group_entity"] = group_entity
        if from_date is not None:
            payload["from_date"] = from_date
        if to_date is not None:
            payload["to_date"] = to_date
        if start_date is not None:
            payload["start_date"] = start_date
        if end_date is not None:
            payload["end_date"] = end_date
        if dp_ids is not None:
            payload["dp_ids"] = dp_ids
        if stores is not None:
            payload["stores"] = stores
        if sales_channels is not None:
            payload["sales_channels"] = sales_channels
        if payment_mode is not None:
            payload["payment_mode"] = payment_mode
        if bag_status is not None:
            payload["bag_status"] = bag_status
        if search_type is not None:
            payload["search_type"] = search_type
        if search_value is not None:
            payload["search_value"] = search_value
        if tags is not None:
            payload["tags"] = tags
        if time_to_dispatch is not None:
            payload["time_to_dispatch"] = time_to_dispatch
        if payment_methods is not None:
            payload["payment_methods"] = payment_methods
        if my_orders is not None:
            payload["my_orders"] = my_orders
        if show_cross_company_data is not None:
            payload["show_cross_company_data"] = show_cross_company_data
        if order_type is not None:
            payload["order_type"] = order_type

        # Parameter validation
        schema = OrderValidator.getLaneConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/lane-config", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"super_lane","description":"Name of lane for which data is to be fetched","required":false,"schema":{"type":"string","enum":["unfulfilled","processed","returns","action_centre"]}},{"in":"query","name":"group_entity","description":"Name of group entity","required":false,"schema":{"type":"string","enum":["shipments","orders","bags"]}},{"in":"query","name":"from_date","description":"Start Date in DD-MM-YYYY format","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"start_date","description":"UTC Start Date in ISO format","required":false,"schema":{"type":"string"}},{"in":"query","name":"end_date","description":"UTC End Date in ISO format","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","description":"Comma separated values of delivery partner ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","description":"Comma separated values of store ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channels","required":false,"schema":{"type":"string"}},{"in":"query","name":"payment_mode","description":"Comma separated values of payment modes","required":false,"schema":{"type":"string"}},{"in":"query","name":"bag_status","description":"Comma separated values of bag statuses","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_value","required":false,"schema":{"type":"string"}},{"in":"query","name":"tags","required":false,"schema":{"type":"string"}},{"in":"query","name":"time_to_dispatch","required":false,"schema":{"type":"integer"}},{"in":"query","name":"payment_methods","required":false,"schema":{"type":"string"}},{"in":"query","name":"my_orders","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"show_cross_company_data","description":"Flag to view cross & non-cross company order","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"order_type","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"super_lane","description":"Name of lane for which data is to be fetched","required":false,"schema":{"type":"string","enum":["unfulfilled","processed","returns","action_centre"]}},{"in":"query","name":"group_entity","description":"Name of group entity","required":false,"schema":{"type":"string","enum":["shipments","orders","bags"]}},{"in":"query","name":"from_date","description":"Start Date in DD-MM-YYYY format","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"start_date","description":"UTC Start Date in ISO format","required":false,"schema":{"type":"string"}},{"in":"query","name":"end_date","description":"UTC End Date in ISO format","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","description":"Comma separated values of delivery partner ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","description":"Comma separated values of store ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channels","required":false,"schema":{"type":"string"}},{"in":"query","name":"payment_mode","description":"Comma separated values of payment modes","required":false,"schema":{"type":"string"}},{"in":"query","name":"bag_status","description":"Comma separated values of bag statuses","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_value","required":false,"schema":{"type":"string"}},{"in":"query","name":"tags","required":false,"schema":{"type":"string"}},{"in":"query","name":"time_to_dispatch","required":false,"schema":{"type":"integer"}},{"in":"query","name":"payment_methods","required":false,"schema":{"type":"string"}},{"in":"query","name":"my_orders","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"show_cross_company_data","description":"Flag to view cross & non-cross company order","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"order_type","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", super_lane=super_lane, group_entity=group_entity, from_date=from_date, to_date=to_date, start_date=start_date, end_date=end_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, payment_mode=payment_mode, bag_status=bag_status, search_type=search_type, search_value=search_value, tags=tags, time_to_dispatch=time_to_dispatch, payment_methods=payment_methods, my_orders=my_orders, show_cross_company_data=show_cross_company_data, order_type=order_type)
        query_string = await create_query_string(super_lane=super_lane, group_entity=group_entity, from_date=from_date, to_date=to_date, start_date=start_date, end_date=end_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, payment_mode=payment_mode, bag_status=bag_status, search_type=search_type, search_value=search_value, tags=tags, time_to_dispatch=time_to_dispatch, payment_methods=payment_methods, my_orders=my_orders, show_cross_company_data=show_cross_company_data, order_type=order_type)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/lane-config", super_lane=super_lane, group_entity=group_entity, from_date=from_date, to_date=to_date, start_date=start_date, end_date=end_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, payment_mode=payment_mode, bag_status=bag_status, search_type=search_type, search_value=search_value, tags=tags, time_to_dispatch=time_to_dispatch, payment_methods=payment_methods, my_orders=my_orders, show_cross_company_data=show_cross_company_data, order_type=order_type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import LaneConfigResponse
            schema = LaneConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getLaneConfig")
                print(e)

        return response
    
    async def getOrders(self, lane=None, search_type=None, bag_status=None, time_to_dispatch=None, payment_methods=None, tags=None, search_value=None, from_date=None, to_date=None, start_date=None, end_date=None, dp_ids=None, stores=None, sales_channels=None, page_no=None, page_size=None, is_priority_sort=None, custom_meta=None, my_orders=None, show_cross_company_data=None, customer_id=None, order_type=None, operational_status=None, financial_status=None, logistics_status=None, parent_view_slug=None, child_view_slug=None, group_entity=None, request_headers:Dict={}):
        """Get Orders Listing
        :param lane : Lane refers to a section where orders are assigned, indicating its grouping : type string
        :param search_type : Search_type refers to the field that will be used as the target for the search operation : type string
        :param bag_status : Bag_status refers to the status of the entity. Filters orders based on the status. : type string
        :param time_to_dispatch : Time_to_dispatch refers to the estimated SLA time. : type integer
        :param payment_methods :  : type string
        :param tags : Tags refer to additional descriptive labels associated with the order : type string
        :param search_value : Search_value is matched against the field specified by the search_type : type string
        :param from_date :  : type string
        :param to_date :  : type string
        :param start_date :  : type string
        :param end_date :  : type string
        :param dp_ids : Delivery Partner IDs to which shipments are assigned. : type string
        :param stores :  : type string
        :param sales_channels :  : type string
        :param page_no :  : type integer
        :param page_size :  : type integer
        :param is_priority_sort :  : type boolean
        :param custom_meta :  : type array
        :param my_orders :  : type boolean
        :param show_cross_company_data : Flag to view cross & non-cross company order : type boolean
        :param customer_id :  : type string
        :param order_type :  : type string
        :param operational_status : Statuses relating to shipment transition in order processing journey. Comma separated values of operational statuses. : type string
        :param financial_status : Statuses relating to finance related operations in the order processing journey. Comma separated values of financial statuses. : type string
        :param logistics_status : Statuses relating to delivery and pickup related operations in the order processing journey. Comma separated values of logistics statuses. : type string
        :param parent_view_slug : Parent view is used for grouping of child views. Slug of parent view. : type string
        :param child_view_slug : Child view is user configured view, which has filters added by the user on which shipments/orders are fetched. Slug of child view. : type string
        :param group_entity : Defines the grouping criterion for retrieving shipments or orders. It specifies whether the results should be organized based on shipment groups or order groups.  For example, using 'shipments' groups results by shipment, while an invalid value like 'abcd' may not be recognized, leading to errors or default behavior. : type string
        """
        payload = {}
        
        if lane is not None:
            payload["lane"] = lane
        if search_type is not None:
            payload["search_type"] = search_type
        if bag_status is not None:
            payload["bag_status"] = bag_status
        if time_to_dispatch is not None:
            payload["time_to_dispatch"] = time_to_dispatch
        if payment_methods is not None:
            payload["payment_methods"] = payment_methods
        if tags is not None:
            payload["tags"] = tags
        if search_value is not None:
            payload["search_value"] = search_value
        if from_date is not None:
            payload["from_date"] = from_date
        if to_date is not None:
            payload["to_date"] = to_date
        if start_date is not None:
            payload["start_date"] = start_date
        if end_date is not None:
            payload["end_date"] = end_date
        if dp_ids is not None:
            payload["dp_ids"] = dp_ids
        if stores is not None:
            payload["stores"] = stores
        if sales_channels is not None:
            payload["sales_channels"] = sales_channels
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if is_priority_sort is not None:
            payload["is_priority_sort"] = is_priority_sort
        if custom_meta is not None:
            payload["custom_meta"] = custom_meta
        if my_orders is not None:
            payload["my_orders"] = my_orders
        if show_cross_company_data is not None:
            payload["show_cross_company_data"] = show_cross_company_data
        if customer_id is not None:
            payload["customer_id"] = customer_id
        if order_type is not None:
            payload["order_type"] = order_type
        if operational_status is not None:
            payload["operational_status"] = operational_status
        if financial_status is not None:
            payload["financial_status"] = financial_status
        if logistics_status is not None:
            payload["logistics_status"] = logistics_status
        if parent_view_slug is not None:
            payload["parent_view_slug"] = parent_view_slug
        if child_view_slug is not None:
            payload["child_view_slug"] = child_view_slug
        if group_entity is not None:
            payload["group_entity"] = group_entity

        # Parameter validation
        schema = OrderValidator.getOrders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders-listing", """{"required":[{"in":"path","name":"company_id","description":"Id of the company","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"lane","description":"Lane refers to a section where orders are assigned, indicating its grouping","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_type","description":"Search_type refers to the field that will be used as the target for the search operation","required":false,"schema":{"type":"string"}},{"in":"query","name":"bag_status","description":"Bag_status refers to the status of the entity. Filters orders based on the status.","required":false,"schema":{"type":"string"}},{"in":"query","name":"time_to_dispatch","description":"Time_to_dispatch refers to the estimated SLA time.","required":false,"schema":{"type":"integer"}},{"in":"query","name":"payment_methods","required":false,"schema":{"type":"string"}},{"in":"query","name":"tags","description":"Tags refer to additional descriptive labels associated with the order","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_value","description":"Search_value is matched against the field specified by the search_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"start_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"end_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","description":"Delivery Partner IDs to which shipments are assigned.","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channels","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"is_priority_sort","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"custom_meta","required":false,"schema":{"type":"array","items":{"type":"object"},"additionalProperties":true}},{"in":"query","name":"my_orders","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"show_cross_company_data","description":"Flag to view cross & non-cross company order","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"customer_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"order_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"operational_status","description":"Statuses relating to shipment transition in order processing journey. Comma separated values of operational statuses.","required":false,"schema":{"type":"string"}},{"in":"query","name":"financial_status","description":"Statuses relating to finance related operations in the order processing journey. Comma separated values of financial statuses.","required":false,"schema":{"type":"string"}},{"in":"query","name":"logistics_status","description":"Statuses relating to delivery and pickup related operations in the order processing journey. Comma separated values of logistics statuses.","required":false,"schema":{"type":"string"}},{"in":"query","name":"parent_view_slug","description":"Parent view is used for grouping of child views. Slug of parent view.","required":false,"schema":{"type":"string"}},{"in":"query","name":"child_view_slug","description":"Child view is user configured view, which has filters added by the user on which shipments/orders are fetched. Slug of child view.","required":false,"schema":{"type":"string"}},{"in":"query","name":"group_entity","description":"Defines the grouping criterion for retrieving shipments or orders. It specifies whether the results should be organized based on shipment groups or order groups.  For example, using 'shipments' groups results by shipment, while an invalid value like 'abcd' may not be recognized, leading to errors or default behavior.","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"lane","description":"Lane refers to a section where orders are assigned, indicating its grouping","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_type","description":"Search_type refers to the field that will be used as the target for the search operation","required":false,"schema":{"type":"string"}},{"in":"query","name":"bag_status","description":"Bag_status refers to the status of the entity. Filters orders based on the status.","required":false,"schema":{"type":"string"}},{"in":"query","name":"time_to_dispatch","description":"Time_to_dispatch refers to the estimated SLA time.","required":false,"schema":{"type":"integer"}},{"in":"query","name":"payment_methods","required":false,"schema":{"type":"string"}},{"in":"query","name":"tags","description":"Tags refer to additional descriptive labels associated with the order","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_value","description":"Search_value is matched against the field specified by the search_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"start_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"end_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","description":"Delivery Partner IDs to which shipments are assigned.","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channels","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"is_priority_sort","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"custom_meta","required":false,"schema":{"type":"array","items":{"type":"object"},"additionalProperties":true}},{"in":"query","name":"my_orders","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"show_cross_company_data","description":"Flag to view cross & non-cross company order","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"customer_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"order_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"operational_status","description":"Statuses relating to shipment transition in order processing journey. Comma separated values of operational statuses.","required":false,"schema":{"type":"string"}},{"in":"query","name":"financial_status","description":"Statuses relating to finance related operations in the order processing journey. Comma separated values of financial statuses.","required":false,"schema":{"type":"string"}},{"in":"query","name":"logistics_status","description":"Statuses relating to delivery and pickup related operations in the order processing journey. Comma separated values of logistics statuses.","required":false,"schema":{"type":"string"}},{"in":"query","name":"parent_view_slug","description":"Parent view is used for grouping of child views. Slug of parent view.","required":false,"schema":{"type":"string"}},{"in":"query","name":"child_view_slug","description":"Child view is user configured view, which has filters added by the user on which shipments/orders are fetched. Slug of child view.","required":false,"schema":{"type":"string"}},{"in":"query","name":"group_entity","description":"Defines the grouping criterion for retrieving shipments or orders. It specifies whether the results should be organized based on shipment groups or order groups.  For example, using 'shipments' groups results by shipment, while an invalid value like 'abcd' may not be recognized, leading to errors or default behavior.","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", lane=lane, search_type=search_type, bag_status=bag_status, time_to_dispatch=time_to_dispatch, payment_methods=payment_methods, tags=tags, search_value=search_value, from_date=from_date, to_date=to_date, start_date=start_date, end_date=end_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, page_no=page_no, page_size=page_size, is_priority_sort=is_priority_sort, custom_meta=custom_meta, my_orders=my_orders, show_cross_company_data=show_cross_company_data, customer_id=customer_id, order_type=order_type, operational_status=operational_status, financial_status=financial_status, logistics_status=logistics_status, parent_view_slug=parent_view_slug, child_view_slug=child_view_slug, group_entity=group_entity)
        query_string = await create_query_string(lane=lane, search_type=search_type, bag_status=bag_status, time_to_dispatch=time_to_dispatch, payment_methods=payment_methods, tags=tags, search_value=search_value, from_date=from_date, to_date=to_date, start_date=start_date, end_date=end_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, page_no=page_no, page_size=page_size, is_priority_sort=is_priority_sort, custom_meta=custom_meta, my_orders=my_orders, show_cross_company_data=show_cross_company_data, customer_id=customer_id, order_type=order_type, operational_status=operational_status, financial_status=financial_status, logistics_status=logistics_status, parent_view_slug=parent_view_slug, child_view_slug=child_view_slug, group_entity=group_entity)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders-listing", lane=lane, search_type=search_type, bag_status=bag_status, time_to_dispatch=time_to_dispatch, payment_methods=payment_methods, tags=tags, search_value=search_value, from_date=from_date, to_date=to_date, start_date=start_date, end_date=end_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, page_no=page_no, page_size=page_size, is_priority_sort=is_priority_sort, custom_meta=custom_meta, my_orders=my_orders, show_cross_company_data=show_cross_company_data, customer_id=customer_id, order_type=order_type, operational_status=operational_status, financial_status=financial_status, logistics_status=logistics_status, parent_view_slug=parent_view_slug, child_view_slug=child_view_slug, group_entity=group_entity), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OrderListingResponse
            schema = OrderListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOrders")
                print(e)

        return response
    
    async def updateUserViewPosition(self, body="", request_headers:Dict={}):
        """Update User view(Parent view and child view) position
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.updateUserViewPosition()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UserViewPosition
        schema = UserViewPosition()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/view/position", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/view/position", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateUpdateDeleteResponse
            schema = CreateUpdateDeleteResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateUserViewPosition")
                print(e)

        return response
    
    async def getUserViews(self, show_in=None, request_headers:Dict={}):
        """Get custom view for every unique user cross company pair.
        :param show_in : Name of view to get filters for. : type string
        """
        payload = {}
        
        if show_in is not None:
            payload["show_in"] = show_in

        # Parameter validation
        schema = OrderValidator.getUserViews()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/views", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}},{"in":"query","name":"show_in","description":"Name of view to get filters for.","required":true,"schema":{"type":"string","enum":["shipment_view","order_view"]}}],"optional":[],"query":[{"in":"query","name":"show_in","description":"Name of view to get filters for.","required":true,"schema":{"type":"string","enum":["shipment_view","order_view"]}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", show_in=show_in)
        query_string = await create_query_string(show_in=show_in)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/views", show_in=show_in), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UserViewsResponse
            schema = UserViewsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getUserViews")
                print(e)

        return response
    
    async def addUserViews(self, body="", request_headers:Dict={}):
        """Add custom view for every unique user cross company pair.
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.addUserViews()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UserViewsResponse
        schema = UserViewsResponse()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/views", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/views", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateUpdateDeleteResponse
            schema = CreateUpdateDeleteResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addUserViews")
                print(e)

        return response
    
    async def updateUserViews(self, body="", request_headers:Dict={}):
        """Update custom view for every unique user cross company pair.
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.updateUserViews()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UserViewsResponse
        schema = UserViewsResponse()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/views", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/views", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateUpdateDeleteResponse
            schema = CreateUpdateDeleteResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateUserViews")
                print(e)

        return response
    
    async def deleteUserViews(self, view_id=None, request_headers:Dict={}):
        """Delete custom view for every unique user cross company pair.
        :param view_id : Comma separated values of view ids : type string
        """
        payload = {}
        
        if view_id is not None:
            payload["view_id"] = view_id

        # Parameter validation
        schema = OrderValidator.deleteUserViews()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/views", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}},{"in":"query","name":"view_id","description":"Comma separated values of view ids","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"in":"query","name":"view_id","description":"Comma separated values of view ids","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", view_id=view_id)
        query_string = await create_query_string(view_id=view_id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/views", view_id=view_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateUpdateDeleteResponse
            schema = CreateUpdateDeleteResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteUserViews")
                print(e)

        return response
    
    async def getGlobalFilters(self, show_in=None, request_headers:Dict={}):
        """Get global filters for populating filter listing and powering views api.
        :param show_in : Name of view to get filters for : type string
        """
        payload = {}
        
        if show_in is not None:
            payload["show_in"] = show_in

        # Parameter validation
        schema = OrderValidator.getGlobalFilters()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/filters", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}},{"in":"query","name":"show_in","description":"Name of view to get filters for","required":true,"schema":{"type":"string","enum":["shipment_view","order_view"]}}],"optional":[],"query":[{"in":"query","name":"show_in","description":"Name of view to get filters for","required":true,"schema":{"type":"string","enum":["shipment_view","order_view"]}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", show_in=show_in)
        query_string = await create_query_string(show_in=show_in)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/filters", show_in=show_in), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GlobalFiltersResponse
            schema = GlobalFiltersResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getGlobalFilters")
                print(e)

        return response
    
    async def getfilters(self, view=None, group_entity=None, request_headers:Dict={}):
        """Get supported filters for various listing operations
        :param view : Name of view : type string
        :param group_entity : Name of group entity : type string
        """
        payload = {}
        
        if view is not None:
            payload["view"] = view
        if group_entity is not None:
            payload["group_entity"] = group_entity

        # Parameter validation
        schema = OrderValidator.getfilters()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/filter-listing", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}},{"in":"query","name":"view","description":"Name of view","required":true,"schema":{"type":"string","default":"manifest"}}],"optional":[{"in":"query","name":"group_entity","description":"Name of group entity","required":false,"schema":{"type":"string","default":"orders","enum":["orders","shipments"]}}],"query":[{"in":"query","name":"view","description":"Name of view","required":true,"schema":{"type":"string","default":"manifest"}},{"in":"query","name":"group_entity","description":"Name of group entity","required":false,"schema":{"type":"string","default":"orders","enum":["orders","shipments"]}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", view=view, group_entity=group_entity)
        query_string = await create_query_string(view=view, group_entity=group_entity)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/filter-listing", view=view, group_entity=group_entity), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import FiltersResponse
            schema = FiltersResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getfilters")
                print(e)

        return response
    
    async def getBulkShipmentExcelFile(self, sales_channels=None, dp_ids=None, start_date=None, end_date=None, stores=None, tags=None, bag_status=None, payment_methods=None, file_type=None, time_to_dispatch=None, page_no=None, page_size=None, request_headers:Dict={}):
        """Generates the report which can be filled and uploaded to perform the bulk operation based on the filters provided
        :param sales_channels : Comma separated values of sales channel ids : type string
        :param dp_ids : Comma separated values of delivery partner ids : type string
        :param start_date : UTC start date in ISO format : type string
        :param end_date : UTC end date in ISO format : type string
        :param stores : Comma separated values of store ids : type string
        :param tags : Comma separated values of tags : type string
        :param bag_status : Comma separated values of bag statuses : type string
        :param payment_methods : Comma separated values of payment methods : type string
        :param file_type : File type to be downloaded : type string
        :param time_to_dispatch : Sla breached or not breached : type integer
        :param page_no :  : type integer
        :param page_size :  : type integer
        """
        payload = {}
        
        if sales_channels is not None:
            payload["sales_channels"] = sales_channels
        if dp_ids is not None:
            payload["dp_ids"] = dp_ids
        if start_date is not None:
            payload["start_date"] = start_date
        if end_date is not None:
            payload["end_date"] = end_date
        if stores is not None:
            payload["stores"] = stores
        if tags is not None:
            payload["tags"] = tags
        if bag_status is not None:
            payload["bag_status"] = bag_status
        if payment_methods is not None:
            payload["payment_methods"] = payment_methods
        if file_type is not None:
            payload["file_type"] = file_type
        if time_to_dispatch is not None:
            payload["time_to_dispatch"] = time_to_dispatch
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = OrderValidator.getBulkShipmentExcelFile()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/generate/file", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"sales_channels","description":"Comma separated values of sales channel ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","description":"Comma separated values of delivery partner ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"start_date","description":"UTC start date in ISO format","required":false,"schema":{"type":"string","format":"date-time"}},{"in":"query","name":"end_date","description":"UTC end date in ISO format","required":false,"schema":{"type":"string","format":"date-time"}},{"in":"query","name":"stores","description":"Comma separated values of store ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"tags","description":"Comma separated values of tags","required":false,"schema":{"type":"string"}},{"in":"query","name":"bag_status","description":"Comma separated values of bag statuses","required":false,"schema":{"type":"string"}},{"in":"query","name":"payment_methods","description":"Comma separated values of payment methods","required":false,"schema":{"type":"string"}},{"in":"query","name":"file_type","description":"File type to be downloaded","required":false,"schema":{"type":"string"}},{"in":"query","name":"time_to_dispatch","description":"Sla breached or not breached","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}}],"query":[{"in":"query","name":"sales_channels","description":"Comma separated values of sales channel ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","description":"Comma separated values of delivery partner ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"start_date","description":"UTC start date in ISO format","required":false,"schema":{"type":"string","format":"date-time"}},{"in":"query","name":"end_date","description":"UTC end date in ISO format","required":false,"schema":{"type":"string","format":"date-time"}},{"in":"query","name":"stores","description":"Comma separated values of store ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"tags","description":"Comma separated values of tags","required":false,"schema":{"type":"string"}},{"in":"query","name":"bag_status","description":"Comma separated values of bag statuses","required":false,"schema":{"type":"string"}},{"in":"query","name":"payment_methods","description":"Comma separated values of payment methods","required":false,"schema":{"type":"string"}},{"in":"query","name":"file_type","description":"File type to be downloaded","required":false,"schema":{"type":"string"}},{"in":"query","name":"time_to_dispatch","description":"Sla breached or not breached","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", sales_channels=sales_channels, dp_ids=dp_ids, start_date=start_date, end_date=end_date, stores=stores, tags=tags, bag_status=bag_status, payment_methods=payment_methods, file_type=file_type, time_to_dispatch=time_to_dispatch, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(sales_channels=sales_channels, dp_ids=dp_ids, start_date=start_date, end_date=end_date, stores=stores, tags=tags, bag_status=bag_status, payment_methods=payment_methods, file_type=file_type, time_to_dispatch=time_to_dispatch, page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/generate/file", sales_channels=sales_channels, dp_ids=dp_ids, start_date=start_date, end_date=end_date, stores=stores, tags=tags, bag_status=bag_status, payment_methods=payment_methods, file_type=file_type, time_to_dispatch=time_to_dispatch, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TemplateDownloadResponse
            schema = TemplateDownloadResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBulkShipmentExcelFile")
                print(e)

        return response
    
    async def getBulkActionTemplate(self, request_headers:Dict={}):
        """Get list of templates so that users can download the required template
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.getBulkActionTemplate()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/bulk-action/get-seller-templates", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/bulk-action/get-seller-templates", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkActionTemplateResponse
            schema = BulkActionTemplateResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBulkActionTemplate")
                print(e)

        return response
    
    async def downloadBulkActionTemplate(self, template_slug=None, request_headers:Dict={}):
        """Download bulk seller templates which can be used to perform operations in bulk
        :param template_slug : Slug name of template to be downloaded : type string
        """
        payload = {}
        
        if template_slug is not None:
            payload["template_slug"] = template_slug

        # Parameter validation
        schema = OrderValidator.downloadBulkActionTemplate()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/bulk-action/download-seller-templates", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"template_slug","description":"Slug name of template to be downloaded","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"template_slug","description":"Slug name of template to be downloaded","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", template_slug=template_slug)
        query_string = await create_query_string(template_slug=template_slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/bulk-action/download-seller-templates", template_slug=template_slug), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TemplateDownloadResponse
            schema = TemplateDownloadResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for downloadBulkActionTemplate")
                print(e)

        return response
    
    async def getShipmentReasons(self, shipment_id=None, bag_id=None, state=None, request_headers:Dict={}):
        """Use this API to retrieve the issues that led to the cancellation of bags within a shipment.
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        :param bag_id : ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        :param state : State for which reasons are required. : type string
        """
        payload = {}
        
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id
        if bag_id is not None:
            payload["bag_id"] = bag_id
        if state is not None:
            payload["state"] = state

        # Parameter validation
        schema = OrderValidator.getShipmentReasons()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/shipments/{shipment_id}/bags/{bag_id}/state/{state}/reasons", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"path","name":"shipment_id","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}},{"in":"path","description":"ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"bag_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"state","description":"State for which reasons are required.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"path","name":"shipment_id","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}},{"in":"path","description":"ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"bag_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"state","description":"State for which reasons are required.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", shipment_id=shipment_id, bag_id=bag_id, state=state)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/shipments/{shipment_id}/bags/{bag_id}/state/{state}/reasons", shipment_id=shipment_id, bag_id=bag_id, state=state), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PlatformShipmentReasonsResponse
            schema = PlatformShipmentReasonsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getShipmentReasons")
                print(e)

        return response
    
    async def getBagById(self, bag_id=None, channel_bag_id=None, channel_id=None, request_headers:Dict={}):
        """Get Order Bag Details.
        :param bag_id : Id of bag : type string
        :param channel_bag_id : Id of application bag : type string
        :param channel_id : Id of application : type string
        """
        payload = {}
        
        if bag_id is not None:
            payload["bag_id"] = bag_id
        if channel_bag_id is not None:
            payload["channel_bag_id"] = channel_bag_id
        if channel_id is not None:
            payload["channel_id"] = channel_id

        # Parameter validation
        schema = OrderValidator.getBagById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/bag-details", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"bag_id","description":"Id of bag","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_bag_id","description":"Id of application bag","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_id","description":"Id of application","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"bag_id","description":"Id of bag","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_bag_id","description":"Id of application bag","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_id","description":"Id of application","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", bag_id=bag_id, channel_bag_id=channel_bag_id, channel_id=channel_id)
        query_string = await create_query_string(bag_id=bag_id, channel_bag_id=channel_bag_id, channel_id=channel_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/bag-details", bag_id=bag_id, channel_bag_id=channel_bag_id, channel_id=channel_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BagDetailsPlatformResponse
            schema = BagDetailsPlatformResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBagById")
                print(e)

        return response
    
    async def getBags(self, bag_ids=None, shipment_ids=None, order_ids=None, channel_bag_ids=None, channel_shipment_ids=None, channel_order_ids=None, channel_id=None, page_no=None, page_size=None, request_headers:Dict={}):
        """Get Bags for the order
        :param bag_ids : Comma separated values of bag ids : type string
        :param shipment_ids : Comma separated values of shipment ids : type string
        :param order_ids : Comma separated values of order ids : type string
        :param channel_bag_ids : Comma separated values of app bag ids : type string
        :param channel_shipment_ids : Comma separated values of app shipment ids : type string
        :param channel_order_ids : Comma separated values of app order ids : type string
        :param channel_id : Comma separated values of app ids : type string
        :param page_no : Page number for paginated data : type integer
        :param page_size : Page size of data received per page : type integer
        """
        payload = {}
        
        if bag_ids is not None:
            payload["bag_ids"] = bag_ids
        if shipment_ids is not None:
            payload["shipment_ids"] = shipment_ids
        if order_ids is not None:
            payload["order_ids"] = order_ids
        if channel_bag_ids is not None:
            payload["channel_bag_ids"] = channel_bag_ids
        if channel_shipment_ids is not None:
            payload["channel_shipment_ids"] = channel_shipment_ids
        if channel_order_ids is not None:
            payload["channel_order_ids"] = channel_order_ids
        if channel_id is not None:
            payload["channel_id"] = channel_id
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = OrderValidator.getBags()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/bags", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"bag_ids","description":"Comma separated values of bag ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"shipment_ids","description":"Comma separated values of shipment ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"order_ids","description":"Comma separated values of order ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_bag_ids","description":"Comma separated values of app bag ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_shipment_ids","description":"Comma separated values of app shipment ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_order_ids","description":"Comma separated values of app order ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_id","description":"Comma separated values of app ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","description":"Page number for paginated data","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","description":"Page size of data received per page","required":false,"schema":{"type":"integer"}}],"query":[{"in":"query","name":"bag_ids","description":"Comma separated values of bag ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"shipment_ids","description":"Comma separated values of shipment ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"order_ids","description":"Comma separated values of order ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_bag_ids","description":"Comma separated values of app bag ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_shipment_ids","description":"Comma separated values of app shipment ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_order_ids","description":"Comma separated values of app order ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_id","description":"Comma separated values of app ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","description":"Page number for paginated data","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","description":"Page size of data received per page","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", bag_ids=bag_ids, shipment_ids=shipment_ids, order_ids=order_ids, channel_bag_ids=channel_bag_ids, channel_shipment_ids=channel_shipment_ids, channel_order_ids=channel_order_ids, channel_id=channel_id, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(bag_ids=bag_ids, shipment_ids=shipment_ids, order_ids=order_ids, channel_bag_ids=channel_bag_ids, channel_shipment_ids=channel_shipment_ids, channel_order_ids=channel_order_ids, channel_id=channel_id, page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/bags", bag_ids=bag_ids, shipment_ids=shipment_ids, order_ids=order_ids, channel_bag_ids=channel_bag_ids, channel_shipment_ids=channel_shipment_ids, channel_order_ids=channel_order_ids, channel_id=channel_id, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetBagsPlatformResponse
            schema = GetBagsPlatformResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBags")
                print(e)

        return response
    
    async def generatePOSReceiptByOrderId(self, order_id=None, shipment_id=None, document_type=None, request_headers:Dict={}):
        """Create a point-of-sale (POS) receipt for a specific order by order Id.
        :param order_id :  : type string
        :param shipment_id :  : type string
        :param document_type :  : type string
        """
        payload = {}
        
        if order_id is not None:
            payload["order_id"] = order_id
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id
        if document_type is not None:
            payload["document_type"] = document_type

        # Parameter validation
        schema = OrderValidator.generatePOSReceiptByOrderId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders/{order_id}/generate/pos-receipt", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"path","name":"order_id","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"shipment_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"document_type","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"shipment_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"document_type","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"path","name":"order_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", order_id=order_id, shipment_id=shipment_id, document_type=document_type)
        query_string = await create_query_string(shipment_id=shipment_id, document_type=document_type)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders/{order_id}/generate/pos-receipt", order_id=order_id, shipment_id=shipment_id, document_type=document_type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GeneratePosOrderReceiptResponse
            schema = GeneratePosOrderReceiptResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for generatePOSReceiptByOrderId")
                print(e)

        return response
    
    async def getAllowedTemplatesForBulk(self, request_headers:Dict={}):
        """Gets All the allowed Templates to perform Bulk Operations.
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.getAllowedTemplatesForBulk()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/jobs/templates", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/jobs/templates", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AllowedTemplatesResponse
            schema = AllowedTemplatesResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAllowedTemplatesForBulk")
                print(e)

        return response
    
    async def getTemplate(self, template_name=None, request_headers:Dict={}):
        """Get the Excel or CSV file URL for the Template.
        :param template_name :  : type string
        """
        payload = {}
        
        if template_name is not None:
            payload["template_name"] = template_name

        # Parameter validation
        schema = OrderValidator.getTemplate()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/jobs/templates/{template_name}", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"path","name":"template_name","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"path","name":"template_name","required":true,"schema":{"type":"string"}}]}""", serverType="platform", template_name=template_name)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/jobs/templates/{template_name}", template_name=template_name), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TemplateDownloadResponse
            schema = TemplateDownloadResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getTemplate")
                print(e)

        return response
    