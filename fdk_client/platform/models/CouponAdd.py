"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .DisplayMeta import DisplayMeta

from .CouponDateMeta import CouponDateMeta

from .Identifier import Identifier

from .RuleDefinition import RuleDefinition

from .Validity import Validity

from .Validation import Validation

from .State import State

from .Ownership import Ownership

from .CouponAction import CouponAction



from .CouponSchedule import CouponSchedule



from .Restrictions import Restrictions

from .Rule import Rule

from .CouponAuthor import CouponAuthor


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    code = fields.Str(required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    state = fields.Nested(State, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    type_slug = fields.Str(required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    

