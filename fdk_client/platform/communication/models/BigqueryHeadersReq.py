"""communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class BigqueryHeadersReq(BaseSchema):
    #  swagger.json

    
    query = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
