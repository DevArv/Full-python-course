import user
import post

app_user_one = user.User("test@test.com", "Joan Alexander", "psw11", "Data analyst py")
app_user_one.get_user_info()

app_user_two = user.User("test1@gmail.com", "agent Demo", "psw22", "Assistant py")
app_user_two.get_user_info()

new_post = post.Post("Now we can upload the module. Work its done", app_user_two.name)
new_post.get_post_info()

new_post = post.Post("Almost a Dev Data analyst of py", app_user_one.name)
new_post.get_post_info()
