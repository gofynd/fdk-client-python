"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .TemplateValidationData import TemplateValidationData



from .TemplateDetails import TemplateDetails



class TemplatesValidationResponse(BaseSchema):
    #  swagger.json

    
    data = fields.Nested(TemplateValidationData, required=False)
    
    template_details = fields.Nested(TemplateDetails, required=False)
    
