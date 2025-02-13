"""Configuration Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .validator import ConfigurationValidator

class Configuration:
    def __init__(self, config: PlatformConfig):
        self._conf = config

    
    async def createApplication(self, body="", request_headers:Dict={}):
        """Generate and add a new sales channel. sales channels are sales channel websites which can be configured, personalized and customized. Use this API to create a new sales channel in the current company.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.createApplication()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateApplicationRequestSchema
        schema = CreateApplicationRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application", """{"required":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string


        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateAppResponseSchema
            schema = CreateAppResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createApplication")
                print(e)

        return response
    
    async def getApplications(self, page_no=None, page_size=None, q=None, request_headers:Dict={}):
        """Retrieve a list of available sales channels. sales channels are sales channel websites which can be configured, personalized and customised. Use this API to fetch a list of sales channels created within a company.
        :param page_no :  : type integer
        :param page_size :  : type integer
        :param q : Search param by name or domain : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if q is not None:
            payload["q"] = q

        # Parameter validation
        schema = ConfigurationValidator.getApplications()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application", """{"required":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}],"optional":[{"in":"query","name":"page_no","schema":{"type":"integer"}},{"name":"page_size","schema":{"type":"integer"},"in":"query"},{"name":"q","schema":{"type":"string"},"in":"query","description":"Search param by name or domain"}],"query":[{"in":"query","name":"page_no","schema":{"type":"integer"}},{"name":"page_size","schema":{"type":"integer"},"in":"query"},{"name":"q","schema":{"type":"string"},"in":"query","description":"Search param by name or domain"}],"headers":[],"path":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}]}""", serverType="platform", page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q)
        if query_string:
            url_with_params += "?" + query_string


        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/application", page_no=page_no, page_size=page_size, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationsResponseSchema
            schema = ApplicationsResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getApplications")
                print(e)

        return response
    
    async def getCurrencies(self, request_headers:Dict={}):
        """Retrieve a list of available currencies.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getCurrencies()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/currencies", """{"required":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string


        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/currencies", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CurrenciesResponseSchema
            schema = CurrenciesResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCurrencies")
                print(e)

        return response
    
    async def getDomainAvailibility(self, body="", request_headers:Dict={}):
        """Check the availability of a specific domain. Use this API to check the domain availability before linking it to sales channel. Also sends domain suggestions that are similar to the queried domain. Note - Custom domain search is currently powered by GoDaddy provider.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getDomainAvailibility()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DomainSuggestionsRequestSchema
        schema = DomainSuggestionsRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/domain/suggestions", """{"required":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string


        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/domain/suggestions", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DomainSuggestionsResponseSchema
            schema = DomainSuggestionsResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDomainAvailibility")
                print(e)

        return response
    
    async def getBrandsByCompany(self, q=None, request_headers:Dict={}):
        """Retrieve all the brands added in a company. Get all the brand names, along with URLs of their logo, banner, and portrait image. can be searched on brand_name.
        :param q : Search text for brand name : type string
        """
        payload = {}
        
        if q is not None:
            payload["q"] = q

        # Parameter validation
        schema = ConfigurationValidator.getBrandsByCompany()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/inventory/brands-by-companies", """{"required":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}],"optional":[{"name":"q","in":"query","schema":{"type":"string"},"description":"Search text for brand name"}],"query":[{"name":"q","in":"query","schema":{"type":"string"},"description":"Search text for brand name"}],"headers":[],"path":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}]}""", serverType="platform", q=q)
        query_string = await create_query_string(q=q)
        if query_string:
            url_with_params += "?" + query_string


        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/inventory/brands-by-companies", q=q), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BrandsByCompanyResponseSchema
            schema = BrandsByCompanyResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBrandsByCompany")
                print(e)

        return response
    
    async def getCompanyByBrands(self, page_no=None, page_size=None, body="", request_headers:Dict={}):
        """Retrieve a paginated list of companies associated with specific brands. Can be searched using the brand ID and company name
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = ConfigurationValidator.getCompanyByBrands()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CompanyByBrandsRequestSchema
        schema = CompanyByBrandsRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/inventory/companies-by-brands", """{"required":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"headers":[],"path":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}]}""", serverType="platform", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        if query_string:
            url_with_params += "?" + query_string


        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/inventory/companies-by-brands", page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CompanyByBrandsResponseSchema
            schema = CompanyByBrandsResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCompanyByBrands")
                print(e)

        return response
    
    async def getStoreByBrands(self, page_no=None, page_size=None, body="", request_headers:Dict={}):
        """Retrieve stores associated with specific brands. Retrieve a list of selling locations (stores) by the brands they deal. Store has information about store name, store type, store code, store address, and company detail. filtering can be done on brand id and brand names
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = ConfigurationValidator.getStoreByBrands()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import StoreByBrandsRequestSchema
        schema = StoreByBrandsRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/inventory/stores-by-brands", """{"required":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"headers":[],"path":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}]}""", serverType="platform", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        if query_string:
            url_with_params += "?" + query_string


        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/inventory/stores-by-brands", page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import StoreByBrandsResponseSchema
            schema = StoreByBrandsResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getStoreByBrands")
                print(e)

        return response
    
    async def getOtherSellerApplications(self, page_no=None, page_size=None, request_headers:Dict={}):
        """Retrieve sales channels of  other sellers. Retrieve all other seller sales channels that were not created within the current company. but have opted for the current company's inventory.
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = ConfigurationValidator.getOtherSellerApplications()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/other-seller-applications", """{"required":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."}],"headers":[],"path":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"}]}""", serverType="platform", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        if query_string:
            url_with_params += "?" + query_string


        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/other-seller-applications", page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OtherSellerApplications
            schema = OtherSellerApplications()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOtherSellerApplications")
                print(e)

        return response
    
    async def getOtherSellerApplicationById(self, id=None, request_headers:Dict={}):
        """Retrieve details of a seller sales channel that was not created within the current company but has opted for the current company's inventory and searched via the sales channel ID of another sales channel
        :param id : Application Id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ConfigurationValidator.getOtherSellerApplicationById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/other-seller-applications/{id}", """{"required":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Application Id","required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Application Id","required":true}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string


        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/other-seller-applications/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OptedApplicationResponseSchema
            schema = OptedApplicationResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOtherSellerApplicationById")
                print(e)

        return response
    
    async def optOutFromApplication(self, id=None, body="", request_headers:Dict={}):
        """This API allows businesses to opt out of sharing their inventory with external seller sales channels. By using this API, companies or stores can prevent specific seller sales channels from fetching their inventory data. This feature is useful for businesses that want to control who  can access their product listings and other inventory information. It helps maintain privacy and control over data distribution, ensuring that sensitive information is only shared with authorized partners.
        :param id : Alphanumeric ID allotted to an application (sales channel website) created within a business account. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ConfigurationValidator.optOutFromApplication()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OptOutInventory
        schema = OptOutInventory()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/other-seller-applications/{id}/opt_out", """{"required":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account.","required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","in":"path","required":true,"name":"company_id"},{"name":"id","in":"path","schema":{"type":"string"},"description":"Alphanumeric ID allotted to an application (sales channel website) created within a business account.","required":true}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string


        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/configuration/v1.0/company/{self._conf.companyId}/other-seller-applications/{id}/opt_out", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessMessageResponseSchema
            schema = SuccessMessageResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for optOutFromApplication")
                print(e)

        return response
    
    async def getCurrencyExchangeRates(self, currency_code=None, exchange_currency_code=None, exchange_country_code=None, request_headers:Dict={}):
        """Retrieve a list of currency exchange rates, relative to a provided currency.
        :param currency_code : The 3-letter ISO 4217 code representing the base currency for the exchange rates.  Defaults to "INR" if not specified. : type string
        :param exchange_currency_code : A 3-letter ISO 4217 currency code for which exchange rates against the base currency are requested. : type string
        :param exchange_country_code : The country code for which exchange rates against the base currency are requested. : type string
        """
        payload = {}
        
        if currency_code is not None:
            payload["currency_code"] = currency_code
        if exchange_currency_code is not None:
            payload["exchange_currency_code"] = exchange_currency_code
        if exchange_country_code is not None:
            payload["exchange_country_code"] = exchange_country_code

        # Parameter validation
        schema = ConfigurationValidator.getCurrencyExchangeRates()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/configuration/v2.0/company/{self._conf.companyId}/currency-exchange", """{"required":[{"in":"path","schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"name":"company_id"}],"optional":[{"in":"query","name":"currency_code","description":"The 3-letter ISO 4217 code representing the base currency for the exchange rates.  Defaults to \"INR\" if not specified.","required":false,"schema":{"type":"string","default":"INR","x-not-enum":true}},{"in":"query","name":"exchange_currency_code","description":"A 3-letter ISO 4217 currency code for which exchange rates against the base currency are requested.","required":false,"schema":{"type":"string","x-not-enum":true}},{"in":"query","name":"exchange_country_code","description":"The country code for which exchange rates against the base currency are requested.","required":false,"schema":{"type":"string","x-not-enum":true}}],"query":[{"in":"query","name":"currency_code","description":"The 3-letter ISO 4217 code representing the base currency for the exchange rates.  Defaults to \"INR\" if not specified.","required":false,"schema":{"type":"string","default":"INR","x-not-enum":true}},{"in":"query","name":"exchange_currency_code","description":"A 3-letter ISO 4217 currency code for which exchange rates against the base currency are requested.","required":false,"schema":{"type":"string","x-not-enum":true}},{"in":"query","name":"exchange_country_code","description":"The country code for which exchange rates against the base currency are requested.","required":false,"schema":{"type":"string","x-not-enum":true}}],"headers":[],"path":[{"in":"path","schema":{"type":"integer"},"description":"Numeric ID allotted to a business account on Fynd Platform","required":true,"name":"company_id"}]}""", serverType="platform", currency_code=currency_code, exchange_currency_code=exchange_currency_code, exchange_country_code=exchange_country_code, )
        query_string = await create_query_string(currency_code=currency_code, exchange_currency_code=exchange_currency_code, exchange_country_code=exchange_country_code, )
        if query_string:
            url_with_params += "?" + query_string


        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/configuration/v2.0/company/{self._conf.companyId}/currency-exchange", currency_code=currency_code, exchange_currency_code=exchange_currency_code, exchange_country_code=exchange_country_code), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CurrencyExchangeResponseV2
            schema = CurrencyExchangeResponseV2()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCurrencyExchangeRates")
                print(e)

        return response
    