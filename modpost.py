class Post:
    def __int__(self, message, author):
        self.user_message = message
        self.author = author

    def get_post_inf(self):
        print(f"Post: {self.user_message} written by {self.author} on this social media.")
