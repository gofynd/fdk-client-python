"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class TicketContext(BaseSchema):

    
    application_id = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    

