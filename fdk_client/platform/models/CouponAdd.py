"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .State import State

from .Ownership import Ownership



from .CouponSchedule import CouponSchedule



from .DisplayMeta import DisplayMeta

from .Identifier import Identifier

from .CouponAuthor import CouponAuthor

from .CouponAction import CouponAction

from .RuleDefinition import RuleDefinition

from .Validity import Validity

from .Restrictions import Restrictions

from .CouponDateMeta import CouponDateMeta



from .Validation import Validation

from .Rule import Rule


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    state = fields.Nested(State, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    type_slug = fields.Str(required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    code = fields.Str(required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    

