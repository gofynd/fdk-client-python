"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class AffiliateInventoryStoreConfig(BaseSchema):
    # Order swagger.json

    
    store = fields.Dict(required=False)
    

