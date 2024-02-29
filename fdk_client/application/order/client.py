"""Order Application Client"""

import base64
import ujson
from urllib.parse import urlparse
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..ApplicationConfig import ApplicationConfig

from .validator import OrderValidator

class Order:
    def __init__(self, config: ApplicationConfig):
        self._conf = config
        self._relativeUrls = {
            "getOrders": "/service/application/order/v1.0/orders",
            "getOrderById": "/service/application/order/v1.0/orders/{order_id}",
            "getPosOrderById": "/service/application/order/v1.0/orders/pos-order/{order_id}",
            "getShipmentById": "/service/application/order/v1.0/orders/shipments/{shipment_id}",
            "getInvoiceByShipmentId": "/service/application/order/v1.0/orders/shipments/{shipment_id}/invoice",
            "trackShipment": "/service/application/order/v1.0/orders/shipments/{shipment_id}/track",
            "getCustomerDetailsByShipmentId": "/service/application/order/v1.0/orders/{order_id}/shipments/{shipment_id}/customer-details",
            "sendOtpToShipmentCustomer": "/service/application/order/v1.0/orders/{order_id}/shipments/{shipment_id}/otp/send/",
            "verifyOtpShipmentCustomer": "/service/application/order/v1.0/orders/{order_id}/shipments/{shipment_id}/otp/verify/",
            "getShipmentBagReasons": "/service/application/order/v1.0/orders/shipments/{shipment_id}/bags/{bag_id}/reasons",
            "getShipmentReasons": "/service/application/order/v1.0/orders/shipments/{shipment_id}/reasons",
            "updateShipmentStatus": "/service/application/order/v1.0/orders/shipments/{shipment_id}/status"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getOrders(self, status=None, page_no=None, page_size=None, from_date=None, to_date=None, start_date=None, end_date=None, custom_meta=None, body="", request_headers:Dict={}):
        """Retrieves all orders associated with a customer account.
        :param status : A filter to retrieve orders by their current status such as _placed_, _delivered_, etc. : type integer
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        :param from_date : The date from which the orders should be retrieved. : type string
        :param to_date : The date till which the orders should be retrieved. : type string
        :param start_date : UTC Start Date in ISO format : type string
        :param end_date : UTC Start Date in ISO format : type string
        :param custom_meta : A filter and retrieve data using special fields included for special use-cases : type string
        """
        payload = {}
        
        if status is not None:
            payload["status"] = status
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if from_date is not None:
            payload["from_date"] = from_date
        if to_date is not None:
            payload["to_date"] = to_date
        if start_date is not None:
            payload["start_date"] = start_date
        if end_date is not None:
            payload["end_date"] = end_date
        if custom_meta is not None:
            payload["custom_meta"] = custom_meta

        # Parameter validation
        schema = OrderValidator.getOrders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOrders"], proccessed_params="""{"required":[],"optional":[{"in":"query","description":"A filter to retrieve orders by their current status such as _placed_, _delivered_, etc.","name":"status","required":false,"schema":{"type":"integer"}},{"in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","description":"The number of items to retrieve in each page. Default value is 10.","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","description":"The date from which the orders should be retrieved.","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","description":"The date till which the orders should be retrieved.","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","description":"UTC Start Date in ISO format","name":"start_date","required":false,"schema":{"type":"string","format":"date-time","example":"2023-08-29T10:49:36.804Z"}},{"in":"query","description":"UTC Start Date in ISO format","name":"end_date","required":false,"schema":{"type":"string","format":"date-time","example":"2023-08-30T10:49:36.804Z"}},{"in":"query","description":"A filter and retrieve data using special fields included for special use-cases","name":"custom_meta","required":false,"schema":{"type":"string","default":"6388422a5ebd6a6cf4a8ede6"}}],"query":[{"in":"query","description":"A filter to retrieve orders by their current status such as _placed_, _delivered_, etc.","name":"status","required":false,"schema":{"type":"integer"}},{"in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","description":"The number of items to retrieve in each page. Default value is 10.","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","description":"The date from which the orders should be retrieved.","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","description":"The date till which the orders should be retrieved.","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","description":"UTC Start Date in ISO format","name":"start_date","required":false,"schema":{"type":"string","format":"date-time","example":"2023-08-29T10:49:36.804Z"}},{"in":"query","description":"UTC Start Date in ISO format","name":"end_date","required":false,"schema":{"type":"string","format":"date-time","example":"2023-08-30T10:49:36.804Z"}},{"in":"query","description":"A filter and retrieve data using special fields included for special use-cases","name":"custom_meta","required":false,"schema":{"type":"string","default":"6388422a5ebd6a6cf4a8ede6"}}],"headers":[],"path":[]}""", status=status, page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, start_date=start_date, end_date=end_date, custom_meta=custom_meta)
        query_string = await create_query_string(status=status, page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, start_date=start_date, end_date=end_date, custom_meta=custom_meta)

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getOrders"]).netloc, "get", await create_url_without_domain("/service/application/order/v1.0/orders", status=status, page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, start_date=start_date, end_date=end_date, custom_meta=custom_meta), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import OrderList
            schema = OrderList()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOrders")
                print(e)

        return response
    
    async def getOrderById(self, order_id=None, allow_inactive=None, body="", request_headers:Dict={}):
        """Retrieve order details such as tracking details, shipment, store information using Fynd Order ID.
        :param order_id : A unique number used for identifying and tracking your orders. : type string
        :param allow_inactive : Flag to allow inactive shipments : type boolean
        """
        payload = {}
        
        if order_id is not None:
            payload["order_id"] = order_id
        if allow_inactive is not None:
            payload["allow_inactive"] = allow_inactive

        # Parameter validation
        schema = OrderValidator.getOrderById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOrderById"], proccessed_params="""{"required":[{"in":"path","name":"order_id","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"allow_inactive","description":"Flag to allow inactive shipments","required":false,"schema":{"type":"boolean","default":false}}],"query":[{"in":"query","name":"allow_inactive","description":"Flag to allow inactive shipments","required":false,"schema":{"type":"boolean","default":false}}],"headers":[],"path":[{"in":"path","name":"order_id","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}}]}""", order_id=order_id, allow_inactive=allow_inactive)
        query_string = await create_query_string(order_id=order_id, allow_inactive=allow_inactive)

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getOrderById"]).netloc, "get", await create_url_without_domain("/service/application/order/v1.0/orders/{order_id}", order_id=order_id, allow_inactive=allow_inactive), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import OrderById
            schema = OrderById()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOrderById")
                print(e)

        return response
    
    async def getPosOrderById(self, order_id=None, body="", request_headers:Dict={}):
        """Retrieve a POS order and all its details such as tracking details, shipment, store information using Fynd Order ID.
        :param order_id : A unique number used for identifying and tracking your orders. : type string
        """
        payload = {}
        
        if order_id is not None:
            payload["order_id"] = order_id

        # Parameter validation
        schema = OrderValidator.getPosOrderById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPosOrderById"], proccessed_params="""{"required":[{"in":"path","name":"order_id","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"order_id","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}}]}""", order_id=order_id)
        query_string = await create_query_string(order_id=order_id)

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPosOrderById"]).netloc, "get", await create_url_without_domain("/service/application/order/v1.0/orders/pos-order/{order_id}", order_id=order_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import OrderById
            schema = OrderById()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPosOrderById")
                print(e)

        return response
    
    async def getShipmentById(self, shipment_id=None, allow_inactive=None, body="", request_headers:Dict={}):
        """Retrieve shipment details such as price breakup, tracking details, store information, etc. using Shipment ID.
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        :param allow_inactive : Flag to allow inactive shipments : type boolean
        """
        payload = {}
        
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id
        if allow_inactive is not None:
            payload["allow_inactive"] = allow_inactive

        # Parameter validation
        schema = OrderValidator.getShipmentById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getShipmentById"], proccessed_params="""{"required":[{"in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"shipment_id","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"allow_inactive","description":"Flag to allow inactive shipments","required":false,"schema":{"type":"boolean","default":false}}],"query":[{"in":"query","name":"allow_inactive","description":"Flag to allow inactive shipments","required":false,"schema":{"type":"boolean","default":false}}],"headers":[],"path":[{"in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"shipment_id","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id, allow_inactive=allow_inactive)
        query_string = await create_query_string(shipment_id=shipment_id, allow_inactive=allow_inactive)

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getShipmentById"]).netloc, "get", await create_url_without_domain("/service/application/order/v1.0/orders/shipments/{shipment_id}", shipment_id=shipment_id, allow_inactive=allow_inactive), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import ShipmentById
            schema = ShipmentById()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getShipmentById")
                print(e)

        return response
    
    async def getInvoiceByShipmentId(self, shipment_id=None, body="", request_headers:Dict={}):
        """Retrieve the invoice corresponding to a specific shipment ID.
        :param shipment_id : ID of the shipment. : type string
        """
        payload = {}
        
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id

        # Parameter validation
        schema = OrderValidator.getInvoiceByShipmentId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getInvoiceByShipmentId"], proccessed_params="""{"required":[{"in":"path","description":"ID of the shipment.","name":"shipment_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","description":"ID of the shipment.","name":"shipment_id","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id)
        query_string = await create_query_string(shipment_id=shipment_id)

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getInvoiceByShipmentId"]).netloc, "get", await create_url_without_domain("/service/application/order/v1.0/orders/shipments/{shipment_id}/invoice", shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import ResponseGetInvoiceShipment
            schema = ResponseGetInvoiceShipment()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getInvoiceByShipmentId")
                print(e)

        return response
    
    async def trackShipment(self, shipment_id=None, body="", request_headers:Dict={}):
        """Track Shipment by shipment id, for application based on application Id.
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id

        # Parameter validation
        schema = OrderValidator.trackShipment()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["trackShipment"], proccessed_params="""{"required":[{"in":"path","name":"shipment_id","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string","default":"16544950215681060915J"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"shipment_id","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string","default":"16544950215681060915J"}}]}""", shipment_id=shipment_id)
        query_string = await create_query_string(shipment_id=shipment_id)

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["trackShipment"]).netloc, "get", await create_url_without_domain("/service/application/order/v1.0/orders/shipments/{shipment_id}/track", shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import ShipmentTrack
            schema = ShipmentTrack()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for trackShipment")
                print(e)

        return response
    
    async def getCustomerDetailsByShipmentId(self, order_id=None, shipment_id=None, body="", request_headers:Dict={}):
        """Retrieve customer details such as mobile number using Shipment ID.
        :param order_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        :param shipment_id : A unique number used for identifying and tracking your orders. : type string
        """
        payload = {}
        
        if order_id is not None:
            payload["order_id"] = order_id
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id

        # Parameter validation
        schema = OrderValidator.getCustomerDetailsByShipmentId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCustomerDetailsByShipmentId"], proccessed_params="""{"required":[{"in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"order_id","required":true,"schema":{"type":"string","default":"16544950215681060915J"}},{"in":"path","description":"A unique number used for identifying and tracking your orders.","name":"shipment_id","required":true,"schema":{"type":"string","default":"FY6299E19701B4EAEFC2"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"order_id","required":true,"schema":{"type":"string","default":"16544950215681060915J"}},{"in":"path","description":"A unique number used for identifying and tracking your orders.","name":"shipment_id","required":true,"schema":{"type":"string","default":"FY6299E19701B4EAEFC2"}}]}""", order_id=order_id, shipment_id=shipment_id)
        query_string = await create_query_string(order_id=order_id, shipment_id=shipment_id)

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCustomerDetailsByShipmentId"]).netloc, "get", await create_url_without_domain("/service/application/order/v1.0/orders/{order_id}/shipments/{shipment_id}/customer-details", order_id=order_id, shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import CustomerDetailsResponse
            schema = CustomerDetailsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCustomerDetailsByShipmentId")
                print(e)

        return response
    
    async def sendOtpToShipmentCustomer(self, order_id=None, shipment_id=None, body="", request_headers:Dict={}):
        """Sends a one-time password (OTP) to the customer for shipment verification.
        :param order_id : A unique number used for identifying and tracking your orders. : type string
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if order_id is not None:
            payload["order_id"] = order_id
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id

        # Parameter validation
        schema = OrderValidator.sendOtpToShipmentCustomer()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["sendOtpToShipmentCustomer"], proccessed_params="""{"required":[{"in":"path","name":"order_id","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string","default":"FY6299E19701B4EAEFC2"}},{"in":"path","name":"shipment_id","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string","default":"16544950215681060915J"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"order_id","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string","default":"FY6299E19701B4EAEFC2"}},{"in":"path","name":"shipment_id","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string","default":"16544950215681060915J"}}]}""", order_id=order_id, shipment_id=shipment_id)
        query_string = await create_query_string(order_id=order_id, shipment_id=shipment_id)

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["sendOtpToShipmentCustomer"]).netloc, "post", await create_url_without_domain("/service/application/order/v1.0/orders/{order_id}/shipments/{shipment_id}/otp/send/", order_id=order_id, shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import SendOtpToCustomerResponse
            schema = SendOtpToCustomerResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for sendOtpToShipmentCustomer")
                print(e)

        return response
    
    async def verifyOtpShipmentCustomer(self, order_id=None, shipment_id=None, body="", request_headers:Dict={}):
        """Confirms the OTP sent to the shipment customer for verification.
        :param order_id : A unique number used for identifying and tracking your orders. : type string
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if order_id is not None:
            payload["order_id"] = order_id
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id

        # Parameter validation
        schema = OrderValidator.verifyOtpShipmentCustomer()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import VerifyOtp
        schema = VerifyOtp()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["verifyOtpShipmentCustomer"], proccessed_params="""{"required":[{"in":"path","name":"order_id","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string","default":"FYMP6294545C010B89FD"}},{"in":"path","name":"shipment_id","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string","default":"16538880933361957252J"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"order_id","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string","default":"FYMP6294545C010B89FD"}},{"in":"path","name":"shipment_id","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string","default":"16538880933361957252J"}}]}""", order_id=order_id, shipment_id=shipment_id)
        query_string = await create_query_string(order_id=order_id, shipment_id=shipment_id)

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["verifyOtpShipmentCustomer"]).netloc, "post", await create_url_without_domain("/service/application/order/v1.0/orders/{order_id}/shipments/{shipment_id}/otp/verify/", order_id=order_id, shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import VerifyOtpResponse
            schema = VerifyOtpResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for verifyOtpShipmentCustomer")
                print(e)

        return response
    
    async def getShipmentBagReasons(self, shipment_id=None, bag_id=None, body="", request_headers:Dict={}):
        """Retrieves reasons that led to the cancellation for the status of shipment bags.
        :param shipment_id : ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        :param bag_id : ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id
        if bag_id is not None:
            payload["bag_id"] = bag_id

        # Parameter validation
        schema = OrderValidator.getShipmentBagReasons()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getShipmentBagReasons"], proccessed_params="""{"required":[{"in":"path","description":"ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"shipment_id","required":true,"schema":{"type":"string"}},{"in":"path","description":"ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"bag_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","description":"ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"shipment_id","required":true,"schema":{"type":"string"}},{"in":"path","description":"ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"bag_id","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id, bag_id=bag_id)
        query_string = await create_query_string(shipment_id=shipment_id, bag_id=bag_id)

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getShipmentBagReasons"]).netloc, "get", await create_url_without_domain("/service/application/order/v1.0/orders/shipments/{shipment_id}/bags/{bag_id}/reasons", shipment_id=shipment_id, bag_id=bag_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import ShipmentBagReasons
            schema = ShipmentBagReasons()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getShipmentBagReasons")
                print(e)

        return response
    
    async def getShipmentReasons(self, shipment_id=None, body="", request_headers:Dict={}):
        """Retrieve reasons explaining various shipment statuses.
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id

        # Parameter validation
        schema = OrderValidator.getShipmentReasons()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getShipmentReasons"], proccessed_params="""{"required":[{"in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"shipment_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"shipment_id","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id)
        query_string = await create_query_string(shipment_id=shipment_id)

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getShipmentReasons"]).netloc, "get", await create_url_without_domain("/service/application/order/v1.0/orders/shipments/{shipment_id}/reasons", shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import ShipmentReasons
            schema = ShipmentReasons()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getShipmentReasons")
                print(e)

        return response
    
    async def updateShipmentStatus(self, shipment_id=None, body="", request_headers:Dict={}):
        """Modifies the current status of a specific shipment using its shipment ID.
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if shipment_id is not None:
            payload["shipment_id"] = shipment_id

        # Parameter validation
        schema = OrderValidator.updateShipmentStatus()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateShipmentStatusRequest
        schema = UpdateShipmentStatusRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["updateShipmentStatus"], proccessed_params="""{"required":[{"in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"shipment_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"shipment_id","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id)
        query_string = await create_query_string(shipment_id=shipment_id)

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["updateShipmentStatus"]).netloc, "put", await create_url_without_domain("/service/application/order/v1.0/orders/shipments/{shipment_id}/status", shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import ShipmentApplicationStatusResponse
            schema = ShipmentApplicationStatusResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateShipmentStatus")
                print(e)

        return response
    