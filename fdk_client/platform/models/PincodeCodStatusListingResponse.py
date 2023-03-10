"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .Error import Error

from .PincodeCodStatusListingPage import PincodeCodStatusListingPage

from .PincodeCodStatusListingSummary import PincodeCodStatusListingSummary


class PincodeCodStatusListingResponse(BaseSchema):
    # Serviceability swagger.json

    
    country = fields.Str(required=False)
    
    data = fields.List(fields.Nested(lambda: PincodeCodStatusListingResponse(exclude=('data')), required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    errors = fields.List(fields.Nested(Error, required=False), required=False)
    
    page = fields.Nested(PincodeCodStatusListingPage, required=False)
    
    summary = fields.Nested(PincodeCodStatusListingSummary, required=False)
    

