"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ApplicationServiceabilityConfig import ApplicationServiceabilityConfig



from .ServiceabilityrErrorResponse import ServiceabilityrErrorResponse


class ApplicationServiceabilityConfigResponse(BaseSchema):
    # Serviceability swagger.json

    
    data = fields.Nested(ApplicationServiceabilityConfig, required=False)
    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(ServiceabilityrErrorResponse, required=False)
    

