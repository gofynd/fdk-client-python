"""communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PayloadSmsTemplateStructure import PayloadSmsTemplateStructure



from .PayloadSmsProviderStructure import PayloadSmsProviderStructure



class PayloadSmsStructure(BaseSchema):
    #  swagger.json

    
    template = fields.Nested(PayloadSmsTemplateStructure, required=False)
    
    provider = fields.Nested(PayloadSmsProviderStructure, required=False)
    
