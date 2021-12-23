"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema



from .RupifiBannerData import RupifiBannerData


class RupifiBannerResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(RupifiBannerData, required=False)
    

