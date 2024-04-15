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
            "getLocations": "/service/application/logistics/v1.0/locations",
            "getCountries": "/service/application/logistics/v1.0/countries",
            "getCountry": "/service/application/logistics/v1.0/countries/{country_iso_code}",
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
        """Retrieve the name of the city associated with a given pincode.
        :param pincode : A `pincode` contains a specific address of a location. : type string
        """
        payload = {}
        
        if pincode is not None:
            payload["pincode"] = pincode

        # Parameter validation
        schema = LogisticValidator.getPincodeCity()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPincodeCity"], proccessed_params="""{"required":[{"in":"path","name":"pincode","description":"A `pincode` contains a specific address of a location.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"pincode","description":"A `pincode` contains a specific address of a location.","schema":{"type":"string"},"required":true}]}""", serverType="application", pincode=pincode)
        query_string = await create_query_string(pincode=pincode)

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
            from .models import PincodeApiResponse
            schema = PincodeApiResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPincodeCity")
                print(e)

        return response
    
    async def getTatProduct(self, body="", request_headers:Dict={}):
        """Retrieve the estimated delivery time for a specific product.
        """
        payload = {}
        

        # Parameter validation
        schema = LogisticValidator.getTatProduct()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import TATViewRequest
        schema = TATViewRequest()
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
            from .models import TATViewResponse
            schema = TATViewResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getTatProduct")
                print(e)

        return response
    
    async def getAllCountries(self, body="", request_headers:Dict={}):
        """Retrieve a list of all countries supported by the system.
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
            from .models import CountryListResponse
            schema = CountryListResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAllCountries")
                print(e)

        return response
    
    async def getPincodeZones(self, body="", request_headers:Dict={}):
        """Retreive the logistical zones corresponding to a given pincode.
        """
        payload = {}
        

        # Parameter validation
        schema = LogisticValidator.getPincodeZones()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GetZoneFromPincodeViewRequest
        schema = GetZoneFromPincodeViewRequest()
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
            from .models import GetZoneFromPincodeViewResponse
            schema = GetZoneFromPincodeViewResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPincodeZones")
                print(e)

        return response
    
    async def getOptimalLocations(self, body="", request_headers:Dict={}):
        """Retrieve the most efficient locations for logistics purposes.
        """
        payload = {}
        

        # Parameter validation
        schema = LogisticValidator.getOptimalLocations()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ReAssignStoreRequest
        schema = ReAssignStoreRequest()
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
            from .models import ReAssignStoreResponse
            schema = ReAssignStoreResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOptimalLocations")
                print(e)

        return response
    
    async def getLocations(self, x_application_id=None, x_application_data=None, country=None, state=None, city=None, pincode=None, sector=None, page_no=None, page_size=None, body="", request_headers:Dict={}):
        """Retrieves a list of all locations of countries, states, cities. 
        :param x-application-id : A `x-application-id` is a unique identifier for a particular sale channel. : type string
        :param x-application-data : A `x-application-data` is a unique identifier for a particular sale channel. : type string
        :param country : A `country` contains a specific value of the country `iso2` code. : type string
        :param state : A `state` contains a specific value of the state, province. : type string
        :param city : A `city` contains a specific value of the city. : type string
        :param pincode : A `pincode` contains a specific value of the city. : type integer
        :param sector : A `sector` contains a specific value of the city. : type string
        :param page_no : page number. : type integer
        :param page_size : page size. : type integer
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
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLocations"], proccessed_params="""{"required":[{"in":"query","name":"x-application-id","description":"A `x-application-id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"query","name":"x-application-data","description":"A `x-application-data` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"country","description":"A `country` contains a specific value of the country `iso2` code.","schema":{"type":"string"},"required":false},{"in":"query","name":"state","description":"A `state` contains a specific value of the state, province.","schema":{"type":"string"},"required":false},{"in":"query","name":"city","description":"A `city` contains a specific value of the city.","schema":{"type":"string"},"required":false},{"in":"query","name":"pincode","description":"A `pincode` contains a specific value of the city.","schema":{"type":"integer"},"required":false},{"in":"query","name":"sector","description":"A `sector` contains a specific value of the city.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"page number.","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"page size.","schema":{"type":"integer"},"required":false}],"query":[{"in":"query","name":"x-application-id","description":"A `x-application-id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"query","name":"x-application-data","description":"A `x-application-data` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true},{"in":"query","name":"country","description":"A `country` contains a specific value of the country `iso2` code.","schema":{"type":"string"},"required":false},{"in":"query","name":"state","description":"A `state` contains a specific value of the state, province.","schema":{"type":"string"},"required":false},{"in":"query","name":"city","description":"A `city` contains a specific value of the city.","schema":{"type":"string"},"required":false},{"in":"query","name":"pincode","description":"A `pincode` contains a specific value of the city.","schema":{"type":"integer"},"required":false},{"in":"query","name":"sector","description":"A `sector` contains a specific value of the city.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"page number.","schema":{"type":"integer"},"required":false},{"in":"query","name":"page_size","description":"page size.","schema":{"type":"integer"},"required":false}],"headers":[],"path":[]}""", serverType="application", x_application_id=x_application_id, x_application_data=x_application_data, country=country, state=state, city=city, pincode=pincode, sector=sector, page_no=page_no, page_size=page_size)
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
            from .models import GetStoreResponse
            schema = GetStoreResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getLocations")
                print(e)

        return response
    
    async def getCountries(self, onboarding=None, page_no=None, page_size=None, q=None, body="", request_headers:Dict={}):
        """Retrieve of all countries.
        :param onboarding : Only fetch countries which allowed for onboard on Platform. : type boolean
        :param page_no : page number. : type integer
        :param page_size : page size. : type integer
        :param q : search. : type string
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

        # Parameter validation
        schema = LogisticValidator.getCountries()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCountries"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"onboarding","description":"Only fetch countries which allowed for onboard on Platform.","schema":{"type":"boolean"},"required":false,"examples":{"Yes":{"value":true},"No":{"value":false}}},{"in":"query","name":"page_no","description":"page number.","schema":{"type":"integer","default":1},"required":false,"examples":{"One":{"value":1},"Ten":{"value":10}}},{"in":"query","name":"page_size","description":"page size.","schema":{"type":"integer","default":12,"maximum":250},"required":false,"examples":{"Six":{"value":6},"Five":{"value":5}}},{"in":"query","name":"q","description":"search.","schema":{"type":"string"},"required":false,"examples":{"400603":{"value":"400603"},"Mumbai":{"value":"Mumbai"}}}],"query":[{"in":"query","name":"onboarding","description":"Only fetch countries which allowed for onboard on Platform.","schema":{"type":"boolean"},"required":false,"examples":{"Yes":{"value":true},"No":{"value":false}}},{"in":"query","name":"page_no","description":"page number.","schema":{"type":"integer","default":1},"required":false,"examples":{"One":{"value":1},"Ten":{"value":10}}},{"in":"query","name":"page_size","description":"page size.","schema":{"type":"integer","default":12,"maximum":250},"required":false,"examples":{"Six":{"value":6},"Five":{"value":5}}},{"in":"query","name":"q","description":"search.","schema":{"type":"string"},"required":false,"examples":{"400603":{"value":"400603"},"Mumbai":{"value":"Mumbai"}}}],"headers":[],"path":[]}""", serverType="application", onboarding=onboarding, page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(onboarding=onboarding, page_no=page_no, page_size=page_size, q=q)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCountries"]).netloc, "get", await create_url_without_domain("/service/application/logistics/v1.0/countries", onboarding=onboarding, page_no=page_no, page_size=page_size, q=q), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

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
        """Retrieve data for a single country and address format.
        :param country_iso_code : The `country_iso_code` is ISO-2 (alpha-2) code for the country. : type string
        """
        payload = {}
        
        if country_iso_code is not None:
            payload["country_iso_code"] = country_iso_code

        # Parameter validation
        schema = LogisticValidator.getCountry()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCountry"], proccessed_params="""{"required":[{"in":"path","name":"country_iso_code","description":"The `country_iso_code` is ISO-2 (alpha-2) code for the country.","schema":{"type":"string"},"required":true,"examples":{"India":{"value":"IN"},"UAE":{"value":"AE"}}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"country_iso_code","description":"The `country_iso_code` is ISO-2 (alpha-2) code for the country.","schema":{"type":"string"},"required":true,"examples":{"India":{"value":"IN"},"UAE":{"value":"AE"}}}]}""", serverType="application", country_iso_code=country_iso_code)
        query_string = await create_query_string(country_iso_code=country_iso_code)

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
    
    async def getLocalities(self, locality_type=None, country=None, state=None, city=None, page_no=None, page_size=None, q=None, body="", request_headers:Dict={}):
        """Get Localities data.
        :param locality_type : A `locality_type` contains unique geographical division. : type string
        :param country : A `country` contains a specific value of the country iso2 code. : type string
        :param state : A `state` contains a specific value of the state, province. : type string
        :param city : A `city` contains a specific value of the city. : type string
        :param page_no : page number. : type integer
        :param page_size : page size. : type integer
        :param q : search. : type string
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
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLocalities"], proccessed_params="""{"required":[{"in":"path","name":"locality_type","description":"A `locality_type` contains unique geographical division.","schema":{"type":"string","enum":["state","city","pincode","sector"]},"required":true,"examples":{"Sector":{"value":"sector"},"City":{"value":"city"}}}],"optional":[{"in":"query","name":"country","description":"A `country` contains a specific value of the country iso2 code.","schema":{"type":"string"},"required":false,"examples":{"India":{"value":"IN"},"UAE":{"value":"AE"}}},{"in":"query","name":"state","description":"A `state` contains a specific value of the state, province.","schema":{"type":"string"},"required":false,"examples":{"Maharashtra":{"value":"MAHARASHTRA"},"Gujurat":{"value":"GUJURAT"}}},{"in":"query","name":"city","description":"A `city` contains a specific value of the city.","schema":{"type":"string"},"required":false,"examples":{"Thane":{"value":"THANE"},"Mumbai":{"value":"MUMBAI"}}},{"in":"query","name":"page_no","description":"page number.","schema":{"type":"integer","default":1},"required":false,"examples":{"One":{"value":1},"Ten":{"value":10}}},{"in":"query","name":"page_size","description":"page size.","schema":{"type":"integer","default":12,"maximum":1000},"required":false,"examples":{"Six":{"value":6},"Five":{"value":5}}},{"in":"query","name":"q","description":"search.","schema":{"type":"string"},"required":false,"examples":{"India":{"value":"India"},"UAE":{"value":"UAE"}}}],"query":[{"in":"query","name":"country","description":"A `country` contains a specific value of the country iso2 code.","schema":{"type":"string"},"required":false,"examples":{"India":{"value":"IN"},"UAE":{"value":"AE"}}},{"in":"query","name":"state","description":"A `state` contains a specific value of the state, province.","schema":{"type":"string"},"required":false,"examples":{"Maharashtra":{"value":"MAHARASHTRA"},"Gujurat":{"value":"GUJURAT"}}},{"in":"query","name":"city","description":"A `city` contains a specific value of the city.","schema":{"type":"string"},"required":false,"examples":{"Thane":{"value":"THANE"},"Mumbai":{"value":"MUMBAI"}}},{"in":"query","name":"page_no","description":"page number.","schema":{"type":"integer","default":1},"required":false,"examples":{"One":{"value":1},"Ten":{"value":10}}},{"in":"query","name":"page_size","description":"page size.","schema":{"type":"integer","default":12,"maximum":1000},"required":false,"examples":{"Six":{"value":6},"Five":{"value":5}}},{"in":"query","name":"q","description":"search.","schema":{"type":"string"},"required":false,"examples":{"India":{"value":"India"},"UAE":{"value":"UAE"}}}],"headers":[],"path":[{"in":"path","name":"locality_type","description":"A `locality_type` contains unique geographical division.","schema":{"type":"string","enum":["state","city","pincode","sector"]},"required":true,"examples":{"Sector":{"value":"sector"},"City":{"value":"city"}}}]}""", serverType="application", locality_type=locality_type, country=country, state=state, city=city, page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(locality_type=locality_type, country=country, state=state, city=city, page_no=page_no, page_size=page_size, q=q)

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
        """Get Locality data
        :param locality_type : A `locality_type` contains value geographical division. : type string
        :param locality_value : A `locality_value` contains a specific name of the locality. : type string
        :param country : A `country` contains a specific value of the country iso2 code. : type string
        :param state : A `state` contains a specific value of the state, province. : type string
        :param city : A `city` contains a specific value of the city. : type string
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
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLocality"], proccessed_params="""{"required":[{"in":"path","name":"locality_type","description":"A `locality_type` contains value geographical division.","schema":{"type":"string","enum":["pincode","sector"]},"required":true,"examples":{"Pincode":{"value":"pincode"},"Sector":{"value":"sector"}}},{"in":"path","name":"locality_value","description":"A `locality_value` contains a specific name of the locality.","schema":{"type":"string"},"required":true,"examples":{"Pincode":{"value":"400603"},"Sector":{"value":"Abu Dhabi"}}}],"optional":[{"in":"query","name":"country","description":"A `country` contains a specific value of the country iso2 code.","schema":{"type":"string"},"required":false,"examples":{"India":{"value":"IN"},"UAE":{"value":"AE"}}},{"in":"query","name":"state","description":"A `state` contains a specific value of the state, province.","schema":{"type":"string"},"required":false,"examples":{"Maharashtra":{"value":"MAHARASHTRA"}}},{"in":"query","name":"city","description":"A `city` contains a specific value of the city.","schema":{"type":"string"},"required":false,"examples":{"Dubai":{"value":"DUBAI"},"Thane":{"value":"THANE"}}}],"query":[{"in":"query","name":"country","description":"A `country` contains a specific value of the country iso2 code.","schema":{"type":"string"},"required":false,"examples":{"India":{"value":"IN"},"UAE":{"value":"AE"}}},{"in":"query","name":"state","description":"A `state` contains a specific value of the state, province.","schema":{"type":"string"},"required":false,"examples":{"Maharashtra":{"value":"MAHARASHTRA"}}},{"in":"query","name":"city","description":"A `city` contains a specific value of the city.","schema":{"type":"string"},"required":false,"examples":{"Dubai":{"value":"DUBAI"},"Thane":{"value":"THANE"}}}],"headers":[],"path":[{"in":"path","name":"locality_type","description":"A `locality_type` contains value geographical division.","schema":{"type":"string","enum":["pincode","sector"]},"required":true,"examples":{"Pincode":{"value":"pincode"},"Sector":{"value":"sector"}}},{"in":"path","name":"locality_value","description":"A `locality_value` contains a specific name of the locality.","schema":{"type":"string"},"required":true,"examples":{"Pincode":{"value":"400603"},"Sector":{"value":"Abu Dhabi"}}}]}""", serverType="application", locality_type=locality_type, locality_value=locality_value, country=country, state=state, city=city)
        query_string = await create_query_string(locality_type=locality_type, locality_value=locality_value, country=country, state=state, city=city)

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
        """Validate given address wrt template
        :param country_iso_code : The ISO code of the country. : type string
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
        from .models import ValidateAddressRequest
        schema = ValidateAddressRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["validateAddress"], proccessed_params="""{"required":[{"in":"path","name":"country_iso_code","description":"The ISO code of the country.","schema":{"type":"string"},"required":true,"examples":{"India":{"value":"IN"},"UAE":{"value":"AE"}}},{"in":"path","name":"template_name","description":"The type of address form.","schema":{"type":"string","enum":["checkout_form","store_os_form","default_display"]},"required":true,"examples":{"India":{"value":"checkout_form"},"UAE":{"value":"checkout_form"}}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"country_iso_code","description":"The ISO code of the country.","schema":{"type":"string"},"required":true,"examples":{"India":{"value":"IN"},"UAE":{"value":"AE"}}},{"in":"path","name":"template_name","description":"The type of address form.","schema":{"type":"string","enum":["checkout_form","store_os_form","default_display"]},"required":true,"examples":{"India":{"value":"checkout_form"},"UAE":{"value":"checkout_form"}}}]}""", serverType="application", country_iso_code=country_iso_code, template_name=template_name)
        query_string = await create_query_string(country_iso_code=country_iso_code, template_name=template_name)

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
            from .models import ValidateAddressRequest
            schema = ValidateAddressRequest()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for validateAddress")
                print(e)

        return response
    