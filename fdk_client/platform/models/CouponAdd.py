"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Rule import Rule

from .Restrictions import Restrictions

from .DisplayMeta import DisplayMeta

from .State import State

from .RuleDefinition import RuleDefinition

from .CouponAction import CouponAction

from .Validity import Validity

from .CouponDateMeta import CouponDateMeta



from .Identifier import Identifier

from .CouponAuthor import CouponAuthor



from .CouponSchedule import CouponSchedule

from .Ownership import Ownership



from .Validation import Validation


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    state = fields.Nested(State, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    code = fields.Str(required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    type_slug = fields.Str(required=False)
    
    validation = fields.Nested(Validation, required=False)
    

