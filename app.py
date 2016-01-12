from flask import Flask, render_template, request
from settings import Common
import yaml, os, re
import stripe


application = Flask(__name__)
application.config.from_object(Common)
stripe.api_key = application.config['STRIPE_KEYS']['secret']

@application.route("/")
def index():
    sponsors = get_config("sponsors")
    events = get_config("events")
    stripeKey = application.config['STRIPE_KEYS']['publishable']
    gallery = get_gallery()
    print(gallery)
    return render_template(
            "index.html",
            sponsors=sponsors,
            events=events,
            stripeKey=stripeKey,
            gallery=gallery,
    )

@application.route("/charge", methods=['POST'])
def donate():
    try:
        stripe.Charge.create(
            amount = request.form['amount'],
            currency= 'usd',
            source = request.form['token'],
            description="Donation to CWRU Food Recovery Network from %s" % request.form['email']
        )
        status = "success"
        message= "Your donation has been processed. Thank you for your support!"
    except stripe.CardError as e:
        status = "danger"
        message = e.json_body['message']
    except (stripe.APIConnectionError, stripe.APIError, stripe.AuthenticationError, stripe.InvalidRequestError, stripe.RateLimitError) as e:
        status = "danger"
        message = "An error occurred while trying to process your donation. Please try again at another time."
    return render_template('base/alert.html', message=message, status=status)

def get_config(filename):
    """
    Retrieves contents of yaml configuration file
    Config directory is "FRN/config", file format is yml
    :param filename: name of the yaml file holding the desired configuration
    :return: contents of the file
    """
    filename = "%s.yaml" % filename if re.search('_*\.yaml$', filename) is None else filename
    data = []
    with open(os.path.join(application.config['CONFIG_DIR'], filename)) as f:
        for item in yaml.load_all(f):
            data.append(item)

    return data

def get_gallery():
    gallery = []
    for file in os.listdir(application.config['GALLERY_DIR_ABSOLUTE']):
        if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
            gallery.append(os.path.join(application.config['STATIC_DIR'], application.config['GALLERY_DIR'], file))
    return gallery

@application.context_processor
def group_rows():
    def _group_rows(data, n):
        """
        Groups data into rows with n items each
        :param data: data to group
        :param n: number of items per row
        :return: data grouped into rows with n items each
        """
        result = []
        for i, item in enumerate(data):
            if i % n == 0:
                result.append(list())
            result[-1].append(item)

        return result
    return dict(group_rows=_group_rows)

@application.context_processor
def is_last():
    def _is_last(item, data):
        return data[-1] == item
    return dict(is_last=_is_last)

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8000, debug=True)
