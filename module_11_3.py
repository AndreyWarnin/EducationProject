import inspect
from inspect import getmodule

class IntrospectionClass:
    list_elements = []
    dict_elements = {}

    def __init__(self, intro_arg, *intro_args):
        self.intro_arg = intro_arg
        self.intro_args = intro_args

    def __str__(self):
        return 'introspection_class'

    def show_message(self):
        print('this is a message')


def introspection_info(obj):
    attributes = []
    methods = []
    obj_type = type(obj)
    module = getmodule(obj)

    attributes.extend(obj.__dict__.keys())
    members = inspect.getmembers(obj)
    for a, b in members:
        if inspect.ismethod(b):
            methods.append(b)

    dict_ = {'type': obj_type, 'attributes': attributes, 'methods':methods, 'module':module}
    print(f'type: {dict_['type']}, attributes: {dict_['attributes']}, methods: {dict_['methods']}, module: {dict_['module']}')

introspection_info(IntrospectionClass('intr_arg', *('ar1', 'ar2', 'ar3')))
