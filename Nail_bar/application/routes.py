from flask import Flask, render_template, url_for, request

from application import app, services

from forms import ContactForm, AppointmentForm

# can use more than one decorator at a time, so if you typed either '/' or '/home' you get the same stuff returned


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/price_list')
def price_list():
    return render_template('price_list.html', title='Price List', services=services)


# uses the secret maths template
@app.route('/cube/<int:number>')
def cube(number):
    cubed = number ** 3
    line_cube = "Your number cubed is" + " " + str(cubed)
    return render_template('maths.html', line_cube=line_cube)


# uses the secret maths template
@app.route('/modulus/<int:number>')
def modulus(number):
    remainder = number % 2
    if remainder == 0:
        line_mod = "Your number is even"
    else:
        line_mod = "Your number is odd"
    return render_template('maths.html', line_mod=line_mod)


# will redirect if they type in something random using url_for()
@app.route('/dynamic/<word>')
def home_redirect(word):
    destination = url_for('home')
    return render_template('redirect.html', destination=destination)

# this one does the validation in the forms.py code using wtforms.validators
@app.route('/appointment', methods=['GET', 'POST'])
def appointment():
    error = ""
    form = AppointmentForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            booking_info = f'Appointment request for {form.service.data} at {form.time.data} sent!'
            return render_template('appointment_booked.html', booking_info=booking_info)

    return render_template('appointment.html', title='Appointments', form=form, message=error)


# will post an appointment request - would do this using a form when we know how!
@app.route('/post/appointment', methods=['POST'])
def post_text():
    data_sent = request.data.decode('utf-8')
    return render_template('appointment.html', data_sent=data_sent, mimetype='text/plain')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    error = ""
    form = ContactForm()

    # contrast this to the data validator - per the class notes - see AppointmentForm
    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        message = form.message.data

        if len(first_name) == 0 or len(last_name) == 0 or len(email) == 0 or '@' not in email or len(message) == 0:
            error = "Please supply all required fields"
        else:
            return 'Thank you for contacting us. We will respond to you shortly'
    return render_template('contact.html', title='Contact Us', form=form, message=error)