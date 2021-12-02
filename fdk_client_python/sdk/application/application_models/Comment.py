"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema



from .DateMeta import DateMeta

from .Entity import Entity





from .FeedbackState import FeedbackState

from .TagMeta import TagMeta

from .VoteCount import VoteCount


class Comment(BaseSchema):

    
    comment = fields.List(fields.Str(required=False), required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    entity = fields.Nested(Entity, required=False)
    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    state = fields.Nested(FeedbackState, required=False)
    
    tags = fields.List(fields.Nested(TagMeta, required=False), required=False)
    
    vote_count = fields.Nested(VoteCount, required=False)
    

