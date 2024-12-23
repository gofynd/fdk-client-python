"""AuditTrail Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .validator import AuditTrailValidator

class AuditTrail:
    def __init__(self, config: PlatformConfig):
        self._conf = config

    
    async def createAuditLog(self, body="", request_headers:Dict={}):
        """Generate and record an audit log entry for a specific event or action.
        """
        payload = {}
        

        # Parameter validation
        schema = AuditTrailValidator.createAuditLog()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import RequestBodyAuditLog
        schema = RequestBodyAuditLog()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/audit/logs/create", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"Value for the company ID"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer","description":"Value for the company ID"}}]}""", serverType="platform", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/audit/logs/create", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateLogResp
            schema = CreateLogResp()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createAuditLog")
                print(e)

        return response
    