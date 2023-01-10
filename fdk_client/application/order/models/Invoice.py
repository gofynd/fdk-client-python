"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class Invoice(BaseSchema):
    #  swagger.json

    
    invoice_url = fields.Str(required=False)
    
    updated_date = fields.Str(required=False)
    
    label_url = fields.Str(required=False)
    
