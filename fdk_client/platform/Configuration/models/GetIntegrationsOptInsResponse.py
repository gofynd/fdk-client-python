"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .IntegrationOptIn import IntegrationOptIn



from .Page import Page



class GetIntegrationsOptInsResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(IntegrationOptIn, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
