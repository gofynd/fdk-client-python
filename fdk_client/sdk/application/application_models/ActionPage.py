"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema










class ActionPage(BaseSchema):
    # Content swagger.json

    
    params = fields.Dict(required=False)
    
    query = fields.Dict(required=False)
    
    url = fields.Str(required=False)
    
    type = fields.Str(required=False, validate=OneOf([val.value for val in PageType.__members__.values()]))
    

