"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DisplayMeta import DisplayMeta

from .Identifier import Identifier

from .Validity import Validity

from .CouponAuthor import CouponAuthor

from .CouponDateMeta import CouponDateMeta



from .Restrictions import Restrictions



from .RuleDefinition import RuleDefinition

from .CouponSchedule import CouponSchedule

from .Ownership import Ownership

from .Validation import Validation

from .CouponAction import CouponAction

from .State import State

from .Rule import Rule




class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    type_slug = fields.Str(required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    code = fields.Str(required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    state = fields.Nested(State, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    

