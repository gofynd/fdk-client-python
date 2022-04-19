"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Validity import Validity

from .CouponSchedule import CouponSchedule

from .Ownership import Ownership

from .CouponAuthor import CouponAuthor

from .Restrictions import Restrictions



from .CouponDateMeta import CouponDateMeta

from .RuleDefinition import RuleDefinition

from .Identifier import Identifier

from .State import State



from .Validation import Validation

from .Rule import Rule

from .CouponAction import CouponAction



from .DisplayMeta import DisplayMeta


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    validity = fields.Nested(Validity, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    code = fields.Str(required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    state = fields.Nested(State, required=False)
    
    type_slug = fields.Str(required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    

