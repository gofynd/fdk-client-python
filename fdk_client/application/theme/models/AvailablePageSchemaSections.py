"""theme Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














from .AvailablePagePredicate import AvailablePagePredicate



class AvailablePageSchemaSections(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    label = fields.Str(required=False)
    
    props = fields.Dict(required=False)
    
    blocks = fields.List(fields.Dict(required=False), required=False)
    
    preset = fields.Dict(required=False)
    
    predicate = fields.Nested(AvailablePagePredicate, required=False)
    
