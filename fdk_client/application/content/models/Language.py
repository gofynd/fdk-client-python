"""content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class Language(BaseSchema):
    #  swagger.json

    
    display = fields.Str(required=False)
    
