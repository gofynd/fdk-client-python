"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Identifier import Identifier

from .Validity import Validity

from .Validation import Validation

from .CouponAction import CouponAction

from .DisplayMeta import DisplayMeta



from .State import State

from .Ownership import Ownership



from .CouponDateMeta import CouponDateMeta

from .Rule import Rule

from .CouponSchedule import CouponSchedule

from .RuleDefinition import RuleDefinition



from .Restrictions import Restrictions

from .CouponAuthor import CouponAuthor


class CouponUpdate(BaseSchema):
    # Cart swagger.json

    
    identifiers = fields.Nested(Identifier, required=False)
    
    validity = fields.Nested(Validity, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    code = fields.Str(required=False)
    
    state = fields.Nested(State, required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    type_slug = fields.Str(required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    

