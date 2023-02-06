"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class LogisticMeta(BaseSchema):
    #  swagger.json

    
    zone = fields.Str(required=False)
    
    deliverables = fields.List(fields.Raw(required=False), required=False)
    
