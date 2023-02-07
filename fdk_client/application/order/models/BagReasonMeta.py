"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class BagReasonMeta(BaseSchema):
    #  swagger.json

    
    show_text_area = fields.Boolean(required=False)
    
