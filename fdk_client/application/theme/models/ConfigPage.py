"""theme Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class ConfigPage(BaseSchema):
    #  swagger.json

    
    settings = fields.Dict(required=False)
    
    page = fields.Str(required=False)
    
