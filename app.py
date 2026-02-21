from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/services/managed-network-wifi-solutions')
def managed_network():
    return render_template('services/managed-network-wifi-solutions.html')

@app.route('/services/commercial-access-control-systems')
def access_control():
    return render_template('services/commercial-access-control-systems.html')

@app.route('/services/commercial-cctv-surveillance')
def cctv():
    return render_template('services/commercial-cctv-surveillance.html')

@app.route('/services/structured-cabling-fiber-installation')
def structured_cabling():
    return render_template('services/structured-cabling-fiber-installation.html')

@app.route('/services/business-voip-phone-systems')
def business_phone():
    return render_template('services/business-voip-phone-systems.html')

@app.route('/services/commercial-tv-digital-display-solutions')
def tv_display():
    return render_template('services/commercial-tv-digital-display-solutions.html')

############### INDUSRIES ##############################################

@app.route('/industries')
def industries_all():
    return render_template('industries/industries-index.html')

@app.route('/industries/commercial-office')
def industry_office():
    return render_template('industries/commercial-office.html')

@app.route('/industries/hospitality')
def industry_hospitality():
    return render_template('industries/hospitality.html')

@app.route('/industries/warehouses-distribution')
def industry_warehouse():
    return render_template('industries/warehouses-distribution.html')

@app.route('/industries/multi-family-communities')
def industry_multifamily():
    return render_template('industries/multi-family-communities.html')


@app.route('/case-studies')
def case_studies():
    return render_template('case-studies.html')

# @app.route('/managed-network-wifi-solutions')
# def managed_network():
#     return render_template('managed-network-wifi.html')

if __name__ == '__main__':
    app.run(debug=True)