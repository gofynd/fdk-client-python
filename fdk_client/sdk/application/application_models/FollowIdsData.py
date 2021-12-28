"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class FollowIdsData(BaseSchema):
    # Catalog swagger.json

    
    collections = fields.List(fields.Int(required=False), required=False)
    
    brands = fields.List(fields.Int(required=False), required=False)
    
    products = fields.List(fields.Int(required=False), required=False)
    

