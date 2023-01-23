from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/<page>')
def load_page(page):
    return render_template(f'{page}')

def write_database(data):
    with open('database.csv', 'a', newline='') as file:
        name = data['name']
        email = data['email']
        message = data['message']
        csv_writer = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_database(data)
            return redirect('/submitted.html')
        except:
            return 'Response was not saved to database. Try again.'
    elif request.method == 'GET':
        print('the method was GET')
    else:
        return 'Something went wrong.'