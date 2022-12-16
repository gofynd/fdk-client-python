

""" Order Platform Client."""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import OrderValidator

class Order:
    def __init__(self, config):
        self._conf = config
    
    async def shipmentStatusUpdate(self, body=""):
        """Update Shipment Status
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.shipmentStatusUpdate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateShipmentStatusBody import UpdateShipmentStatusBody
        schema = UpdateShipmentStatusBody()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/actions/status", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/actions/status", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def activityStatus(self, bag_id=None):
        """Get Activity Status
        :param bag_id : Bag Id : type string
        """
        payload = {}
        
        if bag_id:
            payload["bag_id"] = bag_id
        

        # Parameter validation
        schema = OrderValidator.activityStatus()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/actions/activity/status", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"bag_id","in":"query","description":"Bag Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"bag_id","in":"query","description":"Bag Id","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}]}""", bag_id=bag_id)
        query_string = await create_query_string(bag_id=bag_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/actions/activity/status", bag_id=bag_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def storeProcessShipmentUpdate(self, body=""):
        """Update Store Process-Shipment
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.storeProcessShipmentUpdate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateProcessShipmenstRequestBody import UpdateProcessShipmenstRequestBody
        schema = UpdateProcessShipmenstRequestBody()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/actions/store/process-shipments", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/actions/store/process-shipments", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def checkRefund(self, shipment_id=None):
        """Check Refund is available or not
        :param shipment_id : Shipment Id : type string
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        

        # Parameter validation
        schema = OrderValidator.checkRefund()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/actions/check-refund/{shipment_id}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"Shipment Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"Shipment Id","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/actions/check-refund/{shipment_id}", shipment_id=shipment_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def shipmentBagsCanBreak(self, body=""):
        """Decides if Shipment bags can break
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.shipmentBagsCanBreak()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CanBreakRequestBody import CanBreakRequestBody
        schema = CanBreakRequestBody()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/actions/can-break", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/actions/can-break", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getOrdersByCompanyId(self, page_no=None, page_size=None, from_date=None, to_date=None, is_priority_sort=None, lock_status=None, user_id=None, q=None, stage=None, sales_channels=None, order_id=None, stores=None, deployment_stores=None, status=None, dp=None, filter_type=None):
        """Get Orders
        :param page_no : Current page number : type string
        :param page_size : Page limit : type string
        :param from_date : From Date : type string
        :param to_date : To Date : type string
        :param is_priority_sort : Sorting Order : type boolean
        :param lock_status : Hide Lock Status : type boolean
        :param user_id : User Id : type string
        :param q : Keyword for Search : type string
        :param stage : Specefic Order Stage : type string
        :param sales_channels : Selected Sales Channel : type string
        :param order_id : Order Id : type string
        :param stores : Selected Stores : type string
        :param deployment_stores : Selected Deployment Stores : type string
        :param status : Status of order : type string
        :param dp : Delivery Partners : type string
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
        
        if is_priority_sort:
            payload["is_priority_sort"] = is_priority_sort
        
        if lock_status:
            payload["lock_status"] = lock_status
        
        if user_id:
            payload["user_id"] = user_id
        
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
        
        if deployment_stores:
            payload["deployment_stores"] = deployment_stores
        
        if status:
            payload["status"] = status
        
        if dp:
            payload["dp"] = dp
        
        if filter_type:
            payload["filter_type"] = filter_type
        

        # Parameter validation
        schema = OrderValidator.getOrdersByCompanyId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"Page limit","required":false,"schema":{"type":"string"}},{"name":"from_date","in":"query","description":"From Date","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","description":"To Date","required":false,"schema":{"type":"string"}},{"name":"is_priority_sort","in":"query","description":"Sorting Order","required":false,"schema":{"type":"boolean"}},{"name":"lock_status","in":"query","description":"Hide Lock Status","required":false,"schema":{"type":"boolean"}},{"name":"user_id","in":"query","description":"User Id","required":false,"schema":{"type":"string"}},{"name":"q","in":"query","description":"Keyword for Search","required":false,"schema":{"type":"string"}},{"name":"stage","in":"query","description":"Specefic Order Stage","required":false,"schema":{"type":"string"}},{"name":"sales_channels","in":"query","description":"Selected Sales Channel","required":false,"schema":{"type":"string"}},{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"stores","in":"query","description":"Selected Stores","required":false,"schema":{"type":"string"}},{"name":"deployment_stores","in":"query","description":"Selected Deployment Stores","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"Status of order","required":false,"schema":{"type":"string"}},{"name":"dp","in":"query","description":"Delivery Partners","required":false,"schema":{"type":"string"}},{"name":"filter_type","in":"query","description":"Filters","required":false,"schema":{"type":"string"}}],"query":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"Page limit","required":false,"schema":{"type":"string"}},{"name":"from_date","in":"query","description":"From Date","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","description":"To Date","required":false,"schema":{"type":"string"}},{"name":"is_priority_sort","in":"query","description":"Sorting Order","required":false,"schema":{"type":"boolean"}},{"name":"lock_status","in":"query","description":"Hide Lock Status","required":false,"schema":{"type":"boolean"}},{"name":"user_id","in":"query","description":"User Id","required":false,"schema":{"type":"string"}},{"name":"q","in":"query","description":"Keyword for Search","required":false,"schema":{"type":"string"}},{"name":"stage","in":"query","description":"Specefic Order Stage","required":false,"schema":{"type":"string"}},{"name":"sales_channels","in":"query","description":"Selected Sales Channel","required":false,"schema":{"type":"string"}},{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"stores","in":"query","description":"Selected Stores","required":false,"schema":{"type":"string"}},{"name":"deployment_stores","in":"query","description":"Selected Deployment Stores","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"Status of order","required":false,"schema":{"type":"string"}},{"name":"dp","in":"query","description":"Delivery Partners","required":false,"schema":{"type":"string"}},{"name":"filter_type","in":"query","description":"Filters","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, is_priority_sort=is_priority_sort, lock_status=lock_status, user_id=user_id, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, deployment_stores=deployment_stores, status=status, dp=dp, filter_type=filter_type)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, is_priority_sort=is_priority_sort, lock_status=lock_status, user_id=user_id, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, deployment_stores=deployment_stores, status=status, dp=dp, filter_type=filter_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders", page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, is_priority_sort=is_priority_sort, lock_status=lock_status, user_id=user_id, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, deployment_stores=deployment_stores, status=status, dp=dp, filter_type=filter_type), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getOrderLanesCountByCompanyId(self, page_no=None, page_size=None, from_date=None, to_date=None, q=None, stage=None, sales_channels=None, order_id=None, stores=None, status=None, filter_type=None):
        """Get Orders Seperate Lane Count
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
        
        if filter_type:
            payload["filter_type"] = filter_type
        

        # Parameter validation
        schema = OrderValidator.getOrderLanesCountByCompanyId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders/lane-count", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"Page limit","required":false,"schema":{"type":"string"}},{"name":"from_date","in":"query","description":"From Date","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","description":"To Date","required":false,"schema":{"type":"string"}},{"name":"q","in":"query","description":"Keyword for Search","required":false,"schema":{"type":"string"}},{"name":"stage","in":"query","description":"Specefic Order Stage","required":false,"schema":{"type":"string"}},{"name":"sales_channels","in":"query","description":"Selected Sales Channel","required":false,"schema":{"type":"string"}},{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"stores","in":"query","description":"Selected Stores","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"Status of order","required":false,"schema":{"type":"string"}},{"name":"filter_type","in":"query","description":"Filters","required":false,"schema":{"type":"string"}}],"query":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"Page limit","required":false,"schema":{"type":"string"}},{"name":"from_date","in":"query","description":"From Date","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","description":"To Date","required":false,"schema":{"type":"string"}},{"name":"q","in":"query","description":"Keyword for Search","required":false,"schema":{"type":"string"}},{"name":"stage","in":"query","description":"Specefic Order Stage","required":false,"schema":{"type":"string"}},{"name":"sales_channels","in":"query","description":"Selected Sales Channel","required":false,"schema":{"type":"string"}},{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"stores","in":"query","description":"Selected Stores","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"Status of order","required":false,"schema":{"type":"string"}},{"name":"filter_type","in":"query","description":"Filters","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, status=status, filter_type=filter_type)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, status=status, filter_type=filter_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders/lane-count", page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, status=status, filter_type=filter_type), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getOrderDetails(self, order_id=None, next=None, previous=None):
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
        schema = OrderValidator.getOrderDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders/details", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}],"optional":[{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"next","in":"query","description":"Next","required":false,"schema":{"type":"string"}},{"name":"previous","in":"query","description":"Previous","required":false,"schema":{"type":"string"}}],"query":[{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"next","in":"query","description":"Next","required":false,"schema":{"type":"string"}},{"name":"previous","in":"query","description":"Previous","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}]}""", order_id=order_id, next=next, previous=previous)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders/details", order_id=order_id, next=next, previous=previous), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getPicklistOrdersByCompanyId(self, page_no=None, page_size=None, from_date=None, to_date=None, q=None, stage=None, sales_channels=None, order_id=None, stores=None, status=None, filter_type=None):
        """Get Orders
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
        
        if filter_type:
            payload["filter_type"] = filter_type
        

        # Parameter validation
        schema = OrderValidator.getPicklistOrdersByCompanyId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders/picklist", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"Page limit","required":false,"schema":{"type":"string"}},{"name":"from_date","in":"query","description":"From Date","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","description":"To Date","required":false,"schema":{"type":"string"}},{"name":"q","in":"query","description":"Keyword for Search","required":false,"schema":{"type":"string"}},{"name":"stage","in":"query","description":"Specefic Order Stage","required":false,"schema":{"type":"string"}},{"name":"sales_channels","in":"query","description":"Selected Sales Channel","required":false,"schema":{"type":"string"}},{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"stores","in":"query","description":"Selected Stores","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"Status of order","required":false,"schema":{"type":"string"}},{"name":"filter_type","in":"query","description":"Filters","required":false,"schema":{"type":"string"}}],"query":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"string"}},{"name":"page_size","in":"query","description":"Page limit","required":false,"schema":{"type":"string"}},{"name":"from_date","in":"query","description":"From Date","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","description":"To Date","required":false,"schema":{"type":"string"}},{"name":"q","in":"query","description":"Keyword for Search","required":false,"schema":{"type":"string"}},{"name":"stage","in":"query","description":"Specefic Order Stage","required":false,"schema":{"type":"string"}},{"name":"sales_channels","in":"query","description":"Selected Sales Channel","required":false,"schema":{"type":"string"}},{"name":"order_id","in":"query","description":"Order Id","required":false,"schema":{"type":"string"}},{"name":"stores","in":"query","description":"Selected Stores","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"Status of order","required":false,"schema":{"type":"string"}},{"name":"filter_type","in":"query","description":"Filters","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}}]}""", page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, status=status, filter_type=filter_type)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, status=status, filter_type=filter_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders/picklist", page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, q=q, stage=stage, sales_channels=sales_channels, order_id=order_id, stores=stores, status=status, filter_type=filter_type), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getShipmentAddress(self, shipment_id=None, address_category=None):
        """Get Shipment Address
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        :param address_category : Category of the address it falls into(billing or delivery). : type string
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        if address_category:
            payload["address_category"] = address_category
        

        # Parameter validation
        schema = OrderValidator.getShipmentAddress()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders/shipments/{shipment_id}/address/{address_category}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}},{"name":"address_category","in":"path","description":"Category of the address it falls into(billing or delivery).","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}},{"name":"address_category","in":"path","description":"Category of the address it falls into(billing or delivery).","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id, address_category=address_category)
        query_string = await create_query_string(shipment_id=shipment_id, address_category=address_category)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders/shipments/{shipment_id}/address/{address_category}", shipment_id=shipment_id, address_category=address_category), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateShipmentAddress(self, shipment_id=None, address_category=None, body=""):
        """Update Shipment Address
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        :param address_category : Category of the address it falls into(billing or delivery). : type string
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        if address_category:
            payload["address_category"] = address_category
        

        # Parameter validation
        schema = OrderValidator.updateShipmentAddress()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateShipmentAddressRequest import UpdateShipmentAddressRequest
        schema = UpdateShipmentAddressRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders/shipments/{shipment_id}/address/{address_category}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}},{"name":"address_category","in":"path","description":"Category of the address it falls into(billing or delivery).","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}},{"name":"address_category","in":"path","description":"Category of the address it falls into(billing or delivery).","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id, address_category=address_category)
        query_string = await create_query_string(shipment_id=shipment_id, address_category=address_category)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders/shipments/{shipment_id}/address/{address_category}", shipment_id=shipment_id, address_category=address_category), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def invalidateShipmentCache(self, body=""):
        """Invalidate shipment Cache
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.invalidateShipmentCache()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.InvalidateShipmentCachePayload import InvalidateShipmentCachePayload
        schema = InvalidateShipmentCachePayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/update-cache", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/update-cache", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def reassignLocation(self, body=""):
        """Reassign Location
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.reassignLocation()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.StoreReassign import StoreReassign
        schema = StoreReassign()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/store/reassign-internal", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/store/reassign-internal", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def updateShipmentLock(self, body=""):
        """update shipment lock
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.updateShipmentLock()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateShipmentLockPayload import UpdateShipmentLockPayload
        schema = UpdateShipmentLockPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/entity/lock-manager", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/entity/lock-manager", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getAnnouncements(self, date=None):
        """
        :param date :  : type string
        """
        payload = {}
        
        if date:
            payload["date"] = date
        

        # Parameter validation
        schema = OrderValidator.getAnnouncements()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/announcements", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"date","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"date","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", date=date)
        query_string = await create_query_string(date=date)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/announcements", date=date), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateAddress(self, shipment_id=None, name=None, address=None, address_type=None, pincode=None, phone=None, email=None, landmark=None, address_category=None, city=None, state=None, country=None):
        """
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
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        if name:
            payload["name"] = name
        
        if address:
            payload["address"] = address
        
        if address_type:
            payload["address_type"] = address_type
        
        if pincode:
            payload["pincode"] = pincode
        
        if phone:
            payload["phone"] = phone
        
        if email:
            payload["email"] = email
        
        if landmark:
            payload["landmark"] = landmark
        
        if address_category:
            payload["address_category"] = address_category
        
        if city:
            payload["city"] = city
        
        if state:
            payload["state"] = state
        
        if country:
            payload["country"] = country
        

        # Parameter validation
        schema = OrderValidator.updateAddress()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/delight/update-address", """{"required":[{"in":"query","name":"shipment_id","required":true,"schema":{"type":"string"}},{"in":"query","name":"address_category","required":true,"schema":{"type":"string"}},{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"name","required":false,"schema":{"type":"string"}},{"in":"query","name":"address","required":false,"schema":{"type":"string"}},{"in":"query","name":"address_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"pincode","required":false,"schema":{"type":"string"}},{"in":"query","name":"phone","required":false,"schema":{"type":"string"}},{"in":"query","name":"email","required":false,"schema":{"type":"string"}},{"in":"query","name":"landmark","required":false,"schema":{"type":"string"}},{"in":"query","name":"city","required":false,"schema":{"type":"string"}},{"in":"query","name":"state","required":false,"schema":{"type":"string"}},{"in":"query","name":"country","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"shipment_id","required":true,"schema":{"type":"string"}},{"in":"query","name":"name","required":false,"schema":{"type":"string"}},{"in":"query","name":"address","required":false,"schema":{"type":"string"}},{"in":"query","name":"address_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"pincode","required":false,"schema":{"type":"string"}},{"in":"query","name":"phone","required":false,"schema":{"type":"string"}},{"in":"query","name":"email","required":false,"schema":{"type":"string"}},{"in":"query","name":"landmark","required":false,"schema":{"type":"string"}},{"in":"query","name":"address_category","required":true,"schema":{"type":"string"}},{"in":"query","name":"city","required":false,"schema":{"type":"string"}},{"in":"query","name":"state","required":false,"schema":{"type":"string"}},{"in":"query","name":"country","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", shipment_id=shipment_id, name=name, address=address, address_type=address_type, pincode=pincode, phone=phone, email=email, landmark=landmark, address_category=address_category, city=city, state=state, country=country, )
        query_string = await create_query_string(shipment_id=shipment_id, name=name, address=address, address_type=address_type, pincode=pincode, phone=phone, email=email, landmark=landmark, address_category=address_category, city=city, state=state, country=country, )
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/delight/update-address", shipment_id=shipment_id, name=name, address=address, address_type=address_type, pincode=pincode, phone=phone, email=email, landmark=landmark, address_category=address_category, city=city, state=state, country=country, ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def click2Call(self, caller=None, receiver=None, bag_id=None, calling_to=None, caller_id=None):
        """
        :param caller :  : type string
        :param receiver :  : type string
        :param bag_id :  : type string
        :param calling_to :  : type string
        :param caller_id :  : type string
        """
        payload = {}
        
        if caller:
            payload["caller"] = caller
        
        if receiver:
            payload["receiver"] = receiver
        
        if bag_id:
            payload["bag_id"] = bag_id
        
        if calling_to:
            payload["calling_to"] = calling_to
        
        if caller_id:
            payload["caller_id"] = caller_id
        

        # Parameter validation
        schema = OrderValidator.click2Call()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/ninja/click2call", """{"required":[{"in":"query","name":"caller","required":true,"schema":{"type":"string"}},{"in":"query","name":"receiver","required":true,"schema":{"type":"string"}},{"in":"query","name":"bag_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"calling_to","required":false,"schema":{"type":"string"}},{"in":"query","name":"caller_id","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"caller","required":true,"schema":{"type":"string"}},{"in":"query","name":"receiver","required":true,"schema":{"type":"string"}},{"in":"query","name":"bag_id","required":true,"schema":{"type":"string"}},{"in":"query","name":"calling_to","required":false,"schema":{"type":"string"}},{"in":"query","name":"caller_id","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", caller=caller, receiver=receiver, bag_id=bag_id, calling_to=calling_to, caller_id=caller_id, )
        query_string = await create_query_string(caller=caller, receiver=receiver, bag_id=bag_id, calling_to=calling_to, caller_id=caller_id, )
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/ninja/click2call", caller=caller, receiver=receiver, bag_id=bag_id, calling_to=calling_to, caller_id=caller_id, ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateShipmentStatus(self, body=""):
        """Update shipment status
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.updateShipmentStatus()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateShipmentStatusRequest import UpdateShipmentStatusRequest
        schema = UpdateShipmentStatusRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/shipment/status-internal", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/shipment/status-internal", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def processManifest(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.processManifest()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CreateOrderPayload import CreateOrderPayload
        schema = CreateOrderPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/process-manifest", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/process-manifest", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def dispatchManifest(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.dispatchManifest()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.DispatchManifest import DispatchManifest
        schema = DispatchManifest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/manifest/dispatch", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/manifest/dispatch", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getRoleBasedActions(self, ):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.getRoleBasedActions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/roles", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/roles", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getShipmentHistory(self, shipment_id=None, bag_id=None):
        """
        :param shipment_id :  : type integer
        :param bag_id :  : type integer
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        if bag_id:
            payload["bag_id"] = bag_id
        

        # Parameter validation
        schema = OrderValidator.getShipmentHistory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/shipment/history", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"shipment_id","required":false,"schema":{"type":"integer"}},{"in":"query","name":"bag_id","required":false,"schema":{"type":"integer"}}],"query":[{"in":"query","name":"shipment_id","required":false,"schema":{"type":"integer"}},{"in":"query","name":"bag_id","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", shipment_id=shipment_id, bag_id=bag_id)
        query_string = await create_query_string(shipment_id=shipment_id, bag_id=bag_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/shipment/history", shipment_id=shipment_id, bag_id=bag_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def sendSmsNinja(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.sendSmsNinja()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.SendSmsPayload import SendSmsPayload
        schema = SendSmsPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/ninja/send-sms", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/ninja/send-sms", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def platformManualAssignDPToShipment(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.platformManualAssignDPToShipment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ManualAssignDPToShipment import ManualAssignDPToShipment
        schema = ManualAssignDPToShipment()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/oms/manual-place-shipment", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/oms/manual-place-shipment", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def updatePackagingDimensions(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.updatePackagingDimensions()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CreateOrderPayload import CreateOrderPayload
        schema = CreateOrderPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/update-packaging-dimension", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/update-packaging-dimension", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def createOrder(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.createOrder()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CreateOrderAPI import CreateOrderAPI
        schema = CreateOrderAPI()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/create-order", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/create-order", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def createChannelConfig(self, body=""):
        """createChannelConfig
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.createChannelConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CreateChannelConfigData import CreateChannelConfigData
        schema = CreateChannelConfigData()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/order-config", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/order-config", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getChannelConfig(self, ):
        """getChannelConfig
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.getChannelConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/order-config", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/order-config", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def uploadConsent(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.uploadConsent()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UploadConsent import UploadConsent
        schema = UploadConsent()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/manifest/uploadConsent", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/manifest/uploadConsent", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def checkOrderStatus(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.checkOrderStatus()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.OrderStatus import OrderStatus
        schema = OrderStatus()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/debug/order_status", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/debug/order_status", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getShipments(self, lane=None, search_type=None, search_value=None, search_id=None, from_date=None, to_date=None, dp_ids=None, ordering_company_id=None, stores=None, sales_channel=None, request_by_ext=None, page_no=None, page_size=None, is_priority_sort=None, exclude_locked_shipments=None, payment_methods=None, channel_shipment_id=None, channel_order_id=None, custom_meta=None):
        """
        :param lane :  : type string
        :param search_type :  : type string
        :param search_value :  : type string
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
        :param is_priority_sort :  : type boolean
        :param exclude_locked_shipments :  : type boolean
        :param payment_methods :  : type string
        :param channel_shipment_id :  : type string
        :param channel_order_id :  : type string
        :param custom_meta :  : type string
        """
        payload = {}
        
        if lane:
            payload["lane"] = lane
        
        if search_type:
            payload["search_type"] = search_type
        
        if search_value:
            payload["search_value"] = search_value
        
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
        
        if is_priority_sort:
            payload["is_priority_sort"] = is_priority_sort
        
        if exclude_locked_shipments:
            payload["exclude_locked_shipments"] = exclude_locked_shipments
        
        if payment_methods:
            payload["payment_methods"] = payment_methods
        
        if channel_shipment_id:
            payload["channel_shipment_id"] = channel_shipment_id
        
        if channel_order_id:
            payload["channel_order_id"] = channel_order_id
        
        if custom_meta:
            payload["custom_meta"] = custom_meta
        

        # Parameter validation
        schema = OrderValidator.getShipments()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/orders/v1.0/company/{self._conf.companyId}/shipments-listing", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"lane","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_value","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"ordering_company_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channel","required":false,"schema":{"type":"string"}},{"in":"query","name":"request_by_ext","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"is_priority_sort","required":false,"schema":{"type":"boolean","default":true}},{"in":"query","name":"exclude_locked_shipments","required":false,"schema":{"type":"boolean","default":true}},{"in":"query","name":"payment_methods","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_shipment_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_order_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"custom_meta","required":false,"schema":{"type":"string","default":{"store_id":"6388422a5ebd6a6cf4a8ede6"}}}],"query":[{"in":"query","name":"lane","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_value","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"ordering_company_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channel","required":false,"schema":{"type":"string"}},{"in":"query","name":"request_by_ext","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"is_priority_sort","required":false,"schema":{"type":"boolean","default":true}},{"in":"query","name":"exclude_locked_shipments","required":false,"schema":{"type":"boolean","default":true}},{"in":"query","name":"payment_methods","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_shipment_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_order_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"custom_meta","required":false,"schema":{"type":"string","default":{"store_id":"6388422a5ebd6a6cf4a8ede6"}}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", lane=lane, search_type=search_type, search_value=search_value, search_id=search_id, from_date=from_date, to_date=to_date, dp_ids=dp_ids, ordering_company_id=ordering_company_id, stores=stores, sales_channel=sales_channel, request_by_ext=request_by_ext, page_no=page_no, page_size=page_size, is_priority_sort=is_priority_sort, exclude_locked_shipments=exclude_locked_shipments, payment_methods=payment_methods, channel_shipment_id=channel_shipment_id, channel_order_id=channel_order_id, custom_meta=custom_meta)
        query_string = await create_query_string(lane=lane, search_type=search_type, search_value=search_value, search_id=search_id, from_date=from_date, to_date=to_date, dp_ids=dp_ids, ordering_company_id=ordering_company_id, stores=stores, sales_channel=sales_channel, request_by_ext=request_by_ext, page_no=page_no, page_size=page_size, is_priority_sort=is_priority_sort, exclude_locked_shipments=exclude_locked_shipments, payment_methods=payment_methods, channel_shipment_id=channel_shipment_id, channel_order_id=channel_order_id, custom_meta=custom_meta)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/shipments-listing", lane=lane, search_type=search_type, search_value=search_value, search_id=search_id, from_date=from_date, to_date=to_date, dp_ids=dp_ids, ordering_company_id=ordering_company_id, stores=stores, sales_channel=sales_channel, request_by_ext=request_by_ext, page_no=page_no, page_size=page_size, is_priority_sort=is_priority_sort, exclude_locked_shipments=exclude_locked_shipments, payment_methods=payment_methods, channel_shipment_id=channel_shipment_id, channel_order_id=channel_order_id, custom_meta=custom_meta), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getShipmentById(self, channel_shipment_id=None, shipment_id=None, ordering_company_id=None, request_by_ext=None):
        """
        :param channel_shipment_id :  : type string
        :param shipment_id :  : type string
        :param ordering_company_id :  : type string
        :param request_by_ext :  : type string
        """
        payload = {}
        
        if channel_shipment_id:
            payload["channel_shipment_id"] = channel_shipment_id
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        if ordering_company_id:
            payload["ordering_company_id"] = ordering_company_id
        
        if request_by_ext:
            payload["request_by_ext"] = request_by_ext
        

        # Parameter validation
        schema = OrderValidator.getShipmentById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/orders/v1.0/company/{self._conf.companyId}/shipment-details", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"channel_shipment_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"shipment_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"ordering_company_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"request_by_ext","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"channel_shipment_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"shipment_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"ordering_company_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"request_by_ext","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", channel_shipment_id=channel_shipment_id, shipment_id=shipment_id, ordering_company_id=ordering_company_id, request_by_ext=request_by_ext)
        query_string = await create_query_string(channel_shipment_id=channel_shipment_id, shipment_id=shipment_id, ordering_company_id=ordering_company_id, request_by_ext=request_by_ext)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/shipment-details", channel_shipment_id=channel_shipment_id, shipment_id=shipment_id, ordering_company_id=ordering_company_id, request_by_ext=request_by_ext), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getOrderById(self, order_id=None):
        """
        :param order_id :  : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        

        # Parameter validation
        schema = OrderValidator.getOrderById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/orders/v1.0/company/{self._conf.companyId}/order-details", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"query","name":"order_id","required":true,"schema":{"type":"string","default":"FY6299E19701B4EAEFC2"}}],"optional":[],"query":[{"in":"query","name":"order_id","required":true,"schema":{"type":"string","default":"FY6299E19701B4EAEFC2"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", order_id=order_id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/order-details", order_id=order_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getLaneConfig(self, super_lane=None, group_entity=None, from_date=None, to_date=None, dp_ids=None, stores=None, sales_channel=None, payment_mode=None, bag_status=None):
        """
        :param super_lane :  : type string
        :param group_entity :  : type string
        :param from_date :  : type string
        :param to_date :  : type string
        :param dp_ids :  : type string
        :param stores :  : type string
        :param sales_channel :  : type string
        :param payment_mode :  : type string
        :param bag_status :  : type string
        """
        payload = {}
        
        if super_lane:
            payload["super_lane"] = super_lane
        
        if group_entity:
            payload["group_entity"] = group_entity
        
        if from_date:
            payload["from_date"] = from_date
        
        if to_date:
            payload["to_date"] = to_date
        
        if dp_ids:
            payload["dp_ids"] = dp_ids
        
        if stores:
            payload["stores"] = stores
        
        if sales_channel:
            payload["sales_channel"] = sales_channel
        
        if payment_mode:
            payload["payment_mode"] = payment_mode
        
        if bag_status:
            payload["bag_status"] = bag_status
        

        # Parameter validation
        schema = OrderValidator.getLaneConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/orders/v1.0/company/{self._conf.companyId}/lane-config/", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"super_lane","required":false,"schema":{"type":"string","default":"unfulfilled"}},{"in":"query","name":"group_entity","required":false,"schema":{"type":"string","default":"shipments"}},{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channel","required":false,"schema":{"type":"string"}},{"in":"query","name":"payment_mode","required":false,"schema":{"type":"string"}},{"in":"query","name":"bag_status","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"super_lane","required":false,"schema":{"type":"string","default":"unfulfilled"}},{"in":"query","name":"group_entity","required":false,"schema":{"type":"string","default":"shipments"}},{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channel","required":false,"schema":{"type":"string"}},{"in":"query","name":"payment_mode","required":false,"schema":{"type":"string"}},{"in":"query","name":"bag_status","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", super_lane=super_lane, group_entity=group_entity, from_date=from_date, to_date=to_date, dp_ids=dp_ids, stores=stores, sales_channel=sales_channel, payment_mode=payment_mode, bag_status=bag_status)
        query_string = await create_query_string(super_lane=super_lane, group_entity=group_entity, from_date=from_date, to_date=to_date, dp_ids=dp_ids, stores=stores, sales_channel=sales_channel, payment_mode=payment_mode, bag_status=bag_status)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/lane-config/", super_lane=super_lane, group_entity=group_entity, from_date=from_date, to_date=to_date, dp_ids=dp_ids, stores=stores, sales_channel=sales_channel, payment_mode=payment_mode, bag_status=bag_status), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getOrders(self, lane=None, search_type=None, search_value=None, from_date=None, to_date=None, dp_ids=None, stores=None, sales_channel=None, page_no=None, page_size=None, is_priority_sort=None, custom_meta=None):
        """
        :param lane :  : type string
        :param search_type :  : type string
        :param search_value :  : type string
        :param from_date :  : type string
        :param to_date :  : type string
        :param dp_ids :  : type string
        :param stores :  : type string
        :param sales_channel :  : type string
        :param page_no :  : type integer
        :param page_size :  : type integer
        :param is_priority_sort :  : type boolean
        :param custom_meta :  : type string
        """
        payload = {}
        
        if lane:
            payload["lane"] = lane
        
        if search_type:
            payload["search_type"] = search_type
        
        if search_value:
            payload["search_value"] = search_value
        
        if from_date:
            payload["from_date"] = from_date
        
        if to_date:
            payload["to_date"] = to_date
        
        if dp_ids:
            payload["dp_ids"] = dp_ids
        
        if stores:
            payload["stores"] = stores
        
        if sales_channel:
            payload["sales_channel"] = sales_channel
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if is_priority_sort:
            payload["is_priority_sort"] = is_priority_sort
        
        if custom_meta:
            payload["custom_meta"] = custom_meta
        

        # Parameter validation
        schema = OrderValidator.getOrders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/orders/v1.0/company/{self._conf.companyId}/orders-listing", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"lane","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_value","required":false,"schema":{"type":"string"}},{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channel","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"is_priority_sort","required":false,"schema":{"type":"boolean","default":true}},{"in":"query","name":"custom_meta","required":false,"schema":{"type":"string","default":{"store_id":"6388422a5ebd6a6cf4a8ede6"}}}],"query":[{"in":"query","name":"lane","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_value","required":false,"schema":{"type":"string"}},{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channel","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"is_priority_sort","required":false,"schema":{"type":"boolean","default":true}},{"in":"query","name":"custom_meta","required":false,"schema":{"type":"string","default":{"store_id":"6388422a5ebd6a6cf4a8ede6"}}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", lane=lane, search_type=search_type, search_value=search_value, from_date=from_date, to_date=to_date, dp_ids=dp_ids, stores=stores, sales_channel=sales_channel, page_no=page_no, page_size=page_size, is_priority_sort=is_priority_sort, custom_meta=custom_meta)
        query_string = await create_query_string(lane=lane, search_type=search_type, search_value=search_value, from_date=from_date, to_date=to_date, dp_ids=dp_ids, stores=stores, sales_channel=sales_channel, page_no=page_no, page_size=page_size, is_priority_sort=is_priority_sort, custom_meta=custom_meta)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/orders-listing", lane=lane, search_type=search_type, search_value=search_value, from_date=from_date, to_date=to_date, dp_ids=dp_ids, stores=stores, sales_channel=sales_channel, page_no=page_no, page_size=page_size, is_priority_sort=is_priority_sort, custom_meta=custom_meta), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getMetricCount(self, from_date=None, to_date=None):
        """
        :param from_date :  : type string
        :param to_date :  : type string
        """
        payload = {}
        
        if from_date:
            payload["from_date"] = from_date
        
        if to_date:
            payload["to_date"] = to_date
        

        # Parameter validation
        schema = OrderValidator.getMetricCount()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/orders/v1.0/company/{self._conf.companyId}/shipment/metrics-count/", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", from_date=from_date, to_date=to_date)
        query_string = await create_query_string(from_date=from_date, to_date=to_date)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/shipment/metrics-count/", from_date=from_date, to_date=to_date), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getfilters(self, view=None, group_entity=None):
        """
        :param view :  : type string
        :param group_entity :  : type string
        """
        payload = {}
        
        if view:
            payload["view"] = view
        
        if group_entity:
            payload["group_entity"] = group_entity
        

        # Parameter validation
        schema = OrderValidator.getfilters()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/orders/v1.0/company/{self._conf.companyId}/filter-listing", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"query","name":"view","required":true,"schema":{"type":"string","default":"manifest","enum":["my_orders","bulk_actions","manifest"]}}],"optional":[{"in":"query","name":"group_entity","required":false,"schema":{"type":"string","default":"orders"}}],"query":[{"in":"query","name":"view","required":true,"schema":{"type":"string","default":"manifest","enum":["my_orders","bulk_actions","manifest"]}},{"in":"query","name":"group_entity","required":false,"schema":{"type":"string","default":"orders"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", view=view, group_entity=group_entity)
        query_string = await create_query_string(view=view, group_entity=group_entity)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/filter-listing", view=view, group_entity=group_entity), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createShipmentReport(self, from_date=None, to_date=None):
        """
        :param from_date :  : type string
        :param to_date :  : type string
        """
        payload = {}
        
        if from_date:
            payload["from_date"] = from_date
        
        if to_date:
            payload["to_date"] = to_date
        

        # Parameter validation
        schema = OrderValidator.createShipmentReport()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/orders/v1.0/company/{self._conf.companyId}/reports/shipment", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", from_date=from_date, to_date=to_date)
        query_string = await create_query_string(from_date=from_date, to_date=to_date)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/reports/shipment", from_date=from_date, to_date=to_date), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getReportsShipmentListing(self, page_no=None, page_size=None):
        """
        :param page_no :  : type integer
        :param page_size :  : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = OrderValidator.getReportsShipmentListing()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/orders/v1.0/company/{self._conf.companyId}/reports/shipment-listing", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}}],"query":[{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/reports/shipment-listing", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def upsertJioCode(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.upsertJioCode()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.JioCodeUpsertPayload import JioCodeUpsertPayload
        schema = JioCodeUpsertPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/orders/v1.0/company/{self._conf.companyId}/upsert/jiocode/article", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/upsert/jiocode/article", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getBulkInvoice(self, batch_id=None, doc_type=None):
        """
        :param batch_id :  : type string
        :param doc_type :  : type string
        """
        payload = {}
        
        if batch_id:
            payload["batch_id"] = batch_id
        
        if doc_type:
            payload["doc_type"] = doc_type
        

        # Parameter validation
        schema = OrderValidator.getBulkInvoice()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/orders/v1.0/company/{self._conf.companyId}/bulk-action/invoice", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"query","name":"batch_id","required":true,"schema":{"type":"string"}},{"in":"query","name":"doc_type","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"in":"query","name":"batch_id","required":true,"schema":{"type":"string"}},{"in":"query","name":"doc_type","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", batch_id=batch_id, doc_type=doc_type)
        query_string = await create_query_string(batch_id=batch_id, doc_type=doc_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/bulk-action/invoice", batch_id=batch_id, doc_type=doc_type), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getBulkInvoiceLabel(self, batch_id=None):
        """
        :param batch_id :  : type string
        """
        payload = {}
        
        if batch_id:
            payload["batch_id"] = batch_id
        

        # Parameter validation
        schema = OrderValidator.getBulkInvoiceLabel()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/orders/v1.0/company/{self._conf.companyId}/invoice-label-external", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"query","name":"batch_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"in":"query","name":"batch_id","required":true,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", batch_id=batch_id)
        query_string = await create_query_string(batch_id=batch_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/invoice-label-external", batch_id=batch_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getBulkShipmentExcelFile(self, lane=None, search_type=None, search_id=None, from_date=None, to_date=None, dp_ids=None, ordering_company_id=None, stores=None, sales_channel=None, request_by_ext=None, page_no=None, page_size=None, customer_id=None, is_priority_sort=None):
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
        schema = OrderValidator.getBulkShipmentExcelFile()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/orders/v1.0/company/{self._conf.companyId}/generate/file", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"lane","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"ordering_company_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channel","required":false,"schema":{"type":"string"}},{"in":"query","name":"request_by_ext","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"customer_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"is_priority_sort","required":false,"schema":{"type":"boolean","default":false}}],"query":[{"in":"query","name":"lane","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"ordering_company_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channel","required":false,"schema":{"type":"string"}},{"in":"query","name":"request_by_ext","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"customer_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"is_priority_sort","required":false,"schema":{"type":"boolean","default":false}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", lane=lane, search_type=search_type, search_id=search_id, from_date=from_date, to_date=to_date, dp_ids=dp_ids, ordering_company_id=ordering_company_id, stores=stores, sales_channel=sales_channel, request_by_ext=request_by_ext, page_no=page_no, page_size=page_size, customer_id=customer_id, is_priority_sort=is_priority_sort)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/generate/file", lane=lane, search_type=search_type, search_id=search_id, from_date=from_date, to_date=to_date, dp_ids=dp_ids, ordering_company_id=ordering_company_id, stores=stores, sales_channel=sales_channel, request_by_ext=request_by_ext, page_no=page_no, page_size=page_size, customer_id=customer_id, is_priority_sort=is_priority_sort), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getBulkList(self, lane=None, search_type=None, search_id=None, from_date=None, to_date=None, dp_ids=None, ordering_company_id=None, stores=None, sales_channel=None, request_by_ext=None, page_no=None, page_size=None, customer_id=None, is_priority_sort=None):
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
        schema = OrderValidator.getBulkList()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/orders/v1.0/company/{self._conf.companyId}/bulk-action/listing", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"lane","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"ordering_company_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channel","required":false,"schema":{"type":"string"}},{"in":"query","name":"request_by_ext","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"customer_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"is_priority_sort","required":false,"schema":{"type":"boolean","default":false}}],"query":[{"in":"query","name":"lane","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"ordering_company_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channel","required":false,"schema":{"type":"string"}},{"in":"query","name":"request_by_ext","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"customer_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"is_priority_sort","required":false,"schema":{"type":"boolean","default":false}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", lane=lane, search_type=search_type, search_id=search_id, from_date=from_date, to_date=to_date, dp_ids=dp_ids, ordering_company_id=ordering_company_id, stores=stores, sales_channel=sales_channel, request_by_ext=request_by_ext, page_no=page_no, page_size=page_size, customer_id=customer_id, is_priority_sort=is_priority_sort)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/bulk-action/listing", lane=lane, search_type=search_type, search_id=search_id, from_date=from_date, to_date=to_date, dp_ids=dp_ids, ordering_company_id=ordering_company_id, stores=stores, sales_channel=sales_channel, request_by_ext=request_by_ext, page_no=page_no, page_size=page_size, customer_id=customer_id, is_priority_sort=is_priority_sort), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getManifestList(self, status=None, store_id=None, page_no=None, page_size=None, search_value=None, from_date=None, to_date=None):
        """
        :param status :  : type string
        :param store_id :  : type integer
        :param page_no :  : type integer
        :param page_size :  : type integer
        :param search_value :  : type string
        :param from_date :  : type string
        :param to_date :  : type string
        """
        payload = {}
        
        if status:
            payload["status"] = status
        
        if store_id:
            payload["store_id"] = store_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if search_value:
            payload["search_value"] = search_value
        
        if from_date:
            payload["from_date"] = from_date
        
        if to_date:
            payload["to_date"] = to_date
        

        # Parameter validation
        schema = OrderValidator.getManifestList()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/orders/v1.0/company/{self._conf.companyId}/generated-manifests", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"status","required":false,"schema":{"type":"string"}},{"in":"query","name":"store_id","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"search_value","required":false,"schema":{"type":"string"}},{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"status","required":false,"schema":{"type":"string"}},{"in":"query","name":"store_id","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"search_value","required":false,"schema":{"type":"string"}},{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", status=status, store_id=store_id, page_no=page_no, page_size=page_size, search_value=search_value, from_date=from_date, to_date=to_date)
        query_string = await create_query_string(status=status, store_id=store_id, page_no=page_no, page_size=page_size, search_value=search_value, from_date=from_date, to_date=to_date)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/generated-manifests", status=status, store_id=store_id, page_no=page_no, page_size=page_size, search_value=search_value, from_date=from_date, to_date=to_date), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getManifestDetailsWithShipments(self, manifest_id=None, from_date=None, to_date=None, store_id=None, page=None, page_size=None, lane=None, dp_ids=None, search_type=None, search_value=None):
        """
        :param manifest_id :  : type string
        :param from_date :  : type string
        :param to_date :  : type string
        :param store_id :  : type integer
        :param page :  : type integer
        :param page_size :  : type integer
        :param lane :  : type string
        :param dp_ids :  : type integer
        :param search_type :  : type string
        :param search_value :  : type string
        """
        payload = {}
        
        if manifest_id:
            payload["manifest_id"] = manifest_id
        
        if from_date:
            payload["from_date"] = from_date
        
        if to_date:
            payload["to_date"] = to_date
        
        if store_id:
            payload["store_id"] = store_id
        
        if page:
            payload["page"] = page
        
        if page_size:
            payload["page_size"] = page_size
        
        if lane:
            payload["lane"] = lane
        
        if dp_ids:
            payload["dp_ids"] = dp_ids
        
        if search_type:
            payload["search_type"] = search_type
        
        if search_value:
            payload["search_value"] = search_value
        

        # Parameter validation
        schema = OrderValidator.getManifestDetailsWithShipments()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/orders/v1.0/company/{self._conf.companyId}/manifest-details", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"query","name":"manifest_id","required":true,"schema":{"type":"string"}},{"in":"query","name":"store_id","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"page","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"lane","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","required":false,"schema":{"type":"integer"}},{"in":"query","name":"search_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_value","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"manifest_id","required":true,"schema":{"type":"string"}},{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"store_id","required":true,"schema":{"type":"integer"}},{"in":"query","name":"page","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"lane","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","required":false,"schema":{"type":"integer"}},{"in":"query","name":"search_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_value","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", manifest_id=manifest_id, from_date=from_date, to_date=to_date, store_id=store_id, page=page, page_size=page_size, lane=lane, dp_ids=dp_ids, search_type=search_type, search_value=search_value)
        query_string = await create_query_string(manifest_id=manifest_id, from_date=from_date, to_date=to_date, store_id=store_id, page=page, page_size=page_size, lane=lane, dp_ids=dp_ids, search_type=search_type, search_value=search_value)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/manifest-details", manifest_id=manifest_id, from_date=from_date, to_date=to_date, store_id=store_id, page=page, page_size=page_size, lane=lane, dp_ids=dp_ids, search_type=search_type, search_value=search_value), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getBulkActionFailedReport(self, batch_id=None, report_type=None):
        """
        :param batch_id :  : type string
        :param report_type :  : type string
        """
        payload = {}
        
        if batch_id:
            payload["batch_id"] = batch_id
        
        if report_type:
            payload["report_type"] = report_type
        

        # Parameter validation
        schema = OrderValidator.getBulkActionFailedReport()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/orders/v1.0/company/{self._conf.companyId}/bulk-action-failed-report/", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"in":"query","name":"batch_id","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"report_type","required":false,"schema":{"type":"string","default":"generation_report"}}],"query":[{"in":"query","name":"batch_id","required":true,"schema":{"type":"string"}},{"in":"query","name":"report_type","required":false,"schema":{"type":"string","default":"generation_report"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}}]}""", batch_id=batch_id, report_type=report_type)
        query_string = await create_query_string(batch_id=batch_id, report_type=report_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/bulk-action-failed-report/", batch_id=batch_id, report_type=report_type), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getShipmentReasons(self, shipment_id=None, bag_id=None, state=None):
        """Use this API to retrieve the issues that led to the cancellation of bags within a shipment.
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        :param bag_id : ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        :param state : State for which reasons are required. : type string
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        if bag_id:
            payload["bag_id"] = bag_id
        
        if state:
            payload["state"] = state
        

        # Parameter validation
        schema = OrderValidator.getShipmentReasons()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/orders/v1.0/company/{self._conf.companyId}/shipments/{shipment_id}/bags/{bag_id}/state/{state}/reasons", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"path","name":"shipment_id","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}},{"in":"path","description":"ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"bag_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"state","description":"State for which reasons are required.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"path","name":"shipment_id","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}},{"in":"path","description":"ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"bag_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"state","description":"State for which reasons are required.","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id, bag_id=bag_id, state=state)
        query_string = await create_query_string(shipment_id=shipment_id, bag_id=bag_id, state=state)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/shipments/{shipment_id}/bags/{bag_id}/state/{state}/reasons", shipment_id=shipment_id, bag_id=bag_id, state=state), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def bulkActionProcessXlsxFile(self, body=""):
        """Use this API to start processing Xlsx file.
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.bulkActionProcessXlsxFile()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.BulkActionPayload import BulkActionPayload
        schema = BulkActionPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/orders/v2.0/company/{self._conf.companyId}/bulk-action/", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/orders/v2.0/company/{self._conf.companyId}/bulk-action/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def bulkActionDetails(self, batch_id=None):
        """Returns failed, processing and successfully processed shipments along with their counts and failed reasons.
        :param batch_id :  : type string
        """
        payload = {}
        
        if batch_id:
            payload["batch_id"] = batch_id
        

        # Parameter validation
        schema = OrderValidator.bulkActionDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/orders/v2.0/company/{self._conf.companyId}/bulk-action/{batch_id}", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"batch_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"batch_id","required":true,"schema":{"type":"string"}}]}""", batch_id=batch_id)
        query_string = await create_query_string(batch_id=batch_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v2.0/company/{self._conf.companyId}/bulk-action/{batch_id}", batch_id=batch_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getBagById(self, bag_id=None, channel_bag_id=None, channel_id=None):
        """
        :param bag_id :  : type string
        :param channel_bag_id :  : type string
        :param channel_id :  : type string
        """
        payload = {}
        
        if bag_id:
            payload["bag_id"] = bag_id
        
        if channel_bag_id:
            payload["channel_bag_id"] = channel_bag_id
        
        if channel_id:
            payload["channel_id"] = channel_id
        

        # Parameter validation
        schema = OrderValidator.getBagById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/orders/v1.0/company/{self._conf.companyId}/bag-details/", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"bag_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_bag_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_id","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"bag_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_bag_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_id","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", bag_id=bag_id, channel_bag_id=channel_bag_id, channel_id=channel_id)
        query_string = await create_query_string(bag_id=bag_id, channel_bag_id=channel_bag_id, channel_id=channel_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/bag-details/", bag_id=bag_id, channel_bag_id=channel_bag_id, channel_id=channel_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getBags(self, bag_ids=None, shipment_ids=None, order_ids=None, channel_bag_ids=None, channel_shipment_ids=None, channel_order_ids=None, channel_id=None, page_no=None, page_size=None):
        """
        :param bag_ids :  : type string
        :param shipment_ids :  : type string
        :param order_ids :  : type string
        :param channel_bag_ids :  : type string
        :param channel_shipment_ids :  : type string
        :param channel_order_ids :  : type string
        :param channel_id :  : type string
        :param page_no :  : type integer
        :param page_size :  : type integer
        """
        payload = {}
        
        if bag_ids:
            payload["bag_ids"] = bag_ids
        
        if shipment_ids:
            payload["shipment_ids"] = shipment_ids
        
        if order_ids:
            payload["order_ids"] = order_ids
        
        if channel_bag_ids:
            payload["channel_bag_ids"] = channel_bag_ids
        
        if channel_shipment_ids:
            payload["channel_shipment_ids"] = channel_shipment_ids
        
        if channel_order_ids:
            payload["channel_order_ids"] = channel_order_ids
        
        if channel_id:
            payload["channel_id"] = channel_id
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = OrderValidator.getBags()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/orders/v1.0/company/{self._conf.companyId}/bags", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"bag_ids","required":false,"schema":{"type":"string","example":["1234","2344"]}},{"in":"query","name":"shipment_ids","required":false,"schema":{"type":"string","example":["1661111234","167772344"]}},{"in":"query","name":"order_ids","required":false,"schema":{"type":"string","example":["1661111234","167772344"]}},{"in":"query","name":"channel_bag_ids","required":false,"schema":{"type":"string","example":["B1234","B2344"]}},{"in":"query","name":"channel_shipment_ids","required":false,"schema":{"type":"string","example":["S1234","S2344"]}},{"in":"query","name":"channel_order_ids","required":false,"schema":{"type":"string","example":["O1234","02344"]}},{"in":"query","name":"channel_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer","default":20}}],"query":[{"in":"query","name":"bag_ids","required":false,"schema":{"type":"string","example":["1234","2344"]}},{"in":"query","name":"shipment_ids","required":false,"schema":{"type":"string","example":["1661111234","167772344"]}},{"in":"query","name":"order_ids","required":false,"schema":{"type":"string","example":["1661111234","167772344"]}},{"in":"query","name":"channel_bag_ids","required":false,"schema":{"type":"string","example":["B1234","B2344"]}},{"in":"query","name":"channel_shipment_ids","required":false,"schema":{"type":"string","example":["S1234","S2344"]}},{"in":"query","name":"channel_order_ids","required":false,"schema":{"type":"string","example":["O1234","02344"]}},{"in":"query","name":"channel_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer","default":20}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", bag_ids=bag_ids, shipment_ids=shipment_ids, order_ids=order_ids, channel_bag_ids=channel_bag_ids, channel_shipment_ids=channel_shipment_ids, channel_order_ids=channel_order_ids, channel_id=channel_id, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(bag_ids=bag_ids, shipment_ids=shipment_ids, order_ids=order_ids, channel_bag_ids=channel_bag_ids, channel_shipment_ids=channel_shipment_ids, channel_order_ids=channel_order_ids, channel_id=channel_id, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/bags", bag_ids=bag_ids, shipment_ids=shipment_ids, order_ids=order_ids, channel_bag_ids=channel_bag_ids, channel_shipment_ids=channel_shipment_ids, channel_order_ids=channel_order_ids, channel_id=channel_id, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
