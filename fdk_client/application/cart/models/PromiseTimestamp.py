"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class PromiseTimestamp(BaseSchema):
    #  swagger.json

    
    max = fields.Float(required=False)
    
    min = fields.Float(required=False)
    
