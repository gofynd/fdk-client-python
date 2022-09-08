"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .EntityTransitionError import EntityTransitionError


class UpdateShipmentStatusResponse1(BaseSchema):
    # Order swagger.json

    
    status = fields.Boolean(required=False)
    
    error_entities = fields.List(fields.Nested(EntityTransitionError, required=False), required=False)
    

