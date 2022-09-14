"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .TATError import TATError

from .Promise import Promise







from .Category import Category




class ArticlesResponse(BaseSchema):
    # Logistic swagger.json

    
    error = fields.Nested(TATError, required=False)
    
    promise = fields.Nested(Promise, required=False)
    
    manufacturing_time = fields.Int(required=False)
    
    is_cod_available = fields.Boolean(required=False)
    
    manufacturing_time_unit = fields.Str(required=False)
    
    category = fields.Nested(Category, required=False)
    
    _manufacturing_time_seconds = fields.Str(required=False)
    

