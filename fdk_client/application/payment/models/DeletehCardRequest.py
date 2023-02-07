"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class DeletehCardRequest(BaseSchema):
    #  swagger.json

    
    card_id = fields.Str(required=False)
    
