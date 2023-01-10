"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class StoreDepartments(BaseSchema):
    #  swagger.json

    
    uid = fields.Int(required=False)
    
    priority_order = fields.Int(required=False)
    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
