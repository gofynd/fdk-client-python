"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Restrictions import Restrictions

from .RuleDefinition import RuleDefinition

from .CouponAuthor import CouponAuthor

from .Rule import Rule

from .CouponSchedule import CouponSchedule

from .Identifier import Identifier

from .Ownership import Ownership

from .State import State



from .CouponAction import CouponAction



from .Validity import Validity



from .Validation import Validation

from .CouponDateMeta import CouponDateMeta

from .DisplayMeta import DisplayMeta


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    restrictions = fields.Nested(Restrictions, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    state = fields.Nested(State, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    type_slug = fields.Str(required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    code = fields.Str(required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    

