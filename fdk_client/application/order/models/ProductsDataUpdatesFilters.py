"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class ProductsDataUpdatesFilters(BaseSchema):
    #  swagger.json

    
    line_number = fields.Int(required=False)
    
    identifier = fields.Str(required=False)
    