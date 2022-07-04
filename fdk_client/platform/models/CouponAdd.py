"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DisplayMeta import DisplayMeta



from .CouponSchedule import CouponSchedule

from .Restrictions import Restrictions



from .RuleDefinition import RuleDefinition

from .State import State

from .Validation import Validation

from .Ownership import Ownership

from .Identifier import Identifier

from .CouponAction import CouponAction

from .Validity import Validity



from .CouponAuthor import CouponAuthor

from .CouponDateMeta import CouponDateMeta

from .Rule import Rule


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    type_slug = fields.Str(required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    code = fields.Str(required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    state = fields.Nested(State, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    

