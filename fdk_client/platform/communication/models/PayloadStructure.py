"""communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .PayloadEmailStructure import PayloadEmailStructure



from .PayloadSmsStructure import PayloadSmsStructure





class PayloadStructure(BaseSchema):
    #  swagger.json

    
    data = fields.List(fields.Dict(required=False), required=False)
    
    email = fields.Nested(PayloadEmailStructure, required=False)
    
    sms = fields.Nested(PayloadSmsStructure, required=False)
    
    application = fields.Str(required=False)
    
