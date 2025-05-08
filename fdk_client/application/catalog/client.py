"""Catalog Application Client"""

import base64
import ujson
from urllib.parse import urlparse
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..ApplicationConfig import ApplicationConfig

from .validator import CatalogValidator

class Catalog:
    def __init__(self, config: ApplicationConfig):
        self._conf = config
        self._relativeUrls = {
            "getProductDetailBySlug": "/service/application/catalog/v1.0/products/{slug}/",
            "getProductSizesBySlug": "/service/application/catalog/v1.0/products/{slug}/sizes/",
            "getProductComparisonBySlugs": "/service/application/catalog/v1.0/products/compare/",
            "getSimilarComparisonProductBySlug": "/service/application/catalog/v1.0/products/{slug}/similar/compare/",
            "getComparedFrequentlyProductBySlug": "/service/application/catalog/v1.0/products/{slug}/similar/compared-frequently/",
            "getProductVariantsBySlug": "/service/application/catalog/v1.0/products/{slug}/variants/",
            "getProductStockByIds": "/service/application/catalog/v1.0/products/stock-status/",
            "getProductStockForTimeByIds": "/service/application/catalog/v1.0/products/stock-status/poll/",
            "getProducts": "/service/application/catalog/v1.0/products/",
            "getBrands": "/service/application/catalog/v1.0/brands/",
            "getBrandDetailBySlug": "/service/application/catalog/v1.0/brands/{slug}/",
            "getCategories": "/service/application/catalog/v1.0/categories/",
            "getCategoryDetailBySlug": "/service/application/catalog/v1.0/categories/{slug}/",
            "getHomeProducts": "/service/application/catalog/v1.0/home/listing/",
            "getDepartments": "/service/application/catalog/v1.0/departments/",
            "getSearchResults": "/service/application/catalog/v1.0/auto-complete/",
            "getCollections": "/service/application/catalog/v1.0/collections/",
            "getCollectionItemsBySlug": "/service/application/catalog/v1.0/collections/{slug}/items/",
            "getCollectionDetailBySlug": "/service/application/catalog/v1.0/collections/{slug}/",
            "getFollowedListing": "/service/application/catalog/v1.0/follow/{collection_type}/",
            "unfollowById": "/service/application/catalog/v1.0/follow/{collection_type}/{collection_id}/",
            "followById": "/service/application/catalog/v1.0/follow/{collection_type}/{collection_id}/",
            "getFollowerCountById": "/service/application/catalog/v1.0/follow/{collection_type}/{collection_id}/count/",
            "getFollowIds": "/service/application/catalog/v1.0/follow/ids/",
            "getStores": "/service/application/catalog/v1.0/locations/",
            "getInStockLocations": "/service/application/catalog/v1.0/in-stock/locations/",
            "getLocationDetailsById": "/service/application/catalog/v1.0/locations/{location_id}/",
            "getProductBundlesBySlug": "/service/application/catalog/v1.0/product-grouping/",
            "getProductPriceBySlug": "/service/application/catalog/v3.0/products/{slug}/sizes/{size}/price/",
            "getProductsServiceability": "/service/application/catalog/v1.0/products/serviceability",
            "getProductSellersBySlug": "/service/application/catalog/v3.0/products/{slug}/sizes/{size}/sellers/"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getProductDetailBySlug(self, slug=None, body="", request_headers:Dict={}):
        """Get product details such as price, attributes, HSN code, SKU code, etc.
        :param slug : A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = CatalogValidator.getProductDetailBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getProductDetailBySlug"], proccessed_params="""{"required":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/.","schema":{"type":"string"},"required":true}]}""", serverType="application", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getProductDetailBySlug"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/products/{slug}/", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductDetail
            schema = ProductDetail()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getProductDetailBySlug")
                print(e)

        return response
    
    async def getProductSizesBySlug(self, slug=None, store_id=None, body="", request_headers:Dict={}):
        """Provides detailed information about a product, including its availability (sellable), available sizes with quantities, dimensions, weight, availability status, price details (marked, effective, selling), minimum order quantity (MOQ).
        :param slug : A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/. : type string
        :param store_id : The ID of the store that is selling the product, e.g. 1,2,3. : type integer
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug
        if store_id is not None:
            payload["store_id"] = store_id

        # Parameter validation
        schema = CatalogValidator.getProductSizesBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getProductSizesBySlug"], proccessed_params="""{"required":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"store_id","description":"The ID of the store that is selling the product, e.g. 1,2,3.","schema":{"type":"integer"},"required":false}],"query":[{"in":"query","name":"store_id","description":"The ID of the store that is selling the product, e.g. 1,2,3.","schema":{"type":"integer"},"required":false}],"headers":[],"path":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/.","schema":{"type":"string"},"required":true}]}""", serverType="application", slug=slug, store_id=store_id)
        query_string = await create_query_string(store_id=store_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getProductSizesBySlug"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/products/{slug}/sizes/", slug=slug, store_id=store_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductSizes
            schema = ProductSizes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getProductSizesBySlug")
                print(e)

        return response
    
    async def getProductComparisonBySlugs(self, slug=None, body="", request_headers:Dict={}):
        """Get all the products that have the same category.
        :param slug : A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/. : type array
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = CatalogValidator.getProductComparisonBySlugs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getProductComparisonBySlugs"], proccessed_params="""{"required":[{"in":"query","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/.","schema":{"type":"array","items":{"type":"string"},"minItems":1},"required":true}],"optional":[],"query":[{"in":"query","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/.","schema":{"type":"array","items":{"type":"string"},"minItems":1},"required":true}],"headers":[],"path":[]}""", serverType="application", slug=slug)
        query_string = await create_query_string(slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getProductComparisonBySlugs"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/products/compare/", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductsComparisonResponse
            schema = ProductsComparisonResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getProductComparisonBySlugs")
                print(e)

        return response
    
    async def getSimilarComparisonProductBySlug(self, slug=None, body="", request_headers:Dict={}):
        """Get all products within the same category as the one specified by the provided slug.
        :param slug : A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = CatalogValidator.getSimilarComparisonProductBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getSimilarComparisonProductBySlug"], proccessed_params="""{"required":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/.","schema":{"type":"string"},"required":true}]}""", serverType="application", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getSimilarComparisonProductBySlug"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/products/{slug}/similar/compare/", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductCompareResponse
            schema = ProductCompareResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSimilarComparisonProductBySlug")
                print(e)

        return response
    
    async def getComparedFrequentlyProductBySlug(self, slug=None, body="", request_headers:Dict={}):
        """Get products that are often compared to the product specified by its slug.
        :param slug : A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = CatalogValidator.getComparedFrequentlyProductBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getComparedFrequentlyProductBySlug"], proccessed_params="""{"required":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/.","schema":{"type":"string"},"required":true}]}""", serverType="application", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getComparedFrequentlyProductBySlug"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/products/{slug}/similar/compared-frequently/", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductFrequentlyComparedSimilarResponse
            schema = ProductFrequentlyComparedSimilarResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getComparedFrequentlyProductBySlug")
                print(e)

        return response
    
    async def getProductVariantsBySlug(self, slug=None, body="", request_headers:Dict={}):
        """Get all available variants of a specific product identified by its slug.
        :param slug : A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = CatalogValidator.getProductVariantsBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getProductVariantsBySlug"], proccessed_params="""{"required":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/.","schema":{"type":"string"},"required":true}]}""", serverType="application", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getProductVariantsBySlug"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/products/{slug}/variants/", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductVariantsResponse
            schema = ProductVariantsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getProductVariantsBySlug")
                print(e)

        return response
    
    async def getProductStockByIds(self, item_id=None, alu=None, sku_code=None, ean=None, upc=None, body="", request_headers:Dict={}):
        """Get the current stock status for products identified by their IDs, such as SKU, ALU, EAN, etc.
        :param item_id : The Item ID of the product (Max. 50 allowed). : type string
        :param alu : ALU of the product (limited upto 50 ALU identifier in a single request). : type string
        :param sku_code : Stock-keeping Unit of the product (limited upto 50 SKU Code in a single request). : type string
        :param ean : European Article Number of the product (limited upto 50 EAN identifier in a single request). : type string
        :param upc : Universal Product Code of the product (limited upto 50 UPC identifier in a single request). : type string
        """
        payload = {}
        
        if item_id is not None:
            payload["item_id"] = item_id
        if alu is not None:
            payload["alu"] = alu
        if sku_code is not None:
            payload["sku_code"] = sku_code
        if ean is not None:
            payload["ean"] = ean
        if upc is not None:
            payload["upc"] = upc

        # Parameter validation
        schema = CatalogValidator.getProductStockByIds()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getProductStockByIds"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"item_id","description":"The Item ID of the product (Max. 50 allowed).","schema":{"type":"string"},"required":false},{"in":"query","name":"alu","description":"ALU of the product (limited upto 50 ALU identifier in a single request).","schema":{"type":"string"},"required":false},{"in":"query","name":"sku_code","description":"Stock-keeping Unit of the product (limited upto 50 SKU Code in a single request).","schema":{"type":"string"},"required":false},{"in":"query","name":"ean","description":"European Article Number of the product (limited upto 50 EAN identifier in a single request).","schema":{"type":"string"},"required":false},{"in":"query","name":"upc","description":"Universal Product Code of the product (limited upto 50 UPC identifier in a single request).","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"item_id","description":"The Item ID of the product (Max. 50 allowed).","schema":{"type":"string"},"required":false},{"in":"query","name":"alu","description":"ALU of the product (limited upto 50 ALU identifier in a single request).","schema":{"type":"string"},"required":false},{"in":"query","name":"sku_code","description":"Stock-keeping Unit of the product (limited upto 50 SKU Code in a single request).","schema":{"type":"string"},"required":false},{"in":"query","name":"ean","description":"European Article Number of the product (limited upto 50 EAN identifier in a single request).","schema":{"type":"string"},"required":false},{"in":"query","name":"upc","description":"Universal Product Code of the product (limited upto 50 UPC identifier in a single request).","schema":{"type":"string"},"required":false}],"headers":[],"path":[]}""", serverType="application", item_id=item_id, alu=alu, sku_code=sku_code, ean=ean, upc=upc)
        query_string = await create_query_string(item_id=item_id, alu=alu, sku_code=sku_code, ean=ean, upc=upc)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getProductStockByIds"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/products/stock-status/", item_id=item_id, alu=alu, sku_code=sku_code, ean=ean, upc=upc), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductStockStatusResponse
            schema = ProductStockStatusResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getProductStockByIds")
                print(e)

        return response
    
    async def getProductStockForTimeByIds(self, timestamp=None, page_size=None, page_id=None, body="", request_headers:Dict={}):
        """Get the available stock levels for all products associated with a particular sales channel at a specified future time.
        :param timestamp : Timestamp in UTC format (2020-07-23T10:27:50Z). : type string
        :param page_size : The number of items to retrieve in each page. : type integer
        :param page_id : Page ID to retrieve next set of results. : type string
        """
        payload = {}
        
        if timestamp is not None:
            payload["timestamp"] = timestamp
        if page_size is not None:
            payload["page_size"] = page_size
        if page_id is not None:
            payload["page_id"] = page_id

        # Parameter validation
        schema = CatalogValidator.getProductStockForTimeByIds()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getProductStockForTimeByIds"], proccessed_params="""{"required":[{"in":"query","name":"timestamp","description":"Timestamp in UTC format (2020-07-23T10:27:50Z).","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"page_id","description":"Page ID to retrieve next set of results.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"timestamp","description":"Timestamp in UTC format (2020-07-23T10:27:50Z).","schema":{"type":"string"},"required":true},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"page_id","description":"Page ID to retrieve next set of results.","schema":{"type":"string"},"required":false}],"headers":[],"path":[]}""", serverType="application", timestamp=timestamp, page_size=page_size, page_id=page_id)
        query_string = await create_query_string(timestamp=timestamp, page_size=page_size, page_id=page_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getProductStockForTimeByIds"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/products/stock-status/poll/", timestamp=timestamp, page_size=page_size, page_id=page_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductStockPolling
            schema = ProductStockPolling()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getProductStockForTimeByIds")
                print(e)

        return response
    
    async def getProducts(self, q=None, f=None, filters=None, sort_on=None, page_id=None, page_size=None, page_no=None, page_type=None, body="", request_headers:Dict={}):
        """List all products available in the catalog. It supports filtering based on product name, brand, department, category, collection, and more, while also offering sorting options based on factors like price, ratings, discounts, and other relevant criteria.
        :param q : The search query for entering partial or full name of product, brand, category, or collection. : type string
        :param f : The search filter parameters. Filter parameters will be passed in f parameter as shown in the example below. Double Pipe (||) denotes the OR condition, whereas Triple-colon (:::) indicates a new filter parameter applied as an AND condition. : type string
        :param filters : True for fetching all filter parameters and False for disabling the filter parameters. : type boolean
        :param sort_on : The order in which the list of products should be sorted, e.g. popularity, price, latest and discount, in either ascending or descending order. See the supported values below. : type string
        :param page_id : Page ID to retrieve next set of results. : type string
        :param page_size : The number of items to retrieve in each page. : type integer
        :param page_no : The page number to navigate through the given set of results. : type integer
        :param page_type : Available pagination types are cursor or number. : type string
        """
        payload = {}
        
        if q is not None:
            payload["q"] = q
        if f is not None:
            payload["f"] = f
        if filters is not None:
            payload["filters"] = filters
        if sort_on is not None:
            payload["sort_on"] = sort_on
        if page_id is not None:
            payload["page_id"] = page_id
        if page_size is not None:
            payload["page_size"] = page_size
        if page_no is not None:
            payload["page_no"] = page_no
        if page_type is not None:
            payload["page_type"] = page_type

        # Parameter validation
        schema = CatalogValidator.getProducts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getProducts"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"q","description":"The search query for entering partial or full name of product, brand, category, or collection.","schema":{"type":"string"},"required":false},{"in":"query","name":"f","description":"The search filter parameters. Filter parameters will be passed in f parameter as shown in the example below. Double Pipe (||) denotes the OR condition, whereas Triple-colon (:::) indicates a new filter parameter applied as an AND condition.","schema":{"type":"string","example":"brand:voi-jeans||reliance:::l3_categories:t-shirts||shirts"},"required":false},{"in":"query","name":"filters","description":"True for fetching all filter parameters and False for disabling the filter parameters.","schema":{"type":"boolean","default":true},"required":false},{"in":"query","name":"sort_on","description":"The order in which the list of products should be sorted, e.g. popularity, price, latest and discount, in either ascending or descending order. See the supported values below.","schema":{"type":"string","enum":["latest","popular","price_asc","price_dsc","discount_asc","discount_dsc"]},"required":false},{"in":"query","name":"page_id","description":"Page ID to retrieve next set of results.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_type","description":"Available pagination types are cursor or number.","schema":{"type":"string","default":"cursor"},"required":false}],"query":[{"in":"query","name":"q","description":"The search query for entering partial or full name of product, brand, category, or collection.","schema":{"type":"string"},"required":false},{"in":"query","name":"f","description":"The search filter parameters. Filter parameters will be passed in f parameter as shown in the example below. Double Pipe (||) denotes the OR condition, whereas Triple-colon (:::) indicates a new filter parameter applied as an AND condition.","schema":{"type":"string","example":"brand:voi-jeans||reliance:::l3_categories:t-shirts||shirts"},"required":false},{"in":"query","name":"filters","description":"True for fetching all filter parameters and False for disabling the filter parameters.","schema":{"type":"boolean","default":true},"required":false},{"in":"query","name":"sort_on","description":"The order in which the list of products should be sorted, e.g. popularity, price, latest and discount, in either ascending or descending order. See the supported values below.","schema":{"type":"string","enum":["latest","popular","price_asc","price_dsc","discount_asc","discount_dsc"]},"required":false},{"in":"query","name":"page_id","description":"Page ID to retrieve next set of results.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_type","description":"Available pagination types are cursor or number.","schema":{"type":"string","default":"cursor"},"required":false}],"headers":[],"path":[]}""", serverType="application", q=q, f=f, filters=filters, sort_on=sort_on, page_id=page_id, page_size=page_size, page_no=page_no, page_type=page_type)
        query_string = await create_query_string(q=q, f=f, filters=filters, sort_on=sort_on, page_id=page_id, page_size=page_size, page_no=page_no, page_type=page_type)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getProducts"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/products/", q=q, f=f, filters=filters, sort_on=sort_on, page_id=page_id, page_size=page_size, page_no=page_no, page_type=page_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductListingResponse
            schema = ProductListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getProducts")
                print(e)

        return response
    
    async def getBrands(self, department=None, page_no=None, page_size=None, body="", request_headers:Dict={}):
        """Get a list of all the available brands. Filtering can be applied to the department.
        :param department : The name of the department. Use this parameter to filter products by a particular department. See the list of available departments below. Also, you can get available departments from the endpoint /service/application/catalog/v1.0/departments/. : type string
        :param page_no : The page number to navigate through the given set of results. : type integer
        :param page_size : The number of items to retrieve in each page. : type integer
        """
        payload = {}
        
        if department is not None:
            payload["department"] = department
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = CatalogValidator.getBrands()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getBrands"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"department","description":"The name of the department. Use this parameter to filter products by a particular department. See the list of available departments below. Also, you can get available departments from the endpoint /service/application/catalog/v1.0/departments/.","schema":{"type":"string","enum":["baby-care-kids-essentials","beauty-personal-care","home-living","fashion","others","toys"]},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false}],"query":[{"in":"query","name":"department","description":"The name of the department. Use this parameter to filter products by a particular department. See the list of available departments below. Also, you can get available departments from the endpoint /service/application/catalog/v1.0/departments/.","schema":{"type":"string","enum":["baby-care-kids-essentials","beauty-personal-care","home-living","fashion","others","toys"]},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false}],"headers":[],"path":[]}""", serverType="application", department=department, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(department=department, page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getBrands"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/brands/", department=department, page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BrandListingResponse
            schema = BrandListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBrands")
                print(e)

        return response
    
    async def getBrandDetailBySlug(self, slug=None, body="", request_headers:Dict={}):
        """Get metadata of a brand such as name, information, logo, banner, etc.
        :param slug : A short, human-readable, URL-friendly identifier of a brand. You can get slug value from the endpoint /service/application/catalog/v1.0/brands/. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = CatalogValidator.getBrandDetailBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getBrandDetailBySlug"], proccessed_params="""{"required":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a brand. You can get slug value from the endpoint /service/application/catalog/v1.0/brands/.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a brand. You can get slug value from the endpoint /service/application/catalog/v1.0/brands/.","schema":{"type":"string"},"required":true}]}""", serverType="application", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getBrandDetailBySlug"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/brands/{slug}/", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BrandDetailResponse
            schema = BrandDetailResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBrandDetailBySlug")
                print(e)

        return response
    
    async def getCategories(self, department=None, body="", request_headers:Dict={}):
        """List all available product categories. Also, users can filter the categories by department.
        :param department : The name of the department. Use this parameter to filter products by a particular department. See the list of available departments below. Also, you can get available departments from the endpoint /service/application/catalog/v1.0/departments/. : type string
        """
        payload = {}
        
        if department is not None:
            payload["department"] = department

        # Parameter validation
        schema = CatalogValidator.getCategories()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCategories"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"department","description":"The name of the department. Use this parameter to filter products by a particular department. See the list of available departments below. Also, you can get available departments from the endpoint /service/application/catalog/v1.0/departments/.","schema":{"type":"string","enum":["baby-care-kids-essentials","beauty-personal-care","home-living","fashion","others","toys"]},"required":false}],"query":[{"in":"query","name":"department","description":"The name of the department. Use this parameter to filter products by a particular department. See the list of available departments below. Also, you can get available departments from the endpoint /service/application/catalog/v1.0/departments/.","schema":{"type":"string","enum":["baby-care-kids-essentials","beauty-personal-care","home-living","fashion","others","toys"]},"required":false}],"headers":[],"path":[]}""", serverType="application", department=department)
        query_string = await create_query_string(department=department)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCategories"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/categories/", department=department), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CategoryListingResponse
            schema = CategoryListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCategories")
                print(e)

        return response
    
    async def getCategoryDetailBySlug(self, slug=None, body="", request_headers:Dict={}):
        """Get detailed information about a specific product category using its slug and get metadata of a category such as name, information, logo, banner, etc.
        :param slug : A short, human-readable, URL-friendly identifier of a brand. You can get slug value from the endpoint /service/application/catalog/v1.0/brands/. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = CatalogValidator.getCategoryDetailBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCategoryDetailBySlug"], proccessed_params="""{"required":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a brand. You can get slug value from the endpoint /service/application/catalog/v1.0/brands/.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a brand. You can get slug value from the endpoint /service/application/catalog/v1.0/brands/.","schema":{"type":"string"},"required":true}]}""", serverType="application", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCategoryDetailBySlug"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/categories/{slug}/", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CategoryMetaResponse
            schema = CategoryMetaResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCategoryDetailBySlug")
                print(e)

        return response
    
    async def getHomeProducts(self, sort_on=None, page_id=None, page_size=None, body="", request_headers:Dict={}):
        """List all the products associated with a brand, collection or category in a random order.
        :param sort_on : The order in which the list of products should be sorted, e.g. popularity, price, latest and discount, in either ascending or descending order. : type string
        :param page_id : Page ID to retrieve next set of results. : type string
        :param page_size : The number of items to retrieve in each page. : type integer
        """
        payload = {}
        
        if sort_on is not None:
            payload["sort_on"] = sort_on
        if page_id is not None:
            payload["page_id"] = page_id
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = CatalogValidator.getHomeProducts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getHomeProducts"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"sort_on","description":"The order in which the list of products should be sorted, e.g. popularity, price, latest and discount, in either ascending or descending order.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_id","description":"Page ID to retrieve next set of results.","schema":{"type":"string","default":"1"},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false}],"query":[{"in":"query","name":"sort_on","description":"The order in which the list of products should be sorted, e.g. popularity, price, latest and discount, in either ascending or descending order.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_id","description":"Page ID to retrieve next set of results.","schema":{"type":"string","default":"1"},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false}],"headers":[],"path":[]}""", serverType="application", sort_on=sort_on, page_id=page_id, page_size=page_size)
        query_string = await create_query_string(sort_on=sort_on, page_id=page_id, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getHomeProducts"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/home/listing/", sort_on=sort_on, page_id=page_id, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import HomeListingResponse
            schema = HomeListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getHomeProducts")
                print(e)

        return response
    
    async def getDepartments(self, body="", request_headers:Dict={}):
        """List all departments associated with available products.
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getDepartments()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getDepartments"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getDepartments"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/departments/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DepartmentResponse
            schema = DepartmentResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDepartments")
                print(e)

        return response
    
    async def getSearchResults(self, q=None, body="", request_headers:Dict={}):
        """Get products, brands, or categories based on a search query, which can be a partial or full name match.
        :param q : The search query for entering partial or full name of a product, brand or category. For example, if the given search query `q` is _ski_, the relevant search suggestions could be _skirt_, _ski shoes_, __skin cream_ etc. : type string
        """
        payload = {}
        
        if q is not None:
            payload["q"] = q

        # Parameter validation
        schema = CatalogValidator.getSearchResults()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getSearchResults"], proccessed_params="""{"required":[{"in":"query","name":"q","description":"The search query for entering partial or full name of a product, brand or category. For example, if the given search query `q` is _ski_, the relevant search suggestions could be _skirt_, _ski shoes_, __skin cream_ etc.","schema":{"type":"string"},"required":true}],"optional":[],"query":[{"in":"query","name":"q","description":"The search query for entering partial or full name of a product, brand or category. For example, if the given search query `q` is _ski_, the relevant search suggestions could be _skirt_, _ski shoes_, __skin cream_ etc.","schema":{"type":"string"},"required":true}],"headers":[],"path":[]}""", serverType="application", q=q)
        query_string = await create_query_string(q=q)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getSearchResults"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/auto-complete/", q=q), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AutoCompleteResponse
            schema = AutoCompleteResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSearchResults")
                print(e)

        return response
    
    async def getCollections(self, page_no=None, page_size=None, tag=None, q=None, body="", request_headers:Dict={}):
        """List of curated product collections with filtering options based on tags and collection names.
        :param page_no : The page number to navigate through the given set of results. : type integer
        :param page_size : The number of items to retrieve in each page. : type integer
        :param tag : List of tags  to filter collections. : type array
        :param q : Name of the collection to filter collection. : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if tag is not None:
            payload["tag"] = tag
        if q is not None:
            payload["q"] = q

        # Parameter validation
        schema = CatalogValidator.getCollections()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCollections"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"tag","description":"List of tags  to filter collections.","schema":{"type":"array","items":{"type":"string"},"minItems":1},"required":false},{"in":"query","name":"q","description":"Name of the collection to filter collection.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"tag","description":"List of tags  to filter collections.","schema":{"type":"array","items":{"type":"string"},"minItems":1},"required":false},{"in":"query","name":"q","description":"Name of the collection to filter collection.","schema":{"type":"string"},"required":false}],"headers":[],"path":[]}""", serverType="application", page_no=page_no, page_size=page_size, tag=tag, q=q)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, tag=tag, q=q)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCollections"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/collections/", page_no=page_no, page_size=page_size, tag=tag, q=q), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetCollectionListingResponse
            schema = GetCollectionListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCollections")
                print(e)

        return response
    
    async def getCollectionItemsBySlug(self, slug=None, f=None, q=None, filters=None, sort_on=None, page_id=None, page_size=None, page_no=None, page_type=None, body="", request_headers:Dict={}):
        """Fetch items within a particular collection identified by its slug.
        :param slug : A short, human-readable, URL-friendly identifier of a collection. You can get slug value from the endpoint /service/application/catalog/v1.0/collections/. : type string
        :param f : The search filter parameters. Filter parameters will be passed in f parameter as shown in the example below. Double Pipe (||) denotes the OR condition, whereas Triple-colon (:::) indicates a new filter parameter applied as an AND condition. : type string
        :param q : The search query for entering partial or full name of product, brand, category, or collection. : type string
        :param filters : True for fetching all filter parameters and False for disabling the filter parameters. : type boolean
        :param sort_on : The order in which the list of products should be sorted, e.g. popularity, price, latest and discount, in either ascending or descending order. See the supported values below. : type string
        :param page_id : Page ID to retrieve next set of results. : type string
        :param page_size : The number of items to retrieve in each page. : type integer
        :param page_no : Page Number to retrieve next set of results. : type integer
        :param page_type : Page Type to retrieve set of results can be cursor or number. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug
        if f is not None:
            payload["f"] = f
        if q is not None:
            payload["q"] = q
        if filters is not None:
            payload["filters"] = filters
        if sort_on is not None:
            payload["sort_on"] = sort_on
        if page_id is not None:
            payload["page_id"] = page_id
        if page_size is not None:
            payload["page_size"] = page_size
        if page_no is not None:
            payload["page_no"] = page_no
        if page_type is not None:
            payload["page_type"] = page_type

        # Parameter validation
        schema = CatalogValidator.getCollectionItemsBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCollectionItemsBySlug"], proccessed_params="""{"required":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a collection. You can get slug value from the endpoint /service/application/catalog/v1.0/collections/.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"f","description":"The search filter parameters. Filter parameters will be passed in f parameter as shown in the example below. Double Pipe (||) denotes the OR condition, whereas Triple-colon (:::) indicates a new filter parameter applied as an AND condition.","schema":{"type":"string","example":"brand:voi-jeans||reliance:::l3_categories:t-shirts||shirts"},"required":false},{"in":"query","name":"q","description":"The search query for entering partial or full name of product, brand, category, or collection.","schema":{"type":"string","example":"shirts"},"required":false},{"in":"query","name":"filters","description":"True for fetching all filter parameters and False for disabling the filter parameters.","schema":{"type":"boolean","default":true},"required":false},{"in":"query","name":"sort_on","description":"The order in which the list of products should be sorted, e.g. popularity, price, latest and discount, in either ascending or descending order. See the supported values below.","schema":{"type":"string","enum":["latest","popular","price_asc","price_dsc","discount_asc","discount_dsc"]},"required":false},{"in":"query","name":"page_id","description":"Page ID to retrieve next set of results.","schema":{"type":"string","default":"1"},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"page_no","description":"Page Number to retrieve next set of results.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_type","description":"Page Type to retrieve set of results can be cursor or number.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"f","description":"The search filter parameters. Filter parameters will be passed in f parameter as shown in the example below. Double Pipe (||) denotes the OR condition, whereas Triple-colon (:::) indicates a new filter parameter applied as an AND condition.","schema":{"type":"string","example":"brand:voi-jeans||reliance:::l3_categories:t-shirts||shirts"},"required":false},{"in":"query","name":"q","description":"The search query for entering partial or full name of product, brand, category, or collection.","schema":{"type":"string","example":"shirts"},"required":false},{"in":"query","name":"filters","description":"True for fetching all filter parameters and False for disabling the filter parameters.","schema":{"type":"boolean","default":true},"required":false},{"in":"query","name":"sort_on","description":"The order in which the list of products should be sorted, e.g. popularity, price, latest and discount, in either ascending or descending order. See the supported values below.","schema":{"type":"string","enum":["latest","popular","price_asc","price_dsc","discount_asc","discount_dsc"]},"required":false},{"in":"query","name":"page_id","description":"Page ID to retrieve next set of results.","schema":{"type":"string","default":"1"},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"page_no","description":"Page Number to retrieve next set of results.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_type","description":"Page Type to retrieve set of results can be cursor or number.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a collection. You can get slug value from the endpoint /service/application/catalog/v1.0/collections/.","schema":{"type":"string"},"required":true}]}""", serverType="application", slug=slug, f=f, q=q, filters=filters, sort_on=sort_on, page_id=page_id, page_size=page_size, page_no=page_no, page_type=page_type)
        query_string = await create_query_string(f=f, q=q, filters=filters, sort_on=sort_on, page_id=page_id, page_size=page_size, page_no=page_no, page_type=page_type)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCollectionItemsBySlug"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/collections/{slug}/items/", slug=slug, f=f, q=q, filters=filters, sort_on=sort_on, page_id=page_id, page_size=page_size, page_no=page_no, page_type=page_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductListingResponse
            schema = ProductListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCollectionItemsBySlug")
                print(e)

        return response
    
    async def getCollectionDetailBySlug(self, slug=None, body="", request_headers:Dict={}):
        """Get detailed information about a specific collection using its slug.
        :param slug : A short, human-readable, URL-friendly identifier of a collection. You can get slug value from the endpoint /service/application/catalog/v1.0/collections/. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = CatalogValidator.getCollectionDetailBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCollectionDetailBySlug"], proccessed_params="""{"required":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a collection. You can get slug value from the endpoint /service/application/catalog/v1.0/collections/.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a collection. You can get slug value from the endpoint /service/application/catalog/v1.0/collections/.","schema":{"type":"string"},"required":true}]}""", serverType="application", slug=slug)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCollectionDetailBySlug"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/collections/{slug}/", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CollectionDetailResponse
            schema = CollectionDetailResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCollectionDetailBySlug")
                print(e)

        return response
    
    async def getFollowedListing(self, collection_type=None, page_id=None, page_size=None, body="", request_headers:Dict={}):
        """Get a list of products or brands the user is following.
        :param collection_type : Type of collection followed, i.e. products, brands, or collections. : type string
        :param page_id : Page ID to retrieve next set of results. : type string
        :param page_size : Page ID to retrieve next set of results. : type integer
        """
        payload = {}
        
        if collection_type is not None:
            payload["collection_type"] = collection_type
        if page_id is not None:
            payload["page_id"] = page_id
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = CatalogValidator.getFollowedListing()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getFollowedListing"], proccessed_params="""{"required":[{"in":"path","name":"collection_type","description":"Type of collection followed, i.e. products, brands, or collections.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_id","description":"Page ID to retrieve next set of results.","schema":{"type":"string","default":"1"},"required":false},{"in":"query","name":"page_size","description":"Page ID to retrieve next set of results.","schema":{"type":"integer","default":12},"required":false}],"query":[{"in":"query","name":"page_id","description":"Page ID to retrieve next set of results.","schema":{"type":"string","default":"1"},"required":false},{"in":"query","name":"page_size","description":"Page ID to retrieve next set of results.","schema":{"type":"integer","default":12},"required":false}],"headers":[],"path":[{"in":"path","name":"collection_type","description":"Type of collection followed, i.e. products, brands, or collections.","schema":{"type":"string"},"required":true}]}""", serverType="application", collection_type=collection_type, page_id=page_id, page_size=page_size)
        query_string = await create_query_string(page_id=page_id, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getFollowedListing"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/follow/{collection_type}/", collection_type=collection_type, page_id=page_id, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetFollowListingResponse
            schema = GetFollowListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getFollowedListing")
                print(e)

        return response
    
    async def unfollowById(self, collection_type=None, collection_id=None, body="", request_headers:Dict={}):
        """Remove a followed item, brand, or product using its collection ID.
        :param collection_type : Type of collection followed, i.e. products, brands, or collections. : type string
        :param collection_id : The ID of the collection type. : type string
        """
        payload = {}
        
        if collection_type is not None:
            payload["collection_type"] = collection_type
        if collection_id is not None:
            payload["collection_id"] = collection_id

        # Parameter validation
        schema = CatalogValidator.unfollowById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["unfollowById"], proccessed_params="""{"required":[{"in":"path","name":"collection_type","description":"Type of collection followed, i.e. products, brands, or collections.","schema":{"type":"string"},"required":true},{"in":"path","name":"collection_id","description":"The ID of the collection type.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"collection_type","description":"Type of collection followed, i.e. products, brands, or collections.","schema":{"type":"string"},"required":true},{"in":"path","name":"collection_id","description":"The ID of the collection type.","schema":{"type":"string"},"required":true}]}""", serverType="application", collection_type=collection_type, collection_id=collection_id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["unfollowById"]).netloc, "delete", await create_url_without_domain("/service/application/catalog/v1.0/follow/{collection_type}/{collection_id}/", collection_type=collection_type, collection_id=collection_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import FollowPostResponse
            schema = FollowPostResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for unfollowById")
                print(e)

        return response
    
    async def followById(self, collection_type=None, collection_id=None, body="", request_headers:Dict={}):
        """Add a product, brand, or item to the user's followed list by collection Id.
        :param collection_type : Type of collection followed, i.e. products, brands, or collections. : type string
        :param collection_id : The ID of the collection type. : type string
        """
        payload = {}
        
        if collection_type is not None:
            payload["collection_type"] = collection_type
        if collection_id is not None:
            payload["collection_id"] = collection_id

        # Parameter validation
        schema = CatalogValidator.followById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["followById"], proccessed_params="""{"required":[{"in":"path","name":"collection_type","description":"Type of collection followed, i.e. products, brands, or collections.","schema":{"type":"string"},"required":true},{"in":"path","name":"collection_id","description":"The ID of the collection type.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"collection_type","description":"Type of collection followed, i.e. products, brands, or collections.","schema":{"type":"string"},"required":true},{"in":"path","name":"collection_id","description":"The ID of the collection type.","schema":{"type":"string"},"required":true}]}""", serverType="application", collection_type=collection_type, collection_id=collection_id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["followById"]).netloc, "post", await create_url_without_domain("/service/application/catalog/v1.0/follow/{collection_type}/{collection_id}/", collection_type=collection_type, collection_id=collection_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import FollowPostResponse
            schema = FollowPostResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for followById")
                print(e)

        return response
    
    async def getFollowerCountById(self, collection_type=None, collection_id=None, body="", request_headers:Dict={}):
        """Get the total number of followers for a specific item by its ID.
        :param collection_type : Type of collection, i.e. products, brands, or collections. : type string
        :param collection_id : The ID of the collection type. : type string
        """
        payload = {}
        
        if collection_type is not None:
            payload["collection_type"] = collection_type
        if collection_id is not None:
            payload["collection_id"] = collection_id

        # Parameter validation
        schema = CatalogValidator.getFollowerCountById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getFollowerCountById"], proccessed_params="""{"required":[{"in":"path","name":"collection_type","description":"Type of collection, i.e. products, brands, or collections.","schema":{"type":"string"},"required":true},{"in":"path","name":"collection_id","description":"The ID of the collection type.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"collection_type","description":"Type of collection, i.e. products, brands, or collections.","schema":{"type":"string"},"required":true},{"in":"path","name":"collection_id","description":"The ID of the collection type.","schema":{"type":"string"},"required":true}]}""", serverType="application", collection_type=collection_type, collection_id=collection_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getFollowerCountById"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/follow/{collection_type}/{collection_id}/count/", collection_type=collection_type, collection_id=collection_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import FollowerCountResponse
            schema = FollowerCountResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getFollowerCountById")
                print(e)

        return response
    
    async def getFollowIds(self, collection_type=None, body="", request_headers:Dict={}):
        """Get the IDs of all items the user is currently following, such as Products, Brands, and Collections.
        :param collection_type : Type of collection, i.e. products, brands, collections. : type string
        """
        payload = {}
        
        if collection_type is not None:
            payload["collection_type"] = collection_type

        # Parameter validation
        schema = CatalogValidator.getFollowIds()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getFollowIds"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"collection_type","description":"Type of collection, i.e. products, brands, collections.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"collection_type","description":"Type of collection, i.e. products, brands, collections.","schema":{"type":"string"},"required":false}],"headers":[],"path":[]}""", serverType="application", collection_type=collection_type)
        query_string = await create_query_string(collection_type=collection_type)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getFollowIds"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/follow/ids/", collection_type=collection_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import FollowIdsResponse
            schema = FollowIdsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getFollowIds")
                print(e)

        return response
    
    async def getStores(self, page_no=None, page_size=None, q=None, city=None, range=None, latitude=None, longitude=None, tags=None, body="", request_headers:Dict={}):
        """List all stores associated with the sales channel.
        :param page_no : The page number to navigate through the given set of results. : type integer
        :param page_size : Number of items to retrieve in each page. : type integer
        :param q : Search a store by its name or store_code. : type string
        :param city : Search stores by the city in which they are situated. : type string
        :param range : Use this to retrieve stores within a particular range in meters, e.g. 10000, to indicate a 10km range. : type integer
        :param latitude : Latitude of the location from where one wants to retrieve the nearest stores, e.g. 72.8691788. : type number
        :param longitude : Longitude of the location from where one wants to retrieve the nearest stores, e.g. 19.1174114. : type number
        :param tags : Search stores based on tags. : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if q is not None:
            payload["q"] = q
        if city is not None:
            payload["city"] = city
        if range is not None:
            payload["range"] = range
        if latitude is not None:
            payload["latitude"] = latitude
        if longitude is not None:
            payload["longitude"] = longitude
        if tags is not None:
            payload["tags"] = tags

        # Parameter validation
        schema = CatalogValidator.getStores()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getStores"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search a store by its name or store_code.","schema":{"type":"string"},"required":false},{"in":"query","name":"city","description":"Search stores by the city in which they are situated.","schema":{"type":"string"},"required":false},{"in":"query","name":"range","description":"Use this to retrieve stores within a particular range in meters, e.g. 10000, to indicate a 10km range.","schema":{"type":"integer","default":20000},"required":false},{"in":"query","name":"latitude","description":"Latitude of the location from where one wants to retrieve the nearest stores, e.g. 72.8691788.","schema":{"type":"number"},"required":false},{"in":"query","name":"longitude","description":"Longitude of the location from where one wants to retrieve the nearest stores, e.g. 19.1174114.","schema":{"type":"number"},"required":false},{"in":"query","name":"tags","description":"Search stores based on tags.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search a store by its name or store_code.","schema":{"type":"string"},"required":false},{"in":"query","name":"city","description":"Search stores by the city in which they are situated.","schema":{"type":"string"},"required":false},{"in":"query","name":"range","description":"Use this to retrieve stores within a particular range in meters, e.g. 10000, to indicate a 10km range.","schema":{"type":"integer","default":20000},"required":false},{"in":"query","name":"latitude","description":"Latitude of the location from where one wants to retrieve the nearest stores, e.g. 72.8691788.","schema":{"type":"number"},"required":false},{"in":"query","name":"longitude","description":"Longitude of the location from where one wants to retrieve the nearest stores, e.g. 19.1174114.","schema":{"type":"number"},"required":false},{"in":"query","name":"tags","description":"Search stores based on tags.","schema":{"type":"string"},"required":false}],"headers":[],"path":[]}""", serverType="application", page_no=page_no, page_size=page_size, q=q, city=city, range=range, latitude=latitude, longitude=longitude, tags=tags)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q, city=city, range=range, latitude=latitude, longitude=longitude, tags=tags)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getStores"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/locations/", page_no=page_no, page_size=page_size, q=q, city=city, range=range, latitude=latitude, longitude=longitude, tags=tags), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import StoreListingResponse
            schema = StoreListingResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getStores")
                print(e)

        return response
    
    async def getInStockLocations(self, page_no=None, page_size=None, q=None, city=None, range=None, latitude=None, longitude=None, body="", request_headers:Dict={}):
        """List stores where specified products are currently in stock.
        :param page_no : The page number to navigate through the given set of results. : type integer
        :param page_size : Number of items to retrieve in each page. : type integer
        :param q : Search a store by its name or store_code. : type string
        :param city : Search stores by the city in which they are situated. : type string
        :param range : Use this to retrieve stores within a particular range in meters, e.g. 10000, to indicate a 10km range. : type integer
        :param latitude : Latitude of the location from where one wants to retrieve the nearest stores, e.g. 72.8691788. : type number
        :param longitude : Longitude of the location from where one wants to retrieve the nearest stores, e.g. 19.1174114. : type number
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if q is not None:
            payload["q"] = q
        if city is not None:
            payload["city"] = city
        if range is not None:
            payload["range"] = range
        if latitude is not None:
            payload["latitude"] = latitude
        if longitude is not None:
            payload["longitude"] = longitude

        # Parameter validation
        schema = CatalogValidator.getInStockLocations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getInStockLocations"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search a store by its name or store_code.","schema":{"type":"string"},"required":false},{"in":"query","name":"city","description":"Search stores by the city in which they are situated.","schema":{"type":"string"},"required":false},{"in":"query","name":"range","description":"Use this to retrieve stores within a particular range in meters, e.g. 10000, to indicate a 10km range.","schema":{"type":"integer","default":20000},"required":false},{"in":"query","name":"latitude","description":"Latitude of the location from where one wants to retrieve the nearest stores, e.g. 72.8691788.","schema":{"type":"number"},"required":false},{"in":"query","name":"longitude","description":"Longitude of the location from where one wants to retrieve the nearest stores, e.g. 19.1174114.","schema":{"type":"number"},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search a store by its name or store_code.","schema":{"type":"string"},"required":false},{"in":"query","name":"city","description":"Search stores by the city in which they are situated.","schema":{"type":"string"},"required":false},{"in":"query","name":"range","description":"Use this to retrieve stores within a particular range in meters, e.g. 10000, to indicate a 10km range.","schema":{"type":"integer","default":20000},"required":false},{"in":"query","name":"latitude","description":"Latitude of the location from where one wants to retrieve the nearest stores, e.g. 72.8691788.","schema":{"type":"number"},"required":false},{"in":"query","name":"longitude","description":"Longitude of the location from where one wants to retrieve the nearest stores, e.g. 19.1174114.","schema":{"type":"number"},"required":false}],"headers":[],"path":[]}""", serverType="application", page_no=page_no, page_size=page_size, q=q, city=city, range=range, latitude=latitude, longitude=longitude)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q, city=city, range=range, latitude=latitude, longitude=longitude)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getInStockLocations"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/in-stock/locations/", page_no=page_no, page_size=page_size, q=q, city=city, range=range, latitude=latitude, longitude=longitude), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationStoreListing
            schema = ApplicationStoreListing()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getInStockLocations")
                print(e)

        return response
    
    async def getLocationDetailsById(self, location_id=None, body="", request_headers:Dict={}):
        """Get details about a store based on its location Id.
        :param location_id : Unique Location ID. : type integer
        """
        payload = {}
        
        if location_id is not None:
            payload["location_id"] = location_id

        # Parameter validation
        schema = CatalogValidator.getLocationDetailsById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLocationDetailsById"], proccessed_params="""{"required":[{"in":"path","name":"location_id","description":"Unique Location ID.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"location_id","description":"Unique Location ID.","schema":{"type":"integer"},"required":true}]}""", serverType="application", location_id=location_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getLocationDetailsById"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/locations/{location_id}/", location_id=location_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import StoreDetails
            schema = StoreDetails()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getLocationDetailsById")
                print(e)

        return response
    
    async def getProductBundlesBySlug(self, slug=None, id=None, body="", request_headers:Dict={}):
        """Get products bundles to the one specified by its slug.
        :param slug : Product slug for which bundles need to be fetched. : type string
        :param id : Product uid. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CatalogValidator.getProductBundlesBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getProductBundlesBySlug"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"slug","description":"Product slug for which bundles need to be fetched.","schema":{"type":"string"},"required":false},{"in":"query","name":"id","description":"Product uid.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"slug","description":"Product slug for which bundles need to be fetched.","schema":{"type":"string"},"required":false},{"in":"query","name":"id","description":"Product uid.","schema":{"type":"string"},"required":false}],"headers":[],"path":[]}""", serverType="application", slug=slug, id=id)
        query_string = await create_query_string(slug=slug, id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getProductBundlesBySlug"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/product-grouping/", slug=slug, id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductBundle
            schema = ProductBundle()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getProductBundlesBySlug")
                print(e)

        return response
    
    async def getProductPriceBySlug(self, slug=None, size=None, store_id=None, moq=None, body="", request_headers:Dict={}):
        """Get the price of a product size at all the selling locations near to a PIN Code.
        :param slug : A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/. : type string
        :param size : A string indicating the size of the product, e.g. S, M, XL. You can get slug value from the endpoint /service/application/catalog/v1.0/products/sizes. : type string
        :param store_id : The ID of the store that is selling the product, e.g. 1,2,3. : type integer
        :param moq : An Integer indication the Minimum Order Quantity of a product, e.g. 100. : type integer
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug
        if size is not None:
            payload["size"] = size
        if store_id is not None:
            payload["store_id"] = store_id
        if moq is not None:
            payload["moq"] = moq

        # Parameter validation
        schema = CatalogValidator.getProductPriceBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getProductPriceBySlug"], proccessed_params="""{"required":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/.","schema":{"type":"string"},"required":true},{"in":"path","name":"size","description":"A string indicating the size of the product, e.g. S, M, XL. You can get slug value from the endpoint /service/application/catalog/v1.0/products/sizes.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"store_id","description":"The ID of the store that is selling the product, e.g. 1,2,3.","schema":{"type":"integer"},"required":false},{"in":"query","name":"moq","description":"An Integer indication the Minimum Order Quantity of a product, e.g. 100.","schema":{"type":"integer"},"required":false}],"query":[{"in":"query","name":"store_id","description":"The ID of the store that is selling the product, e.g. 1,2,3.","schema":{"type":"integer"},"required":false},{"in":"query","name":"moq","description":"An Integer indication the Minimum Order Quantity of a product, e.g. 100.","schema":{"type":"integer"},"required":false}],"headers":[],"path":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/.","schema":{"type":"string"},"required":true},{"in":"path","name":"size","description":"A string indicating the size of the product, e.g. S, M, XL. You can get slug value from the endpoint /service/application/catalog/v1.0/products/sizes.","schema":{"type":"string"},"required":true}]}""", serverType="application", slug=slug, size=size, store_id=store_id, moq=moq)
        query_string = await create_query_string(store_id=store_id, moq=moq)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getProductPriceBySlug"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v3.0/products/{slug}/sizes/{size}/price/", slug=slug, size=size, store_id=store_id, moq=moq), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductSizePriceResponseV3
            schema = ProductSizePriceResponseV3()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getProductPriceBySlug")
                print(e)

        return response
    
    async def getProductsServiceability(self, body="", request_headers:Dict={}):
        """Get size price for multiple products, For serviceability, with reduced size of response
        """
        payload = {}
        

        # Parameter validation
        schema = CatalogValidator.getProductsServiceability()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ProductSizePriceServiceabilityRequest
        schema = ProductSizePriceServiceabilityRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["getProductsServiceability"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getProductsServiceability"]).netloc, "post", await create_url_without_domain("/service/application/catalog/v1.0/products/serviceability", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductSizePriceServiceabilityResponse
            schema = ProductSizePriceServiceabilityResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getProductsServiceability")
                print(e)

        return response
    
    async def getProductSellersBySlug(self, slug=None, size=None, strategy=None, page_no=None, page_size=None, body="", request_headers:Dict={}):
        """List all sellers offering a specific product identified by its slug and size.
        :param slug : A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/. : type string
        :param size : A string indicating the size of the product, e.g. S, M, XL. You can get slug value from the endpoint /service/application/catalog/v1.0/products/sizes. : type string
        :param strategy : Sort stores on the basis of strategy. eg, fast-delivery, low-price, optimal. : type string
        :param page_no : The page number to navigate through the given set of results. : type integer
        :param page_size : The number of items to retrieve in each page. : type integer
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug
        if size is not None:
            payload["size"] = size
        if strategy is not None:
            payload["strategy"] = strategy
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = CatalogValidator.getProductSellersBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getProductSellersBySlug"], proccessed_params="""{"required":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/.","schema":{"type":"string"},"required":true},{"in":"path","name":"size","description":"A string indicating the size of the product, e.g. S, M, XL. You can get slug value from the endpoint /service/application/catalog/v1.0/products/sizes.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"strategy","description":"Sort stores on the basis of strategy. eg, fast-delivery, low-price, optimal.","schema":{"type":"string"}},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false}],"query":[{"in":"query","name":"strategy","description":"Sort stores on the basis of strategy. eg, fast-delivery, low-price, optimal.","schema":{"type":"string"}},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false}],"headers":[],"path":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/.","schema":{"type":"string"},"required":true},{"in":"path","name":"size","description":"A string indicating the size of the product, e.g. S, M, XL. You can get slug value from the endpoint /service/application/catalog/v1.0/products/sizes.","schema":{"type":"string"},"required":true}]}""", serverType="application", slug=slug, size=size, strategy=strategy, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(strategy=strategy, page_no=page_no, page_size=page_size)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getProductSellersBySlug"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v3.0/products/{slug}/sizes/{size}/sellers/", slug=slug, size=size, strategy=strategy, page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ProductSizeSellersResponseV3
            schema = ProductSizeSellersResponseV3()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getProductSellersBySlug")
                print(e)

        return response
    