"""Communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PayloadEmailTemplateStructure import PayloadEmailTemplateStructure



from .PayloadEmailProviderStructure import PayloadEmailProviderStructure



class PayloadEmailStructure(BaseSchema):
    #  swagger.json

    
    template = fields.Nested(PayloadEmailTemplateStructure, required=False)
    
    provider = fields.Nested(PayloadEmailProviderStructure, required=False)
    
