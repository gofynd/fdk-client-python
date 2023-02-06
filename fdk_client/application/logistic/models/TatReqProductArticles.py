"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .LogisticRequestCategory import LogisticRequestCategory



class TatReqProductArticles(BaseSchema):
    #  swagger.json

    
    manufacturing_time = fields.Int(required=False)
    
    manufacturing_time_unit = fields.Str(required=False)
    
    category = fields.Nested(LogisticRequestCategory, required=False)
    
