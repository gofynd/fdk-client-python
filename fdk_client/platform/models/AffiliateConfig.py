"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AffiliateAppConfig import AffiliateAppConfig

from .AffiliateInventoryConfig import AffiliateInventoryConfig


class AffiliateConfig(BaseSchema):
    # OrderManage swagger.json

    
    app = fields.Nested(AffiliateAppConfig, required=False)
    
    inventory = fields.Nested(AffiliateInventoryConfig, required=False)
    

