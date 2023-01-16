"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .PincodeErrorSchemaResponse import PincodeErrorSchemaResponse





from .PincodeParentsResponse import PincodeParentsResponse









from .PincodeMetaResponse import PincodeMetaResponse



class PincodeDataResponse(BaseSchema):
    #  swagger.json

    
    error = fields.Nested(PincodeErrorSchemaResponse, required=False)
    
    display_name = fields.Str(required=False)
    
    parents = fields.List(fields.Nested(PincodeParentsResponse, required=False), required=False)
    
    sub_type = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    meta = fields.Nested(PincodeMetaResponse, required=False)
    
