"""Content Public Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PublicModel import BaseSchema




class CredentialSchema(BaseSchema):
    pass


class CredentialsSchema(BaseSchema):
    pass


class ContentAPIError(BaseSchema):
    pass





class CredentialSchema(BaseSchema):
    # Content swagger.json

    
    configuration = fields.Dict(required=False)
    
    entity_type = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    is_enable = fields.Boolean(required=False)
    


class CredentialsSchema(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(CredentialSchema, required=False), required=False)
    


class ContentAPIError(BaseSchema):
    # Content swagger.json

    
    message = fields.Str(required=False)
    
    status = fields.Float(required=False)
    
    code = fields.Str(required=False)
    
    exception = fields.Str(required=False)
    
    info = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    stack_trace = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    


