"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Ownership import Ownership

from .Validity import Validity

from .CouponAuthor import CouponAuthor

from .RuleDefinition import RuleDefinition

from .State import State

from .Rule import Rule

from .Validation import Validation



from .CouponSchedule import CouponSchedule

from .CouponDateMeta import CouponDateMeta



from .DisplayMeta import DisplayMeta

from .Restrictions import Restrictions

from .Identifier import Identifier



from .CouponAction import CouponAction


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    ownership = fields.Nested(Ownership, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    state = fields.Nested(State, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    type_slug = fields.Str(required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    code = fields.Str(required=False)
    
    action = fields.Nested(CouponAction, required=False)
    

