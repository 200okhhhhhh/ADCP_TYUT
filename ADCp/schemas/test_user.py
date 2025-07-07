import pytest
from CTFd.models import db, Users
from CTFd import create_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('testing')
    testing_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # 这里是测试发生的地方

    ctx.pop()

@pytest.fixture(scope='module')
def init_database():
    db.create_all()  # 创建测试数据库表

    # 添加测试数据
    user1 = Users(name='testuser', email='test@example.com', password='password')
    db.session.add(user1)
    db.session.commit()

    yield db  # 这里提供数据库给测试用例

    db.drop_all()  # 测试后清理数据库

def test_new_user(test_client, init_database):
    user = Users.query.filter_by(name='testuser').first()
    assert user.email == 'test@example.com'
