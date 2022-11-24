"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class UpdateShipmentStatusBody(BaseSchema):
    # Order swagger.json

    
    shipments = fields.Dict(required=False)
    
    statuses = fields.List(fields.Raw(required=False), required=False)
    
    force_transition = fields.Boolean(required=False)
    
    task = fields.Boolean(required=False)
    

