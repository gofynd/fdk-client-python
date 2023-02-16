"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .HsnUpsert import HsnUpsert



class BulkHsnUpsert(BaseSchema):
    #  swagger.json

    
    data = fields.List(fields.Nested(HsnUpsert, required=False), required=False)
    
