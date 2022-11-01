"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .TemplateDetails import TemplateDetails



from .TemplateValidationData import TemplateValidationData



class TemplatesValidationResponse(BaseSchema):
    #  swagger.json

    
    template_details = fields.Nested(TemplateDetails, required=False)
    
    data = fields.Nested(TemplateValidationData, required=False)
    
