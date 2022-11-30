"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ApplicationServiceabilityResponse import ApplicationServiceabilityResponse

from .ServiceabilityErrorResponse import ServiceabilityErrorResponse




class ApplicationServiceabilityConfigResponse(BaseSchema):
    # Serviceability swagger.json

    
    data = fields.Nested(ApplicationServiceabilityResponse, required=False)
    
    error = fields.Nested(ServiceabilityErrorResponse, required=False)
    
    success = fields.Boolean(required=False)
    

