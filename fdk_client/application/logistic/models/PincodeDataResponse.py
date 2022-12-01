"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .PincodeMetaResponse import PincodeMetaResponse









from .PincodeParentsResponse import PincodeParentsResponse



from .PincodeErrorSchemaResponse import PincodeErrorSchemaResponse





class PincodeDataResponse(BaseSchema):
    #  swagger.json

    
    meta = fields.Nested(PincodeMetaResponse, required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    parents = fields.List(fields.Nested(PincodeParentsResponse, required=False), required=False)
    
    error = fields.Nested(PincodeErrorSchemaResponse, required=False)
    
    uid = fields.Str(required=False)
    
