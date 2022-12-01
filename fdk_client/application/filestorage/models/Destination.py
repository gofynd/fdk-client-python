"""filestorage Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class Destination(BaseSchema):
    #  swagger.json

    
    namespace = fields.Str(required=False)
    
    rewrite = fields.Str(required=False)
    
    basepath = fields.Str(required=False)
    
