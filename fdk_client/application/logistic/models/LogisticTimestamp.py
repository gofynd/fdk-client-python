"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class LogisticTimestamp(BaseSchema):
    #  swagger.json

    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    
