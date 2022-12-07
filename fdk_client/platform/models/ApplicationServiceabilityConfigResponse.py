"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ServiceabilityErrorResponse import ServiceabilityErrorResponse

from .ApplicationServiceabilityConfig import ApplicationServiceabilityConfig


class ApplicationServiceabilityConfigResponse(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(ServiceabilityErrorResponse, required=False)
    
    data = fields.Nested(ApplicationServiceabilityConfig, required=False)
    

