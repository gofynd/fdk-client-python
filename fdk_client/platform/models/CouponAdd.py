"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Ownership import Ownership

from .CouponAuthor import CouponAuthor

from .Restrictions import Restrictions

from .Identifier import Identifier

from .DisplayMeta import DisplayMeta

from .CouponDateMeta import CouponDateMeta

from .Validity import Validity

from .CouponAction import CouponAction



from .Rule import Rule



from .Validation import Validation

from .RuleDefinition import RuleDefinition

from .CouponSchedule import CouponSchedule



from .State import State


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    ownership = fields.Nested(Ownership, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    code = fields.Str(required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    type_slug = fields.Str(required=False)
    
    state = fields.Nested(State, required=False)
    

