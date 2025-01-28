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
            "getAllCountries": "/service/application/logistics/v1.0/country-list",
            "getZones": "/service/application/logistics/v2.0/company/{company_id}/application/{application_id}/zones",
            "getGeoAreas": "/service/application/logistics/v1.0/company/{company_id}/application/{application_id}/geoareas",
            "getCountries": "/service/application/logistics/v2.0/countries",
            "getCountry": "/service/application/logistics/v1.0/countries/{country_iso_code}",
            "getLocalities": "/service/application/logistics/v1.0/localities/{locality_type}",
            "getLocality": "/service/application/logistics/v1.0/localities/{locality_type}/{locality_value}",
            "validateAddress": "/service/application/logistics/v1.0/country/{country_iso_code}/address/templates/{template_name}/validate",
            "createShipments": "/service/application/logistics/v1.0/company/{company_id}/application/{application_id}/shipments"
            
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
        if query_string:
            url_with_params += "?" + query_string

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
    
    async def getAllCountries(self, body="", request_headers:Dict={}):
        """Get a list of countries within the specified delivery zones for that application.
        """
        payload = {}
        

        # Parameter validation
        schema = LogisticValidator.getAllCountries()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAllCountries"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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
    
    async def getZones(self, company_id=None, application_id=None, stage=None, type=None, page_size=None, page_no=None, is_active=None, q=None, country_iso_code=None, pincode=None, state=None, city=None, sector=None, body="", request_headers:Dict={}):
        """Displays the list of zones defined at the application level.
        :param company_id : The unique identifier for the company. : type integer
        :param application_id : A `application_id` is a unique identifier for a particular sale channel. : type string
        :param stage : Identifies the specific stage of zone bing requested. : type string
        :param type : Using type, you can filter custom or default zones : type string
        :param page_size : Defines the number of items displayed per page. : type integer
        :param page_no : current page number. : type integer
        :param is_active : Status of Zone (either active or inactive) : type boolean
        :param q : Search with name as a free text. : type string
        :param country_iso_code : ISO2 code of the country. : type string
        :param pincode : PIN Code of the country. : type string
        :param state : State of the country. : type string
        :param city : City of the country. : type string
        :param sector : Sector name of mentioned address. : type string
        """
        payload = {}
        
        if company_id is not None:
            payload["company_id"] = company_id
        if application_id is not None:
            payload["application_id"] = application_id
        if stage is not None:
            payload["stage"] = stage
        if type is not None:
            payload["type"] = type
        if page_size is not None:
            payload["page_size"] = page_size
        if page_no is not None:
            payload["page_no"] = page_no
        if is_active is not None:
            payload["is_active"] = is_active
        if q is not None:
            payload["q"] = q
        if country_iso_code is not None:
            payload["country_iso_code"] = country_iso_code
        if pincode is not None:
            payload["pincode"] = pincode
        if state is not None:
            payload["state"] = state
        if city is not None:
            payload["city"] = city
        if sector is not None:
            payload["sector"] = sector

        # Parameter validation
        schema = LogisticValidator.getZones()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getZones"], proccessed_params="""{"required":[{"in":"path","name":"company_id","description":"The unique identifier for the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"stage","description":"Identifies the specific stage of zone bing requested.","schema":{"type":"string","enum":["in_progress","failed","completed"]}},{"in":"query","name":"type","description":"Using type, you can filter custom or default zones","schema":{"type":"string","enum":["default","custom"]}},{"in":"query","name":"page_size","description":"Defines the number of items displayed per page.","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"page_no","description":"current page number.","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"is_active","description":"Status of Zone (either active or inactive)","schema":{"type":"boolean"}},{"in":"query","name":"q","description":"Search with name as a free text.","schema":{"type":"string"}},{"in":"query","name":"country_iso_code","description":"ISO2 code of the country.","schema":{"type":"string"}},{"in":"query","name":"pincode","description":"PIN Code of the country.","schema":{"type":"string"}},{"in":"query","name":"state","description":"State of the country.","schema":{"type":"string"}},{"in":"query","name":"city","description":"City of the country.","schema":{"type":"string"}},{"in":"query","name":"sector","description":"Sector name of mentioned address.","schema":{"type":"string"}}],"query":[{"in":"query","name":"stage","description":"Identifies the specific stage of zone bing requested.","schema":{"type":"string","enum":["in_progress","failed","completed"]}},{"in":"query","name":"type","description":"Using type, you can filter custom or default zones","schema":{"type":"string","enum":["default","custom"]}},{"in":"query","name":"page_size","description":"Defines the number of items displayed per page.","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"page_no","description":"current page number.","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"is_active","description":"Status of Zone (either active or inactive)","schema":{"type":"boolean"}},{"in":"query","name":"q","description":"Search with name as a free text.","schema":{"type":"string"}},{"in":"query","name":"country_iso_code","description":"ISO2 code of the country.","schema":{"type":"string"}},{"in":"query","name":"pincode","description":"PIN Code of the country.","schema":{"type":"string"}},{"in":"query","name":"state","description":"State of the country.","schema":{"type":"string"}},{"in":"query","name":"city","description":"City of the country.","schema":{"type":"string"}},{"in":"query","name":"sector","description":"Sector name of mentioned address.","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"The unique identifier for the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for a particular sale channel.","schema":{"type":"string"},"required":true}]}""", serverType="application", company_id=company_id, application_id=application_id, stage=stage, type=type, page_size=page_size, page_no=page_no, is_active=is_active, q=q, country_iso_code=country_iso_code, pincode=pincode, state=state, city=city, sector=sector)
        query_string = await create_query_string(stage=stage, type=type, page_size=page_size, page_no=page_no, is_active=is_active, q=q, country_iso_code=country_iso_code, pincode=pincode, state=state, city=city, sector=sector)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getZones"]).netloc, "get", await create_url_without_domain("/service/application/logistics/v2.0/company/{company_id}/application/{application_id}/zones", company_id=company_id, application_id=application_id, stage=stage, type=type, page_size=page_size, page_no=page_no, is_active=is_active, q=q, country_iso_code=country_iso_code, pincode=pincode, state=state, city=city, sector=sector), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ListViewResponseV2
            schema = ListViewResponseV2()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getZones")
                print(e)

        return response
    
    async def getGeoAreas(self, application_id=None, company_id=None, page_size=None, page_no=None, type=None, is_active=None, q=None, country_iso_code=None, state=None, city=None, pincode=None, sector=None, body="", request_headers:Dict={}):
        """Retrieves a listing view of created GeoAreas.
        :param application_id : A `application_id` is a unique identifier for an application. : type string
        :param company_id : A `company_id` is a unique identifier for a particular sale channel. : type integer
        :param page_size : Determines the items to be displayed in a page : type integer
        :param page_no : Current page number : type integer
        :param type : To fetch the type of a specific geoarea. : type string
        :param is_active : Status of GeoAreas (either active or inactive) : type boolean
        :param q : search with name as a free text : type string
        :param country_iso_code : ISO2 code of the country : type string
        :param state : State name : type string
        :param city : City name : type string
        :param pincode : Pincode value to search geoareas : type string
        :param sector : Sector value to search geoareas : type string
        """
        payload = {}
        
        if application_id is not None:
            payload["application_id"] = application_id
        if company_id is not None:
            payload["company_id"] = company_id
        if page_size is not None:
            payload["page_size"] = page_size
        if page_no is not None:
            payload["page_no"] = page_no
        if type is not None:
            payload["type"] = type
        if is_active is not None:
            payload["is_active"] = is_active
        if q is not None:
            payload["q"] = q
        if country_iso_code is not None:
            payload["country_iso_code"] = country_iso_code
        if state is not None:
            payload["state"] = state
        if city is not None:
            payload["city"] = city
        if pincode is not None:
            payload["pincode"] = pincode
        if sector is not None:
            payload["sector"] = sector

        # Parameter validation
        schema = LogisticValidator.getGeoAreas()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getGeoAreas"], proccessed_params="""{"required":[{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for an application.","schema":{"type":"string"},"required":true},{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"page_no","description":"Current page number","schema":{"type":"integer"}},{"in":"query","name":"type","description":"To fetch the type of a specific geoarea.","schema":{"type":"string"}},{"in":"query","name":"is_active","description":"Status of GeoAreas (either active or inactive)","schema":{"type":"boolean"}},{"in":"query","name":"q","description":"search with name as a free text","schema":{"type":"string"}},{"in":"query","name":"country_iso_code","description":"ISO2 code of the country","schema":{"type":"string"}},{"in":"query","name":"state","description":"State name","schema":{"type":"string"}},{"in":"query","name":"city","description":"City name","schema":{"type":"string"}},{"in":"query","name":"pincode","description":"Pincode value to search geoareas","schema":{"type":"string"}},{"in":"query","name":"sector","description":"Sector value to search geoareas","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"page_no","description":"Current page number","schema":{"type":"integer"}},{"in":"query","name":"type","description":"To fetch the type of a specific geoarea.","schema":{"type":"string"}},{"in":"query","name":"is_active","description":"Status of GeoAreas (either active or inactive)","schema":{"type":"boolean"}},{"in":"query","name":"q","description":"search with name as a free text","schema":{"type":"string"}},{"in":"query","name":"country_iso_code","description":"ISO2 code of the country","schema":{"type":"string"}},{"in":"query","name":"state","description":"State name","schema":{"type":"string"}},{"in":"query","name":"city","description":"City name","schema":{"type":"string"}},{"in":"query","name":"pincode","description":"Pincode value to search geoareas","schema":{"type":"string"}},{"in":"query","name":"sector","description":"Sector value to search geoareas","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"application_id","description":"A `application_id` is a unique identifier for an application.","schema":{"type":"string"},"required":true},{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", serverType="application", application_id=application_id, company_id=company_id, page_size=page_size, page_no=page_no, type=type, is_active=is_active, q=q, country_iso_code=country_iso_code, state=state, city=city, pincode=pincode, sector=sector)
        query_string = await create_query_string(page_size=page_size, page_no=page_no, type=type, is_active=is_active, q=q, country_iso_code=country_iso_code, state=state, city=city, pincode=pincode, sector=sector)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getGeoAreas"]).netloc, "get", await create_url_without_domain("/service/application/logistics/v1.0/company/{company_id}/application/{application_id}/geoareas", application_id=application_id, company_id=company_id, page_size=page_size, page_no=page_no, type=type, is_active=is_active, q=q, country_iso_code=country_iso_code, state=state, city=city, pincode=pincode, sector=sector), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GeoAreaGetResponseBody
            schema = GeoAreaGetResponseBody()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getGeoAreas")
                print(e)

        return response
    
    async def getCountries(self, onboard=None, page_no=None, page_size=None, q=None, hierarchy=None, body="", request_headers:Dict={}):
        """Retrieve a list of countries for logistical purposes.
        :param onboard : Only fetch countries which allowed for onboard on Platform. : type boolean
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 12 : type integer
        :param q : The search string to search in the list of countries by name. : type string
        :param hierarchy : The search filter to filter countries based on their available hierarchy. : type string
        """
        payload = {}
        
        if onboard is not None:
            payload["onboard"] = onboard
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
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCountries"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"onboard","description":"Only fetch countries which allowed for onboard on Platform.","schema":{"type":"boolean"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results. Default value is 1.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page. Default value is 12","schema":{"type":"integer","default":12,"maximum":300},"required":false},{"in":"query","name":"q","description":"The search string to search in the list of countries by name.","schema":{"type":"string"},"required":false},{"in":"query","name":"hierarchy","description":"The search filter to filter countries based on their available hierarchy.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"onboard","description":"Only fetch countries which allowed for onboard on Platform.","schema":{"type":"boolean"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results. Default value is 1.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page. Default value is 12","schema":{"type":"integer","default":12,"maximum":300},"required":false},{"in":"query","name":"q","description":"The search string to search in the list of countries by name.","schema":{"type":"string"},"required":false},{"in":"query","name":"hierarchy","description":"The search filter to filter countries based on their available hierarchy.","schema":{"type":"string"},"required":false}],"headers":[],"path":[]}""", serverType="application", onboard=onboard, page_no=page_no, page_size=page_size, q=q, hierarchy=hierarchy)
        query_string = await create_query_string(onboard=onboard, page_no=page_no, page_size=page_size, q=q, hierarchy=hierarchy)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCountries"]).netloc, "get", await create_url_without_domain("/service/application/logistics/v2.0/countries", onboard=onboard, page_no=page_no, page_size=page_size, q=q, hierarchy=hierarchy), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

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
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCountry"], proccessed_params="""{"required":[{"in":"path","name":"country_iso_code","description":"The ISO 3166-1 alpha-2 code representing the country (e.g., \"IN\" for India, \"US\" for the United States).","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"country_iso_code","description":"The ISO 3166-1 alpha-2 code representing the country (e.g., \"IN\" for India, \"US\" for the United States).","schema":{"type":"string"},"required":true}]}""", serverType="application", country_iso_code=country_iso_code)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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
    
    async def getLocalities(self, locality_type=None, country=None, state=None, city=None, page_no=None, page_size=None, q=None, name=None, body="", request_headers:Dict={}):
        """Get geographical data for a specific type of locality based on the provided filters. For instance, obtain a list of cities for a given country and state.
        :param locality_type : Unique geographical division. : type string
        :param country : Country name. : type string
        :param state : State or the province. : type string
        :param city : City. : type string
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 12. : type integer
        :param q : This parameter is used to filter or search the records. : type string
        :param name : Search for localities. Either provide a full name or a search term. : type string
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
        if name is not None:
            payload["name"] = name

        # Parameter validation
        schema = LogisticValidator.getLocalities()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLocalities"], proccessed_params="""{"required":[{"in":"path","name":"locality_type","description":"Unique geographical division.","schema":{"type":"string","enum":["state","city","pincode","sector"]},"required":true}],"optional":[{"in":"query","name":"country","description":"Country name.","schema":{"type":"string"},"required":false},{"in":"query","name":"state","description":"State or the province.","schema":{"type":"string"},"required":false},{"in":"query","name":"city","description":"City.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results. Default value is 1.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page. Default value is 12.","schema":{"type":"integer","default":12,"maximum":1000},"required":false},{"in":"query","name":"q","description":"This parameter is used to filter or search the records.","schema":{"type":"string"},"required":false},{"in":"query","name":"name","description":"Search for localities. Either provide a full name or a search term.","schema":{"type":"string"}}],"query":[{"in":"query","name":"country","description":"Country name.","schema":{"type":"string"},"required":false},{"in":"query","name":"state","description":"State or the province.","schema":{"type":"string"},"required":false},{"in":"query","name":"city","description":"City.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results. Default value is 1.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page. Default value is 12.","schema":{"type":"integer","default":12,"maximum":1000},"required":false},{"in":"query","name":"q","description":"This parameter is used to filter or search the records.","schema":{"type":"string"},"required":false},{"in":"query","name":"name","description":"Search for localities. Either provide a full name or a search term.","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"locality_type","description":"Unique geographical division.","schema":{"type":"string","enum":["state","city","pincode","sector"]},"required":true}]}""", serverType="application", locality_type=locality_type, country=country, state=state, city=city, page_no=page_no, page_size=page_size, q=q, name=name)
        query_string = await create_query_string(country=country, state=state, city=city, page_no=page_no, page_size=page_size, q=q, name=name)
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getLocalities"]).netloc, "get", await create_url_without_domain("/service/application/logistics/v1.0/localities/{locality_type}", locality_type=locality_type, country=country, state=state, city=city, page_no=page_no, page_size=page_size, q=q, name=name), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

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
        if query_string:
            url_with_params += "?" + query_string

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
        from .models import ValidateAddressRequest
        schema = ValidateAddressRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["validateAddress"], proccessed_params="""{"required":[{"in":"path","name":"country_iso_code","description":"The ISO 3166-1 alpha-2 code representing the country (e.g., \"IN\" for India, \"US\" for the United States).","schema":{"type":"string"},"required":true},{"in":"path","name":"template_name","description":"The type of address form.","schema":{"type":"string","enum":["checkout_form","store_os_form","default_display"]},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"country_iso_code","description":"The ISO 3166-1 alpha-2 code representing the country (e.g., \"IN\" for India, \"US\" for the United States).","schema":{"type":"string"},"required":true},{"in":"path","name":"template_name","description":"The type of address form.","schema":{"type":"string","enum":["checkout_form","store_os_form","default_display"]},"required":true}]}""", serverType="application", country_iso_code=country_iso_code, template_name=template_name)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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
    
    async def createShipments(self, company_id=None, application_id=None, body="", request_headers:Dict={}):
        """Create and return shipments.
        :param company_id : The ID of the company. : type integer
        :param application_id : The ID of the application. : type string
        """
        payload = {}
        
        if company_id is not None:
            payload["company_id"] = company_id
        if application_id is not None:
            payload["application_id"] = application_id

        # Parameter validation
        schema = LogisticValidator.createShipments()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GenerateShipmentsRequest
        schema = GenerateShipmentsRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["createShipments"], proccessed_params="""{"required":[{"in":"path","name":"company_id","description":"The ID of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"The ID of the application.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"The ID of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"application_id","description":"The ID of the application.","schema":{"type":"string"},"required":true}]}""", serverType="application", company_id=company_id, application_id=application_id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["createShipments"]).netloc, "post", await create_url_without_domain("/service/application/logistics/v1.0/company/{company_id}/application/{application_id}/shipments", company_id=company_id, application_id=application_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GenerateShipmentsAndCourierPartnerResponse
            schema = GenerateShipmentsAndCourierPartnerResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createShipments")
                print(e)

        return response
    