"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Identifier import Identifier

from .DisplayMeta import DisplayMeta

from .Restrictions import Restrictions

from .Rule import Rule

from .CouponAction import CouponAction

from .Ownership import Ownership

from .CouponDateMeta import CouponDateMeta

from .Validity import Validity

from .CouponAuthor import CouponAuthor

from .CouponSchedule import CouponSchedule



from .Validation import Validation





from .State import State

from .RuleDefinition import RuleDefinition


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    identifiers = fields.Nested(Identifier, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    type_slug = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    state = fields.Nested(State, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    

