from flask import Blueprint
from flask_login import current_user
from flask import render_template, redirect, url_for, flash, request
from app.lib.base.provider import Provider
from flask import send_file
import os

bp = Blueprint('password', __name__)


@bp.route('/', methods=['GET'])
def index():
    provider = Provider()
    users = provider.users()
    if users.get_user_count() == 0:
        # Looks like we need to setup the administrator.
        return redirect(url_for('install.index'))

    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))

    return render_template(
        'home/password.html'
    )

@bp.route('/save', methods=['POST'])
def save():
    provider = Provider()
    users = provider.users()
    if users.get_user_count() == 0:
        # Looks like we need to setup the administrator.
        return redirect(url_for('install.index'))

    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))

    settings = provider.settings()
    hashes = request.form['Passwords']
    upload_path = settings.get('wordlists_path')
    try:
        f = open(upload_path+os.sep+'/manual_passwords', "a")
        f.writelines(hashes);
        f.writelines('\n');
        f.close()
    except:
        print("Exception occurred during file appending")
        f.close()

    print(hashes)

    return redirect(url_for('home.index'))

@bp.route('/download', methods=['POST'])
def download():
    provider = Provider()
    users = provider.users()
    if users.get_user_count() == 0:
        # Looks like we need to setup the administrator.
        return redirect(url_for('install.index'))

    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))

    return send_file('/opt/passwords.txt', as_attachment=True)
