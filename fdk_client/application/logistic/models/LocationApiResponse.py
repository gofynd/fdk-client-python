"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .LocationDataResponse import LocationDataResponse





from .PincodeErrorSchemaResponse import PincodeErrorSchemaResponse



class LocationApiResponse(BaseSchema):
    #  swagger.json

    
    data = fields.Nested(LocationDataResponse, required=False)
    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(PincodeErrorSchemaResponse, required=False)
    
