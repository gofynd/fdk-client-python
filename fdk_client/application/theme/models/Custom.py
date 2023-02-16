"""theme Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class Custom(BaseSchema):
    #  swagger.json

    
    props = fields.Dict(required=False)
    
