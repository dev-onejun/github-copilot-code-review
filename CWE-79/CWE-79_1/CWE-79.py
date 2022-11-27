from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<p>Hello World!</p>'

# function which says hello to the user
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name
    # return '<p>Hello, %s!</p>' % name

# run server
if __name__ == '__main__':
    app.run(debug=True)

"""
# example
http://localhost:5000/user/<script>alert('hi')</script>

# result
127.0.0.1 - - [08/Nov/2022 14:23:12] "GET /user/%3Cscript%3Ealert('hi')%3C/script%3E HTTP/1.1" 404 -
<html>
Not Found

The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.
</html>
"""