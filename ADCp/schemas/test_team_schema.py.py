import pytest
from marshmallow import ValidationError
from CTFd.models import Teams
from CTFd.schemas.teams import TeamSchema

# 准备测试数据
@pytest.fixture
def team_data():
    return {
        "name": "Test Team",
        "email": "test@example.com",
        "website": "http://www.example.com",
        "country": "US"
    }

# 测试 TeamSchema 是否能正确加载合法数据
def test_team_schema_load_valid_data(team_data):
    schema = TeamSchema()
    result = schema.load(team_data)
    assert result["name"] == "Test Team"
    assert result["email"] == "test@example.com"

# 测试 TeamSchema 在数据非法时是否抛出 ValidationError
def test_team_schema_load_invalid_data(team_data):
    schema = TeamSchema()
    team_data['email'] = 'not-an-email'  # 故意提供一个格式错误的电子邮件地址
    with pytest.raises(ValidationError):
        schema.load(team_data)
