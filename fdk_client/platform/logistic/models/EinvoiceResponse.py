"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class EinvoiceResponse(BaseSchema):
    #  swagger.json

    
    enabled = fields.Boolean(required=False)
    
