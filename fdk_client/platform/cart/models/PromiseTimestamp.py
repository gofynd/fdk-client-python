"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class PromiseTimestamp(BaseSchema):
    #  swagger.json

    
    max = fields.Float(required=False)
    
    min = fields.Float(required=False)
    
