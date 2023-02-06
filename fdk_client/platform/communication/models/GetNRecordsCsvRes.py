"""communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .GetNRecordsCsvResItems import GetNRecordsCsvResItems



class GetNRecordsCsvRes(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(GetNRecordsCsvResItems, required=False), required=False)
    
