"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






























class StoreDetail(BaseSchema):
    #  swagger.json

    
    manager = fields.Dict(required=False)
    
    address = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    documents = fields.List(fields.Dict(required=False), required=False)
    
    name = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    timing = fields.Dict(required=False)
    
    created_on = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    additional_contacts = fields.List(fields.Dict(required=False), required=False)
    
