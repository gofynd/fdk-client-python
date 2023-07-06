

"""CompanyProfile Platform Client"""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import CompanyProfileValidator

class CompanyProfile:
    def __init__(self, config):
        self._conf = config

    
    async def cbsOnboardGet(self, ):
        """This API allows to view the company profile of the seller account.
        """
        payload = {}
        

        # Parameter validation
        schema = CompanyProfileValidator.cbsOnboardGet()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import GetCompanyProfileSerializerResponse
        schema = GetCompanyProfileSerializerResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for cbsOnboardGet")
            print(e)

        

        return response
    
    async def updateCompany(self, body=""):
        """This API allows to edit the company profile of the seller account.
        """
        payload = {}
        

        # Parameter validation
        schema = CompanyProfileValidator.updateCompany()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateCompany
        schema = UpdateCompany()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import ProfileSuccessResponse
        schema = ProfileSuccessResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for updateCompany")
            print(e)

        

        return response
    
    async def getCompanyMetrics(self, ):
        """This API allows to view the company metrics, i.e. the status of its brand and stores. Also its allows to view the number of products, company documents & store documents which are verified and unverified.
        """
        payload = {}
        

        # Parameter validation
        schema = CompanyProfileValidator.getCompanyMetrics()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/metrics", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller account.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/metrics", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import MetricsSerializer
        schema = MetricsSerializer()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getCompanyMetrics")
            print(e)

        

        return response
    
    async def getBrand(self, brand_id=None):
        """This API helps to get data associated to a particular company brand.
        :param brand_id : Id of the brand to be viewed. : type string
        """
        payload = {}
        
        if brand_id:
            payload["brand_id"] = brand_id
        

        # Parameter validation
        schema = CompanyProfileValidator.getBrand()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/brand/{brand_id}", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to brand that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"brand_id","description":"Id of the brand to be viewed.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to brand that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"brand_id","description":"Id of the brand to be viewed.","schema":{"type":"string"},"required":true}]}""", brand_id=brand_id)
        query_string = await create_query_string(brand_id=brand_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/brand/{brand_id}", brand_id=brand_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import GetBrandResponseSerializer
        schema = GetBrandResponseSerializer()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getBrand")
            print(e)

        

        return response
    
    async def editBrand(self, brand_id=None, body=""):
        """This API allows to edit meta of a brand.
        :param brand_id : Id of the brand to be viewed. : type string
        """
        payload = {}
        
        if brand_id:
            payload["brand_id"] = brand_id
        

        # Parameter validation
        schema = CompanyProfileValidator.editBrand()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateUpdateBrandRequestSerializer
        schema = CreateUpdateBrandRequestSerializer()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/brand/{brand_id}", """{"required":[{"in":"path","name":"company_id","description":"Id of the company associated to brand that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"brand_id","description":"Id of the brand to be viewed.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company associated to brand that is to be viewed.","schema":{"type":"string"},"required":true},{"in":"path","name":"brand_id","description":"Id of the brand to be viewed.","schema":{"type":"string"},"required":true}]}""", brand_id=brand_id)
        query_string = await create_query_string(brand_id=brand_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/brand/{brand_id}", brand_id=brand_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import ProfileSuccessResponse
        schema = ProfileSuccessResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for editBrand")
            print(e)

        

        return response
    
    async def createBrand(self, body=""):
        """This API allows to create a brand associated to a company.
        """
        payload = {}
        

        # Parameter validation
        schema = CompanyProfileValidator.createBrand()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateUpdateBrandRequestSerializer
        schema = CreateUpdateBrandRequestSerializer()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/brand/", """{"required":[{"in":"path","name":"company_id","description":"Id of the company.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/brand/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import ProfileSuccessResponse
        schema = ProfileSuccessResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for createBrand")
            print(e)

        

        return response
    
    async def getBrands(self, page_no=None, page_size=None, q=None):
        """This API helps to get view brands associated to a particular company.
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        :param q : Search term for name. : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        

        # Parameter validation
        schema = CompanyProfileValidator.getBrands()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/company-brand", """{"required":[{"in":"path","name":"company_id","description":"Id of the company.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":20},"required":false},{"in":"query","name":"q","description":"Search term for name.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":20},"required":false},{"in":"query","name":"q","description":"Search term for name.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company.","schema":{"type":"string"},"required":true}]}""", page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/company-brand", page_no=page_no, page_size=page_size, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import CompanyBrandListSerializer
        schema = CompanyBrandListSerializer()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getBrands")
            print(e)

        

        return response
    
    async def createCompanyBrandMapping(self, body=""):
        """This API allows to create a company brand mapping, for a already existing brand in the system.
        """
        payload = {}
        

        # Parameter validation
        schema = CompanyProfileValidator.createCompanyBrandMapping()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CompanyBrandPostRequestSerializer
        schema = CompanyBrandPostRequestSerializer()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/company-brand", """{"required":[{"in":"path","name":"company_id","description":"Id of the company inside which the brand is to be mapped.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company inside which the brand is to be mapped.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/company-brand", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import ProfileSuccessResponse
        schema = ProfileSuccessResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for createCompanyBrandMapping")
            print(e)

        

        return response
    
    async def getLocations(self, store_type=None, q=None, stage=None, page_no=None, page_size=None, location_ids=None):
        """This API allows to view all the locations associated to a company.
        :param store_type : Helps to sort the location list on the basis of location type. : type string
        :param q : Query that is to be searched. : type string
        :param stage : to filter companies on basis of verified or unverified companies. : type string
        :param page_no : The page number to navigate through the given set of results : type integer
        :param page_size : Number of items to retrieve in each page. Default is 10. : type integer
        :param location_ids : Helps to filter stores on the basis of uids. : type array
        """
        payload = {}
        
        if store_type:
            payload["store_type"] = store_type
        
        if q:
            payload["q"] = q
        
        if stage:
            payload["stage"] = stage
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if location_ids:
            payload["location_ids"] = location_ids
        

        # Parameter validation
        schema = CompanyProfileValidator.getLocations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/location", """{"required":[{"in":"path","name":"company_id","description":"Id of the company whose locations are to fetched","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"store_type","description":"Helps to sort the location list on the basis of location type.","schema":{"type":"string"},"required":false},{"in":"query","name":"q","description":"Query that is to be searched.","schema":{"type":"string"},"required":false},{"in":"query","name":"stage","description":"to filter companies on basis of verified or unverified companies.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":20},"required":false},{"in":"query","name":"location_ids","description":"Helps to filter stores on the basis of uids.","schema":{"type":"array","items":{"type":"integer"}},"required":false}],"query":[{"in":"query","name":"store_type","description":"Helps to sort the location list on the basis of location type.","schema":{"type":"string"},"required":false},{"in":"query","name":"q","description":"Query that is to be searched.","schema":{"type":"string"},"required":false},{"in":"query","name":"stage","description":"to filter companies on basis of verified or unverified companies.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page. Default is 10.","schema":{"type":"integer","default":20},"required":false},{"in":"query","name":"location_ids","description":"Helps to filter stores on the basis of uids.","schema":{"type":"array","items":{"type":"integer"}},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company whose locations are to fetched","schema":{"type":"string"},"required":true}]}""", store_type=store_type, q=q, stage=stage, page_no=page_no, page_size=page_size, location_ids=location_ids)
        query_string = await create_query_string(store_type=store_type, q=q, stage=stage, page_no=page_no, page_size=page_size, location_ids=location_ids)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/location", store_type=store_type, q=q, stage=stage, page_no=page_no, page_size=page_size, location_ids=location_ids), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import LocationListSerializer
        schema = LocationListSerializer()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getLocations")
            print(e)

        

        return response
    
    async def createLocation(self, body=""):
        """This API allows to edit a location associated to a company.
        """
        payload = {}
        

        # Parameter validation
        schema = CompanyProfileValidator.createLocation()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import LocationSerializer
        schema = LocationSerializer()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/location", """{"required":[{"in":"path","name":"company_id","description":"Id of the company inside which the location is to be created.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company inside which the location is to be created.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/location", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import ProfileSuccessResponse
        schema = ProfileSuccessResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for createLocation")
            print(e)

        

        return response
    
    async def getLocationDetail(self, location_id=None):
        """This API helps to get data associated to a specific location.
        :param location_id : Id of the location which you want to view. : type string
        """
        payload = {}
        
        if location_id:
            payload["location_id"] = location_id
        

        # Parameter validation
        schema = CompanyProfileValidator.getLocationDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/location/{location_id}", """{"required":[{"in":"path","name":"company_id","description":"Id of the company inside which the location lies.","schema":{"type":"string"},"required":true},{"in":"path","name":"location_id","description":"Id of the location which you want to view.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company inside which the location lies.","schema":{"type":"string"},"required":true},{"in":"path","name":"location_id","description":"Id of the location which you want to view.","schema":{"type":"string"},"required":true}]}""", location_id=location_id)
        query_string = await create_query_string(location_id=location_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/location/{location_id}", location_id=location_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import GetLocationSerializer
        schema = GetLocationSerializer()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getLocationDetail")
            print(e)

        

        return response
    
    async def updateLocation(self, location_id=None, body=""):
        """This API allows to edit a location associated to a company.
        :param location_id : Id of the location which you want to edit. : type string
        """
        payload = {}
        
        if location_id:
            payload["location_id"] = location_id
        

        # Parameter validation
        schema = CompanyProfileValidator.updateLocation()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import LocationSerializer
        schema = LocationSerializer()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/location/{location_id}", """{"required":[{"in":"path","name":"company_id","description":"Id of the company inside which the location is to be created.","schema":{"type":"string"},"required":true},{"in":"path","name":"location_id","description":"Id of the location which you want to edit.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company inside which the location is to be created.","schema":{"type":"string"},"required":true},{"in":"path","name":"location_id","description":"Id of the location which you want to edit.","schema":{"type":"string"},"required":true}]}""", location_id=location_id)
        query_string = await create_query_string(location_id=location_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/location/{location_id}", location_id=location_id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import ProfileSuccessResponse
        schema = ProfileSuccessResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for updateLocation")
            print(e)

        

        return response
    
    async def createLocationBulk(self, body=""):
        """This API allows to create a location associated to a company.
        """
        payload = {}
        

        # Parameter validation
        schema = CompanyProfileValidator.createLocationBulk()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkLocationSerializer
        schema = BulkLocationSerializer()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/location/bulk", """{"required":[{"in":"path","name":"company_id","description":"Id of the company inside which the location is to be created.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Id of the company inside which the location is to be created.","schema":{"type":"string"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/company-profile/v1.0/company/{self._conf.companyId}/location/bulk", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import ProfileSuccessResponse
        schema = ProfileSuccessResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for createLocationBulk")
            print(e)

        

        return response
    

