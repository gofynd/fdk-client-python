

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
            "getOrders": "/service/application/order/v1.0/orders",
            "getOrderById": "/service/application/order/v1.0/orders/{order_id}",
            "getShipmentById": "/service/application/order/v1.0/orders/shipments/{shipment_id}",
            "getShipmentReasons": "/service/application/order/v1.0/orders/shipments/{shipment_id}/reasons",
            "getShipmentBagReasons": "/service/application/order/v1.0/orders/shipments/{shipment_id}/bags/{bag_id}/reasons/",
            "updateShipmentStatus": "/service/application/order/v1.0/orders/shipments/{shipment_id}/status",
            "trackShipment": "/service/application/order/v1.0/orders/shipments/{shipment_id}/track",
            "getPosOrderById": "/service/application/order/v1.0/orders/pos-order/{order_id}",
            "getCustomerDetailsByShipmentId": "/service/application/order/v1.0/orders/{order_id}/shipments/{shipment_id}/customer-details",
            "sendOtpToShipmentCustomer": "/service/application/order/v1.0/orders/{order_id}/shipments/{shipment_id}/otp/send/",
            "verifyOtpShipmentCustomer": "/service/application/order/v1.0/orders/{order_id}/shipments/{shipment_id}/otp/verify",
            "getInvoiceByShipmentId": "/service/application/order/v1.0/orders/shipments/{shipment_id}/invoice",
            "getOrders1": "/service/application/orders/v1.0/orders",
            "getOrderById1": "/service/application/orders/v1.0/orders/{order_id}",
            "getPosOrderById1": "/service/application/orders/v1.0/orders/pos-order/{order_id}",
            "getShipmentById1": "/service/application/orders/v1.0/orders/shipments/{shipment_id}",
            "trackShipment1": "/service/application/orders/v1.0/orders/shipments/{shipment_id}/track",
            "getCustomerDetailsByShipmentId1": "/service/application/orders/v1.0/orders/{order_id}/shipments/{shipment_id}/customer-details",
            "sendOtpToShipmentCustomer1": "/service/application/orders/v1.0/orders/{order_id}/shipments/{shipment_id}/otp/send/",
            "verifyOtpShipmentCustomer1": "/service/application/orders/v1.0/orders/{order_id}/shipments/{shipment_id}/otp/verify/",
            "getShipmentBagReasons1": "/service/application/orders/v1.0/orders/shipments/{shipment_id}/bags/{bag_id}/reasons"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getOrders(self, page_no=None, page_size=None, from_date=None, to_date=None, status=None, body=""):
        """Use this API to retrieve all the orders.
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        :param from_date : The date from which the orders should be retrieved. : type string
        :param to_date : The date till which the orders should be retrieved. : type string
        :param status : A filter to retrieve orders by their current status such as _placed_, _delivered_, etc. : type integer
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
        
        if status:
            payload["status"] = status
        
        # Parameter validation
        schema = OrderValidator.getOrders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOrders"], proccessed_params="""{"required":[],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer"}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer"}},{"name":"from_date","in":"query","description":"The date from which the orders should be retrieved.","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","description":"The date till which the orders should be retrieved.","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"A filter to retrieve orders by their current status such as _placed_, _delivered_, etc.","required":false,"schema":{"type":"integer"}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer"}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer"}},{"name":"from_date","in":"query","description":"The date from which the orders should be retrieved.","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","description":"The date till which the orders should be retrieved.","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"A filter to retrieve orders by their current status such as _placed_, _delivered_, etc.","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[]}""", page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, status=status)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, status=status)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getOrders"]).netloc, "get", await create_url_without_domain("/service/application/order/v1.0/orders", page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, status=status), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
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
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOrderById"], proccessed_params="""{"required":[{"name":"order_id","in":"path","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"order_id","in":"path","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}}]}""", order_id=order_id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getOrderById"]).netloc, "get", await create_url_without_domain("/service/application/order/v1.0/orders/{order_id}", order_id=order_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
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
        

        url_with_params = await create_url_with_params(api_url=self._urls["getShipmentById"], proccessed_params="""{"required":[{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getShipmentById"]).netloc, "get", await create_url_without_domain("/service/application/order/v1.0/orders/shipments/{shipment_id}", shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
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
        

        url_with_params = await create_url_with_params(api_url=self._urls["getShipmentReasons"], proccessed_params="""{"required":[{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getShipmentReasons"]).netloc, "get", await create_url_without_domain("/service/application/order/v1.0/orders/shipments/{shipment_id}/reasons", shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getShipmentBagReasons(self, shipment_id=None, bag_id=None, body=""):
        """Use this API to retrieve the issues that led to the cancellation of bags within a shipment.
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        :param bag_id : ID of the bag. : type string
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        if bag_id:
            payload["bag_id"] = bag_id
        
        # Parameter validation
        schema = OrderValidator.getShipmentBagReasons()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getShipmentBagReasons"], proccessed_params="""{"required":[{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}},{"name":"bag_id","in":"path","description":"ID of the bag.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}},{"name":"bag_id","in":"path","description":"ID of the bag.","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id, bag_id=bag_id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getShipmentBagReasons"]).netloc, "get", await create_url_without_domain("/service/application/order/v1.0/orders/shipments/{shipment_id}/bags/{bag_id}/reasons/", shipment_id=shipment_id, bag_id=bag_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def updateShipmentStatus(self, shipment_id=None, body=""):
        """Use this API to update the status of a shipment using its shipment ID.
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        # Parameter validation
        schema = OrderValidator.updateShipmentStatus()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ShipmentStatusUpdateBody import ShipmentStatusUpdateBody
        schema = ShipmentStatusUpdateBody()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateShipmentStatus"], proccessed_params="""{"required":[{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id)
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
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["updateShipmentStatus"]).netloc, "put", await create_url_without_domain("/service/application/order/v1.0/orders/shipments/{shipment_id}/status", shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def trackShipment(self, shipment_id=None, body=""):
        """Use this API to track a shipment using its shipment ID.
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        # Parameter validation
        schema = OrderValidator.trackShipment()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["trackShipment"], proccessed_params="""{"required":[{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["trackShipment"]).netloc, "get", await create_url_without_domain("/service/application/order/v1.0/orders/shipments/{shipment_id}/track", shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
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
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPosOrderById"], proccessed_params="""{"required":[{"name":"order_id","in":"path","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"order_id","in":"path","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}}]}""", order_id=order_id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getPosOrderById"]).netloc, "get", await create_url_without_domain("/service/application/order/v1.0/orders/pos-order/{order_id}", order_id=order_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getCustomerDetailsByShipmentId(self, order_id=None, shipment_id=None, body=""):
        """Use this API to retrieve customer details such as mobileno using Shipment ID.
        :param order_id : A unique number used for identifying and tracking your orders. : type string
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        # Parameter validation
        schema = OrderValidator.getCustomerDetailsByShipmentId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCustomerDetailsByShipmentId"], proccessed_params="""{"required":[{"name":"order_id","in":"path","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"order_id","in":"path","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}]}""", order_id=order_id, shipment_id=shipment_id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getCustomerDetailsByShipmentId"]).netloc, "get", await create_url_without_domain("/service/application/order/v1.0/orders/{order_id}/shipments/{shipment_id}/customer-details", order_id=order_id, shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
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
        

        url_with_params = await create_url_with_params(api_url=self._urls["sendOtpToShipmentCustomer"], proccessed_params="""{"required":[{"name":"order_id","in":"path","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"order_id","in":"path","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}]}""", order_id=order_id, shipment_id=shipment_id)
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["sendOtpToShipmentCustomer"]).netloc, "post", await create_url_without_domain("/service/application/order/v1.0/orders/{order_id}/shipments/{shipment_id}/otp/send/", order_id=order_id, shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
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
        from .models.ReqBodyVerifyOTPShipment import ReqBodyVerifyOTPShipment
        schema = ReqBodyVerifyOTPShipment()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["verifyOtpShipmentCustomer"], proccessed_params="""{"required":[{"name":"order_id","in":"path","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"order_id","in":"path","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}]}""", order_id=order_id, shipment_id=shipment_id)
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["verifyOtpShipmentCustomer"]).netloc, "post", await create_url_without_domain("/service/application/order/v1.0/orders/{order_id}/shipments/{shipment_id}/otp/verify", order_id=order_id, shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getInvoiceByShipmentId(self, shipment_id=None, body=""):
        """Use this API to get a generated Invoice URL for viewing or download.
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        # Parameter validation
        schema = OrderValidator.getInvoiceByShipmentId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getInvoiceByShipmentId"], proccessed_params="""{"required":[{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getInvoiceByShipmentId"]).netloc, "get", await create_url_without_domain("/service/application/order/v1.0/orders/shipments/{shipment_id}/invoice", shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getOrders1(self, status=None, page_no=None, page_size=None, from_date=None, to_date=None, body=""):
        """Use this API to retrieve all the orders.
        :param status : A filter to retrieve orders by their current status such as _placed_, _delivered_, etc. : type integer
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        :param from_date : The date from which the orders should be retrieved. : type string
        :param to_date : The date till which the orders should be retrieved. : type string
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
        
        # Parameter validation
        schema = OrderValidator.getOrders1()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOrders1"], proccessed_params="""{"required":[],"optional":[{"in":"query","description":"A filter to retrieve orders by their current status such as _placed_, _delivered_, etc.","name":"status","required":false,"schema":{"type":"integer"}},{"in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","description":"The number of items to retrieve in each page. Default value is 10.","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","description":"The date from which the orders should be retrieved.","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","description":"The date till which the orders should be retrieved.","name":"to_date","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","description":"A filter to retrieve orders by their current status such as _placed_, _delivered_, etc.","name":"status","required":false,"schema":{"type":"integer"}},{"in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","name":"page_no","required":false,"schema":{"type":"integer"}},{"in":"query","description":"The number of items to retrieve in each page. Default value is 10.","name":"page_size","required":false,"schema":{"type":"integer"}},{"in":"query","description":"The date from which the orders should be retrieved.","name":"from_date","required":false,"schema":{"type":"string"}},{"in":"query","description":"The date till which the orders should be retrieved.","name":"to_date","required":false,"schema":{"type":"string"}}],"headers":[],"path":[]}""", status=status, page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date)
        query_string = await create_query_string(status=status, page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getOrders1"]).netloc, "get", await create_url_without_domain("/service/application/orders/v1.0/orders", status=status, page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getOrderById1(self, order_id=None, body=""):
        """Use this API to retrieve order details such as tracking details, shipment, store information using Fynd Order ID.
        :param order_id : A unique number used for identifying and tracking your orders. : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        
        # Parameter validation
        schema = OrderValidator.getOrderById1()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOrderById1"], proccessed_params="""{"required":[{"in":"path","name":"order_id","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"order_id","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}}]}""", order_id=order_id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getOrderById1"]).netloc, "get", await create_url_without_domain("/service/application/orders/v1.0/orders/{order_id}", order_id=order_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getPosOrderById1(self, order_id=None, body=""):
        """Use this API to retrieve a POS order and all its details such as tracking details, shipment, store information using Fynd Order ID.
        :param order_id : A unique number used for identifying and tracking your orders. : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        
        # Parameter validation
        schema = OrderValidator.getPosOrderById1()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPosOrderById1"], proccessed_params="""{"required":[{"in":"path","name":"order_id","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"order_id","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}}]}""", order_id=order_id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getPosOrderById1"]).netloc, "get", await create_url_without_domain("/service/application/orders/v1.0/orders/pos-order/{order_id}", order_id=order_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getShipmentById1(self, shipment_id=None, body=""):
        """Use this API to retrieve shipment details such as price breakup, tracking details, store information, etc. using Shipment ID.
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        # Parameter validation
        schema = OrderValidator.getShipmentById1()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getShipmentById1"], proccessed_params="""{"required":[{"in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"shipment_id","required":true,"schema":{"type":"string","default":"16602143565551542371K"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"shipment_id","required":true,"schema":{"type":"string","default":"16602143565551542371K"}}]}""", shipment_id=shipment_id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getShipmentById1"]).netloc, "get", await create_url_without_domain("/service/application/orders/v1.0/orders/shipments/{shipment_id}", shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def trackShipment1(self, shipment_id=None, body=""):
        """Track Shipment by shipment id, for application based on application Id
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        # Parameter validation
        schema = OrderValidator.trackShipment1()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["trackShipment1"], proccessed_params="""{"required":[{"in":"path","name":"shipment_id","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string","default":"16544950215681060915J"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"shipment_id","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string","default":"16544950215681060915J"}}]}""", shipment_id=shipment_id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["trackShipment1"]).netloc, "get", await create_url_without_domain("/service/application/orders/v1.0/orders/shipments/{shipment_id}/track", shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getCustomerDetailsByShipmentId1(self, order_id=None, shipment_id=None, body=""):
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
        schema = OrderValidator.getCustomerDetailsByShipmentId1()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCustomerDetailsByShipmentId1"], proccessed_params="""{"required":[{"in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"order_id","required":true,"schema":{"type":"string","default":"16544950215681060915J"}},{"in":"path","description":"A unique number used for identifying and tracking your orders.","name":"shipment_id","required":true,"schema":{"type":"string","default":"FY6299E19701B4EAEFC2"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"order_id","required":true,"schema":{"type":"string","default":"16544950215681060915J"}},{"in":"path","description":"A unique number used for identifying and tracking your orders.","name":"shipment_id","required":true,"schema":{"type":"string","default":"FY6299E19701B4EAEFC2"}}]}""", order_id=order_id, shipment_id=shipment_id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getCustomerDetailsByShipmentId1"]).netloc, "get", await create_url_without_domain("/service/application/orders/v1.0/orders/{order_id}/shipments/{shipment_id}/customer-details", order_id=order_id, shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def sendOtpToShipmentCustomer1(self, order_id=None, shipment_id=None, body=""):
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
        schema = OrderValidator.sendOtpToShipmentCustomer1()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["sendOtpToShipmentCustomer1"], proccessed_params="""{"required":[{"in":"path","name":"order_id","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string","default":"FY6299E19701B4EAEFC2"}},{"in":"path","name":"shipment_id","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string","default":"16544950215681060915J"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"order_id","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string","default":"FY6299E19701B4EAEFC2"}},{"in":"path","name":"shipment_id","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string","default":"16544950215681060915J"}}]}""", order_id=order_id, shipment_id=shipment_id)
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["sendOtpToShipmentCustomer1"]).netloc, "post", await create_url_without_domain("/service/application/orders/v1.0/orders/{order_id}/shipments/{shipment_id}/otp/send/", order_id=order_id, shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def verifyOtpShipmentCustomer1(self, order_id=None, shipment_id=None, body=""):
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
        schema = OrderValidator.verifyOtpShipmentCustomer1()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.VerifyOtp import VerifyOtp
        schema = VerifyOtp()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["verifyOtpShipmentCustomer1"], proccessed_params="""{"required":[{"in":"path","name":"order_id","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string","default":"FYMP6294545C010B89FD"}},{"in":"path","name":"shipment_id","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string","default":"16538880933361957252J"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"order_id","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string","default":"FYMP6294545C010B89FD"}},{"in":"path","name":"shipment_id","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string","default":"16538880933361957252J"}}]}""", order_id=order_id, shipment_id=shipment_id)
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["verifyOtpShipmentCustomer1"]).netloc, "post", await create_url_without_domain("/service/application/orders/v1.0/orders/{order_id}/shipments/{shipment_id}/otp/verify/", order_id=order_id, shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getShipmentBagReasons1(self, shipment_id=None, bag_id=None, body=""):
        """Use this API to retrieve the issues that led to the cancellation of bags within a shipment.
        :param shipment_id : ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        :param bag_id : ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type integer
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        if bag_id:
            payload["bag_id"] = bag_id
        
        # Parameter validation
        schema = OrderValidator.getShipmentBagReasons1()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getShipmentBagReasons1"], proccessed_params="""{"required":[{"in":"path","description":"ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"shipment_id","required":true,"schema":{"type":"string","default":"16538880933361957252J"}},{"in":"path","description":"ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"bag_id","required":true,"schema":{"type":"integer","default":109080}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","description":"ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"shipment_id","required":true,"schema":{"type":"string","default":"16538880933361957252J"}},{"in":"path","description":"ID of the bag. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","name":"bag_id","required":true,"schema":{"type":"integer","default":109080}}]}""", shipment_id=shipment_id, bag_id=bag_id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getShipmentBagReasons1"]).netloc, "get", await create_url_without_domain("/service/application/orders/v1.0/orders/shipments/{shipment_id}/bags/{bag_id}/reasons", shipment_id=shipment_id, bag_id=bag_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    

