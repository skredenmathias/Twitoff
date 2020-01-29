from flask import Flask
app = Flask(__name__)

@app.route('/')

def home():
    # Deployed model goes here
    return '<h1>Hello, World!</h1>'

if __name__ == "__main__":
    app.run(debug=True, port = 8080)

<!-- <select name="user1">
    {% for user in users %}
        <option value="{{ user.name }}">{{ user.name }}</option>
    {% endfor %}
</select>

name2

input form (compare route)
submit button 
{% endblock %}
-->
<!-- </body>
</html> -->