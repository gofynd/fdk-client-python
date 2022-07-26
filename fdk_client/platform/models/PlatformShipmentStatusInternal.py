"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Statuses import Statuses




class PlatformShipmentStatusInternal(BaseSchema):
    # OrderManage swagger.json

    
    task = fields.Boolean(required=False)
    
    statuses = fields.Nested(Statuses, required=False)
    
    force_transition = fields.Boolean(required=False)
    

