"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




























class StoreDetail(BaseSchema):
    # Catalog swagger.json

    
    timing = fields.Dict(required=False)
    
    store_code = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    address = fields.Dict(required=False)
    
    documents = fields.List(fields.Dict(required=False), required=False)
    
    display_name = fields.Str(required=False)
    
    manager = fields.Dict(required=False)
    
    created_on = fields.Str(required=False)
    
    additional_contacts = fields.List(fields.Dict(required=False), required=False)
    
    uid = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    

