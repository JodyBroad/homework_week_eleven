# in reality, we would be calling this info from a database, dictionary of services to use for price_list

# to then make a dynamic list we could use for a drop down on a form:
# look through the dictionary using enumerate, this gives the index number for each entry which we can use as the
# back-end descriptor, get it to return the name of each service e.g. French Manicure etc
# save this as a separate list (in tuples, so (0, "French Manicure) etc etc
# and then use this to populate the drop down using SelectField


services = [

    {
        'service': 'French Manicure',
        'price': '£30',
        'nail_artist': 'Jody Broad',
        'time_required': '45 minutes'
    },
    {
        'service': 'Gel Polish',
        'price': '£45',
        'nail_artist': 'Alice Caffyn',
        'time_required': '1 hour'
    },
    {
        'service': 'Soak and remove existing gel polish',
        'price': '£5',
        'nail_artist': 'Jody Broad',
        'time_required': '15 minutes'
    },
    {
        'service': 'Acrylic nails - full set',
        'price': '£85',
        'nail_artist': 'Alice Caffyn',
        'time_required': ' 1 hour 45 minutes'
    },
    {
        'service': 'Acrylic nails - infills',
        'price': '£35',
        'nail_artist': 'Alice Caffyn',
        'time_required': '25 minutes'
    }

]

# this is basically the list i need to generate to get a dynamic list - but how do i get it to make this for me?
services_list = [(0, "French Manicure"), (1, "Gel polish"), (2, "Soak and remove existing gel polish"),
                 (3, "Acrylic nails - full set"), (4, "Acrylic nails - infills")]

# this gives the service list names as a basic list, need this to be a list of tuples with index number
# def services_dropdown():
#     service_list = []
#     i = 0
#     for service in services:
#         for service_name in services:
#             service_list.append(services[i]['service'])
#             i += 1
#         return service_list
#
# print(services_dropdown())

# how do i get it in the tuple format victoria suggested with enumerate?
# def services_dropdown():
#     service_list = []
#     for service in services:
#         for count, service_name in enumerate(services):
#             service_list.append(services[count]['service'])
#         return (count, service_list)
#
# print(services_dropdown())

# got it doing the first tuple, but this is still very much not right, why isn't it looping over the other dictionaries?
def services_dropdown():
    service_list = []
    list_entry = ()
    for index in range(len(services)):
        for count, key in enumerate(services[index]):
            list_entry = (count, services[index]['service'])
            service_list.append(list_entry)
            return list_entry
    service_list.append(list_entry)
    return service_list

print(services_dropdown())