"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .CouponAuthor import CouponAuthor

from .RuleDefinition import RuleDefinition

from .Restrictions import Restrictions

from .CouponAction import CouponAction



from .DisplayMeta import DisplayMeta



from .Ownership import Ownership

from .Validation import Validation

from .CouponDateMeta import CouponDateMeta

from .Identifier import Identifier

from .CouponSchedule import CouponSchedule

from .Rule import Rule

from .Validity import Validity

from .State import State


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    code = fields.Str(required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    type_slug = fields.Str(required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    state = fields.Nested(State, required=False)
    

