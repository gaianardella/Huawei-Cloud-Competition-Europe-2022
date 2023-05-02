from flask import Flask, request, redirect, render_template, session
from obs import ObsClient, CorsRule, Options
from datetime import datetime
# import huaweicloud
import boto3

app = Flask(__name__)
app.secret_key = 'secret_key'  # replace with a secret key of your own
app.debug = True



users = [
    {
        'username': 'user1',
        'password': 'password1'
    },
    {
        'username': 'user2',
        'password': 'password2'
    },
    {
        'username': 'user3',
        'password': 'password3'
    }
]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Validate the user's login information
    for user in users:
        if user['username'] == username and user['password'] == password:
            session['auth_token'] = '<Your Authentication Token>'
            return redirect('/upload')

    # If the login information is valid, store the authentication token in a session
    # session['auth_token'] = '<Your Authentication Token>'

    # return redirect('/upload')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     # Get the form data from the request
#     username = request.form['username']
#     password = request.form['password']

#         # Validate the user's registration information

#         # If the registration information is valid, store the user's account information
#         # ...

#     return redirect('/register')

#     # return render_template('register.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Check if the user clicked the "Top" button
        if 'top_btn' in request.form:
            # # Upload the file and redirect to top.html
            # file = request.files['file']

            return redirect('/top')

        # Check if the user clicked the "Bottom" button
        elif 'bottom_btn' in request.form:
            # Upload the file and redirect to bottom.html
            file = request.files['file']

            # Connect to Huawei Cloud and upload the image to the bucket
            # obs = huaweicloud.OBS({
            #     'access_key_id': '<Your Access Key ID>',
            #     'secret_access_key': '<Your Secret Access Key>',
            #     'server': 'obs.cn-north-4.myhuaweicloud.com'
            # })
            # obs.put_object('<Your Bucket Name>', '<Your Object Key>', file.read())

            return redirect('/bottom')

    return render_template('upload.html')

@app.route('/top', methods=['GET', 'POST'])
def top():
    if request.method == 'POST':
        # Upload the file and redirect to top.html
        file = request.files['file']

        obsClient = ObsClient(access_key_id='xxxx', secret_access_key='xxxx', server='obs.eu-west-101.myhuaweicloud.eu')
        bucketClient = obsClient.bucketClient('clothes')
        
        # Getting the current date and time
        dt = datetime.now()
        # getting the timestamp
        ts = datetime.timestamp(dt)

        resp = bucketClient.putContent('top' + str(ts), file.read())
   
        return redirect('/success')

    return render_template('top.html')

if __name__ == '__main__':
    app.run()


@app.route('/bottom', methods=['GET', 'POST'])
def bottom():
    # Upload the file and redirect to top.html
        file = request.files['file']

        obsClient = ObsClient(access_key_id='xxxx', secret_access_key='xxxx', server='obs.eu-west-101.myhuaweicloud.eu')
        bucketClient = obsClient.bucketClient('clothes')
        
        # Getting the current date and time
        dt = datetime.now()
        # getting the timestamp
        ts = datetime.timestamp(dt)

        resp = bucketClient.putContent('bottom' + str(ts), file.read())
   
        return redirect('/success')

    return render_template('bottom.html')


if __name__ == '__main__':
    app.run()
