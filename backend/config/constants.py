import os
import pytz

##############################
# Config
##############################

STATUS = (
    ('active', 'Active'),
    ('inactive', 'Inactive'),
    ('deleted', 'Deleted'),
)
STATUS_DICT = dict(STATUS)

CATEGORIES = (
    ('ALL', 'ALL')
    ('Langerie', 'Langerie'),
    ('Swim Suite', 'Swim Suite'),
    ('Night Gowns', 'Night Gowns'),
)
CATEGORIES_DICT = dict(CATEGORIES)
