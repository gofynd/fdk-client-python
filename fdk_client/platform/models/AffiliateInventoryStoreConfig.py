"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class AffiliateInventoryStoreConfig(BaseSchema):
    # OrderManage swagger.json

    
    store = fields.Dict(required=False)
    

