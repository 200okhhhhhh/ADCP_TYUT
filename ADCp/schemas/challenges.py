from CTFd.models import ma, Challenges
#导入了 Marshmallow 库中的 ModelSchema 类以及 CTFd 应用程序中的 Challenges 模型。
#Challenges 模型是 CTFd 应用程序中表示挑战的数据库模型。
class ChallengeSchema(ma.ModelSchema):
    #这是一个定义的 Python 类 ChallengeSchema，它继承自 Marshmallow 库中的 ModelSchema 类。
    #这意味着 ChallengeSchema 类可以用于将数据库模型转换为序列化的 JSON 对象，以及将 JSON 对象反序列化为数据库模型。
    class Meta:#这是内部类，用于定义元数据配置选项。
        model = Challenges#在 Meta 类中，model 属性指定了要序列化和反序列化的数据库模型，这里是 Challenges 模型。
        include_fk = True#是 Marshmallow 中的一个选项，用于控制是否包含外键字段。在这里，设置为 True 表示要包含外键字段。
        dump_only = ("id",)# 是 Marshmallow 中的另一个选项，用于指定在序列化对象时哪些字段是只读的。
        #在这里，指定了 "id" 字段为只读，意味着在序列化挑战对象时，"id" 字段的值将被包含在结果中，但不会被用于反序列化。
