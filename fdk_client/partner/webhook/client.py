"""Webhook Partner Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PartnerConfig import PartnerConfig

from .validator import WebhookValidator

class Webhook:
    def __init__(self, config: PartnerConfig):
        self._conf = config

    
    async def fetchDeliverySummary(self, extension_id=None, start_date=None, end_date=None, request_headers:Dict={}):
        """Webhook delivery summary
        :param extension_id : extension_id : type string
        :param start_date : start_date : type string
        :param end_date : end_date : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id
        if start_date is not None:
            payload["start_date"] = start_date
        if end_date is not None:
            payload["end_date"] = end_date

        # Parameter validation
        schema = WebhookValidator.fetchDeliverySummary()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/webhook/v1.0/organization/{self._conf.organizationId}/extension/{extension_id}/report/delivery_summary", """{"required":[{"name":"organization_id","in":"path","description":"organization_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}},{"name":"extension_id","in":"path","description":"extension_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}},{"name":"start_date","in":"query","description":"start_date","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"2023-11-01T03:02:51.000Z"}}},{"name":"end_date","in":"query","description":"end_date","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"2023-11-01T03:02:51.000Z"}}}],"optional":[],"query":[{"name":"start_date","in":"query","description":"start_date","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"2023-11-01T03:02:51.000Z"}}},{"name":"end_date","in":"query","description":"end_date","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"2023-11-01T03:02:51.000Z"}}}],"headers":[],"path":[{"name":"organization_id","in":"path","description":"organization_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}},{"name":"extension_id","in":"path","description":"extension_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}}]}""", serverType="partner", extension_id=extension_id, start_date=start_date, end_date=end_date)
        query_string = await create_query_string(extension_id=extension_id, start_date=start_date, end_date=end_date)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/webhook/v1.0/organization/{self._conf.organizationId}/extension/{extension_id}/report/delivery_summary", extension_id=extension_id, start_date=start_date, end_date=end_date), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DeliverySummaryResponse
            schema = DeliverySummaryResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for fetchDeliverySummary")
                print(e)

        return response
    
    async def getDeliveryDetailInsights(self, extension_id=None, body="", request_headers:Dict={}):
        """Get the delivery details insights
        :param extension_id : extension_id : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id

        # Parameter validation
        schema = WebhookValidator.getDeliveryDetailInsights()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DeliveryDetailsRequest
        schema = DeliveryDetailsRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/webhook/v1.0/organization/{self._conf.organizationId}/extension/{extension_id}/report/delivery_details", """{"required":[{"name":"organization_id","in":"path","description":"organization_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}},{"name":"extension_id","in":"path","description":"extension_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"organization_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}},{"name":"extension_id","in":"path","description":"extension_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}}]}""", serverType="partner", extension_id=extension_id)
        query_string = await create_query_string(extension_id=extension_id)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/partner/webhook/v1.0/organization/{self._conf.organizationId}/extension/{extension_id}/report/delivery_details", extension_id=extension_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DeliveryDetailsResponse
            schema = DeliveryDetailsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDeliveryDetailInsights")
                print(e)

        return response
    
    async def fetchDeliveryTs(self, extension_id=None, start_date=None, end_date=None, request_headers:Dict={}):
        """Webhook delivery ts
        :param extension_id : extension_id : type string
        :param start_date : start_date : type string
        :param end_date : end_date : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id
        if start_date is not None:
            payload["start_date"] = start_date
        if end_date is not None:
            payload["end_date"] = end_date

        # Parameter validation
        schema = WebhookValidator.fetchDeliveryTs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/webhook/v1.0/organization/{self._conf.organizationId}/extension/{extension_id}/report/delivery_ts", """{"required":[{"name":"organization_id","in":"path","description":"organization_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}},{"name":"extension_id","in":"path","description":"extension_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}},{"name":"start_date","in":"query","description":"start_date","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"2023-11-01T03:02:51.000Z"}}},{"name":"end_date","in":"query","description":"end_date","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"2023-11-01T03:02:51.000Z"}}}],"optional":[],"query":[{"name":"start_date","in":"query","description":"start_date","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"2023-11-01T03:02:51.000Z"}}},{"name":"end_date","in":"query","description":"end_date","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"2023-11-01T03:02:51.000Z"}}}],"headers":[],"path":[{"name":"organization_id","in":"path","description":"organization_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}},{"name":"extension_id","in":"path","description":"extension_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}}]}""", serverType="partner", extension_id=extension_id, start_date=start_date, end_date=end_date)
        query_string = await create_query_string(extension_id=extension_id, start_date=start_date, end_date=end_date)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/webhook/v1.0/organization/{self._conf.organizationId}/extension/{extension_id}/report/delivery_ts", extension_id=extension_id, start_date=start_date, end_date=end_date), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DeliveryTsResponse
            schema = DeliveryTsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for fetchDeliveryTs")
                print(e)

        return response
    
    async def fetchReportFilters(self, extension_id=None, start_date=None, end_date=None, page_no=None, page_size=None, request_headers:Dict={}):
        """Fetch webhook report filters
        :param extension_id : extension_id : type string
        :param start_date : start_date : type string
        :param end_date : end_date : type string
        :param page_no : page_no : type integer
        :param page_size : page_size : type integer
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id
        if start_date is not None:
            payload["start_date"] = start_date
        if end_date is not None:
            payload["end_date"] = end_date
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size

        # Parameter validation
        schema = WebhookValidator.fetchReportFilters()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/webhook/v1.0/organization/{self._conf.organizationId}/extension/{extension_id}/report/filters", """{"required":[{"name":"organization_id","in":"path","description":"organization_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}},{"name":"extension_id","in":"path","description":"extension_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}},{"name":"start_date","in":"query","description":"start_date","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"2023-11-01T03:02:51.000Z"}}},{"name":"end_date","in":"query","description":"end_date","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"2023-11-01T03:02:51.000Z"}}},{"name":"page_no","in":"query","description":"page_no","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}},{"name":"page_size","in":"query","description":"page_size","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":10}}}],"optional":[],"query":[{"name":"start_date","in":"query","description":"start_date","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"2023-11-01T03:02:51.000Z"}}},{"name":"end_date","in":"query","description":"end_date","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"2023-11-01T03:02:51.000Z"}}},{"name":"page_no","in":"query","description":"page_no","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}},{"name":"page_size","in":"query","description":"page_size","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":10}}}],"headers":[],"path":[{"name":"organization_id","in":"path","description":"organization_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}},{"name":"extension_id","in":"path","description":"extension_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}}]}""", serverType="partner", extension_id=extension_id, start_date=start_date, end_date=end_date, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(extension_id=extension_id, start_date=start_date, end_date=end_date, page_no=page_no, page_size=page_size)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/webhook/v1.0/organization/{self._conf.organizationId}/extension/{extension_id}/report/filters", extension_id=extension_id, start_date=start_date, end_date=end_date, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def cancelReportDownload(self, extension_id=None, filename=None, request_headers:Dict={}):
        """Cancel report download job
        :param extension_id : extension_id : type string
        :param filename : filename : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id
        if filename is not None:
            payload["filename"] = filename

        # Parameter validation
        schema = WebhookValidator.cancelReportDownload()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/webhook/v1.0/organization/{self._conf.organizationId}/extension/{extension_id}/reports/cancel/file/{filename}", """{"required":[{"name":"organization_id","in":"path","description":"organization_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}},{"name":"extension_id","in":"path","description":"extension_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}},{"name":"filename","in":"path","description":"filename","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"test"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"organization_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}},{"name":"extension_id","in":"path","description":"extension_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}},{"name":"filename","in":"path","description":"filename","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"test"}}}]}""", serverType="partner", extension_id=extension_id, filename=filename)
        query_string = await create_query_string(extension_id=extension_id, filename=filename)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/webhook/v1.0/organization/{self._conf.organizationId}/extension/{extension_id}/reports/cancel/file/{filename}", extension_id=extension_id, filename=filename), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CancelDownloadResponse
            schema = CancelDownloadResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for cancelReportDownload")
                print(e)

        return response
    
    async def getHistoricalReports(self, extension_id=None, body="", request_headers:Dict={}):
        """Retrieve history reports for a specific company based on the provided filters.

        :param extension_id : extension_id : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id

        # Parameter validation
        schema = WebhookValidator.getHistoricalReports()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import HistoryPayload
        schema = HistoryPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/webhook/v1.0/organization/{self._conf.organizationId}/extension/{extension_id}/report/history", """{"required":[{"name":"organization_id","in":"path","description":"organization_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}},{"name":"extension_id","in":"path","description":"extension_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"organization_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}},{"name":"extension_id","in":"path","description":"extension_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}}]}""", serverType="partner", extension_id=extension_id)
        query_string = await create_query_string(extension_id=extension_id)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/partner/webhook/v1.0/organization/{self._conf.organizationId}/extension/{extension_id}/report/history", extension_id=extension_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import HistoryResponse
            schema = HistoryResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getHistoricalReports")
                print(e)

        return response
    
    async def getInvalidEventList(self, extension_id=None, body="", request_headers:Dict={}):
        """Get invalid event list.

        :param extension_id : extension_id : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id

        # Parameter validation
        schema = WebhookValidator.getInvalidEventList()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import InvalidEventsRequest
        schema = InvalidEventsRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/webhook/v1.0/organization/{self._conf.organizationId}/extension/{extension_id}/report/invalid_events", """{"required":[{"name":"organization_id","in":"path","description":"organization_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}},{"name":"extension_id","in":"path","description":"extension_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"organization_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}},{"name":"extension_id","in":"path","description":"extension_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}}]}""", serverType="partner", extension_id=extension_id)
        query_string = await create_query_string(extension_id=extension_id)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/partner/webhook/v1.0/organization/{self._conf.organizationId}/extension/{extension_id}/report/invalid_events", extension_id=extension_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def fetchSubscribers(self, extension_id=None, request_headers:Dict={}):
        """Fetch subscriber by filters
        :param extension_id : extension_id : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id

        # Parameter validation
        schema = WebhookValidator.fetchSubscribers()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/webhook/v1.0/organization/{self._conf.organizationId}/extension/{extension_id}/subscriber/", """{"required":[{"name":"organization_id","in":"path","description":"organization_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}},{"name":"extension_id","in":"path","description":"extension_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"organization_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}},{"name":"extension_id","in":"path","description":"extension_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}}]}""", serverType="partner", extension_id=extension_id)
        query_string = await create_query_string(extension_id=extension_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/webhook/v1.0/organization/{self._conf.organizationId}/extension/{extension_id}/subscriber/", extension_id=extension_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SubscriberConfigResponse
            schema = SubscriberConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for fetchSubscribers")
                print(e)

        return response
    
    async def updateSubscriber(self, extension_id=None, subscriber_id=None, body="", request_headers:Dict={}):
        """Update subscriber status by id.

        :param extension_id : extension_id : type string
        :param subscriber_id : subscriber_id : type number
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id
        if subscriber_id is not None:
            payload["subscriber_id"] = subscriber_id

        # Parameter validation
        schema = WebhookValidator.updateSubscriber()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateSubscriberRequest
        schema = UpdateSubscriberRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/webhook/v1.0/organization/{self._conf.organizationId}/extension/{extension_id}/subscriber/{subscriber_id}", """{"required":[{"name":"organization_id","in":"path","description":"organization_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}},{"name":"extension_id","in":"path","description":"extension_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}},{"name":"subscriber_id","in":"path","description":"subscriber_id","required":true,"schema":{"type":"number"},"examples":{"success":{"value":1}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"organization_id","in":"path","description":"organization_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}},{"name":"extension_id","in":"path","description":"extension_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}},{"name":"subscriber_id","in":"path","description":"subscriber_id","required":true,"schema":{"type":"number"},"examples":{"success":{"value":1}}}]}""", serverType="partner", extension_id=extension_id, subscriber_id=subscriber_id)
        query_string = await create_query_string(extension_id=extension_id, subscriber_id=subscriber_id)

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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/partner/webhook/v1.0/organization/{self._conf.organizationId}/extension/{extension_id}/subscriber/{subscriber_id}", extension_id=extension_id, subscriber_id=subscriber_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdateSubscriberResponse
            schema = UpdateSubscriberResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateSubscriber")
                print(e)

        return response
    