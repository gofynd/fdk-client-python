"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CouponAuthor import CouponAuthor



from .Validation import Validation

from .Identifier import Identifier

from .DisplayMeta import DisplayMeta

from .State import State



from .RuleDefinition import RuleDefinition

from .CouponDateMeta import CouponDateMeta

from .Restrictions import Restrictions

from .CouponAction import CouponAction

from .Ownership import Ownership

from .Validity import Validity

from .Rule import Rule



from .CouponSchedule import CouponSchedule


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    author = fields.Nested(CouponAuthor, required=False)
    
    type_slug = fields.Str(required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    state = fields.Nested(State, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    code = fields.Str(required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    

