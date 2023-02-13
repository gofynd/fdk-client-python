"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class AffiliateAppConfigMeta(BaseSchema):
    # OrderManage swagger.json

    
    value = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
