"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ServiceabilityErrorResponse import ServiceabilityErrorResponse





from .ApplicationServiceabilityConfig import ApplicationServiceabilityConfig



class ApplicationServiceabilityConfigResponse(BaseSchema):
    #  swagger.json

    
    error = fields.Nested(ServiceabilityErrorResponse, required=False)
    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(ApplicationServiceabilityConfig, required=False)
    
