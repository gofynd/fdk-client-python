"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Restrictions import Restrictions

from .State import State

from .CouponAction import CouponAction

from .Ownership import Ownership

from .DisplayMeta import DisplayMeta



from .Validation import Validation

from .RuleDefinition import RuleDefinition

from .CouponDateMeta import CouponDateMeta

from .CouponSchedule import CouponSchedule



from .Validity import Validity

from .CouponAuthor import CouponAuthor

from .Identifier import Identifier

from .Rule import Rule


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    type_slug = fields.Str(required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    state = fields.Nested(State, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    code = fields.Str(required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    

