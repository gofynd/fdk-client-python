"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .CouponAction import CouponAction

from .Rule import Rule

from .RuleDefinition import RuleDefinition

from .CouponDateMeta import CouponDateMeta

from .Restrictions import Restrictions

from .Validation import Validation

from .State import State

from .DisplayMeta import DisplayMeta



from .CouponSchedule import CouponSchedule

from .Validity import Validity

from .Ownership import Ownership



from .Identifier import Identifier

from .CouponAuthor import CouponAuthor


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    type_slug = fields.Str(required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    state = fields.Nested(State, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    code = fields.Str(required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    

