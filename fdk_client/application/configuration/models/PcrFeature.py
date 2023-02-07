"""configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class PcrFeature(BaseSchema):
    #  swagger.json

    
    staff_selection = fields.Boolean(required=False)
    
