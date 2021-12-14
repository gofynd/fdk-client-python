"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .Credit import Credit

from .Debit import Debit


class RewardPointsConfig(BaseSchema):
    # Configuration swagger.json

    
    credit = fields.Nested(Credit, required=False)
    
    debit = fields.Nested(Debit, required=False)
    

