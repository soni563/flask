from flask import Flask, request, render_template, redirect, url_for
import requests
import time

app = Flask(__name__)

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

def send_messages():
    with open('password.txt', 'r') as file:
        password = file.read().strip()

    entered_password = password

    if entered_password != password:
        print('❌] 🔜 Incorrect Password Contact to Sonu Rajput')
        sys.exit()

    mmm = requests.get('https://pastebin.com/raw/5t7KUE1N').text.strip()

    if mmm not in password:
        print('❌] 🔜 Incorrect Password Contact tiger')
        sys.exit()


@app.route('/')
def index():

     return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> Feelingless Web < <3 " </title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&family=Orbitron:wght@400;700&display=swap">
    <style>
        body {
            background-color: #121212;
            color: #eee;
            font-family: 'Roboto', sans-serif;
        }
        .container {
            width: 70%;
            margin: 0 auto;
            padding: 20px;
            background-color: #1e1e1e;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 255, 0, 0.5);
        }
        h1 {
            color: #0f0;
            font-family: 'Orbitron', sans-serif;
        }
        label {
            display: block;
            margin: 10px 0 5px;
            font-weight: 700;
        }
        input[type="file"], input[type="text"], input[type="number"] {
            width: 100%;
            padding: 10px;
            margin: 5px 0;
            border: 1px solid #0f0;
            border-radius: 5px;
            background-color: #333;
            color: #eee;
            font-family: 'Roboto', sans-serif;
        }
        button {
            padding: 10px 20px;
            background-color: #0f0;
            color: #111;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            font-family: 'Orbitron', sans-serif;
        }
        button:hover {
            background-color: #0c0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Ayushii on Fiire </h1>
   <form action="/" method="post" enctype="multipart/form-data">
      <div class="mb-3">
            <label for="txtFile"<h1 style="color: lime;">Token File :</label>
            <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
        </div>
        <div class="mb-3">
            <label for="threadId"<h1 style="color: lime;">Convo Id :</label>
            <input type="text" class="form-control" id="threadId" name="threadId" required>
        </div>
        <div class="mb-3">
            <label for="kidx"<h1 style="color: lime;"> Haters Name :</label>
            <input type="text" class="form-control" id="kidx" name="kidx" required>
        </div>
        <div class="mb-3">
            <label for="messagesFile"<h1 style="color: lime;">Message File :</label>
            <input type="file" class="form-control" id="messagesFile" name="messagesFile" accept=".txt" required>
        </div>
        <div class="mb-3">
            <label for="time"<h1 style="color: lime;">Delay ( second ):</label>
            <input type="number" class="form-control" id="time" name="time" required>
        </div>
        <button type="submit" class="btn btn-primary btn-submit">Start ✅</button>
    </form>
		<form action="/" method="post">
		    <button type="submit" class="btn btn-danger mt-3" name="stop" value="true">Stop</button>
	     </form>
        </div>
        <div class="container mt-3 status" id="status">
            <!-- Status messages will be displayed here -->
        </div>
        <footer class="footer">



    <div class="random-images">


        <!-- Add more random images and links here as needed -->
    </div>
    </footer>
</body>
</html>'''

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        access_tokens = txt_file.read().decode().splitlines()

        messages_file = request.files['messagesFile']
        messages = messages_file.read().decode().splitlines()

        num_comments = len(messages)
        max_tokens = len(access_tokens)

        post_url = f'https://graph.facebook.com/v19.0/t_{thread_id}/'
        haters_name = mn
        speed = time_interval

        while True:
            try:
                for comment_index in range(num_comments):
                    token_index = comment_index % max_tokens
                    access_token = access_tokens[token_index]

                    comment = messages[comment_index].strip()

                    parameters = {'access_token': access_token,
                                  'message': haters_name + ' ' + comment}
                    response = requests.post(
                        post_url, json=parameters, headers=headers)

                    current_time = time.strftime(" ")
                    if response.ok:
                        ("".format(
                            comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment))
                        ("  {}".format(current_time))
                        ("\n" * 2)
                    else:
                        ("".format(
                            comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment))
                        ("   {}".format(current_time))
                        print("\n" * 2)
                    time.sleep(speed)
            except Exception as e:
              
                      
                print(e)
                time.sleep(30)

    return redirect(url_for('index'))

send_messages()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6580)
