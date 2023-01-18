"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .PincodeParentsResponse import PincodeParentsResponse





from .PincodeErrorSchemaResponse import PincodeErrorSchemaResponse







from .PincodeMetaResponse import PincodeMetaResponse





class PincodeDataResponse(BaseSchema):
    #  swagger.json

    
    parents = fields.List(fields.Nested(PincodeParentsResponse, required=False), required=False)
    
    uid = fields.Str(required=False)
    
    error = fields.Nested(PincodeErrorSchemaResponse, required=False)
    
    display_name = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    meta = fields.Nested(PincodeMetaResponse, required=False)
    
    sub_type = fields.Str(required=False)
    
