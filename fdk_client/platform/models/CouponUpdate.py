"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .RuleDefinition import RuleDefinition

from .Identifier import Identifier



from .Validity import Validity

from .DisplayMeta import DisplayMeta

from .Ownership import Ownership

from .CouponSchedule import CouponSchedule

from .Validation import Validation





from .CouponAuthor import CouponAuthor

from .CouponDateMeta import CouponDateMeta

from .Rule import Rule

from .CouponAction import CouponAction

from .State import State

from .Restrictions import Restrictions


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    code = fields.Str(required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    type_slug = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    state = fields.Nested(State, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    

