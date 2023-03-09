"""Partner Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ..PlatformModel import BaseSchema





class AddProxyReq(BaseSchema):
    pass


class AddProxyResponse(BaseSchema):
    pass


class APIError(BaseSchema):
    pass


class RemoveProxyResponse(BaseSchema):
    pass





class AddProxyReq(BaseSchema):
    # Partner swagger.json

    
    attached_path = fields.Str(required=False)
    
    proxy_url = fields.Str(required=False)
    


class AddProxyResponse(BaseSchema):
    # Partner swagger.json

    
    _id = fields.Str(required=False)
    
    attached_path = fields.Str(required=False)
    
    proxy_url = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    extension_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    


class APIError(BaseSchema):
    # Partner swagger.json

    
    code = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    info = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    


class RemoveProxyResponse(BaseSchema):
    # Partner swagger.json

    
    message = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    


