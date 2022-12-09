"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .StoreEwaybill import StoreEwaybill

from .StoreEinvoice import StoreEinvoice


class StoreGstCredentials(BaseSchema):
    # Order swagger.json

    
    e_waybill = fields.Nested(StoreEwaybill, required=False)
    
    e_invoice = fields.Nested(StoreEinvoice, required=False)
    

