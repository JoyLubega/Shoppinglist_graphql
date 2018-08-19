def validate_empty_strings(**kwargs):
    """
    Function to validate empty fields when
    saving an object
    :params kwargs
    """
    for field in kwargs:
        if not kwargs.get(field):
            raise AttributeError("{} is required".format(field))

def update_entity_fields(entity, **kwargs):
    """
    Function to update an entities fields
    :param kwargs
    :param entity
    """
    keys = kwargs.keys()
    for key in keys:
        exec("entity.{0} = kwargs['{0}']".format(key))
    return entity