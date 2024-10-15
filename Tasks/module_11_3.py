"""
introspect function
"""
import pprint
import inspect
import sys


def introspection_info(object):
    info_dictionary = {}

    try:
        info_dictionary['1: name'] = object.__name__
        info_dictionary['2: address'] = object
    except AttributeError as exc:
        info_dictionary['1: name'] = "simple object hasn't name"
        info_dictionary['2: value'] = object

    ## type
    info_dictionary['3: type'] = type(object)

    ## attributes (methods)    
    methods = []
    attributes = []

    for attr_name in dir(object):
        attr = getattr(object, attr_name)
        if callable(attr):
            # print(f"Method: {attr_name} - {type(attr)} ")
            methods.append(attr_name)
        else:
            # print(f"Attr: {attr_name} - {type(attr)} ")
            attributes.append(attr_name)
    
    info_dictionary['4: attributes'] = attributes
    info_dictionary['5: methods'] = methods
        
    ## base module
    # if inspect.getmodule(object) == None:
    info_dictionary['6: module'] = f" '{__name__}' from '{sys.argv[0]}' "
    # else:
        # info_dictionary['6: module'] = inspect.getmodule(object)

    return info_dictionary

m_list = []
class ABC():
    def calling():
        print("it's call")
m_class = ABC
m_string = 'alfnma'

number_info = introspection_info(42)
# number_info = introspection_info(m_list)
# number_info = introspection_info(m_class)
# number_info = introspection_info(m_string)
print()
pprint.pprint(number_info)


# class Intro:
#     def __init__(self, object) -> None:
#         self.object = object

#     def __call__(self):
#         return introspection_info(self.object)

# m_str = "sdgfsdg"
# get_info = Intro(m_str)
# pprint.pprint(get_info())
