"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ShipmentDetail import ShipmentDetail




class Statuses(BaseSchema):
    # OrderManage swagger.json

    
    status = fields.Str(required=False)
    
    shipments = fields.Nested(ShipmentDetail, required=False)
    
    exclude_bags_next_state = fields.Str(required=False)
    

