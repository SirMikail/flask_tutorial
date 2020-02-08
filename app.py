from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/sample_database/<column_name>/<column_value>')
def sample(column_name, column_value):
    data = pd.read_csv('sample_data.csv')
    people = []

    column_name = column_name.replace('?', '').upper()
    headers = data.columns.values.tolist()
    headers = [x.replace('?', '').upper() for x in headers]
    for datum in data.values.tolist():
        datum = [str(x).upper() for x in datum]
        people.append(dict(zip(headers, datum)))

    holder = [x for x in people if str(x[column_name]) == column_value.upper()]
    return jsonify(holder)

if __name__ == '__main__':
    app.run()
