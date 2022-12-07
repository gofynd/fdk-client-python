"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class EntitiesReasons(BaseSchema):
    #  swagger.json

    
    filters = fields.List(fields.Dict(required=False), required=False)
    
    data = fields.Dict(required=False)
    
