"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .PromiseTimestamp import PromiseTimestamp

from .PromiseFormatted import PromiseFormatted


class ShipmentPromise(BaseSchema):

    
    timestamp = fields.Nested(PromiseTimestamp, required=False)
    
    formatted = fields.Nested(PromiseFormatted, required=False)
    

