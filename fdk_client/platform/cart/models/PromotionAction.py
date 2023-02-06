"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class PromotionAction(BaseSchema):
    #  swagger.json

    
    action_type = fields.Str(required=False)
    
    action_date = fields.Str(required=False)
    
