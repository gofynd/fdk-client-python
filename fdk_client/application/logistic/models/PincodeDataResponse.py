"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .PincodeLatLongData import PincodeLatLongData







from .PincodeParentsResponse import PincodeParentsResponse





from .PincodeMetaResponse import PincodeMetaResponse



from .CountryMetaResponse import CountryMetaResponse



from .PincodeErrorSchemaResponse import PincodeErrorSchemaResponse





class PincodeDataResponse(BaseSchema):
    #  swagger.json

    
    lat_long = fields.Nested(PincodeLatLongData, required=False)
    
    uid = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    parents = fields.List(fields.Nested(PincodeParentsResponse, required=False), required=False)
    
    display_name = fields.Str(required=False)
    
    meta = fields.Nested(PincodeMetaResponse, required=False)
    
    meta_code = fields.Nested(CountryMetaResponse, required=False)
    
    error = fields.Nested(PincodeErrorSchemaResponse, required=False)
    
    sub_type = fields.Str(required=False)
    
