"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class SubtypeRequest(BaseSchema):
    #  swagger.json

    
    sub_type = fields.Str(required=False)
    
