"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *





from .AddMediaRequest import AddMediaRequest






class AddMediaListRequest(Schema):

    
    entity_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    media_list = fields.List(fields.Nested(AddMediaRequest, required=False), required=False)
    
    ref_id = fields.Str(required=False)
    
    ref_type = fields.Str(required=False)
    

