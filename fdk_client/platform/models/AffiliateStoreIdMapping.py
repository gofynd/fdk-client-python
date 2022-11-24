"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class AffiliateStoreIdMapping(BaseSchema):
    # OrderManage swagger.json

    
    store_id = fields.Int(required=False)
    
    marketplace_store_id = fields.Str(required=False)
    

