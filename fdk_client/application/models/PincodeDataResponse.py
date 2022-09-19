"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .PincodeMetaResponse import PincodeMetaResponse



from .PincodeErrorSchemaResponse import PincodeErrorSchemaResponse

from .PincodeParentsResponse import PincodeParentsResponse


class PincodeDataResponse(BaseSchema):
    # Logistic swagger.json

    
    sub_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    meta = fields.Nested(PincodeMetaResponse, required=False)
    
    display_name = fields.Str(required=False)
    
    error = fields.Nested(PincodeErrorSchemaResponse, required=False)
    
    parents = fields.List(fields.Nested(PincodeParentsResponse, required=False), required=False)
    

