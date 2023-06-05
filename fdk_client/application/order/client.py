

"""Order Application Client"""

import base64
import ujson
from urllib.parse import urlparse

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import OrderValidator

class Order:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "getOrders": "/service/application/orders/v1.0/orders",
            "getOrderById": "/service/application/orders/v1.0/orders/{order_id}",
            "getPosOrderById": "/service/application/orders/v1.0/orders/pos-order/{order_id}",
            "getShipmentById": "/service/application/orders/v1.0/orders/shipments/{shipment_id}",
            "getInvoiceByShipmentId": "/service/application/orders/v1.0/orders/shipments/{shipment_id}/invoice",
            "trackShipment": "/service/application/orders/v1.0/orders/shipments/{shipment_id}/track",
            "getCustomerDetailsByShipmentId": "/service/application/orders/v1.0/orders/{order_id}/shipments/{shipment_id}/customer-details",
            "sendOtpToShipmentCustomer": "/service/application/orders/v1.0/orders/{order_id}/shipments/{shipment_id}/otp/send/",
            "verifyOtpShipmentCustomer": "/service/application/orders/v1.0/orders/{order_id}/shipments/{shipment_id}/otp/verify/",
            "getShipmentBagReasons": "/service/application/orders/v1.0/orders/shipments/{shipment_id}/bags/{bag_id}/reasons",
            "getShipmentReasons": "/service/application/orders/v1.0/orders/shipments/{shipment_id}/reasons",
            "updateShipmentStatus": "/service/application/order-manage/v1.0/orders/shipments/{shipment_id}/status"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getOrders(self, status=None, page_no=None, page_size=None, from_date=None, to_date=None, custom_meta=None, body=""):
        """Use this API to retrieve all the orders.
        :param status : A filter to retrieve orders by their current status such as _placed_, _delivered_, etc. : type integer
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        :param from_date : The date from which the orders should be retrieved. : type string
        :param to_date : The date till which the orders should be retrieved. : type string
        :param custom_meta : A filter and retrieve data using special fields included for special use-cases : type string
        """
        payload = {}
        
        if status:
            payload["status"] = status
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if from_date:
            payload["from_date"] = from_date
        
        if to_date:
            payload["to_date"] = to_date
        
        if custom_meta:
            payload["custom_meta"] = custom_meta
        
        # Parameter validation
        schema = OrderValidator.getOrders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOrders"], proccessed_params="""{"required":[],"optional":[{"in":"query","description":"A filter to retrieve orders by their current status such as _placed_, _delivered_, etc.","name":"status","required":false,"schema":{"type":"integer"}},{"in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","description":"The number of items to retrieve in each page. Default value is 10.","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","description":"The date from which the orders should be retrieved.","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","description":"The date till which the orders should be retrieved.","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","description":"A filter and retrieve data using special fields included for special use-cases","name":"custom_meta","required":false,"schema":{"type":"string","default":{"store_id":"6388422a5ebd6a6cf4a8ede6"}}}],"query":[{"in":"query","description":"A filter to retrieve orders by their current status such as _placed_, _delivered_, etc.","name":"status","required":false,"schema":{"type":"integer"}},{"in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","description":"The number of items to retrieve in each page. Default value is 10.","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","description":"The date from which the orders should be retrieved.","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","description":"The date till which the orders should be retrieved.","name":"to_date","required":false,"schema":{"type":"string"}},{"in":"query","description":"A filter and retrieve data using special fields included for special use-cases","name":"custom_meta","required":false,"schema":{"type":"string","default":{"store_id":"6388422a5ebd6a6cf4a8ede6"}}}],"headers":[],"path":[]}""", status=status, page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, custom_meta=custom_meta)
        query_string = await create_query_string(status=status, page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, custom_meta=custom_meta)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getOrders"]).netloc, "get", await create_url_without_domain("/service/application/orders/v1.0/orders", status=status, page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, custom_meta=custom_meta), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        

        from .models import OrderList
        schema = OrderList()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getOrders")
            print(e)

        

        return response
    
    async def getOrderById(self, order_id=None, body=""):
        """Use this API to retrieve order details such as tracking details, shipment, store information using Fynd Order ID.
        :param order_id : A unique number used for identifying and tracking your orders. : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        
        # Parameter validation
        schema = OrderValidator.getOrderById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOrderById"], proccessed_params="""{"required":[{"in":"path","name":"order_id","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"order_id","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}}]}""", order_id=order_id)
        query_string = await create_query_string(order_id=order_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getOrderById"]).netloc, "get", await create_url_without_domain("/service/application/orders/v1.0/orders/{order_id}", order_id=order_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        

        from .models import OrderById
        schema = OrderById()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getOrderById")
            print(e)

        

        return response
    
    async def getPosOrderById(self, order_id=None, body=""):
        """Use this API to retrieve a POS order and all its details such as tracking details, shipment, store information using Fynd Order ID.
        :param order_id : A unique number used for identifying and tracking your orders. : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        
        # Parameter validation
        schema = OrderValidator.getPosOrderById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPosOrderById"], proccessed_params="""{"required":[{"in":"path","name":"order_id","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"order_id","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}}]}""", order_id=order_id)
        query_string = await create_query_string(order_id=order_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPosOrderById"]).netloc, "get", await create_url_without_domain("/service/application/orders/v1.0/orders/pos-order/{order_id}", order_id=order_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        

        from .models import OrderList
        schema = OrderList()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getPosOrderById")
            print(e)

        

        return response
    
    async def getShipmentById(self, shipment_id=None, body=""):
        """Use this API to retrieve shipment details such as price breakup, tracking details, store information, etc. using Shipment ID.
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        # Parameter validation
        schema = OrderValidator.getShipmentById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getShipmentById"], proccessed_params="""{"required":[{"in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"shipment_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"shipment_id","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id)
        query_string = await create_query_string(shipment_id=shipment_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getShipmentById"]).netloc, "get", await create_url_without_domain("/service/application/orders/v1.0/orders/shipments/{shipment_id}", shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        

        from .models import ShipmentById
        schema = ShipmentById()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getShipmentById")
            print(e)

        

        return response
    
    async def getInvoiceByShipmentId(self, shipment_id=None, body=""):
        """Use this API to retrieve shipment invoice.
        :param shipment_id : ID of the shipment. : type string
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        # Parameter validation
        schema = OrderValidator.getInvoiceByShipmentId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getInvoiceByShipmentId"], proccessed_params="""{"required":[{"in":"path","description":"ID of the shipment.","name":"shipment_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","description":"ID of the shipment.","name":"shipment_id","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id)
        query_string = await create_query_string(shipment_id=shipment_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getInvoiceByShipmentId"]).netloc, "get", await create_url_without_domain("/service/application/orders/v1.0/orders/shipments/{shipment_id}/invoice", shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        

        from .models import ResponseGetInvoiceShipment
        schema = ResponseGetInvoiceShipment()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getInvoiceByShipmentId")
            print(e)

        

        return response
    
    async def trackShipment(self, shipment_id=None, body=""):
        """Track Shipment by shipment id, for application based on application Id
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        # Parameter validation
        schema = OrderValidator.trackShipment()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["trackShipment"], proccessed_params="""{"required":[{"in":"path","name":"shipment_id","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string","default":"16544950215681060915J"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"shipment_id","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string","default":"16544950215681060915J"}}]}""", shipment_id=shipment_id)
        query_string = await create_query_string(shipment_id=shipment_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["trackShipment"]).netloc, "get", await create_url_without_domain("/service/application/orders/v1.0/orders/shipments/{shipment_id}/track", shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        

        from .models import ShipmentTrack
        schema = ShipmentTrack()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for trackShipment")
            print(e)

        

        return response
    
    async def getCustomerDetailsByShipmentId(self, order_id=None, shipment_id=None, body=""):
        """Use this API to retrieve customer details such as mobileno using Shipment ID.
        :param order_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        :param shipment_id : A unique number used for identifying and tracking your orders. : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        # Parameter validation
        schema = OrderValidator.getCustomerDetailsByShipmentId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCustomerDetailsByShipmentId"], proccessed_params="""{"required":[{"in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"order_id","required":true,"schema":{"type":"string","default":"16544950215681060915J"}},{"in":"path","description":"A unique number used for identifying and tracking your orders.","name":"shipment_id","required":true,"schema":{"type":"string","default":"FY6299E19701B4EAEFC2"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"order_id","required":true,"schema":{"type":"string","default":"16544950215681060915J"}},{"in":"path","description":"A unique number used for identifying and tracking your orders.","name":"shipment_id","required":true,"schema":{"type":"string","default":"FY6299E19701B4EAEFC2"}}]}""", order_id=order_id, shipment_id=shipment_id)
        query_string = await create_query_string(order_id=order_id, shipment_id=shipment_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCustomerDetailsByShipmentId"]).netloc, "get", await create_url_without_domain("/service/application/orders/v1.0/orders/{order_id}/shipments/{shipment_id}/customer-details", order_id=order_id, shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        

        from .models import CustomerDetailsResponse
        schema = CustomerDetailsResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getCustomerDetailsByShipmentId")
            print(e)

        

        return response
    
    async def sendOtpToShipmentCustomer(self, order_id=None, shipment_id=None, body=""):
        """Use this API to send OTP to the customer of the mapped Shipment.
        :param order_id : A unique number used for identifying and tracking your orders. : type string
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        # Parameter validation
        schema = OrderValidator.sendOtpToShipmentCustomer()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["sendOtpToShipmentCustomer"], proccessed_params="""{"required":[{"in":"path","name":"order_id","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string","default":"FY6299E19701B4EAEFC2"}},{"in":"path","name":"shipment_id","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string","default":"16544950215681060915J"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"order_id","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string","default":"FY6299E19701B4EAEFC2"}},{"in":"path","name":"shipment_id","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string","default":"16544950215681060915J"}}]}""", order_id=order_id, shipment_id=shipment_id)
        query_string = await create_query_string(order_id=order_id, shipment_id=shipment_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["sendOtpToShipmentCustomer"]).netloc, "post", await create_url_without_domain("/service/application/orders/v1.0/orders/{order_id}/shipments/{shipment_id}/otp/send/", order_id=order_id, shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        

        from .models import SendOtpToCustomerResponse
        schema = SendOtpToCustomerResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for sendOtpToShipmentCustomer")
            print(e)

        

        return response
    
    async def verifyOtpShipmentCustomer(self, order_id=None, shipment_id=None, body=""):
        """Use this API to verify OTP and create a session token with custom payload.
        :param order_id : A unique number used for identifying and tracking your orders. : type string
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        
        if shipment_id:
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
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["verifyOtpShipmentCustomer"]).netloc, "post", await create_url_without_domain("/service/application/orders/v1.0/orders/{order_id}/shipments/{shipment_id}/otp/verify/", order_id=order_id, shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        

        from .models import VerifyOtpResponse
        schema = VerifyOtpResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for verifyOtpShipmentCustomer")
            print(e)

        

        return response
    
    async def getShipmentBagReasons(self, shipment_id=None, bag_id=None, body=""):
        """Use this API to retrieve the issues that led to the cancellation of bags within a shipment.
        :param shipment_id : ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        :param bag_id : ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        if bag_id:
            payload["bag_id"] = bag_id
        
        # Parameter validation
        schema = OrderValidator.getShipmentBagReasons()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getShipmentBagReasons"], proccessed_params="""{"required":[{"in":"path","description":"ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"shipment_id","required":true,"schema":{"type":"string"}},{"in":"path","description":"ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"bag_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","description":"ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"shipment_id","required":true,"schema":{"type":"string"}},{"in":"path","description":"ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"bag_id","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id, bag_id=bag_id)
        query_string = await create_query_string(shipment_id=shipment_id, bag_id=bag_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getShipmentBagReasons"]).netloc, "get", await create_url_without_domain("/service/application/orders/v1.0/orders/shipments/{shipment_id}/bags/{bag_id}/reasons", shipment_id=shipment_id, bag_id=bag_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        

        from .models import ShipmentBagReasons
        schema = ShipmentBagReasons()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getShipmentBagReasons")
            print(e)

        

        return response
    
    async def getShipmentReasons(self, shipment_id=None, body=""):
        """Use this API to retrieve the issues that led to the cancellation of bags within a shipment.
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        # Parameter validation
        schema = OrderValidator.getShipmentReasons()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getShipmentReasons"], proccessed_params="""{"required":[{"in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"shipment_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"shipment_id","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id)
        query_string = await create_query_string(shipment_id=shipment_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getShipmentReasons"]).netloc, "get", await create_url_without_domain("/service/application/orders/v1.0/orders/shipments/{shipment_id}/reasons", shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        

        from .models import ShipmentReasons
        schema = ShipmentReasons()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getShipmentReasons")
            print(e)

        

        return response
    
    async def updateShipmentStatus(self, shipment_id=None, body=""):
        """updateShipmentStatus
        :param shipment_id :  : type string
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        # Parameter validation
        schema = OrderValidator.updateShipmentStatus()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateShipmentStatusRequest
        schema = UpdateShipmentStatusRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateShipmentStatus"], proccessed_params="""{"required":[{"in":"path","name":"shipment_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"shipment_id","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id)
        query_string = await create_query_string(shipment_id=shipment_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["updateShipmentStatus"]).netloc, "put", await create_url_without_domain("/service/application/order-manage/v1.0/orders/shipments/{shipment_id}/status", shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        

        from .models import ShipmentApplicationStatusResponse
        schema = ShipmentApplicationStatusResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for updateShipmentStatus")
            print(e)

        

        return response
    

