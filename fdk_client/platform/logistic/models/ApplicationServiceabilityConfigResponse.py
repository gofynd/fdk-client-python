"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ApplicationServiceabilityConfig import ApplicationServiceabilityConfig





from .ServiceabilityrErrorResponse import ServiceabilityrErrorResponse



class ApplicationServiceabilityConfigResponse(BaseSchema):
    #  swagger.json

    
    data = fields.Nested(ApplicationServiceabilityConfig, required=False)
    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(ServiceabilityrErrorResponse, required=False)
    
