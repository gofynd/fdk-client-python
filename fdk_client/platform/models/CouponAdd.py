"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Validity import Validity

from .Ownership import Ownership

from .CouponAction import CouponAction

from .CouponSchedule import CouponSchedule

from .Identifier import Identifier



from .Validation import Validation





from .State import State

from .DisplayMeta import DisplayMeta

from .CouponAuthor import CouponAuthor

from .Restrictions import Restrictions

from .RuleDefinition import RuleDefinition

from .Rule import Rule

from .CouponDateMeta import CouponDateMeta


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    validity = fields.Nested(Validity, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    type_slug = fields.Str(required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    code = fields.Str(required=False)
    
    state = fields.Nested(State, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    

