"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Validation import Validation

from .Validity import Validity

from .CouponAuthor import CouponAuthor

from .CouponDateMeta import CouponDateMeta



from .Restrictions import Restrictions

from .Identifier import Identifier

from .State import State

from .CouponAction import CouponAction



from .CouponSchedule import CouponSchedule

from .DisplayMeta import DisplayMeta

from .Ownership import Ownership

from .RuleDefinition import RuleDefinition

from .Rule import Rule


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    code = fields.Str(required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    type_slug = fields.Str(required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    state = fields.Nested(State, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    

