"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class AvailablePageScreenPredicate(BaseSchema):
    # Theme swagger.json

    
    mobile = fields.Boolean(required=False)
    
    desktop = fields.Boolean(required=False)
    
    tablet = fields.Boolean(required=False)
    

