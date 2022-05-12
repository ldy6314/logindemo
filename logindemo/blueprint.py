from flask import Blueprint, jsonify
from .models import User
from .extensions import db
bp = Blueprint('bp', __name__)


@bp.route('/')
def index():
    return jsonify("hello, world")


@bp.before_request
def init_db():
    print('init db')
    db.create_all()


@bp.route('/set_user')
def set_users():
    user_list = [
        {
            'username': 'ldy6314',
            'pwd': '123123'
        },
        {
            'username': 'ldy63142',
            'pwd': '123123'
        }
    ]
    try:
        for user in user_list:
            new_user = User(user.get('username'), user.get('pwd'))
            db.session.add(new_user)
        db.session.commit()
        return jsonify('add success')
    except Exception as e:
        print(e)
        return jsonify('add failed')


@bp.route('/users')
def get_users():
    resp = []
    res = User.query.all()
    for user in res:
        resp.append(
            {
                'username': user.username,
                'pwd': user.password_hash
            }
        )
    return jsonify(resp)