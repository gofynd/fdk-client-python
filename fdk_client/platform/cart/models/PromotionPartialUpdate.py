"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .PromotionSchedule import PromotionSchedule



class PromotionPartialUpdate(BaseSchema):
    #  swagger.json

    
    archive = fields.Boolean(required=False)
    
    schedule = fields.Nested(PromotionSchedule, required=False)
    
