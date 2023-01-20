"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .GlobalValidation import GlobalValidation



class TemplateValidationData(BaseSchema):
    #  swagger.json

    
    template_validation = fields.Dict(required=False)
    
    global_validation = fields.Nested(GlobalValidation, required=False)
    
