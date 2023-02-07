"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .EntityReasonData import EntityReasonData





class EntitiesReasons(BaseSchema):
    #  swagger.json

    
    data = fields.Nested(EntityReasonData, required=False)
    
    filters = fields.List(fields.Dict(required=False), required=False)
    
