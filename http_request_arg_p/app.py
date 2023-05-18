from flask import Flask, request,render_template

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

#透過/profile?user_id={user_id}，取得對應的使用者，並透過template/profile.html渲染出name和email資訊
@app.route('/profile')
def profile():
    return ""

if __name__ == '__main__':
    app.run()
