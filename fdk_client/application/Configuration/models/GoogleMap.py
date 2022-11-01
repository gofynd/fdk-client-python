"""Configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .GoogleMapCredentials import GoogleMapCredentials



class GoogleMap(BaseSchema):
    #  swagger.json

    
    credentials = fields.Nested(GoogleMapCredentials, required=False)
    
