"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .State import State

from .Rule import Rule







from .RuleDefinition import RuleDefinition

from .Identifier import Identifier

from .CouponAuthor import CouponAuthor

from .CouponSchedule import CouponSchedule

from .DisplayMeta import DisplayMeta

from .CouponDateMeta import CouponDateMeta

from .Restrictions import Restrictions

from .Ownership import Ownership

from .Validation import Validation

from .Validity import Validity

from .CouponAction import CouponAction


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    state = fields.Nested(State, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    code = fields.Str(required=False)
    
    type_slug = fields.Str(required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    

