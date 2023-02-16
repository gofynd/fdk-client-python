"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class AffiliateInventoryLogisticsConfig(BaseSchema):
    #  swagger.json

    
    dp_assignment = fields.Boolean(required=False)
    
