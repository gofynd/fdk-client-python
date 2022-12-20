"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AffiliateInventoryConfig import AffiliateInventoryConfig

from .AffiliateAppConfig import AffiliateAppConfig


class AffiliateConfig(BaseSchema):
    # Order swagger.json

    
    inventory = fields.Nested(AffiliateInventoryConfig, required=False)
    
    app = fields.Nested(AffiliateAppConfig, required=False)
    

