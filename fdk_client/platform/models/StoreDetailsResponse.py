"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PickupStoreDetail import PickupStoreDetail


class StoreDetailsResponse(BaseSchema):
    # Cart swagger.json

    
    items = fields.List(fields.Nested(PickupStoreDetail, required=False), required=False)
    

