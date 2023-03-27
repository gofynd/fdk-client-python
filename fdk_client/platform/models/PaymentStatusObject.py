"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PaymentObjectListSerializer import PaymentObjectListSerializer




class PaymentStatusObject(BaseSchema):
    # Payment swagger.json

    
    payment_object_list = fields.List(fields.Nested(PaymentObjectListSerializer, required=False), required=False)
    
    merchant_order_id = fields.Str(required=False)
    

