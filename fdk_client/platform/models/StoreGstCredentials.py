"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .StoreEinvoice import StoreEinvoice

from .StoreEwaybill import StoreEwaybill


class StoreGstCredentials(BaseSchema):
    # Orders swagger.json

    
    e_invoice = fields.Nested(StoreEinvoice, required=False)
    
    e_waybill = fields.Nested(StoreEwaybill, required=False)
    

