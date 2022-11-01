"""Communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .BigqueryHeadersResHeaders import BigqueryHeadersResHeaders



class BigqueryHeadersRes(BaseSchema):
    #  swagger.json

    
    headers = fields.List(fields.Nested(BigqueryHeadersResHeaders, required=False), required=False)
    
