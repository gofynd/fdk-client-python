"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






























class StoreDetail(BaseSchema):
    #  swagger.json

    
    store_type = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    additional_contacts = fields.List(fields.Dict(required=False), required=False)
    
    address = fields.Dict(required=False)
    
    modified_on = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    timing = fields.Dict(required=False)
    
    display_name = fields.Str(required=False)
    
    documents = fields.List(fields.Dict(required=False), required=False)
    
    store_code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    manager = fields.Dict(required=False)
    
    company_id = fields.Int(required=False)
    
