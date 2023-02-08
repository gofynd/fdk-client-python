"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class EntitiesDataUpdates(BaseSchema):
    #  swagger.json

    
    data = fields.Dict(required=False)
    
    filters = fields.List(fields.Dict(required=False), required=False)
    
