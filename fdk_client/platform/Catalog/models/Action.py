"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ActionPage import ActionPage





class Action(BaseSchema):
    #  swagger.json

    
    page = fields.Nested(ActionPage, required=False)
    
    type = fields.Str(required=False)
    
