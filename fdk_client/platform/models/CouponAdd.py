"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .RuleDefinition import RuleDefinition



from .CouponSchedule import CouponSchedule

from .Identifier import Identifier

from .CouponAction import CouponAction



from .Ownership import Ownership

from .CouponDateMeta import CouponDateMeta

from .CouponAuthor import CouponAuthor

from .DisplayMeta import DisplayMeta

from .Restrictions import Restrictions

from .Rule import Rule



from .State import State

from .Validation import Validation

from .Validity import Validity


class CouponAdd(BaseSchema):
    # Cart swagger.json

    
    rule_definition = fields.Nested(RuleDefinition, required=False)
    
    code = fields.Str(required=False)
    
    _schedule = fields.Nested(CouponSchedule, required=False)
    
    identifiers = fields.Nested(Identifier, required=False)
    
    action = fields.Nested(CouponAction, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    date_meta = fields.Nested(CouponDateMeta, required=False)
    
    author = fields.Nested(CouponAuthor, required=False)
    
    display_meta = fields.Nested(DisplayMeta, required=False)
    
    restrictions = fields.Nested(Restrictions, required=False)
    
    rule = fields.List(fields.Nested(Rule, required=False), required=False)
    
    type_slug = fields.Str(required=False)
    
    state = fields.Nested(State, required=False)
    
    validation = fields.Nested(Validation, required=False)
    
    validity = fields.Nested(Validity, required=False)
    

