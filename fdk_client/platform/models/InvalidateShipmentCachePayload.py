"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class InvalidateShipmentCachePayload(BaseSchema):
    # OrderManage swagger.json

    
    shipment_ids = fields.List(fields.Str(required=False), required=False)
    

