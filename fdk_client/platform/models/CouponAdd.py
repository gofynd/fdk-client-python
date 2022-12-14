"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Rule import Rule

from .State import State

from .Ownership import Ownership



from .CouponDateMeta import CouponDateMeta

from .CouponSchedule import CouponSchedule

from .CouponAction import CouponAction

from .DisplayMeta import DisplayMeta

from .Validity import Validity

from .Restrictions import Restrictions

from .RuleDefinition import RuleDefinition

from .Identifier import Identifier

from .Validation import Validation



from .CouponAuthor import CouponAuthor


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    tags = fields.List(fields.Str(required=False), required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    state = fields.Nested(State, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    code = fields.Str(required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    type_slug = fields.Str(required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    

