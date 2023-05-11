from flask import Flask, render_template

app = Flask(__name__)

users = {
    'user1': {
        'name': 'User One',
        'email': 'user1@example.com'
    },
    'user2': {
        'name': 'User Two',
        'email': 'user2@example.com'
    },
    'user3': {
        'name': 'User Three',
        'email': 'user3@example.com'
    },
    'user4': {
        'name': 'User Four',
        'email': 'user4@example.com'
    },
    'user5': {
        'name': 'User Five',
        'email': 'user5@example.com'
    },
}

#ToDo 完成以下程式/profile/userid
@app.route("ToDo")
def profile(userid):
    #ToDo
    return ""

if __name__ == '__main__':
    app.run(debug=True)