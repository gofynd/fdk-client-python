"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Ownership import Ownership

from .Validation import Validation

from .Identifier import Identifier



from .State import State

from .CouponAction import CouponAction



from .CouponAuthor import CouponAuthor

from .Restrictions import Restrictions

from .Validity import Validity

from .RuleDefinition import RuleDefinition

from .DisplayMeta import DisplayMeta

from .CouponSchedule import CouponSchedule



from .CouponDateMeta import CouponDateMeta

from .Rule import Rule


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    ownership = fields.Nested(Ownership, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    code = fields.Str(required=False)
    
    state = fields.Nested(State, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    type_slug = fields.Str(required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    

