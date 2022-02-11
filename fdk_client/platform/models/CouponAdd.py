"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Restrictions import Restrictions





from .Validation import Validation

from .State import State

from .Rule import Rule

from .CouponSchedule import CouponSchedule

from .CouponAuthor import CouponAuthor

from .Identifier import Identifier

from .RuleDefinition import RuleDefinition

from .DisplayMeta import DisplayMeta

from .Validity import Validity

from .CouponAction import CouponAction

from .Ownership import Ownership

from .CouponDateMeta import CouponDateMeta




class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    restrictions = fields.Nested(Restrictions, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    type_slug = fields.Str(required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    state = fields.Nested(State, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    code = fields.Str(required=False)
    

