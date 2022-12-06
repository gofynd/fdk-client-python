"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class CompareObject(BaseSchema):
    #  swagger.json

    
    less_than_equals = fields.Float(required=False)
    
    greater_than_equals = fields.Float(required=False)
    
    greater_than = fields.Float(required=False)
    
    equals = fields.Float(required=False)
    
    less_than = fields.Float(required=False)
    
