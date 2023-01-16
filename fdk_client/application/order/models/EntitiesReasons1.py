"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .EntityReasonData1 import EntityReasonData1





class EntitiesReasons1(BaseSchema):
    #  swagger.json

    
    data = fields.Nested(EntityReasonData1, required=False)
    
    filters = fields.List(fields.Dict(required=False), required=False)
    
