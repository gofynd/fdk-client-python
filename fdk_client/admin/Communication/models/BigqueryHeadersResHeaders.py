"""Communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class BigqueryHeadersResHeaders(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
