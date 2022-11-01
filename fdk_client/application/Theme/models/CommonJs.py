"""Theme Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class CommonJs(BaseSchema):
    #  swagger.json

    
    link = fields.Str(required=False)
    
