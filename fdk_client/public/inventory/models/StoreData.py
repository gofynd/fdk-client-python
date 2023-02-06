"""inventory Public Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PublicModel import BaseSchema






class StoreData(BaseSchema):
    #  swagger.json

    
    location_id = fields.Str(required=False)
    
