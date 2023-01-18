"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .State import State

from .DisplayMeta import DisplayMeta





from .Validation import Validation

from .Validity import Validity

from .CouponSchedule import CouponSchedule

from .Identifier import Identifier

from .CouponAuthor import CouponAuthor

from .Rule import Rule

from .RuleDefinition import RuleDefinition

from .CouponDateMeta import CouponDateMeta

from .Ownership import Ownership

from .CouponAction import CouponAction

from .Restrictions import Restrictions




class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    state = fields.Nested(State, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    code = fields.Str(required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    type_slug = fields.Str(required=False)
    

