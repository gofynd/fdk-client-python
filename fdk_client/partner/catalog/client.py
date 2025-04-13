"""Catalog Partner Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PartnerConfig import PartnerConfig

from .validator import CatalogValidator

class Catalog:
    def __init__(self, config: PartnerConfig):
        self._conf = config

    
    async def partnerCompanyDetails(self, body="", request_headers:Dict={}):
        """This API helps in fetch details of partner companies with the help of uid.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.partnerCompanyDetails()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PartnerCompanyDetailsRequestSchema
        schema = PartnerCompanyDetailsRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/catalog/v2.0/organization/{self._conf.organizationId}/company-details", """{"required":[{"in":"path","name":"organization_id","description":"organization id of an organization.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"organization_id","description":"organization id of an organization.","required":true,"schema":{"type":"string"}}]}""", serverType="partner", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/partner/catalog/v2.0/organization/{self._conf.organizationId}/company-details", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CompaniesSerializer
            schema = CompaniesSerializer()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for partnerCompanyDetails")
                print(e)

        return response
    
    async def getCompanies(self, q=None, stage=None, request_headers:Dict={}):
        """This API allows to view the company profile of the seller account.
        :param q : search string used to search company. : type string
        :param stage : to filter companies on basis of verified or unverified. : type string
        """
        payload = {}
        
        if q is not None:
            payload["q"] = q
        if stage is not None:
            payload["stage"] = stage

        # Parameter validation
        schema = CatalogValidator.getCompanies()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/catalog/v2.0/organization/{self._conf.organizationId}/referred-companies", """{"required":[{"in":"path","name":"organization_id","description":"organization id of an organization.","required":true,"schema":{"type":"string"}}],"optional":[{"in":"query","name":"q","description":"search string used to search company.","required":false,"schema":{"type":"string"}},{"in":"query","name":"stage","description":"to filter companies on basis of verified or unverified.","required":false,"schema":{"type":"string"}}],"query":[{"in":"query","name":"q","description":"search string used to search company.","required":false,"schema":{"type":"string"}},{"in":"query","name":"stage","description":"to filter companies on basis of verified or unverified.","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"organization_id","description":"organization id of an organization.","required":true,"schema":{"type":"string"}}]}""", serverType="partner", q=q, stage=stage)
        query_string = await create_query_string(q=q, stage=stage)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/catalog/v2.0/organization/{self._conf.organizationId}/referred-companies", q=q, stage=stage), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CompanyListSerializer
            schema = CompanyListSerializer()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCompanies")
                print(e)

        return response
    