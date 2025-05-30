from flask import Blueprint, render_template
from flask_login import login_required, current_user

from flask import Blueprint, session, redirect, url_for, render_template, request

from applications.common.admin import get_captcha, login_log
from applications.common.utils.http import fail_api, success_api
from applications.models import User



bp = Blueprint('index', __name__, url_prefix='/')


# 首页
@bp.get('/')
@login_required
def index():
    user = current_user
    return render_template('system/index.html', user=user)

