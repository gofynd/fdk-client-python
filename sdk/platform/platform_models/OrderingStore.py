"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .OptedStoreAddress import OptedStoreAddress


















class OrderingStore(BaseSchema):

    
    address = fields.Nested(OptedStoreAddress, required=False)
    
    _id = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    code = fields.Str(required=False)
    

