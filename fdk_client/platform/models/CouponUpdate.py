"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CouponAuthor import CouponAuthor

from .Ownership import Ownership

from .CouponDateMeta import CouponDateMeta

from .Rule import Rule

from .State import State

from .Validity import Validity

from .CouponAction import CouponAction





from .Validation import Validation

from .CouponSchedule import CouponSchedule

from .RuleDefinition import RuleDefinition

from .Restrictions import Restrictions

from .Identifier import Identifier



from .DisplayMeta import DisplayMeta


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    author = fields.Nested(CouponAuthor, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    state = fields.Nested(State, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    code = fields.Str(required=False)
    
    type_slug = fields.Str(required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    

