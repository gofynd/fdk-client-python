"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .PincodeMetaResponse import PincodeMetaResponse



from .PincodeErrorSchemaResponse import PincodeErrorSchemaResponse







from .PincodeParentsResponse import PincodeParentsResponse



from .PincodeLatLongData import PincodeLatLongData





from .CountryMetaResponse import CountryMetaResponse





class PincodeDataResponse(BaseSchema):
    #  swagger.json

    
    meta = fields.Nested(PincodeMetaResponse, required=False)
    
    error = fields.Nested(PincodeErrorSchemaResponse, required=False)
    
    sub_type = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    parents = fields.List(fields.Nested(PincodeParentsResponse, required=False), required=False)
    
    lat_long = fields.Nested(PincodeLatLongData, required=False)
    
    name = fields.Str(required=False)
    
    meta_code = fields.Nested(CountryMetaResponse, required=False)
    
    uid = fields.Str(required=False)
    
