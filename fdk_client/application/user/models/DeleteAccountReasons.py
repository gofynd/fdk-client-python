"""user Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class DeleteAccountReasons(BaseSchema):
    #  swagger.json

    
    reason_text = fields.Str(required=False)
    
    reason_id = fields.Str(required=False)
    
    show_text_area = fields.Boolean(required=False)
    
