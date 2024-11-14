from ..common.aiohttp_helper import AiohttpHelper
from ..common.utils import get_headers_with_signature
from urllib import parse
import base64
import ujson

async def custom_request(self, method, url, query={}, body={}, headers={}, client_type=""):
        cookies = None
        url = self.config.domain + url
        query = parse.urlencode(query, doseq=True)
        if query:
            url += "?" + query

        if client_type == 'application' : 
            if self.config.locationDetails:
              headers["x-location-detail"] = ujson.dumps(self.config.locationDetails)
            cookies = self.config.cookies
            headers["Authorization"] = f'Bearer {base64.b64encode(f"{self.config.applicationID}:{self.config.applicationToken}".encode()).decode()}'
        else:
            headers["Authorization"] = f"Bearer {await self.config.getAccessToken()}"
            
        
        for h in self.config.extraHeaders:
            headers.update(h)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        headers_with_signature = get_headers_with_signature(self.config.domain, method, url, query, headers, body, exclude_headers)

        response = await AiohttpHelper().aiohttp_request(method, url, headers=headers_with_signature, data=body, cookies=cookies, debug = (self.config.logLevel=="DEBUG")  )

        return response