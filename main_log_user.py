from loguser import User
from post import Post

app_user_one = User("test@test.com", "Joan Alexander", "psw11", "Data analyst py")
app_user_one.get_user_info()

app_user_two = User("test1@gmail.com", "Agente Demo", "psw22", "Assistant py")
app_user_two.get_user_info()

new_post = Post("just developing my new project", app_user_two.name)
new_post.get_post_info()
