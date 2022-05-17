"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CouponDateMeta import CouponDateMeta





from .RuleDefinition import RuleDefinition

from .Rule import Rule

from .CouponSchedule import CouponSchedule

from .State import State

from .CouponAuthor import CouponAuthor

from .CouponAction import CouponAction

from .Validation import Validation

from .Validity import Validity



from .Restrictions import Restrictions

from .DisplayMeta import DisplayMeta

from .Ownership import Ownership

from .Identifier import Identifier


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    code = fields.Str(required=False)
    
    type_slug = fields.Str(required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    state = fields.Nested(State, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    

