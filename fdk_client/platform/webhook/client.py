"""Webhook Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .validator import WebhookValidator

class Webhook:
    def __init__(self, config: PlatformConfig):
        self._conf = config

    
    async def manualRetryOfFailedEvent(self, body="", request_headers:Dict={}):
        """Trigger a manual retry for an event that failed to deliver.
        """
        payload = {}
        

        # Parameter validation
        schema = WebhookValidator.manualRetryOfFailedEvent()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import RetryEventRequest
        schema = RetryEventRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/retry", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/retry", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RetrySuccessResponse
            schema = RetrySuccessResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for manualRetryOfFailedEvent")
                print(e)

        return response
    
    async def getEventCounts(self, body="", request_headers:Dict={}):
        """Retrieve the counts of events based on their status.
        """
        payload = {}
        

        # Parameter validation
        schema = WebhookValidator.getEventCounts()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import RetryEventRequest
        schema = RetryEventRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/retry/events/counts", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/retry/events/counts", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RetryCountResponse
            schema = RetryCountResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getEventCounts")
                print(e)

        return response
    
    async def getManualRetryStatus(self, request_headers:Dict={}):
        """Check the status of a manual retry operation.
        """
        payload = {}
        

        # Parameter validation
        schema = WebhookValidator.getManualRetryStatus()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/retry/status", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/retry/status", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import RetryStatusResponse
            schema = RetryStatusResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getManualRetryStatus")
                print(e)

        return response
    
    async def manualRetryCancel(self, request_headers:Dict={}):
        """Cancel a manual retry operation for a failed event.
        """
        payload = {}
        

        # Parameter validation
        schema = WebhookValidator.manualRetryCancel()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/retry/cancel", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/retry/cancel", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def downloadDeliveryReport(self, body="", request_headers:Dict={}):
        """Download detailed delivery reports for events.
        """
        payload = {}
        

        # Parameter validation
        schema = WebhookValidator.downloadDeliveryReport()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EventProcessRequest
        schema = EventProcessRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/reports/download", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/reports/download", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DownloadReportResponse
            schema = DownloadReportResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for downloadDeliveryReport")
                print(e)

        return response
    
    async def pingWebhook(self, body="", request_headers:Dict={}):
        """Send a test ping to a webhook for verification.
        """
        payload = {}
        

        # Parameter validation
        schema = WebhookValidator.pingWebhook()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PingWebhook
        schema = PingWebhook()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/subscriber/ping", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/subscriber/ping", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PingWebhookResponse
            schema = PingWebhookResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for pingWebhook")
                print(e)

        return response
    
    async def getReportFilters(self, body="", request_headers:Dict={}):
        """Retrieve filters used for generating reports.
        """
        payload = {}
        

        # Parameter validation
        schema = WebhookValidator.getReportFilters()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ReportFiltersPayload
        schema = ReportFiltersPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/filters", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/filters", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def getHistoricalReports(self, body="", request_headers:Dict={}):
        """Retrieve historical reports of webhook events.
        """
        payload = {}
        

        # Parameter validation
        schema = WebhookValidator.getHistoricalReports()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import HistoryPayload
        schema = HistoryPayload()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/reports/history", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/reports/history", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import HistoryResponse
            schema = HistoryResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getHistoricalReports")
                print(e)

        return response
    
    async def cancelJobByName(self, filename=None, request_headers:Dict={}):
        """It will cancel export job triggerd by user in order to fetch
historical delivery summery
        :param filename :  : type string
        """
        payload = {}
        
        if filename is not None:
            payload["filename"] = filename

        # Parameter validation
        schema = WebhookValidator.cancelJobByName()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/reports/cancel/file/{filename}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}},{"name":"filename","in":"path","required":true,"schema":{"type":"string","description":"This is filename that will be used for export operation"},"examples":{"success":{"value":"test_file"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}},{"name":"filename","in":"path","required":true,"schema":{"type":"string","description":"This is filename that will be used for export operation"},"examples":{"success":{"value":"test_file"}}}]}""", serverType="platform", filename=filename)
        query_string = await create_query_string(filename=filename)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/reports/cancel/file/{filename}", filename=filename), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CancelResponse
            schema = CancelResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for cancelJobByName")
                print(e)

        return response
    
    async def getDeliveryReports(self, body="", request_headers:Dict={}):
        """Retrieve reports on the delivery status of events.
        """
        payload = {}
        

        # Parameter validation
        schema = WebhookValidator.getDeliveryReports()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EventProcessRequest
        schema = EventProcessRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/reports/event_processed", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/reports/event_processed", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EventProcessReports
            schema = EventProcessReports()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDeliveryReports")
                print(e)

        return response
    
    async def fetchAllEventConfigurations(self, request_headers:Dict={}):
        """Retrieve all configurations for event handling.
        """
        payload = {}
        

        # Parameter validation
        schema = WebhookValidator.fetchAllEventConfigurations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/events", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/events", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EventConfigResponse
            schema = EventConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for fetchAllEventConfigurations")
                print(e)

        return response
    
    async def registerSubscriberToEventV2(self, body="", request_headers:Dict={}):
        """Register Subscriber.

        """
        payload = {}
        

        # Parameter validation
        schema = WebhookValidator.registerSubscriberToEventV2()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SubscriberConfigRequestV2
        schema = SubscriberConfigRequestV2()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v2.0/company/{self._conf.companyId}/subscriber/", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/webhook/v2.0/company/{self._conf.companyId}/subscriber/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SubscriberConfigResponse
            schema = SubscriberConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for registerSubscriberToEventV2")
                print(e)

        return response
    
    async def updateSubscriberV2(self, body="", request_headers:Dict={}):
        """Update Subscriber.

        """
        payload = {}
        

        # Parameter validation
        schema = WebhookValidator.updateSubscriberV2()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SubscriberConfigRequestV2
        schema = SubscriberConfigRequestV2()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v2.0/company/{self._conf.companyId}/subscriber/", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/webhook/v2.0/company/{self._conf.companyId}/subscriber/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SubscriberConfigResponse
            schema = SubscriberConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateSubscriberV2")
                print(e)

        return response
    
    async def registerSubscriberToEvent(self, body="", request_headers:Dict={}):
        """Add a subscriber to receive events of a specific type.
        """
        payload = {}
        

        # Parameter validation
        schema = WebhookValidator.registerSubscriberToEvent()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SubscriberConfig
        schema = SubscriberConfig()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/subscriber/", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/subscriber/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SubscriberConfigResponse
            schema = SubscriberConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for registerSubscriberToEvent")
                print(e)

        return response
    
    async def getSubscribersByCompany(self, page_no=None, page_size=None, extension_id=None, request_headers:Dict={}):
        """Retrieve subscribers associated with a company.
        :param page_no : Page Number : type integer
        :param page_size : Page Size : type integer
        :param extension_id : extension_id : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if extension_id is not None:
            payload["extension_id"] = extension_id

        # Parameter validation
        schema = WebhookValidator.getSubscribersByCompany()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/subscriber/", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}],"optional":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer"},"examples":{"success":{"value":1}}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32"},"examples":{"success":{"value":10}}},{"name":"extension_id","in":"query","description":"extension_id","required":false,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}}],"query":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer"},"examples":{"success":{"value":1}}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32"},"examples":{"success":{"value":10}}},{"name":"extension_id","in":"query","description":"extension_id","required":false,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}]}""", serverType="platform", page_no=page_no, page_size=page_size, extension_id=extension_id)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, extension_id=extension_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/subscriber/", page_no=page_no, page_size=page_size, extension_id=extension_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SubscriberConfigList
            schema = SubscriberConfigList()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSubscribersByCompany")
                print(e)

        return response
    
    async def updateSubscriberConfig(self, body="", request_headers:Dict={}):
        """Modify and update subscriber configuration settings.
        """
        payload = {}
        

        # Parameter validation
        schema = WebhookValidator.updateSubscriberConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SubscriberConfig
        schema = SubscriberConfig()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/subscriber/", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/subscriber/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SubscriberConfigResponse
            schema = SubscriberConfigResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateSubscriberConfig")
                print(e)

        return response
    
    async def getSubscriberById(self, subscriber_id=None, request_headers:Dict={}):
        """Retrieve a subscriber's details by their unique identifier.
        :param subscriber_id : subscriber id : type integer
        """
        payload = {}
        
        if subscriber_id is not None:
            payload["subscriber_id"] = subscriber_id

        # Parameter validation
        schema = WebhookValidator.getSubscriberById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/subscriber/{subscriber_id}", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}},{"name":"subscriber_id","in":"path","description":"subscriber id","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}},{"name":"subscriber_id","in":"path","description":"subscriber id","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}}]}""", serverType="platform", subscriber_id=subscriber_id)
        query_string = await create_query_string(subscriber_id=subscriber_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/subscriber/{subscriber_id}", subscriber_id=subscriber_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SubscriberResponse
            schema = SubscriberResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSubscriberById")
                print(e)

        return response
    
    async def getSubscribersByExtensionId(self, page_no=None, page_size=None, extension_id=None, request_headers:Dict={}):
        """Retrieve subscribers associated with a specific extension.
        :param page_no : Page Number : type integer
        :param page_size : Page Size : type integer
        :param extension_id : extension_id : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if extension_id is not None:
            payload["extension_id"] = extension_id

        # Parameter validation
        schema = WebhookValidator.getSubscribersByExtensionId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/extension/{extension_id}/subscriber/", """{"required":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}},{"name":"extension_id","in":"path","description":"extension_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}}],"optional":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer"},"examples":{"success":{"value":1}}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32"},"examples":{"success":{"value":10}}}],"query":[{"name":"page_no","in":"query","description":"Page Number","required":false,"schema":{"type":"integer"},"examples":{"success":{"value":1}}},{"name":"page_size","in":"query","description":"Page Size","required":false,"schema":{"type":"integer","format":"int32"},"examples":{"success":{"value":10}}}],"headers":[],"path":[{"name":"company_id","in":"path","required":true,"schema":{"type":"integer"},"examples":{"success":{"value":1}}},{"name":"extension_id","in":"path","description":"extension_id","required":true,"schema":{"type":"string"},"examples":{"success":{"value":"64affd97cbddb85348ca8f93"}}}]}""", serverType="platform", page_no=page_no, page_size=page_size, extension_id=extension_id)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, extension_id=extension_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/webhook/v1.0/company/{self._conf.companyId}/extension/{extension_id}/subscriber/", page_no=page_no, page_size=page_size, extension_id=extension_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SubscriberConfigList
            schema = SubscriberConfigList()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSubscribersByExtensionId")
                print(e)

        return response
    