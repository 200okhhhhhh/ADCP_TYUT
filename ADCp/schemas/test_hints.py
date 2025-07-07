import pytest
from CTFd.models import Hints
from CTFd.schemas import HintSchema
from CTFd.utils import string_types
from werkzeug.wsgi import DispatcherMiddleware 
@pytest.fixture
def hint_data():
    return {
        "challenge": 1,
        "content": "This is a hint",
        "cost": 50,
        "type": "standard"
    }

def test_hint_schema_dump_only_fields():
    schema = HintSchema()
    dump_only_fields = schema.opts.dump_only
    assert "id" in dump_only_fields
    assert "type" in dump_only_fields

def test_hint_schema_validation(hint_data):
    # 创建一个 HintSchema 实例
    schema = HintSchema()

    # 验证数据
    validated_data = schema.load(hint_data)
    
    # 预期验证成功
    assert validated_data == hint_data

def test_hint_schema_views(hint_data):
    # 测试不同视图下的字段选择
    schema = HintSchema()

    # 测试 locked 视图
    locked_view = schema.dump(hint_data, view="locked")
    assert set(locked_view.keys()) == {"id", "type", "challenge", "cost"}

    # 测试 unlocked 视图
    unlocked_view = schema.dump(hint_data, view="unlocked")
    assert set(unlocked_view.keys()) == {"id", "type", "challenge", "content", "cost"}

    # 测试 admin 视图
    admin_view = schema.dump(hint_data, view="admin")
    assert set(admin_view.keys()) == {"id", "type", "challenge", "content", "cost", "requirements"}
