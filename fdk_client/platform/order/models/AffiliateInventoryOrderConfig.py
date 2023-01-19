"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class AffiliateInventoryOrderConfig(BaseSchema):
    #  swagger.json

    
    force_reassignment = fields.Boolean(required=False)
    
