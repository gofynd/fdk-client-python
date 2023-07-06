

"""Order Platform Client"""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import OrderValidator

class Order:
    def __init__(self, config):
        self._conf = config

    
    async def getShipments(self, lane=None, bag_status=None, status_override_lane=None, time_to_dispatch=None, search_type=None, search_value=None, from_date=None, to_date=None, dp_ids=None, stores=None, sales_channels=None, page_no=None, page_size=None, fetch_active_shipment=None, exclude_locked_shipments=None, payment_methods=None, channel_shipment_id=None, channel_order_id=None, custom_meta=None, ordering_channel=None, company_affiliate_tag=None, my_orders=None):
        """
        :param lane : Name of lane for which data is to be fetched : type string
        :param bag_status : Comma separated values of bag statuses : type string
        :param status_override_lane : Use this flag to fetch by bag_status and override lane : type boolean
        :param time_to_dispatch :  : type string
        :param search_type : Search type key : type string
        :param search_value : Search type value : type string
        :param from_date : Start Date in DD-MM-YYYY format : type string
        :param to_date : End Date in DD-MM-YYYY format : type string
        :param dp_ids : Comma separated values of delivery partner ids : type string
        :param stores : Comma separated values of store ids : type string
        :param sales_channels : Comma separated values of sales channel ids : type string
        :param page_no : Page number for paginated data : type integer
        :param page_size : Page size of data received per page : type integer
        :param fetch_active_shipment : flag to fetch active shipments : type boolean
        :param exclude_locked_shipments : flag to fetch locked shipments : type boolean
        :param payment_methods : Comma separated values of payment methods : type string
        :param channel_shipment_id : App Shipment Id : type string
        :param channel_order_id : App Order Id : type string
        :param custom_meta :  : type string
        :param ordering_channel :  : type string
        :param company_affiliate_tag :  : type string
        :param my_orders :  : type boolean
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
        

        # Parameter validation
        schema = OrderValidator.getShipments()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/shipments-listing", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer","example":37}}],"optional":[{"in":"query","name":"lane","description":"Name of lane for which data is to be fetched","required":false,"schema":{"type":"string","enum":["new","confirmed","to_be_packed","ready_for_dispatch","in_transit","handed_over_to_customer","delivered","cancelled","return_initiated","return_in_transit","return_delivered","return_accepted"],"example":"new"}},{"in":"query","name":"bag_status","description":"Comma separated values of bag statuses","required":false,"schema":{"type":"string","example":"placed, bag_confirmed, bag_invoiced"}},{"in":"query","name":"status_override_lane","description":"Use this flag to fetch by bag_status and override lane","required":false,"schema":{"type":"boolean","default":false}},{"in":"query","name":"time_to_dispatch","required":false,"schema":{"type":"string","example":1,"enum":[1,-1]}},{"in":"query","name":"search_type","description":"Search type key","required":false,"schema":{"type":"string","example":"shipment_id"}},{"in":"query","name":"search_value","description":"Search type value","required":false,"schema":{"type":"string","example":"16578901076461551493K"}},{"in":"query","name":"from_date","description":"Start Date in DD-MM-YYYY format","required":false,"schema":{"type":"string","format":"date","example":"2023-05-10"}},{"in":"query","name":"to_date","description":"End Date in DD-MM-YYYY format","required":false,"schema":{"type":"string","format":"date","example":"2023-05-13"}},{"in":"query","name":"dp_ids","description":"Comma separated values of delivery partner ids","required":false,"schema":{"type":"string","example":"19,26"}},{"in":"query","name":"stores","description":"Comma separated values of store ids","required":false,"schema":{"type":"string","example":"12,34"}},{"in":"query","name":"sales_channels","description":"Comma separated values of sales channel ids","required":false,"schema":{"type":"string","example":"000000000000000000000001,614b42d1ea943427b5f46d1e"}},{"in":"query","name":"page_no","description":"Page number for paginated data","required":false,"schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","description":"Page size of data received per page","required":false,"schema":{"type":"integer","default":10}},{"in":"query","name":"fetch_active_shipment","description":"flag to fetch active shipments","required":false,"schema":{"type":"boolean","default":true}},{"in":"query","name":"exclude_locked_shipments","description":"flag to fetch locked shipments","required":false,"schema":{"type":"boolean","default":true}},{"in":"query","name":"payment_methods","description":"Comma separated values of payment methods","required":false,"schema":{"type":"string","example":"COD,PREPAID"}},{"in":"query","name":"channel_shipment_id","description":"App Shipment Id","required":false,"schema":{"type":"string","example":16731535496121004000}},{"in":"query","name":"channel_order_id","description":"App Order Id","required":false,"schema":{"type":"string","example":"FY63BA4C0D0125F8A075"}},{"in":"query","name":"custom_meta","required":false,"schema":{"type":"string"}},{"in":"query","name":"ordering_channel","required":false,"schema":{"type":"string"}},{"in":"query","name":"company_affiliate_tag","required":false,"schema":{"type":"string"}},{"in":"query","name":"my_orders","required":false,"schema":{"type":"boolean"}}],"query":[{"in":"query","name":"lane","description":"Name of lane for which data is to be fetched","required":false,"schema":{"type":"string","enum":["new","confirmed","to_be_packed","ready_for_dispatch","in_transit","handed_over_to_customer","delivered","cancelled","return_initiated","return_in_transit","return_delivered","return_accepted"],"example":"new"}},{"in":"query","name":"bag_status","description":"Comma separated values of bag statuses","required":false,"schema":{"type":"string","example":"placed, bag_confirmed, bag_invoiced"}},{"in":"query","name":"status_override_lane","description":"Use this flag to fetch by bag_status and override lane","required":false,"schema":{"type":"boolean","default":false}},{"in":"query","name":"time_to_dispatch","required":false,"schema":{"type":"string","example":1,"enum":[1,-1]}},{"in":"query","name":"search_type","description":"Search type key","required":false,"schema":{"type":"string","example":"shipment_id"}},{"in":"query","name":"search_value","description":"Search type value","required":false,"schema":{"type":"string","example":"16578901076461551493K"}},{"in":"query","name":"from_date","description":"Start Date in DD-MM-YYYY format","required":false,"schema":{"type":"string","format":"date","example":"2023-05-10"}},{"in":"query","name":"to_date","description":"End Date in DD-MM-YYYY format","required":false,"schema":{"type":"string","format":"date","example":"2023-05-13"}},{"in":"query","name":"dp_ids","description":"Comma separated values of delivery partner ids","required":false,"schema":{"type":"string","example":"19,26"}},{"in":"query","name":"stores","description":"Comma separated values of store ids","required":false,"schema":{"type":"string","example":"12,34"}},{"in":"query","name":"sales_channels","description":"Comma separated values of sales channel ids","required":false,"schema":{"type":"string","example":"000000000000000000000001,614b42d1ea943427b5f46d1e"}},{"in":"query","name":"page_no","description":"Page number for paginated data","required":false,"schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","description":"Page size of data received per page","required":false,"schema":{"type":"integer","default":10}},{"in":"query","name":"fetch_active_shipment","description":"flag to fetch active shipments","required":false,"schema":{"type":"boolean","default":true}},{"in":"query","name":"exclude_locked_shipments","description":"flag to fetch locked shipments","required":false,"schema":{"type":"boolean","default":true}},{"in":"query","name":"payment_methods","description":"Comma separated values of payment methods","required":false,"schema":{"type":"string","example":"COD,PREPAID"}},{"in":"query","name":"channel_shipment_id","description":"App Shipment Id","required":false,"schema":{"type":"string","example":16731535496121004000}},{"in":"query","name":"channel_order_id","description":"App Order Id","required":false,"schema":{"type":"string","example":"FY63BA4C0D0125F8A075"}},{"in":"query","name":"custom_meta","required":false,"schema":{"type":"string"}},{"in":"query","name":"ordering_channel","required":false,"schema":{"type":"string"}},{"in":"query","name":"company_affiliate_tag","required":false,"schema":{"type":"string"}},{"in":"query","name":"my_orders","required":false,"schema":{"type":"boolean"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer","example":37}}]}""", lane=lane, bag_status=bag_status, status_override_lane=status_override_lane, time_to_dispatch=time_to_dispatch, search_type=search_type, search_value=search_value, from_date=from_date, to_date=to_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, page_no=page_no, page_size=page_size, fetch_active_shipment=fetch_active_shipment, exclude_locked_shipments=exclude_locked_shipments, payment_methods=payment_methods, channel_shipment_id=channel_shipment_id, channel_order_id=channel_order_id, custom_meta=custom_meta, ordering_channel=ordering_channel, company_affiliate_tag=company_affiliate_tag, my_orders=my_orders)
        query_string = await create_query_string(lane=lane, bag_status=bag_status, status_override_lane=status_override_lane, time_to_dispatch=time_to_dispatch, search_type=search_type, search_value=search_value, from_date=from_date, to_date=to_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, page_no=page_no, page_size=page_size, fetch_active_shipment=fetch_active_shipment, exclude_locked_shipments=exclude_locked_shipments, payment_methods=payment_methods, channel_shipment_id=channel_shipment_id, channel_order_id=channel_order_id, custom_meta=custom_meta, ordering_channel=ordering_channel, company_affiliate_tag=company_affiliate_tag, my_orders=my_orders)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/shipments-listing", lane=lane, bag_status=bag_status, status_override_lane=status_override_lane, time_to_dispatch=time_to_dispatch, search_type=search_type, search_value=search_value, from_date=from_date, to_date=to_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, page_no=page_no, page_size=page_size, fetch_active_shipment=fetch_active_shipment, exclude_locked_shipments=exclude_locked_shipments, payment_methods=payment_methods, channel_shipment_id=channel_shipment_id, channel_order_id=channel_order_id, custom_meta=custom_meta, ordering_channel=ordering_channel, company_affiliate_tag=company_affiliate_tag, my_orders=my_orders), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ShipmentInternalPlatformViewResponse
            schema = ShipmentInternalPlatformViewResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getShipments")
                print(e)

        

        return response
    
    async def getShipmentById(self, channel_shipment_id=None, shipment_id=None):
        """
        :param channel_shipment_id : App Shipment Id : type string
        :param shipment_id : Shipment Id : type string
        """
        payload = {}
        
        if channel_shipment_id is not None:
            payload["channel_shipment_id"] = channel_shipment_id
        
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id
        

        # Parameter validation
        schema = OrderValidator.getShipmentById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/shipment-details", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer","example":37}}],"optional":[{"in":"query","name":"channel_shipment_id","description":"App Shipment Id","required":false,"schema":{"type":"string","example":16731535496121004000}},{"in":"query","name":"shipment_id","description":"Shipment Id","required":false,"schema":{"type":"string","example":16731535496121004000}}],"query":[{"in":"query","name":"channel_shipment_id","description":"App Shipment Id","required":false,"schema":{"type":"string","example":16731535496121004000}},{"in":"query","name":"shipment_id","description":"Shipment Id","required":false,"schema":{"type":"string","example":16731535496121004000}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer","example":37}}]}""", channel_shipment_id=channel_shipment_id, shipment_id=shipment_id)
        query_string = await create_query_string(channel_shipment_id=channel_shipment_id, shipment_id=shipment_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/shipment-details", channel_shipment_id=channel_shipment_id, shipment_id=shipment_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ShipmentInfoResponse
            schema = ShipmentInfoResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getShipmentById")
                print(e)

        

        return response
    
    async def getOrderById(self, order_id=None):
        """
        :param order_id :  : type string
        """
        payload = {}
        
        if order_id is not None:
            payload["order_id"] = order_id
        

        # Parameter validation
        schema = OrderValidator.getOrderById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/order-details", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}},{"in":"query","name":"order_id","required":true,"schema":{"type":"string","default":"FY6299E19701B4EAEFC2"}}],"optional":[],"query":[{"in":"query","name":"order_id","required":true,"schema":{"type":"string","default":"FY6299E19701B4EAEFC2"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", order_id=order_id)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/order-details", order_id=order_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import OrderDetailsResponse
            schema = OrderDetailsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOrderById")
                print(e)

        

        return response
    
    async def getLaneConfig(self, super_lane=None, group_entity=None, from_date=None, to_date=None, dp_ids=None, stores=None, sales_channels=None, payment_mode=None, bag_status=None, search_type=None, search_value=None, tags=None, time_to_dispatch=None, payment_methods=None, my_orders=None):
        """
        :param super_lane : Name of lane for which data is to be fetched : type string
        :param group_entity : Name of group entity : type string
        :param from_date : Start Date in DD-MM-YYYY format : type string
        :param to_date : End Date in DD-MM-YYYY format : type string
        :param dp_ids : Comma separated values of delivery partner ids : type string
        :param stores : Comma separated values of store ids : type string
        :param sales_channels :  : type string
        :param payment_mode : Comma separated values of payment modes : type string
        :param bag_status : Comma separated values of bag statuses : type string
        :param search_type :  : type string
        :param search_value :  : type string
        :param tags :  : type string
        :param time_to_dispatch :  : type string
        :param payment_methods :  : type string
        :param my_orders :  : type boolean
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
        

        # Parameter validation
        schema = OrderValidator.getLaneConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/lane-config/", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"super_lane","description":"Name of lane for which data is to be fetched","required":false,"schema":{"type":"string","enum":["unfulfilled","processed","returns","action_centre"],"default":"unfulfilled"}},{"in":"query","name":"group_entity","description":"Name of group entity","required":false,"schema":{"type":"string","enum":["shipments","orders","bags"],"default":"shipments"}},{"in":"query","name":"from_date","description":"Start Date in DD-MM-YYYY format","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","description":"End Date in DD-MM-YYYY format","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","description":"Comma separated values of delivery partner ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","description":"Comma separated values of store ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channels","required":false,"schema":{"type":"string"}},{"in":"query","name":"payment_mode","description":"Comma separated values of payment modes","required":false,"schema":{"type":"string"}},{"in":"query","name":"bag_status","description":"Comma separated values of bag statuses","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_value","required":false,"schema":{"type":"string"}},{"in":"query","name":"tags","required":false,"schema":{"type":"string"}},{"in":"query","name":"time_to_dispatch","required":false,"schema":{"type":"string"}},{"in":"query","name":"payment_methods","required":false,"schema":{"type":"string"}},{"in":"query","name":"my_orders","required":false,"schema":{"type":"boolean"}}],"query":[{"in":"query","name":"super_lane","description":"Name of lane for which data is to be fetched","required":false,"schema":{"type":"string","enum":["unfulfilled","processed","returns","action_centre"],"default":"unfulfilled"}},{"in":"query","name":"group_entity","description":"Name of group entity","required":false,"schema":{"type":"string","enum":["shipments","orders","bags"],"default":"shipments"}},{"in":"query","name":"from_date","description":"Start Date in DD-MM-YYYY format","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","description":"End Date in DD-MM-YYYY format","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","description":"Comma separated values of delivery partner ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","description":"Comma separated values of store ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channels","required":false,"schema":{"type":"string"}},{"in":"query","name":"payment_mode","description":"Comma separated values of payment modes","required":false,"schema":{"type":"string"}},{"in":"query","name":"bag_status","description":"Comma separated values of bag statuses","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_type","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_value","required":false,"schema":{"type":"string"}},{"in":"query","name":"tags","required":false,"schema":{"type":"string"}},{"in":"query","name":"time_to_dispatch","required":false,"schema":{"type":"string"}},{"in":"query","name":"payment_methods","required":false,"schema":{"type":"string"}},{"in":"query","name":"my_orders","required":false,"schema":{"type":"boolean"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", super_lane=super_lane, group_entity=group_entity, from_date=from_date, to_date=to_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, payment_mode=payment_mode, bag_status=bag_status, search_type=search_type, search_value=search_value, tags=tags, time_to_dispatch=time_to_dispatch, payment_methods=payment_methods, my_orders=my_orders)
        query_string = await create_query_string(super_lane=super_lane, group_entity=group_entity, from_date=from_date, to_date=to_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, payment_mode=payment_mode, bag_status=bag_status, search_type=search_type, search_value=search_value, tags=tags, time_to_dispatch=time_to_dispatch, payment_methods=payment_methods, my_orders=my_orders)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/lane-config/", super_lane=super_lane, group_entity=group_entity, from_date=from_date, to_date=to_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, payment_mode=payment_mode, bag_status=bag_status, search_type=search_type, search_value=search_value, tags=tags, time_to_dispatch=time_to_dispatch, payment_methods=payment_methods, my_orders=my_orders), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import LaneConfigResponse
            schema = LaneConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getLaneConfig")
                print(e)

        

        return response
    
    async def getOrders(self, lane=None, search_type=None, bag_status=None, time_to_dispatch=None, payment_methods=None, tags=None, search_value=None, from_date=None, to_date=None, dp_ids=None, stores=None, sales_channels=None, page_no=None, page_size=None, is_priority_sort=None, custom_meta=None, my_orders=None):
        """
        :param lane : lane refers to a section where orders are assigned, indicating its grouping : type string
        :param search_type : search_type refers to the field that will be used as the target for the search operation : type string
        :param bag_status : bag_status refers to status of the entity. Filters orders based on the status. : type string
        :param time_to_dispatch : time_to_dispatch refers to estimated SLA time. : type string
        :param payment_methods :  : type string
        :param tags : tags refers to additional descriptive labels associated with the order : type string
        :param search_value : search_value is matched against the field specified by the search_type : type string
        :param from_date :  : type string
        :param to_date :  : type string
        :param dp_ids : Delivery Partner IDs to which shipments are assigned. : type string
        :param stores :  : type string
        :param sales_channels :  : type string
        :param page_no :  : type integer
        :param page_size :  : type integer
        :param is_priority_sort :  : type boolean
        :param custom_meta :  : type string
        :param my_orders :  : type boolean
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
        

        # Parameter validation
        schema = OrderValidator.getOrders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders-listing", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer","default":37}}],"optional":[{"in":"query","name":"lane","description":"lane refers to a section where orders are assigned, indicating its grouping","required":false,"schema":{"type":"string","default":"new"}},{"in":"query","name":"search_type","description":"search_type refers to the field that will be used as the target for the search operation","required":false,"schema":{"type":"string","default":"shipment_id"}},{"in":"query","name":"bag_status","description":"bag_status refers to status of the entity. Filters orders based on the status.","required":false,"schema":{"type":"string"}},{"in":"query","name":"time_to_dispatch","description":"time_to_dispatch refers to estimated SLA time.","required":false,"schema":{"type":"string"}},{"in":"query","name":"payment_methods","required":false,"schema":{"type":"string"}},{"in":"query","name":"tags","description":"tags refers to additional descriptive labels associated with the order","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_value","description":"search_value is matched against the field specified by the search_type","required":false,"schema":{"type":"string","default":16854460524441037000}},{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","description":"Delivery Partner IDs to which shipments are assigned.","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channels","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"is_priority_sort","required":false,"schema":{"type":"boolean","default":true}},{"in":"query","name":"custom_meta","required":false,"schema":{"type":"string","default":{"store_id":"6388422a5ebd6a6cf4a8ede6"}}},{"in":"query","name":"my_orders","required":false,"schema":{"type":"boolean"}}],"query":[{"in":"query","name":"lane","description":"lane refers to a section where orders are assigned, indicating its grouping","required":false,"schema":{"type":"string","default":"new"}},{"in":"query","name":"search_type","description":"search_type refers to the field that will be used as the target for the search operation","required":false,"schema":{"type":"string","default":"shipment_id"}},{"in":"query","name":"bag_status","description":"bag_status refers to status of the entity. Filters orders based on the status.","required":false,"schema":{"type":"string"}},{"in":"query","name":"time_to_dispatch","description":"time_to_dispatch refers to estimated SLA time.","required":false,"schema":{"type":"string"}},{"in":"query","name":"payment_methods","required":false,"schema":{"type":"string"}},{"in":"query","name":"tags","description":"tags refers to additional descriptive labels associated with the order","required":false,"schema":{"type":"string"}},{"in":"query","name":"search_value","description":"search_value is matched against the field specified by the search_type","required":false,"schema":{"type":"string","default":16854460524441037000}},{"in":"query","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","description":"Delivery Partner IDs to which shipments are assigned.","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","required":false,"schema":{"type":"string"}},{"in":"query","name":"sales_channels","required":false,"schema":{"type":"string"}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","name":"is_priority_sort","required":false,"schema":{"type":"boolean","default":true}},{"in":"query","name":"custom_meta","required":false,"schema":{"type":"string","default":{"store_id":"6388422a5ebd6a6cf4a8ede6"}}},{"in":"query","name":"my_orders","required":false,"schema":{"type":"boolean"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer","default":37}}]}""", lane=lane, search_type=search_type, bag_status=bag_status, time_to_dispatch=time_to_dispatch, payment_methods=payment_methods, tags=tags, search_value=search_value, from_date=from_date, to_date=to_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, page_no=page_no, page_size=page_size, is_priority_sort=is_priority_sort, custom_meta=custom_meta, my_orders=my_orders)
        query_string = await create_query_string(lane=lane, search_type=search_type, bag_status=bag_status, time_to_dispatch=time_to_dispatch, payment_methods=payment_methods, tags=tags, search_value=search_value, from_date=from_date, to_date=to_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, page_no=page_no, page_size=page_size, is_priority_sort=is_priority_sort, custom_meta=custom_meta, my_orders=my_orders)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders-listing", lane=lane, search_type=search_type, bag_status=bag_status, time_to_dispatch=time_to_dispatch, payment_methods=payment_methods, tags=tags, search_value=search_value, from_date=from_date, to_date=to_date, dp_ids=dp_ids, stores=stores, sales_channels=sales_channels, page_no=page_no, page_size=page_size, is_priority_sort=is_priority_sort, custom_meta=custom_meta, my_orders=my_orders), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import OrderListingResponse
            schema = OrderListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOrders")
                print(e)

        

        return response
    
    async def getfilters(self, view=None, group_entity=None):
        """
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/filter-listing", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}},{"in":"query","name":"view","description":"Name of view","required":true,"schema":{"type":"string","default":"manifest","enum":["my_orders","bulk_actions","manifest"]}}],"optional":[{"in":"query","name":"group_entity","description":"Name of group entity","required":false,"schema":{"type":"string","default":"orders","enum":["orders","shipments"]}}],"query":[{"in":"query","name":"view","description":"Name of view","required":true,"schema":{"type":"string","default":"manifest","enum":["my_orders","bulk_actions","manifest"]}},{"in":"query","name":"group_entity","description":"Name of group entity","required":false,"schema":{"type":"string","default":"orders","enum":["orders","shipments"]}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", view=view, group_entity=group_entity)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/filter-listing", view=view, group_entity=group_entity), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import FiltersResponse
            schema = FiltersResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getfilters")
                print(e)

        

        return response
    
    async def getBulkShipmentExcelFile(self, sales_channels=None, dp_ids=None, from_date=None, to_date=None, stores=None, tags=None, bag_status=None, payment_methods=None, file_type=None, time_to_dispatch=None, page_no=None, page_size=None):
        """
        :param sales_channels : Comma separated values of sales channel ids : type string
        :param dp_ids : Comma separated values of delivery partner ids : type string
        :param from_date : Start Date in DD-MM-YYYY format : type string
        :param to_date : End Date in DD-MM-YYYY format : type string
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
        
        if from_date is not None:
            payload["from_date"] = from_date
        
        if to_date is not None:
            payload["to_date"] = to_date
        
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/generate/file", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"sales_channels","description":"Comma separated values of sales channel ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","description":"Comma separated values of delivery partner ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"from_date","description":"Start Date in DD-MM-YYYY format","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","description":"End Date in DD-MM-YYYY format","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","description":"Comma separated values of store ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"tags","description":"Comma separated values of tags","required":false,"schema":{"type":"string"}},{"in":"query","name":"bag_status","description":"Comma separated values of bag statuses","required":false,"schema":{"type":"string"}},{"in":"query","name":"payment_methods","description":"Comma separated values of payment methods","required":false,"schema":{"type":"string"}},{"in":"query","name":"file_type","description":"File type to be downloaded","required":false,"schema":{"type":"string"}},{"in":"query","name":"time_to_dispatch","description":"Sla breached or not breached","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer","default":10}}],"query":[{"in":"query","name":"sales_channels","description":"Comma separated values of sales channel ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"dp_ids","description":"Comma separated values of delivery partner ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"from_date","description":"Start Date in DD-MM-YYYY format","required":false,"schema":{"type":"string"}},{"in":"query","name":"to_date","description":"End Date in DD-MM-YYYY format","required":false,"schema":{"type":"string"}},{"in":"query","name":"stores","description":"Comma separated values of store ids","required":false,"schema":{"type":"string"}},{"in":"query","name":"tags","description":"Comma separated values of tags","required":false,"schema":{"type":"string"}},{"in":"query","name":"bag_status","description":"Comma separated values of bag statuses","required":false,"schema":{"type":"string"}},{"in":"query","name":"payment_methods","description":"Comma separated values of payment methods","required":false,"schema":{"type":"string"}},{"in":"query","name":"file_type","description":"File type to be downloaded","required":false,"schema":{"type":"string"}},{"in":"query","name":"time_to_dispatch","description":"Sla breached or not breached","required":false,"schema":{"type":"integer"}},{"in":"query","name":"page_no","required":false,"schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", sales_channels=sales_channels, dp_ids=dp_ids, from_date=from_date, to_date=to_date, stores=stores, tags=tags, bag_status=bag_status, payment_methods=payment_methods, file_type=file_type, time_to_dispatch=time_to_dispatch, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(sales_channels=sales_channels, dp_ids=dp_ids, from_date=from_date, to_date=to_date, stores=stores, tags=tags, bag_status=bag_status, payment_methods=payment_methods, file_type=file_type, time_to_dispatch=time_to_dispatch, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/generate/file", sales_channels=sales_channels, dp_ids=dp_ids, from_date=from_date, to_date=to_date, stores=stores, tags=tags, bag_status=bag_status, payment_methods=payment_methods, file_type=file_type, time_to_dispatch=time_to_dispatch, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import FileResponse
            schema = FileResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBulkShipmentExcelFile")
                print(e)

        

        return response
    
    async def getBulkActionTemplate(self, ):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.getBulkActionTemplate()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/bulk-action/get-seller-templates", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/bulk-action/get-seller-templates", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkActionTemplateResponse
            schema = BulkActionTemplateResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBulkActionTemplate")
                print(e)

        

        return response
    
    async def downloadBulkActionTemplate(self, template_slug=None):
        """
        :param template_slug : Slug name of template to be downloaded : type string
        """
        payload = {}
        
        if template_slug is not None:
            payload["template_slug"] = template_slug
        

        # Parameter validation
        schema = OrderValidator.downloadBulkActionTemplate()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/bulk-action/download-seller-templates", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"template_slug","description":"Slug name of template to be downloaded","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"template_slug","description":"Slug name of template to be downloaded","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", template_slug=template_slug)
        query_string = await create_query_string(template_slug=template_slug)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/bulk-action/download-seller-templates", template_slug=template_slug), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import FileResponse
            schema = FileResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for downloadBulkActionTemplate")
                print(e)

        

        return response
    
    async def getShipmentReasons(self, shipment_id=None, bag_id=None, state=None):
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/shipments/{shipment_id}/bags/{bag_id}/state/{state}/reasons", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"path","name":"shipment_id","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}},{"in":"path","description":"ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"bag_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"state","description":"State for which reasons are required.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"path","name":"shipment_id","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}},{"in":"path","description":"ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"bag_id","required":true,"schema":{"type":"string"}},{"in":"path","name":"state","description":"State for which reasons are required.","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id, bag_id=bag_id, state=state)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/shipments/{shipment_id}/bags/{bag_id}/state/{state}/reasons", shipment_id=shipment_id, bag_id=bag_id, state=state), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import PlatformShipmentReasonsResponse
            schema = PlatformShipmentReasonsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getShipmentReasons")
                print(e)

        

        return response
    
    async def getBagById(self, bag_id=None, channel_bag_id=None, channel_id=None):
        """
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/bag-details/", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"bag_id","description":"Id of bag","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_bag_id","description":"Id of application bag","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_id","description":"Id of application","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"bag_id","description":"Id of bag","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_bag_id","description":"Id of application bag","required":false,"schema":{"type":"string"}},{"in":"query","name":"channel_id","description":"Id of application","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", bag_id=bag_id, channel_bag_id=channel_bag_id, channel_id=channel_id)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/bag-details/", bag_id=bag_id, channel_bag_id=channel_bag_id, channel_id=channel_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import BagDetailsPlatformResponse
            schema = BagDetailsPlatformResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBagById")
                print(e)

        

        return response
    
    async def getBags(self, bag_ids=None, shipment_ids=None, order_ids=None, channel_bag_ids=None, channel_shipment_ids=None, channel_order_ids=None, channel_id=None, page_no=None, page_size=None):
        """
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/bags", """{"required":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"bag_ids","description":"Comma separated values of bag ids","required":false,"schema":{"type":"string","example":"1234,2344"}},{"in":"query","name":"shipment_ids","description":"Comma separated values of shipment ids","required":false,"schema":{"type":"string","example":"1661111234,167772344"}},{"in":"query","name":"order_ids","description":"Comma separated values of order ids","required":false,"schema":{"type":"string","example":"1661111234,167772344"}},{"in":"query","name":"channel_bag_ids","description":"Comma separated values of app bag ids","required":false,"schema":{"type":"string","example":"B1234,B2344"}},{"in":"query","name":"channel_shipment_ids","description":"Comma separated values of app shipment ids","required":false,"schema":{"type":"string","example":"S1234,S2344"}},{"in":"query","name":"channel_order_ids","description":"Comma separated values of app order ids","required":false,"schema":{"type":"string","example":"O1234,02344"}},{"in":"query","name":"channel_id","description":"Comma separated values of app ids","required":false,"schema":{"type":"string","example":"000000000000000000000001,614b42d1ea943427b5f46d1e"}},{"in":"query","name":"page_no","description":"Page number for paginated data","required":false,"schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","description":"Page size of data received per page","required":false,"schema":{"type":"integer","default":20}}],"query":[{"in":"query","name":"bag_ids","description":"Comma separated values of bag ids","required":false,"schema":{"type":"string","example":"1234,2344"}},{"in":"query","name":"shipment_ids","description":"Comma separated values of shipment ids","required":false,"schema":{"type":"string","example":"1661111234,167772344"}},{"in":"query","name":"order_ids","description":"Comma separated values of order ids","required":false,"schema":{"type":"string","example":"1661111234,167772344"}},{"in":"query","name":"channel_bag_ids","description":"Comma separated values of app bag ids","required":false,"schema":{"type":"string","example":"B1234,B2344"}},{"in":"query","name":"channel_shipment_ids","description":"Comma separated values of app shipment ids","required":false,"schema":{"type":"string","example":"S1234,S2344"}},{"in":"query","name":"channel_order_ids","description":"Comma separated values of app order ids","required":false,"schema":{"type":"string","example":"O1234,02344"}},{"in":"query","name":"channel_id","description":"Comma separated values of app ids","required":false,"schema":{"type":"string","example":"000000000000000000000001,614b42d1ea943427b5f46d1e"}},{"in":"query","name":"page_no","description":"Page number for paginated data","required":false,"schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","description":"Page size of data received per page","required":false,"schema":{"type":"integer","default":20}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of company","required":true,"schema":{"type":"integer"}}]}""", bag_ids=bag_ids, shipment_ids=shipment_ids, order_ids=order_ids, channel_bag_ids=channel_bag_ids, channel_shipment_ids=channel_shipment_ids, channel_order_ids=channel_order_ids, channel_id=channel_id, page_no=page_no, page_size=page_size)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/bags", bag_ids=bag_ids, shipment_ids=shipment_ids, order_ids=order_ids, channel_bag_ids=channel_bag_ids, channel_shipment_ids=channel_shipment_ids, channel_order_ids=channel_order_ids, channel_id=channel_id, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetBagsPlatformResponse
            schema = GetBagsPlatformResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBags")
                print(e)

        

        return response
    
    async def generatePOSReceiptByOrderId(self, order_id=None, shipment_id=None, document_type=None):
        """
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders/{order_id}/generate/pos-receipt", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"path","name":"order_id","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"shipment_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"document_type","required":false,"schema":{"type":"string","default":"invoice_receipt"}}],"query":[{"in":"query","name":"shipment_id","required":false,"schema":{"type":"string"}},{"in":"query","name":"document_type","required":false,"schema":{"type":"string","default":"invoice_receipt"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}},{"in":"path","name":"order_id","required":true,"schema":{"type":"string"}}]}""", order_id=order_id, shipment_id=shipment_id, document_type=document_type)
        query_string = await create_query_string(order_id=order_id, shipment_id=shipment_id, document_type=document_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order/v1.0/company/{self._conf.companyId}/orders/{order_id}/generate/pos-receipt", order_id=order_id, shipment_id=shipment_id, document_type=document_type), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GeneratePosOrderReceiptResponse
            schema = GeneratePosOrderReceiptResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for generatePOSReceiptByOrderId")
                print(e)

        

        return response
    
    async def invalidateShipmentCache(self, body=""):
        """Invalidate shipment Cache
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.invalidateShipmentCache()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import InvalidateShipmentCachePayload
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
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/update-cache", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import InvalidateShipmentCacheResponse
            schema = InvalidateShipmentCacheResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for invalidateShipmentCache")
                print(e)

        

        return response
    
    async def reassignLocation(self, body=""):
        """Reassign Location
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.reassignLocation()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import StoreReassign
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/store/reassign-internal", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import StoreReassignResponse
            schema = StoreReassignResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for reassignLocation")
                print(e)

        

        return response
    
    async def updateShipmentLock(self, body=""):
        """update shipment/bag lock and check status
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.updateShipmentLock()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateShipmentLockPayload
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/entity/lock-manager", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdateShipmentLockResponse
            schema = UpdateShipmentLockResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateShipmentLock")
                print(e)

        

        return response
    
    async def getAnnouncements(self, date=None):
        """
        :param date : Date On which the announcement is Active (Date should in ISO Datetime format IST Time) : type string
        """
        payload = {}
        
        if date is not None:
            payload["date"] = date
        

        # Parameter validation
        schema = OrderValidator.getAnnouncements()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/announcements", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"in":"query","name":"date","required":false,"description":"Date On which the announcement is Active (Date should in ISO Datetime format IST Time)","schema":{"type":"string"}}],"query":[{"in":"query","name":"date","required":false,"description":"Date On which the announcement is Active (Date should in ISO Datetime format IST Time)","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", date=date)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/announcements", date=date), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import AnnouncementsResponse
            schema = AnnouncementsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAnnouncements")
                print(e)

        

        return response
    
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/delight/update-address", shipment_id=shipment_id, name=name, address=address, address_type=address_type, pincode=pincode, phone=phone, email=email, landmark=landmark, address_category=address_category, city=city, state=state, country=country, ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import BaseResponse
            schema = BaseResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAddress")
                print(e)

        

        return response
    
    async def click2Call(self, caller=None, receiver=None, bag_id=None, caller_id=None, method=None):
        """
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/ninja/click2call", """{"required":[{"in":"query","name":"caller","required":true,"description":"Call Number","schema":{"type":"string"}},{"in":"query","name":"receiver","required":true,"description":"Receiver Number","schema":{"type":"string"}},{"in":"query","name":"bag_id","required":true,"description":"Bag Id for the query","schema":{"type":"string"}},{"in":"path","name":"company_id","required":true,"description":"Company Id","schema":{"type":"integer"}}],"optional":[{"in":"query","name":"caller_id","required":false,"description":"Caller Id","schema":{"type":"string"}},{"in":"query","name":"method","required":false,"description":"Provider Method to Call","schema":{"type":"string","example":"dial.click2call"}}],"query":[{"in":"query","name":"caller","required":true,"description":"Call Number","schema":{"type":"string"}},{"in":"query","name":"receiver","required":true,"description":"Receiver Number","schema":{"type":"string"}},{"in":"query","name":"bag_id","required":true,"description":"Bag Id for the query","schema":{"type":"string"}},{"in":"query","name":"caller_id","required":false,"description":"Caller Id","schema":{"type":"string"}},{"in":"query","name":"method","required":false,"description":"Provider Method to Call","schema":{"type":"string","example":"dial.click2call"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Company Id","schema":{"type":"integer"}}]}""", caller=caller, receiver=receiver, bag_id=bag_id, caller_id=caller_id, method=method, )
        query_string = await create_query_string(caller=caller, receiver=receiver, bag_id=bag_id, caller_id=caller_id, method=method, )
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/ninja/click2call", caller=caller, receiver=receiver, bag_id=bag_id, caller_id=caller_id, method=method, ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import Click2CallResponse
            schema = Click2CallResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for click2Call")
                print(e)

        

        return response
    
    async def updateShipmentStatus(self, body=""):
        """This API is for Shipment State transition or Shipment data update or both below example is for partial state transition with data update
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.updateShipmentStatus()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateShipmentStatusRequest
        schema = UpdateShipmentStatusRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/shipment/status-internal", """{"required":[{"in":"path","name":"company_id","description":"company id from where are transitioning the shipment state or data","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"company id from where are transitioning the shipment state or data","required":true,"schema":{"type":"integer"}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/shipment/status-internal", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdateShipmentStatusResponseBody
            schema = UpdateShipmentStatusResponseBody()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateShipmentStatus")
                print(e)

        

        return response
    
    async def processManifest(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.processManifest()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateOrderPayload
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/process-manifest", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateOrderResponse
            schema = CreateOrderResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for processManifest")
                print(e)

        

        return response
    
    async def dispatchManifest(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.dispatchManifest()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DispatchManifest
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/manifest/dispatch", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponse
            schema = SuccessResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for dispatchManifest")
                print(e)

        

        return response
    
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/roles", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetActionsResponse
            schema = GetActionsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getRoleBasedActions")
                print(e)

        

        return response
    
    async def getShipmentHistory(self, shipment_id=None, bag_id=None):
        """
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/shipment/history", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Company Id","schema":{"type":"integer"}}],"optional":[{"in":"query","name":"shipment_id","description":"Shipment Id","required":false,"schema":{"type":"string"}},{"in":"query","name":"bag_id","description":"Bag/Product Id","required":false,"schema":{"type":"integer"}}],"query":[{"in":"query","name":"shipment_id","description":"Shipment Id","required":false,"schema":{"type":"string"}},{"in":"query","name":"bag_id","description":"Bag/Product Id","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Company Id","schema":{"type":"integer"}}]}""", shipment_id=shipment_id, bag_id=bag_id)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/shipment/history", shipment_id=shipment_id, bag_id=bag_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ShipmentHistoryResponse
            schema = ShipmentHistoryResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getShipmentHistory")
                print(e)

        

        return response
    
    async def postShipmentHistory(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.postShipmentHistory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PostShipmentHistory
        schema = PostShipmentHistory()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/shipment/history", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/shipment/history", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ShipmentHistoryResponse
            schema = ShipmentHistoryResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for postShipmentHistory")
                print(e)

        

        return response
    
    async def sendSmsNinja(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.sendSmsNinja()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SendSmsPayload
        schema = SendSmsPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/ninja/send-sms", """{"required":[{"in":"path","name":"company_id","required":true,"description":"Company Id","schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"description":"Company Id","schema":{"type":"integer"}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/ninja/send-sms", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import OrderStatusResult
            schema = OrderStatusResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for sendSmsNinja")
                print(e)

        

        return response
    
    async def updatePackagingDimensions(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.updatePackagingDimensions()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdatePackagingDimensionsPayload
        schema = UpdatePackagingDimensionsPayload()
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/update-packaging-dimension", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdatePackagingDimensionsResponse
            schema = UpdatePackagingDimensionsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePackagingDimensions")
                print(e)

        

        return response
    
    async def createOrder(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.createOrder()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateOrderAPI
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/create-order", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateOrderResponse
            schema = CreateOrderResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createOrder")
                print(e)

        

        return response
    
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/order-config", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateChannelConfigData
            schema = CreateChannelConfigData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getChannelConfig")
                print(e)

        

        return response
    
    async def createChannelConfig(self, body=""):
        """createChannelConfig
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.createChannelConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateChannelConfigData
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/order-config", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateChannelConfigResponse
            schema = CreateChannelConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createChannelConfig")
                print(e)

        

        return response
    
    async def uploadConsent(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.uploadConsent()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UploadConsent
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/manifest/uploadConsent", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessResponse
            schema = SuccessResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for uploadConsent")
                print(e)

        

        return response
    
    async def orderUpdate(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.orderUpdate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PlatformOrderUpdate
        schema = PlatformOrderUpdate()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/order/validation", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/order/validation", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ResponseDetail
            schema = ResponseDetail()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for orderUpdate")
                print(e)

        

        return response
    
    async def checkOrderStatus(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.checkOrderStatus()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OrderStatus
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/debug/order_status", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import OrderStatusResult
            schema = OrderStatusResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for checkOrderStatus")
                print(e)

        

        return response
    
    async def getStateTransitionMap(self, ):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.getStateTransitionMap()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/bag/state/transition", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/bag/state/transition", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import BagStateTransitionMap
            schema = BagStateTransitionMap()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getStateTransitionMap")
                print(e)

        

        return response
    
    async def fetchCreditBalanceDetail(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.fetchCreditBalanceDetail()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import FetchCreditBalanceRequestPayload
        schema = FetchCreditBalanceRequestPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/customer-credit-balance", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/customer-credit-balance", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import FetchCreditBalanceResponsePayload
            schema = FetchCreditBalanceResponsePayload()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for fetchCreditBalanceDetail")
                print(e)

        

        return response
    
    async def fetchRefundModeConfig(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.fetchRefundModeConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import RefundModeConfigRequestPayload
        schema = RefundModeConfigRequestPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/refund-mode-config", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/refund-mode-config", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import RefundModeConfigResponsePayload
            schema = RefundModeConfigResponsePayload()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for fetchRefundModeConfig")
                print(e)

        

        return response
    
    async def attachOrderUser(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.attachOrderUser()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AttachOrderUser
        schema = AttachOrderUser()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/user/attach", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/user/attach", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import AttachOrderUserResponse
            schema = AttachOrderUserResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for attachOrderUser")
                print(e)

        

        return response
    
    async def sendUserMobileOTP(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.sendUserMobileOTP()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SendUserMobileOTP
        schema = SendUserMobileOTP()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/user/send/otp/mobile", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/user/send/otp/mobile", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import SendUserMobileOtpResponse
            schema = SendUserMobileOtpResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for sendUserMobileOTP")
                print(e)

        

        return response
    
    async def verifyMobileOTP(self, body=""):
        """
        """
        payload = {}
        

        # Parameter validation
        schema = OrderValidator.verifyMobileOTP()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import VerifyMobileOTP
        schema = VerifyMobileOTP()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/user/verify/otp", """{"required":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","required":true,"schema":{"type":"integer"}}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/order-manage/v1.0/company/{self._conf.companyId}/user/verify/otp", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import VerifyOtpResponse
            schema = VerifyOtpResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for verifyMobileOTP")
                print(e)

        

        return response
    

