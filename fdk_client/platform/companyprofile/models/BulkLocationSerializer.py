"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .LocationSerializer import LocationSerializer



class BulkLocationSerializer(BaseSchema):
    #  swagger.json

    
    data = fields.List(fields.Nested(LocationSerializer, required=False), required=False)
    
