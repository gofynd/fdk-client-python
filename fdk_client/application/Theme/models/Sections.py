"""Theme Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class Sections(BaseSchema):
    #  swagger.json

    
    attributes = fields.Str(required=False)
    
