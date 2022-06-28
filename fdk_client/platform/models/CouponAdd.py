"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .CouponDateMeta import CouponDateMeta

from .Rule import Rule

from .Ownership import Ownership

from .CouponSchedule import CouponSchedule





from .Validation import Validation

from .Restrictions import Restrictions

from .RuleDefinition import RuleDefinition

from .DisplayMeta import DisplayMeta

from .CouponAuthor import CouponAuthor

from .State import State

from .Validity import Validity

from .CouponAction import CouponAction

from .Identifier import Identifier


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    type_slug = fields.Str(required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    code = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    state = fields.Nested(State, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    

