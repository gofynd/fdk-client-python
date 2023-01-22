"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class Dimension(BaseSchema):
    #  swagger.json

    
    width = fields.Float(required=False)
    
    is_default = fields.Boolean(required=False)
    
    unit = fields.Str(required=False)
    
    height = fields.Float(required=False)
    
    length = fields.Float(required=False)
    