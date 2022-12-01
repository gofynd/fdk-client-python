"""communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class PayloadSmsTemplateStructure(BaseSchema):
    #  swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Raw(required=False)
    
