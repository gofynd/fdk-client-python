"""user Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class MetaSchema(BaseSchema):
    #  swagger.json

    
    fynd_default = fields.Boolean(required=False)
    
