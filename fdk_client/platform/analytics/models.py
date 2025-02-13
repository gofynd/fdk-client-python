"""Analytics Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class Page(BaseSchema):
    pass


class FileDownloadRequestBody(BaseSchema):
    pass


class JobExecute(BaseSchema):
    pass


class JobExecutionResult(BaseSchema):
    pass


class JobStatus(BaseSchema):
    pass





class Page(BaseSchema):
    # Analytics swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    


class FileDownloadRequestBody(BaseSchema):
    # Analytics swagger.json

    
    query = fields.Str(required=False)
    
    split_files = fields.Boolean(required=False)
    


class JobExecute(BaseSchema):
    # Analytics swagger.json

    
    query = fields.Str(required=False)
    
    page = fields.Nested(Page, required=False)
    


class JobExecutionResult(BaseSchema):
    # Analytics swagger.json

    
    rows = fields.List(fields.Dict(required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class JobStatus(BaseSchema):
    # Analytics swagger.json

    
    start_date = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    file_metadata = fields.List(fields.Dict(required=False), required=False)
    


