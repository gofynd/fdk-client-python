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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/update-cache", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform","schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform","schema":{"type":"integer"}}]}""", serverType="platform", )
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
    
    async def reassignLocation(self, body="", request_headers:Dict={}):
        """Reassign the shipment to a another location and update its status to 'Store Reassigned.'
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.reassignLocation()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import StoreReassign
        schema = StoreReassign()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/store/reassign-internal", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}]}""", serverType="platform", )
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
    
    async def updateShipmentLock(self, body="", request_headers:Dict={}):
        """Modify shipment/bag lock status and update lock/unlock messages.
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.updateShipmentLock()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateShipmentLockPayload
        schema = UpdateShipmentLockPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/entity/lock-manager", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of a company on the platform.","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of a company on the platform.","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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
    
    async def getAnnouncements(self, date=None, request_headers:Dict={}):
        """Retrieve announcements related to orders fulfilment configured by platform or company admin
        :param date : Date On which the announcement is Active. : type string
        """
        payload = {}
        
        if date is not None:
            payload["date"] = date

        # Parameter validation
        schema = OrderValidator.getAnnouncements()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/announcements", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}],"optional":[{"in":"query","name":"date","required":false,"description":"Date On which the announcement is Active.","schema":{"type":"string"}}],"query":[{"in":"query","name":"date","required":false,"description":"Date On which the announcement is Active.","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}]}""", serverType="platform", date=date)
        query_string = await create_query_string(date=date)

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
    
    async def updateAddress(self, shipment_id=None, name=None, address=None, address_type=None, pincode=None, phone=None, email=None, landmark=None, address_category=None, city=None, state=None, country=None, request_headers:Dict={}):
        """Modify the address details of an existing shipment
        :param shipment_id :  : type string
        :param name :  : type string
        :param address :  : type string
        :param address_type :  : type string
        :param pincode :  : type string
        :param phone :  : type string
        :param email :  : type string
        :param landmark :  : type string
        :param address_category :  : type string
        :param city :  : type string
        :param state :  : type string
        :param country :  : type string
        """
        payload = {}
        
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id
        if name is not None:
            payload["name"] = name
        if address is not None:
            payload["address"] = address
        if address_type is not None:
            payload["address_type"] = address_type
        if pincode is not None:
            payload["pincode"] = pincode
        if phone is not None:
            payload["phone"] = phone
        if email is not None:
            payload["email"] = email
        if landmark is not None:
            payload["landmark"] = landmark
        if address_category is not None:
            payload["address_category"] = address_category
        if city is not None:
            payload["city"] = city
        if state is not None:
            payload["state"] = state
        if country is not None:
            payload["country"] = country

        # Parameter validation
        schema = OrderValidator.updateAddress()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/delight/update-address", """{"required":[{"in":"query","name":"shipment_id","required":true,"schema":{"type":"string"}},{"in":"query","name":"address_category","required":true,"schema":{"type":"string"}},{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"name","required":false,"schema":{"type":"string"}},{"in":"query","name":"address","required":false,"schema":{"type":"string"}},{"in":"query","name":"address_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"pincode","required":false,"schema":{"type":"string"}},{"in":"query","name":"phone","required":false,"schema":{"type":"string"}},{"in":"query","name":"email","required":false,"schema":{"type":"string"}},{"in":"query","name":"landmark","required":false,"schema":{"type":"string"}},{"in":"query","name":"city","required":false,"schema":{"type":"string"}},{"in":"query","name":"state","required":false,"schema":{"type":"string"}},{"in":"query","name":"country","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"shipment_id","required":true,"schema":{"type":"string"}},{"in":"query","name":"name","required":false,"schema":{"type":"string"}},{"in":"query","name":"address","required":false,"schema":{"type":"string"}},{"in":"query","name":"address_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"pincode","required":false,"schema":{"type":"string"}},{"in":"query","name":"phone","required":false,"schema":{"type":"string"}},{"in":"query","name":"email","required":false,"schema":{"type":"string"}},{"in":"query","name":"landmark","required":false,"schema":{"type":"string"}},{"in":"query","name":"address_category","required":true,"schema":{"type":"string"}},{"in":"query","name":"city","required":false,"schema":{"type":"string"}},{"in":"query","name":"state","required":false,"schema":{"type":"string"}},{"in":"query","name":"country","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", shipment_id=shipment_id, name=name, address=address, address_type=address_type, pincode=pincode, phone=phone, email=email, landmark=landmark, address_category=address_category, city=city, state=state, country=country, )
        query_string = await create_query_string(shipment_id=shipment_id, name=name, address=address, address_type=address_type, pincode=pincode, phone=phone, email=email, landmark=landmark, address_category=address_category, city=city, state=state, country=country, )

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/delight/update-address", shipment_id=shipment_id, name=name, address=address, address_type=address_type, pincode=pincode, phone=phone, email=email, landmark=landmark, address_category=address_category, city=city, state=state, country=country), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BaseResponse
            schema = BaseResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAddress")
                print(e)

        return response
    
    async def updateShipmentStatus(self, body="", request_headers:Dict={}):
        """Used for updating a shipment and its status. Can also be used for updating bags present in that shipment.
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.updateShipmentStatus()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateShipmentStatusRequestSchema
        schema = UpdateShipmentStatusRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/shipment/status-internal", """{"required":[{"in":"path","name":"company_id","description":"company id from where are transitioning the shipment state or data","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"company id from where are transitioning the shipment state or data","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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
    
    async def getRoleBasedActions(self, request_headers:Dict={}):
        """Retrieve permissible actions based on user roles such as company_admin,  company_operation, customer_care, and read_only.
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.getRoleBasedActions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/roles", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of a company on the platform.","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of a company on the platform.","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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
    
    async def getShipmentHistory(self, shipment_id=None, bag_id=None, request_headers:Dict={}):
        """Get the history of the shipment
        :param shipment_id : Identifier for the shipment : type string
        :param bag_id : Identifier for a bag or product. : type integer
        """
        payload = {}
        
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id
        if bag_id is not None:
            payload["bag_id"] = bag_id

        # Parameter validation
        schema = OrderValidator.getShipmentHistory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/shipment/history", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}],"optional":[{"in":"query","name":"shipment_id","description":"Identifier for the shipment","required":false,"schema":{"type":"string"}},{"in":"query","name":"bag_id","description":"Identifier for a bag or product.","required":false,"schema":{"type":"integer"}}],"query":[{"in":"query","name":"shipment_id","description":"Identifier for the shipment","required":false,"schema":{"type":"string"}},{"in":"query","name":"bag_id","description":"Identifier for a bag or product.","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}]}""", serverType="platform", shipment_id=shipment_id, bag_id=bag_id)
        query_string = await create_query_string(shipment_id=shipment_id, bag_id=bag_id)

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
        """Used to add logs in history for a bag for the provided Shipment ID
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/ninja/send-sms", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/ninja/send-sms", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BaseResponse
            schema = BaseResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for sendSmsNinja")
                print(e)

        return response
    
    async def updatePackagingDimensions(self, body="", request_headers:Dict={}):
        """Used to modify the packaging dimension of a shipment
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.updatePackagingDimensions()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdatePackagingDimensionsPayload
        schema = UpdatePackagingDimensionsPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/update-packaging-dimension", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}]}""", serverType="platform", )
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
    
    async def createOrder(self, body="", request_headers:Dict={}):
        """Creates an order
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.createOrder()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateOrderAPI
        schema = CreateOrderAPI()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/create-order", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"},"description":"Unique identifier of a company on the platform."}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"},"description":"Unique identifier of a company on the platform."}]}""", serverType="platform", )
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/order/validation", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}]}""", serverType="platform", )
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
    
    async def checkOrderStatus(self, body="", request_headers:Dict={}):
        """Used to verify the status of order. It queries error logs, resyncs the shipments if there was an issue with sync etc.
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.checkOrderStatus()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OrderStatus
        schema = OrderStatus()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/debug/order_status", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}]}""", serverType="platform", )
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
    
    async def getStateTransitionMap(self, request_headers:Dict={}):
        """Retrieve a map of state transitions for orders
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.getStateTransitionMap()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/bag/state/transition", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}]}""", serverType="platform", )
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
        """Retrieve next possible states based on logged in user's role
        :param ordering_channel : The channel through which orders are placed. : type string
        :param status : The status key indicates the current status for which the API will provide a list of possible next state transitions. : type string
        """
        payload = {}
        
        if ordering_channel is not None:
            payload["ordering_channel"] = ordering_channel
        if status is not None:
            payload["status"] = status

        # Parameter validation
        schema = OrderValidator.getAllowedStateTransition()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/allowed/state/transition", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of a company on the platform.","required":true,"schema":{"type":"integer"}},{"in":"query","name":"ordering_channel","description":"The channel through which orders are placed.","required":true,"schema":{"type":"string","enum":["fynd","affiliate"]}},{"in":"query","name":"status","description":"The status key indicates the current status for which the API will provide a list of possible next state transitions.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"in":"query","name":"ordering_channel","description":"The channel through which orders are placed.","required":true,"schema":{"type":"string","enum":["fynd","affiliate"]}},{"in":"query","name":"status","description":"The status key indicates the current status for which the API will provide a list of possible next state transitions.","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of a company on the platform.","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", ordering_channel=ordering_channel, status=status)
        query_string = await create_query_string(ordering_channel=ordering_channel, status=status)

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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/refund-mode-config", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of a company on the platform.","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of a company on the platform.","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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
        """Attach an anonymous order to a customer based on OTP verification
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.attachOrderUser()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AttachOrderUser
        schema = AttachOrderUser()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/user/attach", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}]}""", serverType="platform", )
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
        """Send a one-time OTP to a customer mobile number
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.sendUserMobileOTP()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SendUserMobileOTP
        schema = SendUserMobileOTP()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/user/send/otp/mobile", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}]}""", serverType="platform", )
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
        """Perform OTP verification to link a user to an anonymous order
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.verifyMobileOTP()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import VerifyMobileOTP
        schema = VerifyMobileOTP()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/user/verify/otp", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}]}""", serverType="platform", )
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/reports/lanes/download", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}]}""", serverType="platform", )
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
        """Performs state transisiton in bulk using the CSV or excel file for the given shipments. The bulk transition CSV or excel template can be downloaded using the seller template download method. Current supported format is excel and CSV.
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.bulkStateTransistion()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkStateTransistionRequestSchema
        schema = BulkStateTransistionRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/jobs/state-transition", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}]}""", serverType="platform", )
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
        """Get list of bulk operation that is initiated and completed as per the filters provided
        :param page_size : The number of records to return per page in the response. : type integer
        :param page_no : The page number to fetch from the paginated results. : type integer
        :param start_date : The start date for filtering the jobs, expressed in UTC format : type string
        :param end_date : The end date for filtering the jobs, expressed in UTC format : type string
        :param status : The status of the jobs to filter the results. : type string
        :param bulk_action_type : pecifies the type of job action being requested. : type string
        :param search_key : A key or keyword used to search for specific jobs. : type string
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/jobs", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of a company on the platform.","required":true,"schema":{"type":"integer"}},{"in":"query","name":"page_size","description":"The number of records to return per page in the response.","required":true,"schema":{"type":"integer"}},{"in":"query","name":"page_no","description":"The page number to fetch from the paginated results.","required":true,"schema":{"type":"integer"}},{"in":"query","name":"start_date","description":"The start date for filtering the jobs, expressed in UTC format","required":true,"schema":{"type":"string","format":"date-time"}},{"in":"query","name":"end_date","description":"The end date for filtering the jobs, expressed in UTC format","required":true,"schema":{"type":"string","format":"date-time"}}],"optional":[{"in":"query","name":"status","description":"The status of the jobs to filter the results.","required":false,"schema":{"type":"string","enum":["ALL","COMPLETED","FAILED","PARTIALLY COMPLETED","PROCESSING"]}},{"in":"query","name":"bulk_action_type","description":"pecifies the type of job action being requested.","required":false,"schema":{"type":"string","enum":["order_processing","invoice_label","reports"]}},{"in":"query","name":"search_key","description":"A key or keyword used to search for specific jobs.","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"page_size","description":"The number of records to return per page in the response.","required":true,"schema":{"type":"integer"}},{"in":"query","name":"page_no","description":"The page number to fetch from the paginated results.","required":true,"schema":{"type":"integer"}},{"in":"query","name":"start_date","description":"The start date for filtering the jobs, expressed in UTC format","required":true,"schema":{"type":"string","format":"date-time"}},{"in":"query","name":"end_date","description":"The end date for filtering the jobs, expressed in UTC format","required":true,"schema":{"type":"string","format":"date-time"}},{"in":"query","name":"status","description":"The status of the jobs to filter the results.","required":false,"schema":{"type":"string","enum":["ALL","COMPLETED","FAILED","PARTIALLY COMPLETED","PROCESSING"]}},{"in":"query","name":"bulk_action_type","description":"pecifies the type of job action being requested.","required":false,"schema":{"type":"string","enum":["order_processing","invoice_label","reports"]}},{"in":"query","name":"search_key","description":"A key or keyword used to search for specific jobs.","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of a company on the platform.","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", page_size=page_size, page_no=page_no, start_date=start_date, end_date=end_date, status=status, bulk_action_type=bulk_action_type, search_key=search_key)
        query_string = await create_query_string(page_size=page_size, page_no=page_no, start_date=start_date, end_date=end_date, status=status, bulk_action_type=bulk_action_type, search_key=search_key)

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
        """Fetches details of the job for the provided batch Id
        :param batch_id : A unique identifier for the batch associated with this bulk action. : type string
        """
        payload = {}
        
        if batch_id is not None:
            payload["batch_id"] = batch_id

        # Parameter validation
        schema = OrderValidator.jobDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/jobs/{batch_id}", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}},{"in":"path","name":"batch_id","required":true,"description":"A unique identifier for the batch associated with this bulk action.","schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}},{"in":"path","name":"batch_id","required":true,"description":"A unique identifier for the batch associated with this bulk action.","schema":{"type":"string"}}]}""", serverType="platform", batch_id=batch_id)
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
        :param batch_id : Batch Id to identify the bulk operation request. : type string
        :param status : The status of the jobs to filter the results. : type string
        :param file_type : The type of file to be downloaded. : type string
        :param report_type : The type of report to be downloaded. : type string
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/jobs/{batch_id}/file", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"},"description":"Unique identifier of a company on the platform."},{"in":"path","name":"batch_id","required":true,"description":"Batch Id to identify the bulk operation request.","schema":{"type":"string"}},{"in":"query","name":"status","required":true,"schema":{"type":"string"},"description":"The status of the jobs to filter the results."},{"in":"query","name":"file_type","required":true,"description":"The type of file to be downloaded.","schema":{"type":"string","default":"xlsx","enum":["xlsx","csv"]}}],"optional":[{"in":"query","name":"report_type","description":"The type of report to be downloaded.","schema":{"type":"string","default":"generation_report","enum":["generation_report","invoice_report"]}}],"query":[{"in":"query","name":"status","required":true,"schema":{"type":"string"},"description":"The status of the jobs to filter the results."},{"in":"query","name":"file_type","required":true,"description":"The type of file to be downloaded.","schema":{"type":"string","default":"xlsx","enum":["xlsx","csv"]}},{"in":"query","name":"report_type","description":"The type of report to be downloaded.","schema":{"type":"string","default":"generation_report","enum":["generation_report","invoice_report"]}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"},"description":"Unique identifier of a company on the platform."},{"in":"path","name":"batch_id","required":true,"description":"Batch Id to identify the bulk operation request.","schema":{"type":"string"}}]}""", serverType="platform", batch_id=batch_id, status=status, file_type=file_type, report_type=report_type)
        query_string = await create_query_string(status=status, file_type=file_type, report_type=report_type)

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
    
    async def getManifestShipments(self, dp_ids=None, stores=None, to_date=None, from_date=None, dp_name=None, sales_channels=None, search_type=None, search_value=None, page_no=None, page_size=None, request_headers:Dict={}):
        """Get list of shipments tagged to that manifest, the user can also search the shipments on the basis of shipment Id, order Id and AWB number
        :param dp_ids : Filter shipments with the specific Courier partner Ids which is a combination of courier partner extension and scheme Ids. : type string
        :param stores : Filter results based on specific store IDs. : type integer
        :param to_date : End date for the shipment search range. : type string
        :param from_date : Start date for the shipment search range. : type string
        :param dp_name : Filter results based on specific courier partner name. : type string
        :param sales_channels : Filter results based on comma-separated list of sales channels. : type string
        :param search_type : Filter results based on search type. : type string
        :param search_value : Filter results based on the search value. : type string
        :param page_no : Page number for pagination. : type integer
        :param page_size : Number of records per page for pagination. : type integer
        """
        payload = {}
        
        if dp_ids is not None:
            payload["dp_ids"] = dp_ids
        if stores is not None:
            payload["stores"] = stores
        if to_date is not None:
            payload["to_date"] = to_date
        if from_date is not None:
            payload["from_date"] = from_date
        if dp_name is not None:
            payload["dp_name"] = dp_name
        if sales_channels is not None:
            payload["sales_channels"] = sales_channels
        if search_type is not None:
            payload["search_type"] = search_type
        if search_value is not None:
            payload["search_value"] = search_value
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = OrderValidator.getManifestShipments()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/manifest/shipments-listing", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of a company on the platform.","required":true,"schema":{"type":"integer"}},{"in":"query","name":"dp_ids","description":"Filter shipments with the specific Courier partner Ids which is a combination of courier partner extension and scheme Ids.","required":true,"schema":{"type":"string"}},{"in":"query","name":"stores","description":"Filter results based on specific store IDs.","required":true,"schema":{"type":"integer"}},{"in":"query","name":"to_date","description":"End date for the shipment search range.","required":true,"schema":{"type":"string","format":"date-time"}},{"in":"query","name":"from_date","description":"Start date for the shipment search range.","required":true,"schema":{"type":"string","format":"date-time"}}],"optional":[{"in":"query","name":"dp_name","description":"Filter results based on specific courier partner name.","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channels","description":"Filter results based on comma-separated list of sales channels.","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_type","description":"Filter results based on search type.","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_value","description":"Filter results based on the search value.","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","description":"Page number for pagination.","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","description":"Number of records per page for pagination.","required":false,"schema":{"type":"integer"}}],"query":[{"in":"query","name":"dp_ids","description":"Filter shipments with the specific Courier partner Ids which is a combination of courier partner extension and scheme Ids.","required":true,"schema":{"type":"string"}},{"in":"query","name":"stores","description":"Filter results based on specific store IDs.","required":true,"schema":{"type":"integer"}},{"in":"query","name":"to_date","description":"End date for the shipment search range.","required":true,"schema":{"type":"string","format":"date-time"}},{"in":"query","name":"from_date","description":"Start date for the shipment search range.","required":true,"schema":{"type":"string","format":"date-time"}},{"in":"query","name":"dp_name","description":"Filter results based on specific courier partner name.","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channels","description":"Filter results based on comma-separated list of sales channels.","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_type","description":"Filter results based on search type.","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_value","description":"Filter results based on the search value.","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","description":"Page number for pagination.","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","description":"Number of records per page for pagination.","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of a company on the platform.","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", dp_ids=dp_ids, stores=stores, to_date=to_date, from_date=from_date, dp_name=dp_name, sales_channels=sales_channels, search_type=search_type, search_value=search_value, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(dp_ids=dp_ids, stores=stores, to_date=to_date, from_date=from_date, dp_name=dp_name, sales_channels=sales_channels, search_type=search_type, search_value=search_value, page_no=page_no, page_size=page_size)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/manifest/shipments-listing", dp_ids=dp_ids, stores=stores, to_date=to_date, from_date=from_date, dp_name=dp_name, sales_channels=sales_channels, search_type=search_type, search_value=search_value, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ManifestShipmentListing
            schema = ManifestShipmentListing()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getManifestShipments")
                print(e)

        return response
    
    async def getManifests(self, status=None, start_date=None, end_date=None, search_type=None, store_id=None, search_value=None, dp_ids=None, page_no=None, page_size=None, request_headers:Dict={}):
        """Get a list of manifest as per the filter provided
        :param status : Filter for the status of manifests. : type string
        :param start_date : The starting date for filtering manifests in ISO format : type string
        :param end_date : The end date for filtering manifests in ISO format : type string
        :param search_type : Specifies the type of search to perform. : type string
        :param store_id : Filter to fetch manifests for a specific store by its ID. : type integer
        :param search_value : The value to search for based on the selected search type. : type string
        :param dp_ids : A comma-separated list of courier partner IDs (DP IDs) to filter the manifests. : type string
        :param page_no : The number of the page to fetch data. : type integer
        :param page_size : The number of records to return per page for pagination. : type integer
        """
        payload = {}
        
        if status is not None:
            payload["status"] = status
        if start_date is not None:
            payload["start_date"] = start_date
        if end_date is not None:
            payload["end_date"] = end_date
        if search_type is not None:
            payload["search_type"] = search_type
        if store_id is not None:
            payload["store_id"] = store_id
        if search_value is not None:
            payload["search_value"] = search_value
        if dp_ids is not None:
            payload["dp_ids"] = dp_ids
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = OrderValidator.getManifests()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/manifest/listing", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier for the company on the platform.","schema":{"type":"integer"}}],"optional":[{"in":"query","name":"status","required":false,"description":"Filter for the status of manifests.","schema":{"type":"string","enum":["active","closed"],"default":"active"}},{"in":"query","name":"start_date","description":"The starting date for filtering manifests in ISO format","required":false,"schema":{"type":"string"}},{"in":"query","name":"end_date","description":"The end date for filtering manifests in ISO format","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_type","required":false,"description":"Specifies the type of search to perform.","schema":{"type":"string","enum":["fynd_order_id","shipment_id","manifest_id","dp_name","awb_no"]}},{"in":"query","name":"store_id","required":false,"description":"Filter to fetch manifests for a specific store by its ID.","schema":{"type":"integer"}},{"in":"query","name":"search_value","required":false,"description":"The value to search for based on the selected search type.","schema":{"type":"string"}},{"in":"query","name":"dp_ids","required":false,"description":"A comma-separated list of courier partner IDs (DP IDs) to filter the manifests.","schema":{"type":"string"}},{"in":"query","name":"page_no","required":false,"description":"The number of the page to fetch data.","schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"},"description":"The number of records to return per page for pagination."}],"query":[{"in":"query","name":"status","required":false,"description":"Filter for the status of manifests.","schema":{"type":"string","enum":["active","closed"],"default":"active"}},{"in":"query","name":"start_date","description":"The starting date for filtering manifests in ISO format","required":false,"schema":{"type":"string"}},{"in":"query","name":"end_date","description":"The end date for filtering manifests in ISO format","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_type","required":false,"description":"Specifies the type of search to perform.","schema":{"type":"string","enum":["fynd_order_id","shipment_id","manifest_id","dp_name","awb_no"]}},{"in":"query","name":"store_id","required":false,"description":"Filter to fetch manifests for a specific store by its ID.","schema":{"type":"integer"}},{"in":"query","name":"search_value","required":false,"description":"The value to search for based on the selected search type.","schema":{"type":"string"}},{"in":"query","name":"dp_ids","required":false,"description":"A comma-separated list of courier partner IDs (DP IDs) to filter the manifests.","schema":{"type":"string"}},{"in":"query","name":"page_no","required":false,"description":"The number of the page to fetch data.","schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"},"description":"The number of records to return per page for pagination."}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier for the company on the platform.","schema":{"type":"integer"}}]}""", serverType="platform", status=status, start_date=start_date, end_date=end_date, search_type=search_type, store_id=store_id, search_value=search_value, dp_ids=dp_ids, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(status=status, start_date=start_date, end_date=end_date, search_type=search_type, store_id=store_id, search_value=search_value, dp_ids=dp_ids, page_no=page_no, page_size=page_size)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/manifest/listing", status=status, start_date=start_date, end_date=end_date, search_type=search_type, store_id=store_id, search_value=search_value, dp_ids=dp_ids, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ManifestList
            schema = ManifestList()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getManifests")
                print(e)

        return response
    
    async def generateProcessManifest(self, body="", request_headers:Dict={}):
        """Endpoint to save and process order manifests.
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.generateProcessManifest()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ProcessManifestRequest
        schema = ProcessManifestRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/process-manifest", """{"required":[{"name":"company_id","in":"path","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/process-manifest", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ManifestResponse
            schema = ManifestResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for generateProcessManifest")
                print(e)

        return response
    
    async def getManifestDetails(self, manifest_id=None, dp_ids=None, end_date=None, start_date=None, page_no=None, page_size=None, request_headers:Dict={}):
        """Get details regarding a manifest which can be used to perform further actions on it
        :param manifest_id : The unique identifier assigned to the manifest. : type string
        :param dp_ids : Filter shipments with the specific Courier partner Ids which is a combination of courier partner extension and scheme Ids. : type string
        :param end_date : End date for the shipment search range in manifest. : type string
        :param start_date : Start date for the shipment search range in manifest. : type string
        :param page_no : Page number for pagination. : type integer
        :param page_size : Number of records per page for pagination. : type integer
        """
        payload = {}
        
        if manifest_id is not None:
            payload["manifest_id"] = manifest_id
        if dp_ids is not None:
            payload["dp_ids"] = dp_ids
        if end_date is not None:
            payload["end_date"] = end_date
        if start_date is not None:
            payload["start_date"] = start_date
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = OrderValidator.getManifestDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/manifest/details", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"},"description":"Unique identifier of a company on the platform."},{"in":"query","name":"manifest_id","description":"The unique identifier assigned to the manifest.","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"dp_ids","description":"Filter shipments with the specific Courier partner Ids which is a combination of courier partner extension and scheme Ids.","required":false,"schema":{"type":"string"}},{"in":"query","name":"end_date","description":"End date for the shipment search range in manifest.","required":false,"schema":{"type":"string","format":"date-time"}},{"in":"query","name":"start_date","description":"Start date for the shipment search range in manifest.","required":false,"schema":{"type":"string","format":"date-time"}},{"in":"query","name":"page_no","description":"Page number for pagination.","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","description":"Number of records per page for pagination.","required":false,"schema":{"type":"integer"}}],"query":[{"in":"query","name":"manifest_id","description":"The unique identifier assigned to the manifest.","required":true,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","description":"Filter shipments with the specific Courier partner Ids which is a combination of courier partner extension and scheme Ids.","required":false,"schema":{"type":"string"}},{"in":"query","name":"end_date","description":"End date for the shipment search range in manifest.","required":false,"schema":{"type":"string","format":"date-time"}},{"in":"query","name":"start_date","description":"Start date for the shipment search range in manifest.","required":false,"schema":{"type":"string","format":"date-time"}},{"in":"query","name":"page_no","description":"Page number for pagination.","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","description":"Number of records per page for pagination.","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"},"description":"Unique identifier of a company on the platform."}]}""", serverType="platform", manifest_id=manifest_id, dp_ids=dp_ids, end_date=end_date, start_date=start_date, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(manifest_id=manifest_id, dp_ids=dp_ids, end_date=end_date, start_date=start_date, page_no=page_no, page_size=page_size)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/manifest/details", manifest_id=manifest_id, dp_ids=dp_ids, end_date=end_date, start_date=start_date, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ManifestDetails
            schema = ManifestDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getManifestDetails")
                print(e)

        return response
    
    async def dispatchManifests(self, body="", request_headers:Dict={}):
        """Updates the status of the manifest to processed and change the status of the shipments in the manifest to dispatch status
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.dispatchManifests()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DispatchManifest
        schema = DispatchManifest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/manifest/dispatch", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/manifest/dispatch", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponse
            schema = SuccessResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for dispatchManifests")
                print(e)

        return response
    
    async def uploadConsents(self, body="", request_headers:Dict={}):
        """Uploads the consent signed by courier partner and seller to keep records
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.uploadConsents()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UploadManifestConsent
        schema = UploadManifestConsent()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/manifest/uploadConsent", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/manifest/uploadConsent", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponse
            schema = SuccessResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for uploadConsents")
                print(e)

        return response
    
    async def getManifestfilters(self, view=None, request_headers:Dict={}):
        """Get supported filter for listing manifests
        :param view : Name of View : type string
        """
        payload = {}
        
        if view is not None:
            payload["view"] = view

        # Parameter validation
        schema = OrderValidator.getManifestfilters()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/filter/listing", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of a company on the platform.","required":true,"schema":{"type":"integer"}},{"in":"query","name":"view","description":"Name of View","required":true,"schema":{"type":"string","default":"manifest","enum":["my_orders","bulk_action","manifest","bulk_invoice"]}}],"optional":[],"query":[{"in":"query","name":"view","description":"Name of View","required":true,"schema":{"type":"string","default":"manifest","enum":["my_orders","bulk_action","manifest","bulk_invoice"]}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of a company on the platform.","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", view=view)
        query_string = await create_query_string(view=view)

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
        """Reattempt the generation of an E-invoice
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
        """Retrieve courier partner tracking details for a given shipment Id or AWB number
        :param shipment_id : Unique identifier of a shipment on the platform. : type string
        :param awb : AWB number : type string
        :param page_no : Page number for pagination. : type integer
        :param page_size : Number of records per page for pagination. : type integer
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/tracking", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of a company on the platform.","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"shipment_id","description":"Unique identifier of a shipment on the platform.","required":false,"schema":{"type":"string"}},{"in":"query","name":"awb","required":false,"description":"AWB number","schema":{"type":"string"}},{"in":"query","name":"page_no","description":"Page number for pagination.","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","description":"Number of records per page for pagination.","required":false,"schema":{"type":"integer"}}],"query":[{"in":"query","name":"shipment_id","description":"Unique identifier of a shipment on the platform.","required":false,"schema":{"type":"string"}},{"in":"query","name":"awb","required":false,"description":"AWB number","schema":{"type":"string"}},{"in":"query","name":"page_no","description":"Page number for pagination.","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","description":"Number of records per page for pagination.","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of a company on the platform.","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", shipment_id=shipment_id, awb=awb, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(shipment_id=shipment_id, awb=awb, page_no=page_no, page_size=page_size)

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
        """Modify courier partner tracking details for a given shipment Id or AWB number
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.updateShipmentTracking()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CourierPartnerTrackingDetails
        schema = CourierPartnerTrackingDetails()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/tracking", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Unique identifier of a company on the platform.","schema":{"type":"integer"}}]}""", serverType="platform", )
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
    
    async def generateInvoiceID(self, invoice_type=None, body="", request_headers:Dict={}):
        """Generate and attach Invoice Ids against shipments.
        :param invoice_type : mention the type of invoice id to generate : type string
        """
        payload = {}
        
        if invoice_type is not None:
            payload["invoice_type"] = invoice_type

        # Parameter validation
        schema = OrderValidator.generateInvoiceID()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GenerateInvoiceIDRequestSchema
        schema = GenerateInvoiceIDRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/{invoice_type}/id/generate", """{"required":[{"in":"path","name":"company_id","description":"company id from where are transitioning the shipment state or data","required":true,"schema":{"type":"integer"}},{"in":"path","name":"invoice_type","description":"mention the type of invoice id to generate","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"company id from where are transitioning the shipment state or data","required":true,"schema":{"type":"integer"}},{"in":"path","name":"invoice_type","description":"mention the type of invoice id to generate","required":true,"schema":{"type":"string"}}]}""", serverType="platform", invoice_type=invoice_type)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/{invoice_type}/id/generate", invoice_type=invoice_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GenerateInvoiceIDResponse
            schema = GenerateInvoiceIDResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for generateInvoiceID")
                print(e)

        return response
    
    async def failedOrderLogDetails(self, log_id=None, request_headers:Dict={}):
        """Get the exact error trace from the log Id provided in the failed order list API response 
        :param log_id : Log Error ID : type string
        """
        payload = {}
        
        if log_id is not None:
            payload["log_id"] = log_id

        # Parameter validation
        schema = OrderValidator.failedOrderLogDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/orders/failed/logs/{log_id}", """{"required":[{"in":"path","name":"company_id","description":"Company ID","required":true,"schema":{"type":"integer","example":2}},{"in":"path","name":"log_id","description":"Log Error ID","required":true,"schema":{"type":"string","example":"a3b6b771-38e6-4014-9b05-b8e4df5a3a89"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company ID","required":true,"schema":{"type":"integer","example":2}},{"in":"path","name":"log_id","description":"Log Error ID","required":true,"schema":{"type":"string","example":"a3b6b771-38e6-4014-9b05-b8e4df5a3a89"}}]}""", serverType="platform", log_id=log_id)
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
    
    async def addStateManagerConfig(self, body="", request_headers:Dict={}):
        """Update ESM config
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.addStateManagerConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import TransitionConfigPayload
        schema = TransitionConfigPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/state/manager/config", """{"required":[{"name":"company_id","in":"path","required":true,"description":"The Id Of The Company.","schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"description":"The Id Of The Company.","schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/state/manager/config", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ConfigUpdatedResponse
            schema = ConfigUpdatedResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addStateManagerConfig")
                print(e)

        return response
    
    async def getStateManagerConfig(self, app_id=None, ordering_channel=None, entity=None, request_headers:Dict={}):
        """This endpoint retrieves the ESM (Entity State Manager) configuration for a specific application within a company. The retrieval is based on parameters such as application ID, ordering channel, and entity type.
The ESM config stores order processing configuration. Each document in the ESM config collection of  Order Management System - OMS's database is a JSON object representing the configuration of a specific application ID. This includes filters, hooks, flags set on different state-transitions.  This configuration is picked and accordingly features are enabled. 

        :param app_id : The unique identifier of the application. : type string
        :param ordering_channel : The channel through which orders are placed. : type string
        :param entity : The entity for which the configuration is applied. : type string
        """
        payload = {}
        
        if app_id is not None:
            payload["app_id"] = app_id
        if ordering_channel is not None:
            payload["ordering_channel"] = ordering_channel
        if entity is not None:
            payload["entity"] = entity

        # Parameter validation
        schema = OrderValidator.getStateManagerConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/state/manager/config", """{"required":[{"name":"company_id","in":"path","required":true,"description":"The unique identifier of the company.","schema":{"type":"integer"}}],"optional":[{"name":"app_id","in":"query","required":false,"description":"The unique identifier of the application.","schema":{"type":"string"}},{"name":"ordering_channel","in":"query","required":false,"description":"The channel through which orders are placed.","schema":{"type":"string"}},{"name":"entity","in":"query","required":false,"description":"The entity for which the configuration is applied.","schema":{"type":"string"}}],"query":[{"name":"app_id","in":"query","required":false,"description":"The unique identifier of the application.","schema":{"type":"string"}},{"name":"ordering_channel","in":"query","required":false,"description":"The channel through which orders are placed.","schema":{"type":"string"}},{"name":"entity","in":"query","required":false,"description":"The entity for which the configuration is applied.","schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"description":"The unique identifier of the company.","schema":{"type":"integer"}}]}""", serverType="platform", app_id=app_id, ordering_channel=ordering_channel, entity=entity)
        query_string = await create_query_string(app_id=app_id, ordering_channel=ordering_channel, entity=entity)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/state/manager/config", app_id=app_id, ordering_channel=ordering_channel, entity=entity), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def getShipments(self, lane=None, bag_status=None, status_override_lane=None, time_to_dispatch=None, search_type=None, search_value=None, from_date=None, to_date=None, start_date=None, end_date=None, dp_ids=None, stores=None, sales_channels=None, page_no=None, page_size=None, fetch_active_shipment=None, allow_inactive=None, exclude_locked_shipments=None, payment_methods=None, channel_shipment_id=None, channel_order_id=None, custom_meta=None, ordering_channel=None, company_affiliate_tag=None, my_orders=None, platform_user_id=None, sort_type=None, show_cross_company_data=None, tags=None, customer_id=None, order_type=None, request_headers:Dict={}):
        """Get a list of shipments based on the filters provided
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

        # Parameter validation
        schema = OrderValidator.getShipments()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/shipments-listing", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer","example":37}}],"optional":[{"in":"query","name":"lane","description":"Name of lane for which data is to be fetched","required":false,"schema":{"type":"string","enum":["new","confirmed","to_be_packed","ready_for_dispatch","in_transit","handed_over_to_customer","delivered","cancelled","return_initiated","return_in_transit","return_delivered","return_accepted"],"example":"new"}},{"in":"query","name":"bag_status","description":"Comma separated values of bag statuses","required":false,"schema":{"type":"string","example":"placed, bag_confirmed, bag_invoiced"}},{"in":"query","name":"status_override_lane","description":"Use this flag to fetch by bag_status and override lane","required":false,"schema":{"type":"boolean","default":false}},{"in":"query","name":"time_to_dispatch","required":false,"schema":{"type":"integer","example":1,"enum":[1,-1]}},{"in":"query","name":"search_type","description":"Search type key","required":false,"schema":{"type":"string","example":"shipment_id"}},{"in":"query","name":"search_value","description":"Search type value","required":false,"schema":{"type":"string","example":"16578901076461551493K"}},{"in":"query","name":"from_date","description":"Start Date in DD-MM-YYYY format","required":false,"schema":{"type":"string","format":"date","example":"2023-05-10T00:00:00.000Z"}},{"in":"query","name":"to_date","description":"End Date in DD-MM-YYYY format","required":false,"schema":{"type":"string","format":"date","example":"2023-05-13T00:00:00.000Z"}},{"in":"query","name":"start_date","description":"UTC Start Date in ISO format","required":false,"schema":{"type":"string","format":"date-time","example":"2023-08-21T09:48:40.000Z"}},{"in":"query","name":"end_date","description":"UTC End Date in ISO format","required":false,"schema":{"type":"string","format":"date-time","example":"2023-08-21T09:48:40.000Z"}},{"in":"query","name":"dp_ids","description":"Comma separated values of delivery partner ids","required":false,"schema":{"type":"string","example":"19,26"}},{"in":"query","name":"stores","description":"Comma separated values of store ids","required":false,"schema":{"type":"string","example":"12,34"}},{"in":"query","name":"sales_channels","description":"Comma separated values of sales channel ids","required":false,"schema":{"type":"string","example":"000000000000000000000001,614b42d1ea943427b5f46d1e"}},{"in":"query","name":"page_no","description":"Page number for paginated data","required":false,"schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","description":"Page size of data received per page","required":false,"schema":{"type":"integer","default":10}},{"in":"query","name":"fetch_active_shipment","description":"flag to fetch active shipments","required":false,"schema":{"type":"boolean","default":true}},{"in":"query","name":"allow_inactive","description":"Flag to allow inactive shipments","required":false,"schema":{"type":"boolean","default":false}},{"in":"query","name":"exclude_locked_shipments","description":"flag to fetch locked shipments","required":false,"schema":{"type":"boolean","default":true}},{"in":"query","name":"payment_methods","description":"Comma separated values of payment methods","required":false,"schema":{"type":"string","example":"COD,PREPAID"}},{"in":"query","name":"channel_shipment_id","description":"App Shipment Id","required":false,"schema":{"type":"string","example":"16731535496121004000"}},{"in":"query","name":"channel_order_id","description":"App Order Id","required":false,"schema":{"type":"string","example":"FY63BA4C0D0125F8A075"}},{"in":"query","name":"custom_meta","required":false,"schema":{"type":"string"}},{"in":"query","name":"ordering_channel","required":false,"schema":{"type":"string"}},{"in":"query","name":"company_affiliate_tag","required":false,"schema":{"type":"string"}},{"in":"query","name":"my_orders","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"platform_user_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"sort_type","description":"Sort the result data on basis of input","required":false,"schema":{"type":"string","enum":["sla_asc","created_date_asc","created_date_desc"],"default":"sla_asc"}},{"in":"query","name":"show_cross_company_data","description":"Flag to view cross & non-cross company order","required":false,"schema":{"type":"boolean","default":false}},{"in":"query","name":"tags","description":"Comma separated values of tags","required":false,"schema":{"type":"string","example":"gifting,international"}},{"in":"query","name":"customer_id","required":false,"schema":{"type":"string","example":"63a2ce177e9f59d3166dd700"}},{"in":"query","name":"order_type","required":false,"schema":{"type":"string","example":"HomeDelivery"}}],"query":[{"in":"query","name":"lane","description":"Name of lane for which data is to be fetched","required":false,"schema":{"type":"string","enum":["new","confirmed","to_be_packed","ready_for_dispatch","in_transit","handed_over_to_customer","delivered","cancelled","return_initiated","return_in_transit","return_delivered","return_accepted"],"example":"new"}},{"in":"query","name":"bag_status","description":"Comma separated values of bag statuses","required":false,"schema":{"type":"string","example":"placed, bag_confirmed, bag_invoiced"}},{"in":"query","name":"status_override_lane","description":"Use this flag to fetch by bag_status and override lane","required":false,"schema":{"type":"boolean","default":false}},{"in":"query","name":"time_to_dispatch","required":false,"schema":{"type":"integer","example":1,"enum":[1,-1]}},{"in":"query","name":"search_type","description":"Search type key","required":false,"schema":{"type":"string","example":"shipment_id"}},{"in":"query","name":"search_value","description":"Search type value","required":false,"schema":{"type":"string","example":"16578901076461551493K"}},{"in":"query","name":"from_date","description":"Start Date in DD-MM-YYYY format","required":false,"schema":{"type":"string","format":"date","example":"2023-05-10T00:00:00.000Z"}},{"in":"query","name":"to_date","description":"End Date in DD-MM-YYYY format","required":false,"schema":{"type":"string","format":"date","example":"2023-05-13T00:00:00.000Z"}},{"in":"query","name":"start_date","description":"UTC Start Date in ISO format","required":false,"schema":{"type":"string","format":"date-time","example":"2023-08-21T09:48:40.000Z"}},{"in":"query","name":"end_date","description":"UTC End Date in ISO format","required":false,"schema":{"type":"string","format":"date-time","example":"2023-08-21T09:48:40.000Z"}},{"in":"query","name":"dp_ids","description":"Comma separated values of delivery partner ids","required":false,"schema":{"type":"string","example":"19,26"}},{"in":"query","name":"stores","description":"Comma separated values of store ids","required":false,"schema":{"type":"string","example":"12,34"}},{"in":"query","name":"sales_channels","description":"Comma separated values of sales channel ids","required":false,"schema":{"type":"string","example":"000000000000000000000001,614b42d1ea943427b5f46d1e"}},{"in":"query","name":"page_no","description":"Page number for paginated data","required":false,"schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","description":"Page size of data received per page","required":false,"schema":{"type":"integer","default":10}},{"in":"query","name":"fetch_active_shipment","description":"flag to fetch active shipments","required":false,"schema":{"type":"boolean","default":true}},{"in":"query","name":"allow_inactive","description":"Flag to allow inactive shipments","required":false,"schema":{"type":"boolean","default":false}},{"in":"query","name":"exclude_locked_shipments","description":"flag to fetch locked shipments","required":false,"schema":{"type":"boolean","default":true}},{"in":"query","name":"payment_methods","description":"Comma separated values of payment methods","required":false,"schema":{"type":"string","example":"COD,PREPAID"}},{"in":"query","name":"channel_shipment_id","description":"App Shipment Id","required":false,"schema":{"type":"string","example":"16731535496121004000"}},{"in":"query","name":"channel_order_id","description":"App Order Id","required":false,"schema":{"type":"string","example":"FY63BA4C0D0125F8A075"}},{"in":"query","name":"custom_meta","required":false,"schema":{"type":"string"}},{"in":"query","name":"ordering_channel","required":false,"schema":{"type":"string"}},{"in":"query","name":"company_affiliate_tag","required":false,"schema":{"type":"string"}},{"in":"query","name":"my_orders","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"platform_user_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"sort_type","description":"Sort the result data on basis of input","required":false,"schema":{"type":"string","enum":["sla_asc","created_date_asc","created_date_desc"],"default":"sla_asc"}},{"in":"query","name":"show_cross_company_data","description":"Flag to view cross & non-cross company order","required":false,"schema":{"type":"boolean","default":false}},{"in":"query","name":"tags","description":"Comma separated values of tags","required":false,"schema":{"type":"string","example":"gifting,international"}},{"in":"query","name":"customer_id","required":false,"schema":{"type":"string","example":"63a2ce177e9f59d3166dd700"}},{"in":"query","name":"order_type","required":false,"schema":{"type":"string","example":"HomeDelivery"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer","example":37}}]}""", serverType="platform", lane=lane, bag_status=bag_status, status_override_lane=status_override_lane, time_to_dispatch=time_to_dispatch, search_type=search_type, search_value=search_value, from_date=from_date, to_date=to_date, start_date=start_date, end_date=end_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, page_no=page_no, page_size=page_size, fetch_active_shipment=fetch_active_shipment, allow_inactive=allow_inactive, exclude_locked_shipments=exclude_locked_shipments, payment_methods=payment_methods, channel_shipment_id=channel_shipment_id, channel_order_id=channel_order_id, custom_meta=custom_meta, ordering_channel=ordering_channel, company_affiliate_tag=company_affiliate_tag, my_orders=my_orders, platform_user_id=platform_user_id, sort_type=sort_type, show_cross_company_data=show_cross_company_data, tags=tags, customer_id=customer_id, order_type=order_type)
        query_string = await create_query_string(lane=lane, bag_status=bag_status, status_override_lane=status_override_lane, time_to_dispatch=time_to_dispatch, search_type=search_type, search_value=search_value, from_date=from_date, to_date=to_date, start_date=start_date, end_date=end_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, page_no=page_no, page_size=page_size, fetch_active_shipment=fetch_active_shipment, allow_inactive=allow_inactive, exclude_locked_shipments=exclude_locked_shipments, payment_methods=payment_methods, channel_shipment_id=channel_shipment_id, channel_order_id=channel_order_id, custom_meta=custom_meta, ordering_channel=ordering_channel, company_affiliate_tag=company_affiliate_tag, my_orders=my_orders, platform_user_id=platform_user_id, sort_type=sort_type, show_cross_company_data=show_cross_company_data, tags=tags, customer_id=customer_id, order_type=order_type)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/shipments-listing", lane=lane, bag_status=bag_status, status_override_lane=status_override_lane, time_to_dispatch=time_to_dispatch, search_type=search_type, search_value=search_value, from_date=from_date, to_date=to_date, start_date=start_date, end_date=end_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, page_no=page_no, page_size=page_size, fetch_active_shipment=fetch_active_shipment, allow_inactive=allow_inactive, exclude_locked_shipments=exclude_locked_shipments, payment_methods=payment_methods, channel_shipment_id=channel_shipment_id, channel_order_id=channel_order_id, custom_meta=custom_meta, ordering_channel=ordering_channel, company_affiliate_tag=company_affiliate_tag, my_orders=my_orders, platform_user_id=platform_user_id, sort_type=sort_type, show_cross_company_data=show_cross_company_data, tags=tags, customer_id=customer_id, order_type=order_type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ShipmentInternalPlatformViewResponse
            schema = ShipmentInternalPlatformViewResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getShipments")
                print(e)

        return response
    
    async def getShipmentById(self, channel_shipment_id=None, shipment_id=None, fetch_active_shipment=None, allow_inactive=None, request_headers:Dict={}):
        """Get detailed information about a specific shipment
        :param channel_shipment_id : App Shipment Id : type string
        :param shipment_id : Shipment Id : type string
        :param fetch_active_shipment : flag to fetch active or deactivated shipments : type boolean
        :param allow_inactive : Flag indicating whether inactive shipments are allowed : type boolean
        """
        payload = {}
        
        if channel_shipment_id is not None:
            payload["channel_shipment_id"] = channel_shipment_id
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id
        if fetch_active_shipment is not None:
            payload["fetch_active_shipment"] = fetch_active_shipment
        if allow_inactive is not None:
            payload["allow_inactive"] = allow_inactive

        # Parameter validation
        schema = OrderValidator.getShipmentById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/shipment-details", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer","example":37}}],"optional":[{"in":"query","name":"channel_shipment_id","description":"App Shipment Id","required":false,"schema":{"type":"string","example":"16731535496121004000"}},{"in":"query","name":"shipment_id","description":"Shipment Id","required":false,"schema":{"type":"string","example":"16731535496121004000"}},{"in":"query","name":"fetch_active_shipment","description":"flag to fetch active or deactivated shipments","required":false,"schema":{"type":"boolean","example":false}},{"in":"query","name":"allow_inactive","description":"Flag indicating whether inactive shipments are allowed","required":false,"schema":{"type":"boolean","default":false}}],"query":[{"in":"query","name":"channel_shipment_id","description":"App Shipment Id","required":false,"schema":{"type":"string","example":"16731535496121004000"}},{"in":"query","name":"shipment_id","description":"Shipment Id","required":false,"schema":{"type":"string","example":"16731535496121004000"}},{"in":"query","name":"fetch_active_shipment","description":"flag to fetch active or deactivated shipments","required":false,"schema":{"type":"boolean","example":false}},{"in":"query","name":"allow_inactive","description":"Flag indicating whether inactive shipments are allowed","required":false,"schema":{"type":"boolean","default":false}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer","example":37}}]}""", serverType="platform", channel_shipment_id=channel_shipment_id, shipment_id=shipment_id, fetch_active_shipment=fetch_active_shipment, allow_inactive=allow_inactive)
        query_string = await create_query_string(channel_shipment_id=channel_shipment_id, shipment_id=shipment_id, fetch_active_shipment=fetch_active_shipment, allow_inactive=allow_inactive)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/shipment-details", channel_shipment_id=channel_shipment_id, shipment_id=shipment_id, fetch_active_shipment=fetch_active_shipment, allow_inactive=allow_inactive), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

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
        """Get detailed information about a specific order
        :param order_id :  : type string
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/order-details", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}},{"in":"query","name":"order_id","required":true,"schema":{"type":"string","default":"FY6299E19701B4EAEFC2"}}],"optional":[{"in":"query","name":"my_orders","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"allow_inactive","description":"Flag to allow inactive shipments","required":false,"schema":{"type":"boolean","default":false}}],"query":[{"in":"query","name":"order_id","required":true,"schema":{"type":"string","default":"FY6299E19701B4EAEFC2"}},{"in":"query","name":"my_orders","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"allow_inactive","description":"Flag to allow inactive shipments","required":false,"schema":{"type":"boolean","default":false}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", order_id=order_id, my_orders=my_orders, allow_inactive=allow_inactive)
        query_string = await create_query_string(order_id=order_id, my_orders=my_orders, allow_inactive=allow_inactive)

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
        """Get configuration settings for lanes
        :param super_lane : Name of lane for which data is to be fetched : type string
        :param group_entity : Name of group entity : type string
        :param from_date : Start Date in DD-MM-YYYY format : type string
        :param to_date : End Date in DD-MM-YYYY format : type string
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/lane-config/", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"super_lane","description":"Name of lane for which data is to be fetched","required":false,"schema":{"type":"string","enum":["unfulfilled","processed","returns","action_centre"],"default":"unfulfilled"}},{"in":"query","name":"group_entity","description":"Name of group entity","required":false,"schema":{"type":"string","enum":["shipments","orders","bags"],"default":"shipments"}},{"in":"query","name":"from_date","description":"Start Date in DD-MM-YYYY format","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","description":"End Date in DD-MM-YYYY format","required":false,"schema":{"type":"string"}},{"in":"query","name":"start_date","description":"UTC Start Date in ISO format","required":false,"schema":{"type":"string"}},{"in":"query","name":"end_date","description":"UTC End Date in ISO format","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","description":"Comma separated values of delivery partner ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","description":"Comma separated values of store ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channels","required":false,"schema":{"type":"string"}},{"in":"query","name":"payment_mode","description":"Comma separated values of payment modes","required":false,"schema":{"type":"string"}},{"in":"query","name":"bag_status","description":"Comma separated values of bag statuses","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_value","required":false,"schema":{"type":"string"}},{"in":"query","name":"tags","required":false,"schema":{"type":"string"}},{"in":"query","name":"time_to_dispatch","required":false,"schema":{"type":"integer","example":1,"enum":[1,-1]}},{"in":"query","name":"payment_methods","required":false,"schema":{"type":"string"}},{"in":"query","name":"my_orders","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"show_cross_company_data","description":"Flag to view cross & non-cross company order","required":false,"schema":{"type":"boolean","default":false}},{"in":"query","name":"order_type","required":false,"schema":{"type":"string","example":"HomeDelivery"}}],"query":[{"in":"query","name":"super_lane","description":"Name of lane for which data is to be fetched","required":false,"schema":{"type":"string","enum":["unfulfilled","processed","returns","action_centre"],"default":"unfulfilled"}},{"in":"query","name":"group_entity","description":"Name of group entity","required":false,"schema":{"type":"string","enum":["shipments","orders","bags"],"default":"shipments"}},{"in":"query","name":"from_date","description":"Start Date in DD-MM-YYYY format","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","description":"End Date in DD-MM-YYYY format","required":false,"schema":{"type":"string"}},{"in":"query","name":"start_date","description":"UTC Start Date in ISO format","required":false,"schema":{"type":"string"}},{"in":"query","name":"end_date","description":"UTC End Date in ISO format","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","description":"Comma separated values of delivery partner ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","description":"Comma separated values of store ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channels","required":false,"schema":{"type":"string"}},{"in":"query","name":"payment_mode","description":"Comma separated values of payment modes","required":false,"schema":{"type":"string"}},{"in":"query","name":"bag_status","description":"Comma separated values of bag statuses","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_value","required":false,"schema":{"type":"string"}},{"in":"query","name":"tags","required":false,"schema":{"type":"string"}},{"in":"query","name":"time_to_dispatch","required":false,"schema":{"type":"integer","example":1,"enum":[1,-1]}},{"in":"query","name":"payment_methods","required":false,"schema":{"type":"string"}},{"in":"query","name":"my_orders","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"show_cross_company_data","description":"Flag to view cross & non-cross company order","required":false,"schema":{"type":"boolean","default":false}},{"in":"query","name":"order_type","required":false,"schema":{"type":"string","example":"HomeDelivery"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", super_lane=super_lane, group_entity=group_entity, from_date=from_date, to_date=to_date, start_date=start_date, end_date=end_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, payment_mode=payment_mode, bag_status=bag_status, search_type=search_type, search_value=search_value, tags=tags, time_to_dispatch=time_to_dispatch, payment_methods=payment_methods, my_orders=my_orders, show_cross_company_data=show_cross_company_data, order_type=order_type)
        query_string = await create_query_string(super_lane=super_lane, group_entity=group_entity, from_date=from_date, to_date=to_date, start_date=start_date, end_date=end_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, payment_mode=payment_mode, bag_status=bag_status, search_type=search_type, search_value=search_value, tags=tags, time_to_dispatch=time_to_dispatch, payment_methods=payment_methods, my_orders=my_orders, show_cross_company_data=show_cross_company_data, order_type=order_type)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/lane-config/", super_lane=super_lane, group_entity=group_entity, from_date=from_date, to_date=to_date, start_date=start_date, end_date=end_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, payment_mode=payment_mode, bag_status=bag_status, search_type=search_type, search_value=search_value, tags=tags, time_to_dispatch=time_to_dispatch, payment_methods=payment_methods, my_orders=my_orders, show_cross_company_data=show_cross_company_data, order_type=order_type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import LaneConfigResponse
            schema = LaneConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getLaneConfig")
                print(e)

        return response
    
    async def getOrders(self, lane=None, search_type=None, bag_status=None, time_to_dispatch=None, payment_methods=None, tags=None, search_value=None, from_date=None, to_date=None, start_date=None, end_date=None, dp_ids=None, stores=None, sales_channels=None, page_no=None, page_size=None, is_priority_sort=None, custom_meta=None, my_orders=None, show_cross_company_data=None, customer_id=None, order_type=None, allow_inactive=None, request_headers:Dict={}):
        """Get a list of orders based on the filters provided
        :param lane : lane refers to a section where orders are assigned, indicating its grouping : type string
        :param search_type : search_type refers to the field that will be used as the target for the search operation : type string
        :param bag_status : bag_status refers to status of the entity. Filters orders based on the status. : type string
        :param time_to_dispatch : time_to_dispatch refers to estimated SLA time. : type integer
        :param payment_methods :  : type string
        :param tags : tags refers to additional descriptive labels associated with the order : type string
        :param search_value : search_value is matched against the field specified by the search_type : type string
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
        :param custom_meta :  : type string
        :param my_orders :  : type boolean
        :param show_cross_company_data : Flag to view cross & non-cross company order : type boolean
        :param customer_id :  : type string
        :param order_type :  : type string
        :param allow_inactive : Flag indicating whether inactive shipments are allowed : type boolean
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
        if allow_inactive is not None:
            payload["allow_inactive"] = allow_inactive

        # Parameter validation
        schema = OrderValidator.getOrders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders-listing", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer","default":37}}],"optional":[{"in":"query","name":"lane","description":"lane refers to a section where orders are assigned, indicating its grouping","required":false,"schema":{"type":"string","default":"new"}},{"in":"query","name":"search_type","description":"search_type refers to the field that will be used as the target for the search operation","required":false,"schema":{"type":"string","default":"shipment_id"}},{"in":"query","name":"bag_status","description":"bag_status refers to status of the entity. Filters orders based on the status.","required":false,"schema":{"type":"string"}},{"in":"query","name":"time_to_dispatch","description":"time_to_dispatch refers to estimated SLA time.","required":false,"schema":{"type":"integer","example":1,"enum":[1,-1]}},{"in":"query","name":"payment_methods","required":false,"schema":{"type":"string"}},{"in":"query","name":"tags","description":"tags refers to additional descriptive labels associated with the order","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_value","description":"search_value is matched against the field specified by the search_type","required":false,"schema":{"type":"string","default":"16854460524441037000"}},{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"start_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"end_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","description":"Delivery Partner IDs to which shipments are assigned.","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channels","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"is_priority_sort","required":false,"schema":{"type":"boolean","default":true}},{"in":"query","name":"custom_meta","required":false,"schema":{"type":"string","default":"6388422a5ebd6a6cf4a8ede6"}},{"in":"query","name":"my_orders","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"show_cross_company_data","description":"Flag to view cross & non-cross company order","required":false,"schema":{"type":"boolean","default":false}},{"in":"query","name":"customer_id","required":false,"schema":{"type":"string","example":"63a2ce177e9f59d3166dd700"}},{"in":"query","name":"order_type","required":false,"schema":{"type":"string","example":"HomeDelivery"}},{"in":"query","name":"allow_inactive","description":"Flag indicating whether inactive shipments are allowed","required":false,"schema":{"type":"boolean","default":false}}],"query":[{"in":"query","name":"lane","description":"lane refers to a section where orders are assigned, indicating its grouping","required":false,"schema":{"type":"string","default":"new"}},{"in":"query","name":"search_type","description":"search_type refers to the field that will be used as the target for the search operation","required":false,"schema":{"type":"string","default":"shipment_id"}},{"in":"query","name":"bag_status","description":"bag_status refers to status of the entity. Filters orders based on the status.","required":false,"schema":{"type":"string"}},{"in":"query","name":"time_to_dispatch","description":"time_to_dispatch refers to estimated SLA time.","required":false,"schema":{"type":"integer","example":1,"enum":[1,-1]}},{"in":"query","name":"payment_methods","required":false,"schema":{"type":"string"}},{"in":"query","name":"tags","description":"tags refers to additional descriptive labels associated with the order","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_value","description":"search_value is matched against the field specified by the search_type","required":false,"schema":{"type":"string","default":"16854460524441037000"}},{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"start_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"end_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","description":"Delivery Partner IDs to which shipments are assigned.","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channels","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"is_priority_sort","required":false,"schema":{"type":"boolean","default":true}},{"in":"query","name":"custom_meta","required":false,"schema":{"type":"string","default":"6388422a5ebd6a6cf4a8ede6"}},{"in":"query","name":"my_orders","required":false,"schema":{"type":"boolean"}},{"in":"query","name":"show_cross_company_data","description":"Flag to view cross & non-cross company order","required":false,"schema":{"type":"boolean","default":false}},{"in":"query","name":"customer_id","required":false,"schema":{"type":"string","example":"63a2ce177e9f59d3166dd700"}},{"in":"query","name":"order_type","required":false,"schema":{"type":"string","example":"HomeDelivery"}},{"in":"query","name":"allow_inactive","description":"Flag indicating whether inactive shipments are allowed","required":false,"schema":{"type":"boolean","default":false}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer","default":37}}]}""", serverType="platform", lane=lane, search_type=search_type, bag_status=bag_status, time_to_dispatch=time_to_dispatch, payment_methods=payment_methods, tags=tags, search_value=search_value, from_date=from_date, to_date=to_date, start_date=start_date, end_date=end_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, page_no=page_no, page_size=page_size, is_priority_sort=is_priority_sort, custom_meta=custom_meta, my_orders=my_orders, show_cross_company_data=show_cross_company_data, customer_id=customer_id, order_type=order_type, allow_inactive=allow_inactive)
        query_string = await create_query_string(lane=lane, search_type=search_type, bag_status=bag_status, time_to_dispatch=time_to_dispatch, payment_methods=payment_methods, tags=tags, search_value=search_value, from_date=from_date, to_date=to_date, start_date=start_date, end_date=end_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, page_no=page_no, page_size=page_size, is_priority_sort=is_priority_sort, custom_meta=custom_meta, my_orders=my_orders, show_cross_company_data=show_cross_company_data, customer_id=customer_id, order_type=order_type, allow_inactive=allow_inactive)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders-listing", lane=lane, search_type=search_type, bag_status=bag_status, time_to_dispatch=time_to_dispatch, payment_methods=payment_methods, tags=tags, search_value=search_value, from_date=from_date, to_date=to_date, start_date=start_date, end_date=end_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, page_no=page_no, page_size=page_size, is_priority_sort=is_priority_sort, custom_meta=custom_meta, my_orders=my_orders, show_cross_company_data=show_cross_company_data, customer_id=customer_id, order_type=order_type, allow_inactive=allow_inactive), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OrderListingResponse
            schema = OrderListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOrders")
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/filter-listing", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}},{"in":"query","name":"view","description":"Name of view","required":true,"schema":{"type":"string","default":"manifest","enum":["my_orders","bulk_action","bulk_invoice","manifest"]}}],"optional":[{"in":"query","name":"group_entity","description":"Name of group entity","required":false,"schema":{"type":"string","default":"orders","enum":["orders","shipments"]}}],"query":[{"in":"query","name":"view","description":"Name of view","required":true,"schema":{"type":"string","default":"manifest","enum":["my_orders","bulk_action","bulk_invoice","manifest"]}},{"in":"query","name":"group_entity","description":"Name of group entity","required":false,"schema":{"type":"string","default":"orders","enum":["orders","shipments"]}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", view=view, group_entity=group_entity)
        query_string = await create_query_string(view=view, group_entity=group_entity)

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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/generate/file", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"sales_channels","description":"Comma separated values of sales channel ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","description":"Comma separated values of delivery partner ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"start_date","description":"UTC start date in ISO format","required":false,"schema":{"type":"string","format":"date-time"}},{"in":"query","name":"end_date","description":"UTC end date in ISO format","required":false,"schema":{"type":"string","format":"date-time"}},{"in":"query","name":"stores","description":"Comma separated values of store ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"tags","description":"Comma separated values of tags","required":false,"schema":{"type":"string"}},{"in":"query","name":"bag_status","description":"Comma separated values of bag statuses","required":false,"schema":{"type":"string"}},{"in":"query","name":"payment_methods","description":"Comma separated values of payment methods","required":false,"schema":{"type":"string"}},{"in":"query","name":"file_type","description":"File type to be downloaded","required":false,"schema":{"type":"string"}},{"in":"query","name":"time_to_dispatch","description":"Sla breached or not breached","required":false,"schema":{"type":"integer","example":1,"enum":[1,-1]}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer","default":10}}],"query":[{"in":"query","name":"sales_channels","description":"Comma separated values of sales channel ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","description":"Comma separated values of delivery partner ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"start_date","description":"UTC start date in ISO format","required":false,"schema":{"type":"string","format":"date-time"}},{"in":"query","name":"end_date","description":"UTC end date in ISO format","required":false,"schema":{"type":"string","format":"date-time"}},{"in":"query","name":"stores","description":"Comma separated values of store ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"tags","description":"Comma separated values of tags","required":false,"schema":{"type":"string"}},{"in":"query","name":"bag_status","description":"Comma separated values of bag statuses","required":false,"schema":{"type":"string"}},{"in":"query","name":"payment_methods","description":"Comma separated values of payment methods","required":false,"schema":{"type":"string"}},{"in":"query","name":"file_type","description":"File type to be downloaded","required":false,"schema":{"type":"string"}},{"in":"query","name":"time_to_dispatch","description":"Sla breached or not breached","required":false,"schema":{"type":"integer","example":1,"enum":[1,-1]}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", sales_channels=sales_channels, dp_ids=dp_ids, start_date=start_date, end_date=end_date, stores=stores, tags=tags, bag_status=bag_status, payment_methods=payment_methods, file_type=file_type, time_to_dispatch=time_to_dispatch, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(sales_channels=sales_channels, dp_ids=dp_ids, start_date=start_date, end_date=end_date, stores=stores, tags=tags, bag_status=bag_status, payment_methods=payment_methods, file_type=file_type, time_to_dispatch=time_to_dispatch, page_no=page_no, page_size=page_size)

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
            from .models import FileResponse
            schema = FileResponse()
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
            from .models import FileResponse
            schema = FileResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for downloadBulkActionTemplate")
                print(e)

        return response
    
    async def getShipmentReasons(self, shipment_id=None, bag_id=None, state=None, request_headers:Dict={}):
        """Get reasons to perform full or partial cancellation of a bag
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
        """Retrieve detailed information about a specific bag
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/bag-details/", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"bag_id","description":"Id of bag","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_bag_id","description":"Id of application bag","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_id","description":"Id of application","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"bag_id","description":"Id of bag","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_bag_id","description":"Id of application bag","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_id","description":"Id of application","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", bag_id=bag_id, channel_bag_id=channel_bag_id, channel_id=channel_id)
        query_string = await create_query_string(bag_id=bag_id, channel_bag_id=channel_bag_id, channel_id=channel_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/bag-details/", bag_id=bag_id, channel_bag_id=channel_bag_id, channel_id=channel_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

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
        """Get paginated list of bags based on provided filters
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/bags", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"bag_ids","description":"Comma separated values of bag ids","required":false,"schema":{"type":"string","example":"1234,2344"}},{"in":"query","name":"shipment_ids","description":"Comma separated values of shipment ids","required":false,"schema":{"type":"string","example":"1661111234,167772344"}},{"in":"query","name":"order_ids","description":"Comma separated values of order ids","required":false,"schema":{"type":"string","example":"1661111234,167772344"}},{"in":"query","name":"channel_bag_ids","description":"Comma separated values of app bag ids","required":false,"schema":{"type":"string","example":"B1234,B2344"}},{"in":"query","name":"channel_shipment_ids","description":"Comma separated values of app shipment ids","required":false,"schema":{"type":"string","example":"S1234,S2344"}},{"in":"query","name":"channel_order_ids","description":"Comma separated values of app order ids","required":false,"schema":{"type":"string","example":"O1234,02344"}},{"in":"query","name":"channel_id","description":"Comma separated values of app ids","required":false,"schema":{"type":"string","example":"000000000000000000000001,614b42d1ea943427b5f46d1e"}},{"in":"query","name":"page_no","description":"Page number for paginated data","required":false,"schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","description":"Page size of data received per page","required":false,"schema":{"type":"integer","default":20}}],"query":[{"in":"query","name":"bag_ids","description":"Comma separated values of bag ids","required":false,"schema":{"type":"string","example":"1234,2344"}},{"in":"query","name":"shipment_ids","description":"Comma separated values of shipment ids","required":false,"schema":{"type":"string","example":"1661111234,167772344"}},{"in":"query","name":"order_ids","description":"Comma separated values of order ids","required":false,"schema":{"type":"string","example":"1661111234,167772344"}},{"in":"query","name":"channel_bag_ids","description":"Comma separated values of app bag ids","required":false,"schema":{"type":"string","example":"B1234,B2344"}},{"in":"query","name":"channel_shipment_ids","description":"Comma separated values of app shipment ids","required":false,"schema":{"type":"string","example":"S1234,S2344"}},{"in":"query","name":"channel_order_ids","description":"Comma separated values of app order ids","required":false,"schema":{"type":"string","example":"O1234,02344"}},{"in":"query","name":"channel_id","description":"Comma separated values of app ids","required":false,"schema":{"type":"string","example":"000000000000000000000001,614b42d1ea943427b5f46d1e"}},{"in":"query","name":"page_no","description":"Page number for paginated data","required":false,"schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","description":"Page size of data received per page","required":false,"schema":{"type":"integer","default":20}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", bag_ids=bag_ids, shipment_ids=shipment_ids, order_ids=order_ids, channel_bag_ids=channel_bag_ids, channel_shipment_ids=channel_shipment_ids, channel_order_ids=channel_order_ids, channel_id=channel_id, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(bag_ids=bag_ids, shipment_ids=shipment_ids, order_ids=order_ids, channel_bag_ids=channel_bag_ids, channel_shipment_ids=channel_shipment_ids, channel_order_ids=channel_order_ids, channel_id=channel_id, page_no=page_no, page_size=page_size)

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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders/{order_id}/generate/pos-receipt", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"path","name":"order_id","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"shipment_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"document_type","required":false,"schema":{"type":"string","default":"invoice_receipt"}}],"query":[{"in":"query","name":"shipment_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"document_type","required":false,"schema":{"type":"string","default":"invoice_receipt"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"path","name":"order_id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", order_id=order_id, shipment_id=shipment_id, document_type=document_type)
        query_string = await create_query_string(shipment_id=shipment_id, document_type=document_type)

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
        """Gets all the allowed templates to perform bulk operations.
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.getAllowedTemplatesForBulk()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/jobs/templates", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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
        """Get the excel or CSV file URL for the template.
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
    