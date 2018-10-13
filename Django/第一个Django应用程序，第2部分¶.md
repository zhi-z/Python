# 第一个Django应用程序，第2部分[¶](https://docs.djangoproject.com/en/2.1/intro/tutorial02/#writing-your-first-django-app-part-2)

本教程从[教程1](https://docs.djangoproject.com/en/2.1/intro/tutorial01/)停止的地方开始。我们将设置数据库，创建您的第一个模型，并快速介绍Django自动生成的管理站点。

## 数据库设置[¶](https://docs.djangoproject.com/en/2.1/intro/tutorial02/#database-setup)

现在，打开`mysite/settings.py`。这是一个普通的Python模块，其中模块级变量代表Django设置。

默认情况下，配置使用SQLite。如果您是数据库新手，或者您只是想尝试Django，这是最简单的选择。SQLite包含在Python中，因此您无需安装任何其他东西来支持您的数据库。但是，在启动第一个真正的项目时，您可能希望使用像PostgreSQL这样的更具伸缩性的数据库，以避免数据库切换问题。

如果要使用其他数据库，请安装相应的[数据库绑定](https://docs.djangoproject.com/en/2.1/topics/install/#database-installation)并更改项中的以下键 以匹配数据库连接设置：[`DATABASES`](https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-DATABASES) `'default'`

- [`ENGINE`](https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-DATABASE-ENGINE)-要么 `'django.db.backends.sqlite3'`， `'django.db.backends.postgresql'`，`'django.db.backends.mysql'`，或 `'django.db.backends.oracle'`。其他后端[也可用](https://docs.djangoproject.com/en/2.1/ref/databases/#third-party-notes)。
- [`NAME`](https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-NAME) - 数据库的名称。如果您使用的是SQLite，则数据库将是您计算机上的文件; 在这种情况下，[`NAME`](https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-NAME) 应该是该文件的完整绝对路径，包括文件名。默认值,, 将文件存储在项目目录中。`os.path.join(BASE_DIR, 'db.sqlite3')`

如果你不使用SQLite作为数据库，额外的设置，例如 [`USER`](https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-USER)，[`PASSWORD`](https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-PASSWORD)和[`HOST`](https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-HOST)必须加入。有关更多详细信息，请参阅参考文档[`DATABASES`](https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-DATABASES)。

对于SQLite以外的数据库

如果您使用的是除SQLite之外的数据库，请确保此时已创建数据库。在数据库的交互式提示中使用“ ” 执行此操作。`CREATEDATABASE database_name;`

还要确保提供的数据库用户`mysite/settings.py` 具有“create database”特权。这允许自动创建 [测试数据库](https://docs.djangoproject.com/en/2.1/topics/testing/overview/#the-test-database)，这将在以后的教程中使用。

如果您使用的是SQLite，则无需事先创建任何内容 - 数据库文件将在需要时自动创建。

在编辑时`mysite/settings.py`，请设置[`TIME_ZONE`](https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-TIME_ZONE)为您的时区。

另外，请注意[`INSTALLED_APPS`](https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-INSTALLED_APPS)文件顶部的设置。它包含在这个Django实例中激活的所有Django应用程序的名称。应用程序可以在多个项目中使用，您可以打包和分发它们以供项目中的其他人使用。

默认情况下，[`INSTALLED_APPS`](https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-INSTALLED_APPS)包含以下应用程序，所有这些应用程序都随Django一起提供：

- [`django.contrib.admin`](https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#module-django.contrib.admin) - 管理站点。你很快就会用到它。
- [`django.contrib.auth`](https://docs.djangoproject.com/en/2.1/topics/auth/#module-django.contrib.auth) - 认证系统。
- [`django.contrib.contenttypes`](https://docs.djangoproject.com/en/2.1/ref/contrib/contenttypes/#module-django.contrib.contenttypes) - 内容类型的框架。
- [`django.contrib.sessions`](https://docs.djangoproject.com/en/2.1/topics/http/sessions/#module-django.contrib.sessions) - 会话框架。
- [`django.contrib.messages`](https://docs.djangoproject.com/en/2.1/ref/contrib/messages/#module-django.contrib.messages) - 消息传递框架。
- [`django.contrib.staticfiles`](https://docs.djangoproject.com/en/2.1/ref/contrib/staticfiles/#module-django.contrib.staticfiles) - 用于管理静态文件的框架。

默认情况下包含这些应用程序，以方便常见情况。

其中一些应用程序至少使用了一个数据库表，因此我们需要在使用它们之前在数据库中创建表。为此，请运行以下命令：

```
$ python manage.py migrate
```

该[`migrate`](https://docs.djangoproject.com/en/2.1/ref/django-admin/#django-admin-migrate)命令查看[`INSTALLED_APPS`](https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-INSTALLED_APPS)设置并根据`mysite/settings.py`文件中的数据库设置和应用程序附带的数据库迁移创建任何必要的数据库表（稍后我们将介绍这些表）。您将看到适用于每次迁移的消息。如果您有兴趣，请运行数据库的命令行客户端并键入`\dt`（PostgreSQL），（MySQL）， （SQLite）或（Oracle）以显示Django创建的表。`SHOW TABLES;``.schema``SELECT TABLE_NAMEFROM USER_TABLES;`

对于极简主义者

就像我们上面所说的那样，默认应用程序包含在常见情况中，但不是每个人都需要它们。如果您不需要其中任何一个或全部，请[`INSTALLED_APPS`](https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-INSTALLED_APPS)在运行前随意注释或删除相应的行 [`migrate`](https://docs.djangoproject.com/en/2.1/ref/django-admin/#django-admin-migrate)。该 [`migrate`](https://docs.djangoproject.com/en/2.1/ref/django-admin/#django-admin-migrate)命令仅运行应用程序的迁移[`INSTALLED_APPS`](https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-INSTALLED_APPS)。

## 创建模型[¶](https://docs.djangoproject.com/en/2.1/intro/tutorial02/#creating-models)

现在我们将定义您的模型 - 本质上是您的数据库布局，以及其他元数据。

注意：

模型是单独的，是数据的来源。它包含您要存储的数据的基本字段和行为。Django遵循[DRY原则](https://docs.djangoproject.com/en/2.1/misc/design-philosophies/#dry)。目标是在一个地方定义您的数据模型，并自动从中获取数据。

这包括迁移 - 与Ruby On Rails不同，例如，迁移完全来自您的模型文件，并且基本上只是Django可以通过更新数据库模式以匹配您当前模型的历史记录。

在我们简单的民意调查应用程序中，我们将创建两个模型：`Question`和`Choice`。A `Question`有问题和出版日期。A `Choice`有两个字段：选择的文本和投票记录。每个`Choice`都与一个`Question`。

这些概念由简单的Python类表示。编辑 `polls/models.py`文件，使其如下所示：

民调/ models.py中[¶](https://docs.djangoproject.com/en/2.1/intro/tutorial02/#id2)

```
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

代码很简单。每个模型由一个子类表示[`django.db.models.Model`](https://docs.djangoproject.com/en/2.1/ref/models/instances/#django.db.models.Model)。每个模型都有许多类变量，每个变量代表模型中的数据库字段。

每个字段由[`Field`](https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.Field) 类的实例表示- 例如，[`CharField`](https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.CharField)用于字符字段和 [`DateTimeField`](https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.DateTimeField)日期时间。这告诉Django每个字段包含哪种类型的数据。

每个[`Field`](https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.Field)实例的名称（例如 `question_text`或`pub_date`）是字段名称，采用机器友好格式。您将在Python代码中使用此值，并且您的数据库将使用它作为列名。

您可以使用可选的第一个位置参数 [`Field`](https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.Field)来指定一个人类可读的名称。这在Django的几个内省部分中使用，并且它兼作文档。如果未提供此字段，Django将使用机器可读的名称。在这个例子中，我们只定义了一个人类可读的名称`Question.pub_date`。对于此模型中的所有其他字段，字段的机器可读名称就足以作为其可读的名称。

有些[`Field`](https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.Field)类需要参数。 [`CharField`](https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.CharField)例如，要求你给它一个 [`max_length`](https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.CharField.max_length)。这不仅在数据库模式中使用，而且在验证中使用，我们很快就会看到。

A [`Field`](https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.Field)也可以有各种可选参数; 在这种情况下，我们将[`default`](https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.Field.default)值 设置`votes`为0。

最后，请注意使用的定义关系 [`ForeignKey`](https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.ForeignKey)。这告诉Django每个`Choice`都与单个相关`Question`。Django支持所有常见的数据库关系：多对一，多对多和一对一。

## 激活模型[¶](https://docs.djangoproject.com/en/2.1/intro/tutorial02/#activating-models)

这一小部分模型代码为Django提供了大量信息。有了它，Django能够：

- 为此应用程序创建数据库模式（语句）。`CREATE TABLE`
- 创建用于访问`Question`和`Choice`对象的Python数据库访问API 。

但首先我们需要告诉我们的项目`polls`应用程序已安装。

注意：

Django应用程序是“可插拔的”：您可以在多个项目中使用应用程序，并且可以分发应用程序，因为它们不必绑定到给定的Django安装。

要在我们的项目中包含应用程序，我们需要在设置中添加对其配置类的引用[`INSTALLED_APPS`](https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-INSTALLED_APPS)。该 `PollsConfig`班是在`polls/apps.py`文件中，所以它的虚线路径`'polls.apps.PollsConfig'`。编辑`mysite/settings.py`文件并将该虚线路径添加到[`INSTALLED_APPS`](https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-INSTALLED_APPS)设置中。它看起来像这样：

mysite [/settings.py¶](https://docs.djangoproject.com/en/2.1/intro/tutorial02/#id3)

```
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

现在Django知道要包含该`polls`应用程序。让我们运行另一个命令：

```
$ python manage.py makemigrations polls
```

您应该看到类似于以下内容的内容：

```
Migrations for 'polls':
  polls/migrations/0001_initial.py:
    - Create model Choice
    - Create model Question
    - Add field question to choice
```

通过运行`makemigrations`，您告诉Django您已对模型进行了一些更改（在这种情况下，您已经创建了新模型），并且您希望将更改存储为*迁移*。

迁移是Django如何存储对模型（以及数据库模式）的更改 - 它们只是磁盘上的文件。如果您愿意，可以阅读新模型的迁移; 这是文件`polls/migrations/0001_initial.py`。不要担心，每次Django制作时都不会读它们，但是如果你想手动调整Django如何改变它们，它们的设计是人为可编辑的。

有一个命令可以为您运行迁移并自动管理您的数据库模式 - 这是被调用的[`migrate`](https://docs.djangoproject.com/en/2.1/ref/django-admin/#django-admin-migrate)，我们马上就会看到它 - 但首先，让我们看看迁移将运行的SQL。该 [`sqlmigrate`](https://docs.djangoproject.com/en/2.1/ref/django-admin/#django-admin-sqlmigrate)命令获取迁移名称并返回其SQL：

```
$ python manage.py sqlmigrate polls 0001
```

您应该看到类似于以下内容的东西（为了便于阅读，我们重新格式化了它）：

```
BEGIN;
--
-- Create model Choice
--
CREATE TABLE "polls_choice" (
    "id" serial NOT NULL PRIMARY KEY,
    "choice_text" varchar(200) NOT NULL,
    "votes" integer NOT NULL
);
--
-- Create model Question
--
CREATE TABLE "polls_question" (
    "id" serial NOT NULL PRIMARY KEY,
    "question_text" varchar(200) NOT NULL,
    "pub_date" timestamp with time zone NOT NULL
);
--
-- Add field question to choice
--
ALTER TABLE "polls_choice" ADD COLUMN "question_id" integer NOT NULL;
ALTER TABLE "polls_choice" ALTER COLUMN "question_id" DROP DEFAULT;
CREATE INDEX "polls_choice_7aa0f6ee" ON "polls_choice" ("question_id");
ALTER TABLE "polls_choice"
  ADD CONSTRAINT "polls_choice_question_id_246c99a640fbbd72_fk_polls_question_id"
    FOREIGN KEY ("question_id")
    REFERENCES "polls_question" ("id")
    DEFERRABLE INITIALLY DEFERRED;

COMMIT;
```

请注意以下事项：

- 确切的输出将根据您使用的数据库而有所不同。上面的示例是为PostgreSQL生成的。
- 表名是通过组合应用程序的名称（自动生成`polls`）和模型的小写名字- `question`和 `choice`。（您可以覆盖此行为。）
- 主键（ID）会自动添加。（你也可以覆盖它。）
- 按照惯例，Django附加`"_id"`到外键字段名称。（是的，你也可以覆盖它。）
- 外键关系通过 约束显式化。不要担心零件; 这只是告诉PostgreSQL在事务结束前不强制执行外键。`FOREIGN KEY``DEFERRABLE`
- 它是根据您正在使用的数据库量身定制的，因此可以自动为您处理特定于数据库的字段类型，如`auto_increment`（MySQL），`serial`（PostgreSQL）或（SQLite）。引用字段名称也是如此 - 例如，使用双引号或单引号。`integer primary keyautoincrement`
- 该[`sqlmigrate`](https://docs.djangoproject.com/en/2.1/ref/django-admin/#django-admin-sqlmigrate)命令实际上并不在您的数据库上运行迁移 - 它只是将其打印到屏幕上，以便您可以看到SQL Django认为需要什么。它对于检查Django将要执行的操作或者是否有需要SQL脚本进行更改的数据库管理员非常有用。

如果你有兴趣，你也可以跑 ; 这将检查项目中的任何问题，而无需进行迁移或触摸数据库。[`python manage.py check`](https://docs.djangoproject.com/en/2.1/ref/django-admin/#django-admin-check)

现在，[`migrate`](https://docs.djangoproject.com/en/2.1/ref/django-admin/#django-admin-migrate)再次运行以在数据库中创建这些模型表：

```
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Rendering model states... DONE
  Applying polls.0001_initial... OK
```

该[`migrate`](https://docs.djangoproject.com/en/2.1/ref/django-admin/#django-admin-migrate)命令将执行所有尚未应用的迁移（Django跟踪使用数据库中的特殊表来应用哪些迁移`django_migrations`）并针对您的数据库运行它们 - 实际上，您将对模型所做的更改与模型中的模式同步数据库。

迁移功能非常强大，您可以在开发项目时随时更改模型，而无需删除数据库或表并创建新数据库 - 它专门用于实时升级数据库，而不会丢失数据。我们将在本教程的后续部分中更深入地介绍它们，但是现在，请记住进行模型更改的三步指南：

- 更改模型（in `models.py`）。
- 运行以创建这些更改的迁移[`python manage.py makemigrations`](https://docs.djangoproject.com/en/2.1/ref/django-admin/#django-admin-makemigrations)
- 运行以将这些更改应用于数据库。[`python manage.py migrate`](https://docs.djangoproject.com/en/2.1/ref/django-admin/#django-admin-migrate)

之所以有单独的命令来制作和应用迁移是因为您将提交迁移到您的版本控制系统并将其与您的应用程序一起发送; 它们不仅使您的开发更容易，而且还可供其他开发人员和生产中使用。

阅读[django-admin文档](https://docs.djangoproject.com/en/2.1/ref/django-admin/)，了解该`manage.py`实用程序可以执行的操作的完整信息。

## 使用[API¶](https://docs.djangoproject.com/en/2.1/intro/tutorial02/#playing-with-the-api)

现在，让我们进入交互式Python shell并使用Django为您提供的免费API。要调用Python shell，请使用以下命令：

```
$ python manage.py shell
```

我们使用它而不是简单地输入“python”，因为`manage.py` 设置了`DJANGO_SETTINGS_MODULE`环境变量，这为Django提供了`mysite/settings.py`文件的Python导入路径。

进入shell后，浏览[数据库API](https://docs.djangoproject.com/en/2.1/topics/db/queries/)：

```
>>> from polls.models import Choice, Question  # Import the model classes we just wrote.

# No questions are in the system yet.
>>> Question.objects.all()
<QuerySet []>

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
>>> q.save()

# Now it has an ID.
>>> q.id
1

# Access model field values via Python attributes.
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

# Change values by changing the attributes, then calling save().
>>> q.question_text = "What's up?"
>>> q.save()

# objects.all() displays all the questions in the database.
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>
```

不是这个对象的有用表示。让我们来解决这个问题通过编辑模型（在文件），并加入 到两个方法和 ：`<Question: Questionobject (1)>``Question``polls/models.py`[`__str__()`](https://docs.djangoproject.com/en/2.1/ref/models/instances/#django.db.models.Model.__str__)`Question``Choice`

民调/ models.py中[¶](https://docs.djangoproject.com/en/2.1/intro/tutorial02/#id4)

```
from django.db import models

class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text
```

[`__str__()`](https://docs.djangoproject.com/en/2.1/ref/models/instances/#django.db.models.Model.__str__)向模型添加方法非常重要，不仅是为了您在处理交互式提示时的方便，还因为在Django自动生成的管理中使用了对象的表示。

请注意，这些是普通的Python方法。让我们添加一个自定义方法，仅用于演示：

民调/ models.py中[¶](https://docs.djangoproject.com/en/2.1/intro/tutorial02/#id5)

```
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
```

请注意添加和分别引用Python的标准模块和Django的时区相关实用程序。如果您不熟悉Python中的时区处理，可以在[时区支持文档中](https://docs.djangoproject.com/en/2.1/topics/i18n/timezones/)了解更多信息。`import datetime``from django.utils import timezone`[`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime)[`django.utils.timezone`](https://docs.djangoproject.com/en/2.1/ref/utils/#module-django.utils.timezone)

保存这些更改并通过再次运行启动新的Python交互式shell ：`python manage.py shell`

```
>>> from polls.models import Choice, Question

# Make sure our __str__() addition worked.
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>

# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
>>> Question.objects.filter(question_text__startswith='What')
<QuerySet [<Question: What's up?>]>

# Get the question that was published this year.
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

# Request an ID that doesn't exist, this will raise an exception.
>>> Question.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Question matching query does not exist.

# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Question.objects.get(id=1).
>>> Question.objects.get(pk=1)
<Question: What's up?>

# Make sure our custom method worked.
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.
>>> q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
>>> q.choice_set.all()
<QuerySet []>

# Create three choices.
>>> q.choice_set.create(choice_text='Not much', votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text='The sky', votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)

# Choice objects have API access to their related Question objects.
>>> c.question
<Question: What's up?>

# And vice versa: Question objects get access to Choice objects.
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# Let's delete one of the choices. Use delete() for that.
>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()
```

有关模型关系的更多信息，请参阅[访问相关对象](https://docs.djangoproject.com/en/2.1/ref/models/relations/)。有关如何使用双下划线通过API执行字段查找的更多信息，请参阅[字段查找](https://docs.djangoproject.com/en/2.1/topics/db/queries/#field-lookups-intro)。有关数据库API的完整详细信息，请参阅我们的[数据库API参考](https://docs.djangoproject.com/en/2.1/topics/db/queries/)。

## 介绍Django管理员[¶](https://docs.djangoproject.com/en/2.1/intro/tutorial02/#introducing-the-django-admin)

**简介**

为您的员工或客户生成管理网站以添加，更改和删除内容是繁琐的工作，不需要太多的过程。出于这个原因，Django完全自动化为模型创建管理界面。

Django是在新闻编辑室环境中编写的，“内容发布者”和“公共”网站之间有明显的分离。站点管理员使用该系统添加新闻报道，事件，体育比分等，并且该内容显示在公共站点上。Django解决了为站点管理员创建统一界面以编辑内容的问题。

管理员不打算由网站访问者使用。它适用于网站管理员。

### 创建管理员用户[¶](https://docs.djangoproject.com/en/2.1/intro/tutorial02/#creating-an-admin-user)

首先，我们需要创建一个可以登录管理站点的用户。运行以下命令：

```
$ python manage.py createsuperuser
```

输入所需的用户名，然后按Enter键。

```
Username: admin
```

然后，系统将提示您输入所需的电子邮件地址：

```
Email address: admin@example.com
```

最后一步是输入密码。系统会要求您输入两次密码，第二次输入密码作为第一次确认。

```
Password: **********
Password (again): *********
Superuser created successfully.
```

### 启动开发服务器[¶](https://docs.djangoproject.com/en/2.1/intro/tutorial02/#start-the-development-server)

Django管理站点默认激活。让我们启动开发服务器并进行探索。

如果服务器没有运行，请启动它：

```
$ python manage.py runserver
```

现在，打开Web浏览器并转到本地域的“/ admin /” - 例如 <http://127.0.0.1:8000/admin/>。您应该看到管理员的登录屏幕：

![](https://docs.djangoproject.com/en/2.1/_images/admin01.png)

由于默认情况下打开[翻译](https://docs.djangoproject.com/en/2.1/topics/i18n/translation/)，因此登录屏幕可能会以您自己的语言显示，具体取决于您的浏览器设置以及Django是否有此语言的翻译。

### 进入管理站点[¶](https://docs.djangoproject.com/en/2.1/intro/tutorial02/#enter-the-admin-site)

现在，尝试使用您在上一步中创建的超级用户帐户登录。你应该看到Django管理员索引页面：

![](https://docs.djangoproject.com/en/2.1/_images/admin02.png)

您应该看到几种类型的可编辑内容：组和用户。它们[`django.contrib.auth`](https://docs.djangoproject.com/en/2.1/topics/auth/#module-django.contrib.auth)由Django 提供的身份验证框架提供。

### 在管理员中修改民意调查应用程序[¶](https://docs.djangoproject.com/en/2.1/intro/tutorial02/#make-the-poll-app-modifiable-in-the-admin)

但是我们的投票应用程序在哪里？它不会显示在管理员索引页面上。

只需做一件事：我们需要告诉管理员`Question` 对象有一个管理界面。为此，请打开该`polls/admin.py` 文件，然后将其编辑为如下所示：

民调/ admin.py中[¶](https://docs.djangoproject.com/en/2.1/intro/tutorial02/#id6)

```
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```

### 探索免费的管理功能[¶](https://docs.djangoproject.com/en/2.1/intro/tutorial02/#explore-the-free-admin-functionality)

现在我们已经注册了`Question`，Django知道它应该显示在管理员索引页面上：

单击“Questions ”。现在，您将进入“更改列表”页面以查询问题。此页面显示数据库中的所有问题，您可以选择一个更改它。我们之前创建了“What's up？”这个问题：

点击“What's up？”问题进行编辑：

这里要注意的事项：

- 表单是从`Question`模型自动生成的。
- 不同的模型字段类型（[`DateTimeField`](https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.DateTimeField)， [`CharField`](https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.CharField)）对应于相应的HTML输入窗口小部件。每种类型的字段都知道如何在Django管理员中显示自己。
- 每个都[`DateTimeField`](https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.DateTimeField)获得免费的JavaScript快捷方式。日期获得“今日”快捷方式和日历弹出窗口，时间获得“现在”快捷方式和方便的弹出窗口，列出常用的输入时间。

页面底部为您提供了几个选项：

- 保存 - 保存更改并返回此类对象的更改列表页面。
- 保存并继续编辑 - 保存更改并重新加载此对象的管理页面。
- 保存并添加另一个 - 保存更改并为此类对象加载新的空白表单。
- 删除 - 显示删除确认页面。

如果“发布日期”的值与您在[教程1中](https://docs.djangoproject.com/en/2.1/intro/tutorial01/)创建问题的时间不匹配，则可能意味着您忘记为该[`TIME_ZONE`](https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-TIME_ZONE)设置设置正确的值。更改它，重新加载页面并检查是否显示正确的值。

单击“今天”和“立即”快捷方式更改“发布日期”。然后单击“保存并继续编辑”。然后单击右上角的“历史记录”。您将看到一个页面，其中列出了通过Django管理员对此对象所做的所有更改，以及进行更改的人员的时间戳和用户名：

![](https://docs.djangoproject.com/en/2.1/_images/admin06t.png)

如果您对模型API感到满意并熟悉管理网站，请阅读[本教程的第3部分](https://docs.djangoproject.com/en/2.1/intro/tutorial03/)，了解如何向民意调查应用添加更多视图。