"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ServiceabilityErrorResponse import ServiceabilityErrorResponse

from .ApplicationServiceabilityResponse import ApplicationServiceabilityResponse




class ApplicationServiceabilityConfigResponse(BaseSchema):
    # Serviceability swagger.json

    
    error = fields.Nested(ServiceabilityErrorResponse, required=False)
    
    data = fields.Nested(ApplicationServiceabilityResponse, required=False)
    
    success = fields.Boolean(required=False)
    

