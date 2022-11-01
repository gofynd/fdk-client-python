"""Communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class GetNRecordsCsvReq(BaseSchema):
    #  swagger.json

    
    url = fields.Str(required=False)
    
    header = fields.Boolean(required=False)
    
    count = fields.Int(required=False)
    
