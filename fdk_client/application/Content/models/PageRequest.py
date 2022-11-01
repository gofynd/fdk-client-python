"""Content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .CronSchedule import CronSchedule





from .Author import Author









from .Asset import Asset











from .SEO import SEO





class PageRequest(BaseSchema):
    #  swagger.json

    
    _schedule = fields.Nested(CronSchedule, required=False)
    
    application = fields.Str(required=False)
    
    author = fields.Nested(Author, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    orientation = fields.Str(required=False)
    
    content = fields.List(fields.Dict(required=False), required=False)
    
    feature_image = fields.Nested(Asset, required=False)
    
    published = fields.Boolean(required=False)
    
    reading_time = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    seo = fields.Nested(SEO, required=False)
    
    title = fields.Str(required=False)
    
