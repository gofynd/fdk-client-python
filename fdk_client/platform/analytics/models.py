"""Analytics Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ..PlatformModel import BaseSchema





class StatGroup(BaseSchema):
    pass


class ErrorRes(BaseSchema):
    pass


class StatsGroups(BaseSchema):
    pass


class StatsGroupComponent(BaseSchema):
    pass


class StatsGroupComponents(BaseSchema):
    pass


class StatsRes(BaseSchema):
    pass


class ReceivedAt(BaseSchema):
    pass


class AbandonCartsDetail(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class AbandonCartsList(BaseSchema):
    pass


class AbandonCartDetail(BaseSchema):
    pass


class ExportJobReq(BaseSchema):
    pass


class ExportJobRes(BaseSchema):
    pass


class ExportJobStatusRes(BaseSchema):
    pass


class GetLogsListReq(BaseSchema):
    pass


class MkpLogsResp(BaseSchema):
    pass


class GetLogsListRes(BaseSchema):
    pass


class SearchLogReq(BaseSchema):
    pass


class LogInfo(BaseSchema):
    pass


class SearchLogRes(BaseSchema):
    pass





class StatGroup(BaseSchema):
    # Analytics swagger.json

    
    key = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    title = fields.Str(required=False)
    


class ErrorRes(BaseSchema):
    # Analytics swagger.json

    
    message = fields.Str(required=False)
    


class StatsGroups(BaseSchema):
    # Analytics swagger.json

    
    groups = fields.List(fields.Nested(StatGroup, required=False), required=False)
    


class StatsGroupComponent(BaseSchema):
    # Analytics swagger.json

    
    key = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    filters = fields.Dict(required=False)
    


class StatsGroupComponents(BaseSchema):
    # Analytics swagger.json

    
    title = fields.Str(required=False)
    
    components = fields.List(fields.Nested(StatsGroupComponent, required=False), required=False)
    


class StatsRes(BaseSchema):
    # Analytics swagger.json

    
    key = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    


class ReceivedAt(BaseSchema):
    # Analytics swagger.json

    
    value = fields.Str(required=False)
    


class AbandonCartsDetail(BaseSchema):
    # Analytics swagger.json

    
    properties_cart_id = fields.Str(required=False)
    
    context_traits_first_name = fields.Str(required=False)
    
    context_traits_last_name = fields.Str(required=False)
    
    context_traits_phone_number = fields.Str(required=False)
    
    context_traits_email = fields.Str(required=False)
    
    context_app_application_id = fields.Str(required=False)
    
    properties_breakup_values_raw_total = fields.Str(required=False)
    
    received_at = fields.Nested(ReceivedAt, required=False)
    


class Page(BaseSchema):
    # Analytics swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    


class AbandonCartsList(BaseSchema):
    # Analytics swagger.json

    
    items = fields.List(fields.Nested(AbandonCartsDetail, required=False), required=False)
    
    cart_total = fields.Str(required=False)
    
    page = fields.Nested(Page, required=False)
    


class AbandonCartDetail(BaseSchema):
    # Analytics swagger.json

    
    _id = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    cart_value = fields.Str(required=False)
    
    articles = fields.List(fields.Dict(required=False), required=False)
    
    breakup = fields.Dict(required=False)
    
    address = fields.Dict(required=False)
    


class ExportJobReq(BaseSchema):
    # Analytics swagger.json

    
    marketplace_name = fields.Str(required=False)
    
    start_time = fields.Str(required=False)
    
    end_time = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    trace_id = fields.Str(required=False)
    


class ExportJobRes(BaseSchema):
    # Analytics swagger.json

    
    status = fields.Str(required=False)
    
    job_id = fields.Str(required=False)
    


class ExportJobStatusRes(BaseSchema):
    # Analytics swagger.json

    
    status = fields.Str(required=False)
    
    job_id = fields.Str(required=False)
    
    download_url = fields.Str(required=False)
    


class GetLogsListReq(BaseSchema):
    # Analytics swagger.json

    
    marketplace_name = fields.Str(required=False)
    
    start_date = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    


class MkpLogsResp(BaseSchema):
    # Analytics swagger.json

    
    start_time_iso = fields.Str(required=False)
    
    end_time_iso = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    trace_id = fields.Str(required=False)
    
    count = fields.Str(required=False)
    
    status = fields.Str(required=False)
    


class GetLogsListRes(BaseSchema):
    # Analytics swagger.json

    
    items = fields.List(fields.Nested(MkpLogsResp, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class SearchLogReq(BaseSchema):
    # Analytics swagger.json

    
    marketplace_name = fields.Str(required=False)
    
    start_date = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    identifier_value = fields.Str(required=False)
    


class LogInfo(BaseSchema):
    # Analytics swagger.json

    
    _id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    marketplace_name = fields.Str(required=False)
    
    event = fields.Str(required=False)
    
    trace_id = fields.Str(required=False)
    
    company_id = fields.Float(required=False)
    
    brand_id = fields.Float(required=False)
    
    store_code = fields.Str(required=False)
    
    store_id = fields.Float(required=False)
    
    item_id = fields.Float(required=False)
    
    article_id = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    


class SearchLogRes(BaseSchema):
    # Analytics swagger.json

    
    items = fields.List(fields.Nested(LogInfo, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


