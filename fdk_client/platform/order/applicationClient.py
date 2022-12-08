

"""Order Platform Client."""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .applicationValidator import OrderValidator

class Order:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    
    async def getOrderDetails1(self, order_id=None, next=None, previous=None):
        """Get Orders
        :param order_id : Order Id : type string
        :param next : Next : type string
        :param previous : Previous : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        
        if next:
            payload["next"] = next
        
        if previous:
            payload["previous"] = previous
        

        # Parameter validation
        schema = OrderValidator.getOrderDetails1()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/details", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}}],"optional":[{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"next","in":"query","description":"Next","required":false,"schema":{"type":"string"}},{"name":"previous","in":"query","description":"Previous","required":false,"schema":{"type":"string"}}],"query":[{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"next","in":"query","description":"Next","required":false,"schema":{"type":"string"}},{"name":"previous","in":"query","description":"Previous","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}}]}""", order_id=order_id, next=next, previous=previous)
        query_string = await create_query_string(order_id=order_id, next=next, previous=previous)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/details", order_id=order_id, next=next, previous=previous), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def trackShipmentPlatform(self, shipment_id=None):
        """Shipment Track
        :param shipment_id : Shipment Id : type string
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        

        # Parameter validation
        schema = OrderValidator.trackShipmentPlatform()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/shipments/{shipment_id}/track", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"Shipment Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"Shipment Id","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id)
        query_string = await create_query_string(shipment_id=shipment_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/shipments/{shipment_id}/track", shipment_id=shipment_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def trackOrder(self, order_id=None):
        """Order Track
        :param order_id : Order Id : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        

        # Parameter validation
        schema = OrderValidator.trackOrder()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/{order_id}/track", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"order_id","in":"path","description":"Order Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"order_id","in":"path","description":"Order Id","required":true,"schema":{"type":"string"}}]}""", order_id=order_id)
        query_string = await create_query_string(order_id=order_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/{order_id}/track", order_id=order_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def failedOrders(self, ):
        """Failed Orders
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.failedOrders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/failed", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/failed", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def reprocessOrder(self, order_id=None):
        """Order Reprocess
        :param order_id : Order Id : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        

        # Parameter validation
        schema = OrderValidator.reprocessOrder()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/{order_id}/reprocess", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"order_id","in":"path","description":"Order Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"order_id","in":"path","description":"Order Id","required":true,"schema":{"type":"string"}}]}""", order_id=order_id)
        query_string = await create_query_string(order_id=order_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/{order_id}/reprocess", order_id=order_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateShipment(self, shipment_id=None, body=""):
        """Update the shipment
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        

        # Parameter validation
        schema = OrderValidator.updateShipment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ShipmentUpdateRequest import ShipmentUpdateRequest
        schema = ShipmentUpdateRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/shipments/{shipment_id}/update", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id)
        query_string = await create_query_string(shipment_id=shipment_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/shipments/{shipment_id}/update", shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getPlatformShipmentReasons(self, action=None):
        """Get reasons behind full or partial cancellation of a shipment
        :param action : Action : type string
        """
        payload = {}
        
        if action:
            payload["action"] = action
        

        # Parameter validation
        schema = OrderValidator.getPlatformShipmentReasons()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/shipments/reasons/{action}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"action","in":"path","description":"Action","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"action","in":"path","description":"Action","required":true,"schema":{"type":"string"}}]}""", action=action)
        query_string = await create_query_string(action=action)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/shipments/reasons/{action}", action=action), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getShipmentTrackDetails(self, order_id=None, shipment_id=None):
        """Track shipment
        :param order_id : ID of the order. : type string
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        

        # Parameter validation
        schema = OrderValidator.getShipmentTrackDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/{order_id}/shipments/{shipment_id}/track", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"order_id","in":"path","description":"ID of the order.","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"order_id","in":"path","description":"ID of the order.","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}]}""", order_id=order_id, shipment_id=shipment_id)
        query_string = await create_query_string(order_id=order_id, shipment_id=shipment_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/{order_id}/shipments/{shipment_id}/track", order_id=order_id, shipment_id=shipment_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getOrdersByApplicationId(self, page_no=None, page_size=None, from_date=None, to_date=None, q=None, stage=None, sales_channels=None, order_id=None, stores=None, status=None, dp=None, user_id=None, filter_type=None):
        """Get Orders at Application Level
        :param page_no : Current page number : type string
        :param page_size : Page limit : type string
        :param from_date : From Date : type string
        :param to_date : To Date : type string
        :param q : Keyword for Search : type string
        :param stage : Specefic Order Stage : type string
        :param sales_channels : Selected Sales Channel : type string
        :param order_id : Order Id : type string
        :param stores : Selected Stores : type string
        :param status : Status of order : type string
        :param dp : Delivery Partners : type string
        :param user_id : User Id : type string
        :param filter_type : Filters : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if from_date:
            payload["from_date"] = from_date
        
        if to_date:
            payload["to_date"] = to_date
        
        if q:
            payload["q"] = q
        
        if stage:
            payload["stage"] = stage
        
        if sales_channels:
            payload["sales_channels"] = sales_channels
        
        if order_id:
            payload["order_id"] = order_id
        
        if stores:
            payload["stores"] = stores
        
        if status:
            payload["status"] = status
        
        if dp:
            payload["dp"] = dp
        
        if user_id:
            payload["user_id"] = user_id
        
        if filter_type:
            payload["filter_type"] = filter_type
        

        # Parameter validation
        schema = OrderValidator.getOrdersByApplicationId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"Page limit","required":false,"schema":{"type":"string"}},{"name":"from_date","in":"query","description":"From Date","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","description":"To Date","required":false,"schema":{"type":"string"}},{"name":"q","in":"query","description":"Keyword for Search","required":false,"schema":{"type":"string"}},{"name":"stage","in":"query","description":"Specefic Order Stage","required":false,"schema":{"type":"string"}},{"name":"sales_channels","in":"query","description":"Selected Sales Channel","required":false,"schema":{"type":"string"}},{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"stores","in":"query","description":"Selected Stores","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"Status of order","required":false,"schema":{"type":"string"}},{"name":"dp","in":"query","description":"Delivery Partners","required":false,"schema":{"type":"string"}},{"name":"user_id","in":"query","description":"User Id","required":false,"schema":{"type":"string"}},{"name":"filter_type","in":"query","description":"Filters","required":false,"schema":{"type":"string"}}],"query":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"Page limit","required":false,"schema":{"type":"string"}},{"name":"from_date","in":"query","description":"From Date","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","description":"To Date","required":false,"schema":{"type":"string"}},{"name":"q","in":"query","description":"Keyword for Search","required":false,"schema":{"type":"string"}},{"name":"stage","in":"query","description":"Specefic Order Stage","required":false,"schema":{"type":"string"}},{"name":"sales_channels","in":"query","description":"Selected Sales Channel","required":false,"schema":{"type":"string"}},{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"stores","in":"query","description":"Selected Stores","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"Status of order","required":false,"schema":{"type":"string"}},{"name":"dp","in":"query","description":"Delivery Partners","required":false,"schema":{"type":"string"}},{"name":"user_id","in":"query","description":"User Id","required":false,"schema":{"type":"string"}},{"name":"filter_type","in":"query","description":"Filters","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, status=status, dp=dp, user_id=user_id, filter_type=filter_type)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, status=status, dp=dp, user_id=user_id, filter_type=filter_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders", page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, status=status, dp=dp, user_id=user_id, filter_type=filter_type), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getApplicationShipments(self, lane=None, search_type=None, search_id=None, from_date=None, to_date=None, dp_ids=None, ordering_company_id=None, stores=None, sales_channel=None, request_by_ext=None, page_no=None, page_size=None, customer_id=None, is_priority_sort=None):
        """
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
        """
        payload = {}
        
        if lane:
            payload["lane"] = lane
        
        if search_type:
            payload["search_type"] = search_type
        
        if search_id:
            payload["search_id"] = search_id
        
        if from_date:
            payload["from_date"] = from_date
        
        if to_date:
            payload["to_date"] = to_date
        
        if dp_ids:
            payload["dp_ids"] = dp_ids
        
        if ordering_company_id:
            payload["ordering_company_id"] = ordering_company_id
        
        if stores:
            payload["stores"] = stores
        
        if sales_channel:
            payload["sales_channel"] = sales_channel
        
        if request_by_ext:
            payload["request_by_ext"] = request_by_ext
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if customer_id:
            payload["customer_id"] = customer_id
        
        if is_priority_sort:
            payload["is_priority_sort"] = is_priority_sort
        

        # Parameter validation
        schema = OrderValidator.getApplicationShipments()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/orders/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/shipments/", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"path","name":"application_id","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"lane","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"ordering_company_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channel","required":false,"schema":{"type":"string"}},{"in":"query","name":"request_by_ext","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"customer_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"is_priority_sort","required":false,"schema":{"type":"boolean","default":true}}],"query":[{"in":"query","name":"lane","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"ordering_company_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channel","required":false,"schema":{"type":"string"}},{"in":"query","name":"request_by_ext","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"customer_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"is_priority_sort","required":false,"schema":{"type":"boolean","default":true}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", lane=lane, search_type=search_type, search_id=search_id, from_date=from_date, to_date=to_date, dp_ids=dp_ids, ordering_company_id=ordering_company_id, stores=stores, sales_channel=sales_channel, request_by_ext=request_by_ext, page_no=page_no, page_size=page_size, customer_id=customer_id, is_priority_sort=is_priority_sort)
        query_string = await create_query_string(lane=lane, search_type=search_type, search_id=search_id, from_date=from_date, to_date=to_date, dp_ids=dp_ids, ordering_company_id=ordering_company_id, stores=stores, sales_channel=sales_channel, request_by_ext=request_by_ext, page_no=page_no, page_size=page_size, customer_id=customer_id, is_priority_sort=is_priority_sort)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/shipments/", lane=lane, search_type=search_type, search_id=search_id, from_date=from_date, to_date=to_date, dp_ids=dp_ids, ordering_company_id=ordering_company_id, stores=stores, sales_channel=sales_channel, request_by_ext=request_by_ext, page_no=page_no, page_size=page_size, customer_id=customer_id, is_priority_sort=is_priority_sort), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getAppOrderShipmentDetails(self, order_id=None):
        """
        :param order_id :  : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        

        # Parameter validation
        schema = OrderValidator.getAppOrderShipmentDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/orders/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/order-details", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"in":"query","name":"order_id","required":true,"schema":{"type":"string","default":"FY6299E19701B4EAEFC2"}}],"optional":[],"query":[{"in":"query","name":"order_id","required":true,"schema":{"type":"string","default":"FY6299E19701B4EAEFC2"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"path","name":"application_id","required":true,"schema":{"type":"string"}}]}""", order_id=order_id)
        query_string = await create_query_string(order_id=order_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/order-details", order_id=order_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def trackPlatformShipment(self, shipment_id=None):
        """Track Shipment by shipment id, for application based on application Id
        :param shipment_id :  : type string
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        

        # Parameter validation
        schema = OrderValidator.trackPlatformShipment()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/orders/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/shipments/{shipment_id}/track", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"shipment_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"application_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"shipment_id","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id)
        query_string = await create_query_string(shipment_id=shipment_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/orders/shipments/{shipment_id}/track", shipment_id=shipment_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    

