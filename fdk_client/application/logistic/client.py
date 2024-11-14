"""Logistic Application Client"""

import base64
import ujson
from urllib.parse import urlparse
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..ApplicationConfig import ApplicationConfig

from .validator import LogisticValidator

class Logistic:
    def __init__(self, config: ApplicationConfig):
        self._conf = config
        self._relativeUrls = {
            "getPincodeCity": "/service/application/logistics/v1.0/pincode/{pincode}",
            "getTatProduct": "/service/application/logistics/v1.0/",
            "getAllCountries": "/service/application/logistics/v1.0/country-list",
            "getPincodeZones": "/service/application/logistics/v1.0/pincode/zones",
            "getOptimalLocations": "/service/application/logistics/v1.0/reassign_stores",
            "getCourierPartners": "/service/application/logistics/v1.0/company/{company_id}/application/{application_id}/shipment/courier-partners",
            "getLocations": "/service/application/logistics/v1.0/locations",
            "getCountries": "/service/application/logistics/v2.0/countries",
            "getCountry": "/service/application/logistics/v1.0/countries/{country_iso_code}",
            "getDeliveryPromise": "/service/application/logistics/v1.0/delivery-promise",
            "getLocalities": "/service/application/logistics/v1.0/localities/{locality_type}",
            "getLocality": "/service/application/logistics/v1.0/localities/{locality_type}/{locality_value}",
            "validateAddress": "/service/application/logistics/v1.0/country/{country_iso_code}/address/templates/{template_name}/validate"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getPincodeCity(self, pincode=None, body="", request_headers:Dict={}):
        """Get details of a specific pincode, such as obtaining its city and state information.
        :param pincode : Postal code or PIN code of the address area. : type string
        """
        payload = {}
        
        if pincode is not None:
            payload["pincode"] = pincode

        # Parameter validation
        schema = LogisticValidator.getPincodeCity()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPincodeCity"], proccessed_params="""{"required":[{"in":"path","name":"pincode","description":"Postal code or PIN code of the address area.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"pincode","description":"Postal code or PIN code of the address area.","schema":{"type":"string"},"required":true}]}""", serverType="application", pincode=pincode)
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPincodeCity"]).netloc, "get", await create_url_without_domain("/service/application/logistics/v1.0/pincode/{pincode}", pincode=pincode), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PincodeDetails
            schema = PincodeDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPincodeCity")
                print(e)

        return response
    
    async def getTatProduct(self, body="", request_headers:Dict={}):
        """Get the estimated delivery time frame for a specific product from a designated store.
        """
        payload = {}
        

        # Parameter validation
        schema = LogisticValidator.getTatProduct()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import TATViewDetails
        schema = TATViewDetails()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["getTatProduct"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getTatProduct"]).netloc, "post", await create_url_without_domain("/service/application/logistics/v1.0/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TATViewResult
            schema = TATViewResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getTatProduct")
                print(e)

        return response
    
    async def getAllCountries(self, body="", request_headers:Dict={}):
        """Get a list of countries within the specified delivery zones for that application.
        """
        payload = {}
        

        # Parameter validation
        schema = LogisticValidator.getAllCountries()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAllCountries"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getAllCountries"]).netloc, "get", await create_url_without_domain("/service/application/logistics/v1.0/country-list", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CountryListResult
            schema = CountryListResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAllCountries")
                print(e)

        return response
    
    async def getPincodeZones(self, body="", request_headers:Dict={}):
        """Get the delivery zone associated with a given pincode.
        """
        payload = {}
        

        # Parameter validation
        schema = LogisticValidator.getPincodeZones()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GetZoneFromPincodeViewDetails
        schema = GetZoneFromPincodeViewDetails()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["getPincodeZones"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPincodeZones"]).netloc, "post", await create_url_without_domain("/service/application/logistics/v1.0/pincode/zones", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetZoneFromPincodeViewResult
            schema = GetZoneFromPincodeViewResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPincodeZones")
                print(e)

        return response
    
    async def getOptimalLocations(self, body="", request_headers:Dict={}):
        """Get optimal fulfillment centre for customers by analyzing their location, product availability, and inventory levels.
        """
        payload = {}
        

        # Parameter validation
        schema = LogisticValidator.getOptimalLocations()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ReAssignStoreDetails
        schema = ReAssignStoreDetails()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["getOptimalLocations"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getOptimalLocations"]).netloc, "post", await create_url_without_domain("/service/application/logistics/v1.0/reassign_stores", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ReAssignStoreResult
            schema = ReAssignStoreResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOptimalLocations")
                print(e)

        return response
    
    async def getCourierPartners(self, company_id=None, application_id=None, body="", request_headers:Dict={}):
        """Get all the serviceable courier partners of a destination and the shipments.
        :param company_id : Unique identifier of the company. : type integer
        :param application_id : Unique identifier of the sales channel. : type string
        """
        payload = {}
        
        if company_id is not None:
            payload["company_id"] = company_id
        if application_id is not None:
            payload["application_id"] = application_id

        # Parameter validation
        schema = LogisticValidator.getCourierPartners()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ShipmentCourierPartnerDetails
        schema = ShipmentCourierPartnerDetails()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["getCourierPartners"], proccessed_params="""{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique identifier of the sales channel.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"Unique identifier of the sales channel.","schema":{"type":"string"},"required":true}]}""", serverType="application", company_id=company_id, application_id=application_id)
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCourierPartners"]).netloc, "post", await create_url_without_domain("/service/application/logistics/v1.0/company/{company_id}/application/{application_id}/shipment/courier-partners", company_id=company_id, application_id=application_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ShipmentCourierPartnerResult
            schema = ShipmentCourierPartnerResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCourierPartners")
                print(e)

        return response
    
    async def getLocations(self, x_application_id=None, x_application_data=None, country=None, state=None, city=None, pincode=None, sector=None, page_no=None, page_size=None, body="", request_headers:Dict={}):
        """Get stores available for the application based on Delivery Zones and Order Orchestration rules.
        :param x-application-id : Unique identifier for a particular sales channel. : type string
        :param x-application-data : Sales channel details. : type string
        :param country : The country `iso2` code. : type string
        :param state : State or the province. : type string
        :param city : City. : type string
        :param pincode : Pincode of the area. : type integer
        :param sector : Specific sector of the city. : type string
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 12. : type integer
        """
        payload = {}
        
        if x_application_id is not None:
            payload["x_application_id"] = x_application_id
        if x_application_data is not None:
            payload["x_application_data"] = x_application_data
        if country is not None:
            payload["country"] = country
        if state is not None:
            payload["state"] = state
        if city is not None:
            payload["city"] = city
        if pincode is not None:
            payload["pincode"] = pincode
        if sector is not None:
            payload["sector"] = sector
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = LogisticValidator.getLocations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLocations"], proccessed_params="""{"required":[{"in":"query","name":"x-application-id","description":"Unique identifier for a particular sales channel.","schema":{"type":"string"},"required":true},{"in":"query","name":"x-application-data","description":"Sales channel details.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"country","description":"The country `iso2` code.","schema":{"type":"string"},"required":false},{"in":"query","name":"state","description":"State or the province.","schema":{"type":"string"},"required":false},{"in":"query","name":"city","description":"City.","schema":{"type":"string"},"required":false},{"in":"query","name":"pincode","description":"Pincode of the area.","schema":{"type":"integer"},"required":false},{"in":"query","name":"sector","description":"Specific sector of the city.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results. Default value is 1.","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page. Default value is 12.","schema":{"type":"integer"},"required":false}],"query":[{"in":"query","name":"x-application-id","description":"Unique identifier for a particular sales channel.","schema":{"type":"string"},"required":true},{"in":"query","name":"x-application-data","description":"Sales channel details.","schema":{"type":"string"},"required":true},{"in":"query","name":"country","description":"The country `iso2` code.","schema":{"type":"string"},"required":false},{"in":"query","name":"state","description":"State or the province.","schema":{"type":"string"},"required":false},{"in":"query","name":"city","description":"City.","schema":{"type":"string"},"required":false},{"in":"query","name":"pincode","description":"Pincode of the area.","schema":{"type":"integer"},"required":false},{"in":"query","name":"sector","description":"Specific sector of the city.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results. Default value is 1.","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page. Default value is 12.","schema":{"type":"integer"},"required":false}],"headers":[],"path":[]}""", serverType="application", x_application_id=x_application_id, x_application_data=x_application_data, country=country, state=state, city=city, pincode=pincode, sector=sector, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(x_application_id=x_application_id, x_application_data=x_application_data, country=country, state=state, city=city, pincode=pincode, sector=sector, page_no=page_no, page_size=page_size)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getLocations"]).netloc, "get", await create_url_without_domain("/service/application/logistics/v1.0/locations", x_application_id=x_application_id, x_application_data=x_application_data, country=country, state=state, city=city, pincode=pincode, sector=sector, page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetStoreResult
            schema = GetStoreResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getLocations")
                print(e)

        return response
    
    async def getCountries(self, onboarding=None, page_no=None, page_size=None, q=None, hierarchy=None, body="", request_headers:Dict={}):
        """List of supported countries.
        :param onboarding : List countries which allowed for onboard on Platform. : type boolean
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 12. : type integer
        :param q : Search countries by pincode, city, country name etc : type string
        :param hierarchy : Fetch countries that has certain heirarchy present. : type string
        """
        payload = {}
        
        if onboarding is not None:
            payload["onboarding"] = onboarding
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if q is not None:
            payload["q"] = q
        if hierarchy is not None:
            payload["hierarchy"] = hierarchy

        # Parameter validation
        schema = LogisticValidator.getCountries()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCountries"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"onboarding","description":"List countries which allowed for onboard on Platform.","schema":{"type":"boolean"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results. Default value is 1.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page. Default value is 12.","schema":{"type":"integer","default":12,"maximum":250},"required":false},{"in":"query","name":"q","description":"Search countries by pincode, city, country name etc","schema":{"type":"string"},"required":false},{"in":"query","name":"hierarchy","description":"Fetch countries that has certain heirarchy present.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"onboarding","description":"List countries which allowed for onboard on Platform.","schema":{"type":"boolean"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results. Default value is 1.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page. Default value is 12.","schema":{"type":"integer","default":12,"maximum":250},"required":false},{"in":"query","name":"q","description":"Search countries by pincode, city, country name etc","schema":{"type":"string"},"required":false},{"in":"query","name":"hierarchy","description":"Fetch countries that has certain heirarchy present.","schema":{"type":"string"},"required":false}],"headers":[],"path":[]}""", serverType="application", onboarding=onboarding, page_no=page_no, page_size=page_size, q=q, hierarchy=hierarchy)
        query_string = await create_query_string(onboarding=onboarding, page_no=page_no, page_size=page_size, q=q, hierarchy=hierarchy)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCountries"]).netloc, "get", await create_url_without_domain("/service/application/logistics/v2.0/countries", onboarding=onboarding, page_no=page_no, page_size=page_size, q=q, hierarchy=hierarchy), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetCountries
            schema = GetCountries()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCountries")
                print(e)

        return response
    
    async def getCountry(self, country_iso_code=None, body="", request_headers:Dict={}):
        """Get details about a particular country and its address format customized for different business scenarios.
        :param country_iso_code : The ISO 3166-1 alpha-2 code representing the country (e.g., "IN" for India, "US" for the United States). : type string
        """
        payload = {}
        
        if country_iso_code is not None:
            payload["country_iso_code"] = country_iso_code

        # Parameter validation
        schema = LogisticValidator.getCountry()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCountry"], proccessed_params="""{"required":[{"in":"path","name":"country_iso_code","description":"The ISO 3166-1 alpha-2 code representing the country (e.g., \"IN\" for India, \"US\" for the United States).","schema":{"type":"string","x-not-enum":true},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"country_iso_code","description":"The ISO 3166-1 alpha-2 code representing the country (e.g., \"IN\" for India, \"US\" for the United States).","schema":{"type":"string","x-not-enum":true},"required":true}]}""", serverType="application", country_iso_code=country_iso_code)
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCountry"]).netloc, "get", await create_url_without_domain("/service/application/logistics/v1.0/countries/{country_iso_code}", country_iso_code=country_iso_code), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetCountry
            schema = GetCountry()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCountry")
                print(e)

        return response
    
    async def getDeliveryPromise(self, page_no=None, page_size=None, body="", request_headers:Dict={}):
        """Get delivery promises for both global and store levels based on a specific locality type.
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 12. : type integer
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = LogisticValidator.getDeliveryPromise()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getDeliveryPromise"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results. Default value is 1.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page. Default value is 12.","schema":{"type":"integer","default":12},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results. Default value is 1.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page. Default value is 12.","schema":{"type":"integer","default":12},"required":false}],"headers":[],"path":[]}""", serverType="application", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getDeliveryPromise"]).netloc, "get", await create_url_without_domain("/service/application/logistics/v1.0/delivery-promise", page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetPromiseDetails
            schema = GetPromiseDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDeliveryPromise")
                print(e)

        return response
    
    async def getLocalities(self, locality_type=None, country=None, state=None, city=None, page_no=None, page_size=None, q=None, body="", request_headers:Dict={}):
        """Get geographical data for a specific type of locality based on the provided filters. For instance, obtain a list of cities for a given country and state.
        :param locality_type : Unique geographical division. : type string
        :param country : Country name. : type string
        :param state : State or the province. : type string
        :param city : City. : type string
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 12. : type integer
        :param q : This parameter is used to filter or search the records. : type string
        """
        payload = {}
        
        if locality_type is not None:
            payload["locality_type"] = locality_type
        if country is not None:
            payload["country"] = country
        if state is not None:
            payload["state"] = state
        if city is not None:
            payload["city"] = city
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if q is not None:
            payload["q"] = q

        # Parameter validation
        schema = LogisticValidator.getLocalities()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLocalities"], proccessed_params="""{"required":[{"in":"path","name":"locality_type","description":"Unique geographical division.","schema":{"type":"string","enum":["state","city","pincode","sector"]},"required":true}],"optional":[{"in":"query","name":"country","description":"Country name.","schema":{"type":"string"},"required":false},{"in":"query","name":"state","description":"State or the province.","schema":{"type":"string"},"required":false},{"in":"query","name":"city","description":"City.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results. Default value is 1.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page. Default value is 12.","schema":{"type":"integer","default":12,"maximum":1000},"required":false},{"in":"query","name":"q","description":"This parameter is used to filter or search the records.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"country","description":"Country name.","schema":{"type":"string"},"required":false},{"in":"query","name":"state","description":"State or the province.","schema":{"type":"string"},"required":false},{"in":"query","name":"city","description":"City.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results. Default value is 1.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page. Default value is 12.","schema":{"type":"integer","default":12,"maximum":1000},"required":false},{"in":"query","name":"q","description":"This parameter is used to filter or search the records.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"locality_type","description":"Unique geographical division.","schema":{"type":"string","enum":["state","city","pincode","sector"]},"required":true}]}""", serverType="application", locality_type=locality_type, country=country, state=state, city=city, page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(country=country, state=state, city=city, page_no=page_no, page_size=page_size, q=q)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getLocalities"]).netloc, "get", await create_url_without_domain("/service/application/logistics/v1.0/localities/{locality_type}", locality_type=locality_type, country=country, state=state, city=city, page_no=page_no, page_size=page_size, q=q), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetLocalities
            schema = GetLocalities()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getLocalities")
                print(e)

        return response
    
    async def getLocality(self, locality_type=None, locality_value=None, country=None, state=None, city=None, body="", request_headers:Dict={}):
        """Get detailed geographical data for a specific locality, such as a pincode. For example, for a pincode value of 400603, the service returns its parent locations, including city, state, and country details.
        :param locality_type : Geographical division. : type string
        :param locality_value : Name of the locality. : type string
        :param country : Country name. : type string
        :param state : State or the province. : type string
        :param city : City. : type string
        """
        payload = {}
        
        if locality_type is not None:
            payload["locality_type"] = locality_type
        if locality_value is not None:
            payload["locality_value"] = locality_value
        if country is not None:
            payload["country"] = country
        if state is not None:
            payload["state"] = state
        if city is not None:
            payload["city"] = city

        # Parameter validation
        schema = LogisticValidator.getLocality()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLocality"], proccessed_params="""{"required":[{"in":"path","name":"locality_type","description":"Geographical division.","schema":{"type":"string","enum":["pincode","sector"]},"required":true},{"in":"path","name":"locality_value","description":"Name of the locality.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"country","description":"Country name.","schema":{"type":"string"},"required":false},{"in":"query","name":"state","description":"State or the province.","schema":{"type":"string"},"required":false},{"in":"query","name":"city","description":"City.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"country","description":"Country name.","schema":{"type":"string"},"required":false},{"in":"query","name":"state","description":"State or the province.","schema":{"type":"string"},"required":false},{"in":"query","name":"city","description":"City.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"locality_type","description":"Geographical division.","schema":{"type":"string","enum":["pincode","sector"]},"required":true},{"in":"path","name":"locality_value","description":"Name of the locality.","schema":{"type":"string"},"required":true}]}""", serverType="application", locality_type=locality_type, locality_value=locality_value, country=country, state=state, city=city)
        query_string = await create_query_string(country=country, state=state, city=city)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getLocality"]).netloc, "get", await create_url_without_domain("/service/application/logistics/v1.0/localities/{locality_type}/{locality_value}", locality_type=locality_type, locality_value=locality_value, country=country, state=state, city=city), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetLocality
            schema = GetLocality()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getLocality")
                print(e)

        return response
    
    async def validateAddress(self, country_iso_code=None, template_name=None, body="", request_headers:Dict={}):
        """Validate addresses using specific templates customized for each country and tailored to various business scenarios. This validation ensures that the data conforms to the information currently stored in the system.
        :param country_iso_code : The ISO 3166-1 alpha-2 code representing the country (e.g., "IN" for India, "US" for the United States). : type string
        :param template_name : The type of address form. : type string
        """
        payload = {}
        
        if country_iso_code is not None:
            payload["country_iso_code"] = country_iso_code
        if template_name is not None:
            payload["template_name"] = template_name

        # Parameter validation
        schema = LogisticValidator.validateAddress()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ValidateAddressDetails
        schema = ValidateAddressDetails()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["validateAddress"], proccessed_params="""{"required":[{"in":"path","name":"country_iso_code","description":"The ISO 3166-1 alpha-2 code representing the country (e.g., \"IN\" for India, \"US\" for the United States).","schema":{"type":"string","x-not-enum":true},"required":true},{"in":"path","name":"template_name","description":"The type of address form.","schema":{"type":"string","enum":["checkout_form","store_os_form","default_display"]},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"country_iso_code","description":"The ISO 3166-1 alpha-2 code representing the country (e.g., \"IN\" for India, \"US\" for the United States).","schema":{"type":"string","x-not-enum":true},"required":true},{"in":"path","name":"template_name","description":"The type of address form.","schema":{"type":"string","enum":["checkout_form","store_os_form","default_display"]},"required":true}]}""", serverType="application", country_iso_code=country_iso_code, template_name=template_name)
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["validateAddress"]).netloc, "post", await create_url_without_domain("/service/application/logistics/v1.0/country/{country_iso_code}/address/templates/{template_name}/validate", country_iso_code=country_iso_code, template_name=template_name), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ValidateAddressDetails
            schema = ValidateAddressDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for validateAddress")
                print(e)

        return response
    