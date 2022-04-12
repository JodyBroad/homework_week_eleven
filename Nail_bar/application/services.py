# in reality, we would be calling this info from a database, dictionary of services to use for price_list

# move the services dictionary here

# to then make a dynamic list we could use for a drop down on a form:
# look through the dictionary using enumerate, this gives the index number for each entry which we can use as the
# back-end descriptor, get it to return the name of each service e.g. French Manicure etc
# save this as a separate list (in tuples, so (0, "French Manicure) etc etc
# and then use this to populate the drop down using SelectField

# also clean stuff up - have a seperate routes file, and an app file, we don't have __init__.py file as isn't currently
# a package and we also don't have app.py, we have nail_bar_app

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
