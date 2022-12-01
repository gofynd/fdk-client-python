"""content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .Action import Action





from .CreatedBySchema import CreatedBySchema



from .DateMeta import DateMeta











class LandingPageSchema(BaseSchema):
    #  swagger.json

    
    slug = fields.Str(required=False)
    
    action = fields.Nested(Action, required=False)
    
    platform = fields.List(fields.Str(required=False), required=False)
    
    created_by = fields.Nested(CreatedBySchema, required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    _id = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    archived = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
