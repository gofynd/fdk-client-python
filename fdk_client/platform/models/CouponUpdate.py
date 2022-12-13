"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DisplayMeta import DisplayMeta

from .CouponAction import CouponAction

from .RuleDefinition import RuleDefinition

from .Validity import Validity

from .Validation import Validation

from .Restrictions import Restrictions



from .CouponAuthor import CouponAuthor

from .Rule import Rule

from .CouponSchedule import CouponSchedule





from .State import State

from .CouponDateMeta import CouponDateMeta

from .Ownership import Ownership

from .Identifier import Identifier


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    type_slug = fields.Str(required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    code = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    state = fields.Nested(State, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    

