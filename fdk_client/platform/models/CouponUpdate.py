"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Restrictions import Restrictions

from .Ownership import Ownership

from .Rule import Rule



from .Validation import Validation

from .CouponAuthor import CouponAuthor



from .CouponDateMeta import CouponDateMeta

from .DisplayMeta import DisplayMeta



from .Validity import Validity

from .CouponAction import CouponAction

from .State import State

from .RuleDefinition import RuleDefinition

from .Identifier import Identifier

from .CouponSchedule import CouponSchedule


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    restrictions = fields.Nested(Restrictions, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    code = fields.Str(required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    type_slug = fields.Str(required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    state = fields.Nested(State, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    

