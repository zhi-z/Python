作者：北漂-Public 
来源：CSDN 
原文：https://blog.csdn.net/xiaotao745324325/article/details/51834169 
版权声明：本文为博主原创文章，转载请附上博文链接！

# rest_framework中的ModelSerializer

1、ModelSerializer 比Serializer封装好了一层，直接自己生成的create和update，不用覆盖了，其实推荐用这个，毕竟Serializer封装的很低级，既然用django，就要用好点的。 

正常的应该是这样的 

```
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'account_name', 'users', 'created')
```

```
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
```

官网推荐用第一种，因为第二种，改变model时，可能无意会泄露数据

2、还有个省事的，exclude是除了某个字段，其他的都显示

```
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = ('users',)
```

3、当一个model有外键的时候，默认显示的是外键的id，此时要显示外键的所有值可以用下面，depth，会把外键的所有值显示出来 

```
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'account_name', 'users', 'created')
        depth = 1
```

4、如果一个serializer中，要包含出了model以外的字段，可以

```
class AccountSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    groups = serializers.PrimaryKeyRelatedField(many=True)
 
    class Meta:
        model = Account
```

5、把一个字段变成只读字段，需要如下操作，自增字段默认是只读的，不显式表示也是可以的 

```
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'account_name', 'users', 'created')
        read_only_fields = ('account_name',)
```

```
user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
```

6、把某一个字段变为只读，然后存储，通过额外字段指定。 

```
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}
 
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
```

7、关于外键的嵌套，嵌套类型的关系可以看http://www.django-rest-framework.org/api-guide/relations/   还没研究这个

8、可以使用父类的Meta 但是强烈不推荐

```
class AccountSerializer(MyBaseSerializer):
    class Meta(MyBaseSerializer.Meta):
        model = Account

```

9、然后就自定义字段了