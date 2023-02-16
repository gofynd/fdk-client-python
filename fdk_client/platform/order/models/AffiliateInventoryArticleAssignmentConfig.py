"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class AffiliateInventoryArticleAssignmentConfig(BaseSchema):
    #  swagger.json

    
    post_order_reassignment = fields.Boolean(required=False)
    
