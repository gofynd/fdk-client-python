"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Restrictions import Restrictions



from .CouponDateMeta import CouponDateMeta



from .CouponAuthor import CouponAuthor

from .CouponSchedule import CouponSchedule

from .Rule import Rule

from .Ownership import Ownership

from .Identifier import Identifier

from .State import State

from .DisplayMeta import DisplayMeta

from .Validation import Validation



from .RuleDefinition import RuleDefinition

from .CouponAction import CouponAction

from .Validity import Validity


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    restrictions = fields.Nested(Restrictions, required=False)
    
    type_slug = fields.Str(required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    state = fields.Nested(State, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    code = fields.Str(required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    validity = fields.Nested(Validity, required=False)
    

