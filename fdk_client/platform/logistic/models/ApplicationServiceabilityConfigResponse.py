"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ApplicationServiceabilityConfig import ApplicationServiceabilityConfig



from .ServiceabilityErrorResponse import ServiceabilityErrorResponse





class ApplicationServiceabilityConfigResponse(BaseSchema):
    #  swagger.json

    
    data = fields.Nested(ApplicationServiceabilityConfig, required=False)
    
    error = fields.Nested(ServiceabilityErrorResponse, required=False)
    
    success = fields.Boolean(required=False)
    
