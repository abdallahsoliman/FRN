from flask import Flask, render_template
from settings import Common
import yaml, os, re


application = Flask(__name__)
application.config.from_object(Common)

@application.route("/")
def index():
    sponsors = get_config("sponsors")
    events = get_config("events")
    return render_template(
            "index.html",
            sponsors=sponsors,
            events=events,
    )

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
