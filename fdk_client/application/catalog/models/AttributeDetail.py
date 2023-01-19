"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class AttributeDetail(BaseSchema):
    #  swagger.json

    
    logo = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
