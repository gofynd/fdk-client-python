"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class AffiliateStoreIdMapping(BaseSchema):
    # Order swagger.json

    
    marketplace_store_id = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    

