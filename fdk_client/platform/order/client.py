

"""Order Platform Client"""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import OrderValidator

class Order:
    def __init__(self, config):
        self._conf = config

    
    async def getShipments(self, lane=None, bag_status=None, status_override_lane=None, search_type=None, search_value=None, search_id=None, from_date=None, to_date=None, dp_ids=None, ordering_company_id=None, stores=None, sales_channels=None, request_by_ext=None, page_no=None, page_size=None, is_priority_sort=None, fetch_active_shipment=None, exclude_locked_shipments=None, payment_methods=None, channel_shipment_id=None, channel_order_id=None, custom_meta=None, ordering_channel=None, company_affiliate_tag=None):
        """
        :param lane :  : type string
        :param bag_status :  : type string
        :param status_override_lane :  : type boolean
        :param search_type :  : type string
        :param search_value :  : type string
        :param search_id :  : type string
        :param from_date :  : type string
        :param to_date :  : type string
        :param dp_ids :  : type string
        :param ordering_company_id :  : type string
        :param stores :  : type string
        :param sales_channels :  : type string
        :param request_by_ext :  : type string
        :param page_no :  : type integer
        :param page_size :  : type integer
        :param is_priority_sort :  : type boolean
        :param fetch_active_shipment :  : type boolean
        :param exclude_locked_shipments :  : type boolean
        :param payment_methods :  : type string
        :param channel_shipment_id :  : type string
        :param channel_order_id :  : type string
        :param custom_meta :  : type string
        :param ordering_channel :  : type string
        :param company_affiliate_tag :  : type string
        """
        payload = {}
        
        if lane:
            payload["lane"] = lane
        
        if bag_status:
            payload["bag_status"] = bag_status
        
        if status_override_lane:
            payload["status_override_lane"] = status_override_lane
        
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
        
        if sales_channels:
            payload["sales_channels"] = sales_channels
        
        if request_by_ext:
            payload["request_by_ext"] = request_by_ext
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if is_priority_sort:
            payload["is_priority_sort"] = is_priority_sort
        
        if fetch_active_shipment:
            payload["fetch_active_shipment"] = fetch_active_shipment
        
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
        
        if ordering_channel:
            payload["ordering_channel"] = ordering_channel
        
        if company_affiliate_tag:
            payload["company_affiliate_tag"] = company_affiliate_tag
        

        # Parameter validation
        schema = OrderValidator.getShipments()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/orders/v1.0/company/{self._conf.companyId}/shipments-listing", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"lane","required":false,"schema":{"type":"string"}},{"in":"query","name":"bag_status","required":false,"schema":{"type":"string"}},{"in":"query","name":"status_override_lane","required":false,"schema":{"type":"boolean","default":false}},{"in":"query","name":"search_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_value","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"ordering_company_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channels","required":false,"schema":{"type":"string"}},{"in":"query","name":"request_by_ext","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"is_priority_sort","required":false,"schema":{"type":"boolean","default":true}},{"in":"query","name":"fetch_active_shipment","required":false,"schema":{"type":"boolean","default":true}},{"in":"query","name":"exclude_locked_shipments","required":false,"schema":{"type":"boolean","default":true}},{"in":"query","name":"payment_methods","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_shipment_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_order_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"custom_meta","required":false,"schema":{"type":"string","default":{"store_id":"6388422a5ebd6a6cf4a8ede6"}}},{"in":"query","name":"ordering_channel","required":false,"schema":{"type":"string"}},{"in":"query","name":"company_affiliate_tag","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"lane","required":false,"schema":{"type":"string"}},{"in":"query","name":"bag_status","required":false,"schema":{"type":"string"}},{"in":"query","name":"status_override_lane","required":false,"schema":{"type":"boolean","default":false}},{"in":"query","name":"search_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_value","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"ordering_company_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channels","required":false,"schema":{"type":"string"}},{"in":"query","name":"request_by_ext","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"is_priority_sort","required":false,"schema":{"type":"boolean","default":true}},{"in":"query","name":"fetch_active_shipment","required":false,"schema":{"type":"boolean","default":true}},{"in":"query","name":"exclude_locked_shipments","required":false,"schema":{"type":"boolean","default":true}},{"in":"query","name":"payment_methods","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_shipment_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_order_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"custom_meta","required":false,"schema":{"type":"string","default":{"store_id":"6388422a5ebd6a6cf4a8ede6"}}},{"in":"query","name":"ordering_channel","required":false,"schema":{"type":"string"}},{"in":"query","name":"company_affiliate_tag","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", lane=lane, bag_status=bag_status, status_override_lane=status_override_lane, search_type=search_type, search_value=search_value, search_id=search_id, from_date=from_date, to_date=to_date, dp_ids=dp_ids, ordering_company_id=ordering_company_id, stores=stores, sales_channels=sales_channels, request_by_ext=request_by_ext, page_no=page_no, page_size=page_size, is_priority_sort=is_priority_sort, fetch_active_shipment=fetch_active_shipment, exclude_locked_shipments=exclude_locked_shipments, payment_methods=payment_methods, channel_shipment_id=channel_shipment_id, channel_order_id=channel_order_id, custom_meta=custom_meta, ordering_channel=ordering_channel, company_affiliate_tag=company_affiliate_tag)
        query_string = await create_query_string(lane=lane, bag_status=bag_status, status_override_lane=status_override_lane, search_type=search_type, search_value=search_value, search_id=search_id, from_date=from_date, to_date=to_date, dp_ids=dp_ids, ordering_company_id=ordering_company_id, stores=stores, sales_channels=sales_channels, request_by_ext=request_by_ext, page_no=page_no, page_size=page_size, is_priority_sort=is_priority_sort, fetch_active_shipment=fetch_active_shipment, exclude_locked_shipments=exclude_locked_shipments, payment_methods=payment_methods, channel_shipment_id=channel_shipment_id, channel_order_id=channel_order_id, custom_meta=custom_meta, ordering_channel=ordering_channel, company_affiliate_tag=company_affiliate_tag)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/shipments-listing", lane=lane, bag_status=bag_status, status_override_lane=status_override_lane, search_type=search_type, search_value=search_value, search_id=search_id, from_date=from_date, to_date=to_date, dp_ids=dp_ids, ordering_company_id=ordering_company_id, stores=stores, sales_channels=sales_channels, request_by_ext=request_by_ext, page_no=page_no, page_size=page_size, is_priority_sort=is_priority_sort, fetch_active_shipment=fetch_active_shipment, exclude_locked_shipments=exclude_locked_shipments, payment_methods=payment_methods, channel_shipment_id=channel_shipment_id, channel_order_id=channel_order_id, custom_meta=custom_meta, ordering_channel=ordering_channel, company_affiliate_tag=company_affiliate_tag), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import ShipmentInternalPlatformViewResponse
        schema = ShipmentInternalPlatformViewResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getShipments")
            print(e)

        

        return response
    
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/shipment-details", channel_shipment_id=channel_shipment_id, shipment_id=shipment_id, ordering_company_id=ordering_company_id, request_by_ext=request_by_ext), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import ShipmentInfoResponse
        schema = ShipmentInfoResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getShipmentById")
            print(e)

        

        return response
    
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/order-details", order_id=order_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import ShipmentDetailsResponse
        schema = ShipmentDetailsResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getOrderById")
            print(e)

        

        return response
    
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/lane-config/", super_lane=super_lane, group_entity=group_entity, from_date=from_date, to_date=to_date, dp_ids=dp_ids, stores=stores, sales_channel=sales_channel, payment_mode=payment_mode, bag_status=bag_status), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import LaneConfigResponse
        schema = LaneConfigResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getLaneConfig")
            print(e)

        

        return response
    
    async def getOrders(self, lane=None, search_type=None, bag_status=None, time_to_dispatch=None, payment_methods=None, tags=None, search_value=None, from_date=None, to_date=None, dp_ids=None, stores=None, sales_channels=None, page_no=None, page_size=None, is_priority_sort=None, custom_meta=None):
        """
        :param lane :  : type string
        :param search_type :  : type string
        :param bag_status :  : type string
        :param time_to_dispatch :  : type string
        :param payment_methods :  : type string
        :param tags :  : type string
        :param search_value :  : type string
        :param from_date :  : type string
        :param to_date :  : type string
        :param dp_ids :  : type string
        :param stores :  : type string
        :param sales_channels :  : type string
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
        
        if bag_status:
            payload["bag_status"] = bag_status
        
        if time_to_dispatch:
            payload["time_to_dispatch"] = time_to_dispatch
        
        if payment_methods:
            payload["payment_methods"] = payment_methods
        
        if tags:
            payload["tags"] = tags
        
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
        
        if sales_channels:
            payload["sales_channels"] = sales_channels
        
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/orders/v1.0/company/{self._conf.companyId}/orders-listing", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"lane","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"bag_status","required":false,"schema":{"type":"string"}},{"in":"query","name":"time_to_dispatch","required":false,"schema":{"type":"string"}},{"in":"query","name":"payment_methods","required":false,"schema":{"type":"string"}},{"in":"query","name":"tags","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_value","required":false,"schema":{"type":"string"}},{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channels","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"is_priority_sort","required":false,"schema":{"type":"boolean","default":true}},{"in":"query","name":"custom_meta","required":false,"schema":{"type":"string","default":{"store_id":"6388422a5ebd6a6cf4a8ede6"}}}],"query":[{"in":"query","name":"lane","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"bag_status","required":false,"schema":{"type":"string"}},{"in":"query","name":"time_to_dispatch","required":false,"schema":{"type":"string"}},{"in":"query","name":"payment_methods","required":false,"schema":{"type":"string"}},{"in":"query","name":"tags","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_value","required":false,"schema":{"type":"string"}},{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channels","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"is_priority_sort","required":false,"schema":{"type":"boolean","default":true}},{"in":"query","name":"custom_meta","required":false,"schema":{"type":"string","default":{"store_id":"6388422a5ebd6a6cf4a8ede6"}}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", lane=lane, search_type=search_type, bag_status=bag_status, time_to_dispatch=time_to_dispatch, payment_methods=payment_methods, tags=tags, search_value=search_value, from_date=from_date, to_date=to_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, page_no=page_no, page_size=page_size, is_priority_sort=is_priority_sort, custom_meta=custom_meta)
        query_string = await create_query_string(lane=lane, search_type=search_type, bag_status=bag_status, time_to_dispatch=time_to_dispatch, payment_methods=payment_methods, tags=tags, search_value=search_value, from_date=from_date, to_date=to_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, page_no=page_no, page_size=page_size, is_priority_sort=is_priority_sort, custom_meta=custom_meta)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/orders-listing", lane=lane, search_type=search_type, bag_status=bag_status, time_to_dispatch=time_to_dispatch, payment_methods=payment_methods, tags=tags, search_value=search_value, from_date=from_date, to_date=to_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, page_no=page_no, page_size=page_size, is_priority_sort=is_priority_sort, custom_meta=custom_meta), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import OrderListingResponse
        schema = OrderListingResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getOrders")
            print(e)

        

        return response
    
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/shipment/metrics-count/", from_date=from_date, to_date=to_date), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import MetricCountResponse
        schema = MetricCountResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getMetricCount")
            print(e)

        

        return response
    
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/filter-listing", view=view, group_entity=group_entity), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import FiltersResponse
        schema = FiltersResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getfilters")
            print(e)

        

        return response
    
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/reports/shipment", from_date=from_date, to_date=to_date), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import Success
        schema = Success()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for createShipmentReport")
            print(e)

        

        return response
    
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/reports/shipment-listing", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import OmsReports
        schema = OmsReports()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getReportsShipmentListing")
            print(e)

        

        return response
    
    async def upsertJioCode(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.upsertJioCode()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import JioCodeUpsertPayload
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/upsert/jiocode/article", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import JioCodeUpsertResponse
        schema = JioCodeUpsertResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for upsertJioCode")
            print(e)

        

        return response
    
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/bulk-action/invoice", batch_id=batch_id, doc_type=doc_type), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import BulkInvoicingResponse
        schema = BulkInvoicingResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getBulkInvoice")
            print(e)

        

        return response
    
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/invoice-label-external", batch_id=batch_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import BulkInvoiceLabelResponse
        schema = BulkInvoiceLabelResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getBulkInvoiceLabel")
            print(e)

        

        return response
    
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/generate/file", lane=lane, search_type=search_type, search_id=search_id, from_date=from_date, to_date=to_date, dp_ids=dp_ids, ordering_company_id=ordering_company_id, stores=stores, sales_channel=sales_channel, request_by_ext=request_by_ext, page_no=page_no, page_size=page_size, customer_id=customer_id, is_priority_sort=is_priority_sort), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import FileResponse
        schema = FileResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getBulkShipmentExcelFile")
            print(e)

        

        return response
    
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/bulk-action/listing", lane=lane, search_type=search_type, search_id=search_id, from_date=from_date, to_date=to_date, dp_ids=dp_ids, ordering_company_id=ordering_company_id, stores=stores, sales_channel=sales_channel, request_by_ext=request_by_ext, page_no=page_no, page_size=page_size, customer_id=customer_id, is_priority_sort=is_priority_sort), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import BulkListingResponse
        schema = BulkListingResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getBulkList")
            print(e)

        

        return response
    
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/bulk-action-failed-report/", batch_id=batch_id, report_type=report_type), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import FileResponse
        schema = FileResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getBulkActionFailedReport")
            print(e)

        

        return response
    
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/shipments/{shipment_id}/bags/{bag_id}/state/{state}/reasons", shipment_id=shipment_id, bag_id=bag_id, state=state), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import PlatformShipmentReasonsResponse
        schema = PlatformShipmentReasonsResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getShipmentReasons")
            print(e)

        

        return response
    
    async def bulkActionProcessXlsxFile(self, body=""):
        """Use this API to start processing Xlsx file.
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.bulkActionProcessXlsxFile()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkActionPayload
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/orders/v2.0/company/{self._conf.companyId}/bulk-action/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import BulkActionResponse
        schema = BulkActionResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for bulkActionProcessXlsxFile")
            print(e)

        

        return response
    
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v2.0/company/{self._conf.companyId}/bulk-action/{batch_id}", batch_id=batch_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import BulkActionDetailsResponse
        schema = BulkActionDetailsResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for bulkActionDetails")
            print(e)

        

        return response
    
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/bag-details/", bag_id=bag_id, channel_bag_id=channel_bag_id, channel_id=channel_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import BagDetailsPlatformResponse
        schema = BagDetailsPlatformResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getBagById")
            print(e)

        

        return response
    
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/orders/v1.0/company/{self._conf.companyId}/bags", bag_ids=bag_ids, shipment_ids=shipment_ids, order_ids=order_ids, channel_bag_ids=channel_bag_ids, channel_shipment_ids=channel_shipment_ids, channel_order_ids=channel_order_ids, channel_id=channel_id, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import GetBagsPlatformResponse
        schema = GetBagsPlatformResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getBags")
            print(e)

        

        return response
    

