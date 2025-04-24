"""Catalog Public Client"""

from urllib.parse import urlparse
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PublicConfig import PublicConfig

from .validator import CatalogValidator

class Catalog:
    def __init__(self, config: PublicConfig):
        self._conf = config
        self._relativeUrls = {
            "getTaxonomyByLevel": "/service/public/catalog/v1.0/taxonomy/level/{level}"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getTaxonomyByLevel(self, level=None, l0_slug=None, l1_slug=None, l2_slug=None, l3_slug=None, limit=None, body="", request_headers:Dict={}):
        """Get Taxonomy Details for a given level
        :param level : The level of taxonomy hierarchy to fetch: 0: Fetch departments. 1: Fetch L1 categories. 2: Fetch L2 categories. 3: Fetch L3 categories. : type integer
        :param l0_slug : Level 0 (Department) slug of the taxonomy to filter results.  : type string
        :param l1_slug : Level 1 (L1 Category) slug of the taxonomy to filter results.  : type string
        :param l2_slug : Level 2 (L2 Category) slug of the taxonomy to filter results.  : type string
        :param l3_slug : Level 3 (L3 Category) slug of the taxonomy to filter results.  : type string
        :param limit : Applied limit on the number of items to be returned. Default is 5000. : type number
        """
        payload = {}
        
        if level is not None:
            payload["level"] = level
        if l0_slug is not None:
            payload["l0_slug"] = l0_slug
        if l1_slug is not None:
            payload["l1_slug"] = l1_slug
        if l2_slug is not None:
            payload["l2_slug"] = l2_slug
        if l3_slug is not None:
            payload["l3_slug"] = l3_slug
        if limit is not None:
            payload["limit"] = limit

        # Parameter validation
        schema = CatalogValidator.getTaxonomyByLevel()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getTaxonomyByLevel"], proccessed_params="""{"required":[{"in":"path","name":"level","required":true,"schema":{"type":"integer","enum":[0,1,2,3]},"description":"The level of taxonomy hierarchy to fetch: 0: Fetch departments. 1: Fetch L1 categories. 2: Fetch L2 categories. 3: Fetch L3 categories."}],"optional":[{"in":"query","name":"l0_slug","schema":{"type":"string"},"description":"Level 0 (Department) slug of the taxonomy to filter results. "},{"in":"query","name":"l1_slug","schema":{"type":"string"},"description":"Level 1 (L1 Category) slug of the taxonomy to filter results. "},{"in":"query","name":"l2_slug","schema":{"type":"string"},"description":"Level 2 (L2 Category) slug of the taxonomy to filter results. "},{"in":"query","name":"l3_slug","schema":{"type":"string"},"description":"Level 3 (L3 Category) slug of the taxonomy to filter results. "},{"in":"query","name":"limit","schema":{"type":"number"},"description":"Applied limit on the number of items to be returned. Default is 5000."}],"query":[{"in":"query","name":"l0_slug","schema":{"type":"string"},"description":"Level 0 (Department) slug of the taxonomy to filter results. "},{"in":"query","name":"l1_slug","schema":{"type":"string"},"description":"Level 1 (L1 Category) slug of the taxonomy to filter results. "},{"in":"query","name":"l2_slug","schema":{"type":"string"},"description":"Level 2 (L2 Category) slug of the taxonomy to filter results. "},{"in":"query","name":"l3_slug","schema":{"type":"string"},"description":"Level 3 (L3 Category) slug of the taxonomy to filter results. "},{"in":"query","name":"limit","schema":{"type":"number"},"description":"Applied limit on the number of items to be returned. Default is 5000."}],"headers":[],"path":[{"in":"path","name":"level","required":true,"schema":{"type":"integer","enum":[0,1,2,3]},"description":"The level of taxonomy hierarchy to fetch: 0: Fetch departments. 1: Fetch L1 categories. 2: Fetch L2 categories. 3: Fetch L3 categories."}]}""", serverType="public", level=level, l0_slug=l0_slug, l1_slug=l1_slug, l2_slug=l2_slug, l3_slug=l3_slug, limit=limit)
        query_string = await create_query_string(l0_slug=l0_slug, l1_slug=l1_slug, l2_slug=l2_slug, l3_slug=l3_slug, limit=limit)
        if query_string:
            url_with_params += "?" + query_string

        headers = {
            "User-Agent": self._conf.userAgent,
            "Accept-Language": self._conf.language,
            "x-currency-code":   self._conf.currency
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getTaxonomyByLevel"]).netloc, "get", await create_url_without_domain("/service/public/catalog/v1.0/taxonomy/level/{level}", level=level, l0_slug=l0_slug, l1_slug=l1_slug, l2_slug=l2_slug, l3_slug=l3_slug, limit=limit), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TaxonomyResponseSchema
            schema = TaxonomyResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getTaxonomyByLevel")
                print(e)

        return response
    