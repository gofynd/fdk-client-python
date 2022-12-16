"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema


















class DeviceDetails(BaseSchema):
    #  swagger.json

    
    os = fields.Str(required=False)
    
    os_version = fields.Str(required=False)
    
    identifier_type = fields.Str(required=False)
    
    identification_number = fields.Str(required=False)
    
    device_model = fields.Str(required=False)
    
    device_type = fields.Str(required=False)
    
    device_make = fields.Str(required=False)
    