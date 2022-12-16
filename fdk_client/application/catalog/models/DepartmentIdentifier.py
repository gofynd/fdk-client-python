"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class DepartmentIdentifier(BaseSchema):
    #  swagger.json

    
    slug = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    