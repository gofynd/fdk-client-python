"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class ArticleAssignmentV2(BaseSchema):
    #  swagger.json

    
    strategy = fields.Str(required=False)
    
    level = fields.Str(required=False)
    
