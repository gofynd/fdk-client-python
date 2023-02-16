"""configuration Public Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PublicModel import BaseSchema






class ApplicationAuth(BaseSchema):
    #  swagger.json

    
    enabled = fields.Boolean(required=False)
    
