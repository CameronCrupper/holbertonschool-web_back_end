#!/usr/bin/env python3
"""
Flask Module
"""


from flask import Flask, jsonify, request, abort, redirect, make_response
from sqlalchemy.orm.exc import NoResultFound
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@ app.route('/profile', methods=['GET'])
def profile() -> str:
    """
    gets profile session id
    """
    session_id = request.cookies.get('session_id', None)

    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    return jsonify({"email": user.email}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
