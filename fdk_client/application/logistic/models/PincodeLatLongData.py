"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class PincodeLatLongData(BaseSchema):
    #  swagger.json

    
    coordinates = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
