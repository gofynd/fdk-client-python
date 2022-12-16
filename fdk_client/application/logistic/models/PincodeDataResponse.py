"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










from .PincodeErrorSchemaResponse import PincodeErrorSchemaResponse



from .PincodeMetaResponse import PincodeMetaResponse





from .PincodeParentsResponse import PincodeParentsResponse



class PincodeDataResponse(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    error = fields.Nested(PincodeErrorSchemaResponse, required=False)
    
    meta = fields.Nested(PincodeMetaResponse, required=False)
    
    uid = fields.Str(required=False)
    
    parents = fields.List(fields.Nested(PincodeParentsResponse, required=False), required=False)
    