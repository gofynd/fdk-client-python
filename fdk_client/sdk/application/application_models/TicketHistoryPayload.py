"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class TicketHistoryPayload(BaseSchema):
    # Lead swagger.json

    
    value = fields.Dict(required=False)
    
    type = fields.Str(required=False, validate=OneOf([val.value for val in HistoryTypeEnum.__members__.values()]))
    

