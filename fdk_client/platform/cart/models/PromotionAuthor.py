"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class PromotionAuthor(BaseSchema):
    #  swagger.json

    
    modified_by = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    
