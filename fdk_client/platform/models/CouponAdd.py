"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CouponAction import CouponAction



from .Rule import Rule

from .Ownership import Ownership

from .CouponAuthor import CouponAuthor

from .DisplayMeta import DisplayMeta

from .CouponDateMeta import CouponDateMeta





from .Restrictions import Restrictions

from .RuleDefinition import RuleDefinition

from .Validity import Validity

from .State import State

from .Validation import Validation

from .CouponSchedule import CouponSchedule

from .Identifier import Identifier


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    action = fields.Nested(CouponAction, required=False)
    
    code = fields.Str(required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    type_slug = fields.Str(required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    state = fields.Nested(State, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    

