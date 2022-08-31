"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CancelledChequePayload import CancelledChequePayload

from .PennyDropPayload import PennyDropPayload


class PayoutPennyDropAndChequePayload(BaseSchema):
    # Payment swagger.json

    
    cancelled_cheque = fields.Nested(CancelledChequePayload, required=False)
    
    penny_drop = fields.Nested(PennyDropPayload, required=False)
    

