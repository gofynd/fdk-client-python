"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .RuleDefinition import RuleDefinition

from .DisplayMeta import DisplayMeta

from .Validity import Validity

from .CouponDateMeta import CouponDateMeta

from .CouponAuthor import CouponAuthor

from .Rule import Rule

from .CouponAction import CouponAction



from .Ownership import Ownership

from .Validation import Validation





from .CouponSchedule import CouponSchedule

from .Restrictions import Restrictions

from .State import State

from .Identifier import Identifier


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    type_slug = fields.Str(required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    code = fields.Str(required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    state = fields.Nested(State, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    

