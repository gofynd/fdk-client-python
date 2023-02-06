"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .PincodeErrorSchemaResponse import PincodeErrorSchemaResponse





from .LocationDataResponse import LocationDataResponse



class LocationApiResponse(BaseSchema):
    #  swagger.json

    
    error = fields.Nested(PincodeErrorSchemaResponse, required=False)
    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(LocationDataResponse, required=False)
    
