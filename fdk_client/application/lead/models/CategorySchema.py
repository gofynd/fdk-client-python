"""lead Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












from .FeedbackForm import FeedbackForm



class CategorySchema(BaseSchema):
    #  swagger.json

    
    display = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    sub_categories = fields.Nested(lambda: CategorySchema(exclude=('sub_categories')), required=False)
    
    group_id = fields.Float(required=False)
    
    feedback_form = fields.Nested(FeedbackForm, required=False)
    
