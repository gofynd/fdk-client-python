"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .AttributeDetail import AttributeDetail



class AttributeMetadata(BaseSchema):
    #  swagger.json

    
    title = fields.Str(required=False)
    
    details = fields.List(fields.Nested(AttributeDetail, required=False), required=False)
    
