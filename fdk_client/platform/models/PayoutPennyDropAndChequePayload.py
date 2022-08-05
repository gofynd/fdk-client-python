"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PennyDropPayload import PennyDropPayload

from .CancelledChequePayload import CancelledChequePayload


class PayoutPennyDropAndChequePayload(BaseSchema):
    # Payment swagger.json

    
    penny_drop = fields.Nested(PennyDropPayload, required=False)
    
    cancelled_cheque = fields.Nested(CancelledChequePayload, required=False)
    

