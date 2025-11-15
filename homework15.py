class User:
    def __init__(self, name):
        self.name = name
        self.posts = []
        self.friends = set()

    def create_post(self, content):
        post = Post(content, self)
        self.posts.append(post)
        print(f"{self.name}მ შექმნა პოსტი: '{content}'")
        return post

    def comment_on_post(self, post, comment_content):
        comment = post.add_comment(comment_content, self)
        print(f"{self.name}მ დაწერა კომენტარი: '{comment_content}'")
        return comment

    def like_post(self, post):
        post.add_like(self)
        print(f"{self.name}მ მოიწონა პოსტი: '{post.content}'")

    def add_friend(self, user):
        self.friends.add(user)
        user.friends.add(self)
        print(f"{self.name} და {user.name} გახდნენ მეგობრები")

    def __str__(self):
        return self.name


class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.comments = []
        self.likes = []

    def add_comment(self, content, author):
        comment = Comment(content, author)
        self.comments.append(comment)
        return comment

    def add_like(self, user):
        if user not in self.likes:
            self.likes.append(user)

    def display_post(self):
        print(f"\n{'=' * 50}")
        print(f"პოსტი: {self.content}")
        print(f"ავტორი: {self.author.name}")
        print(f"მოწონებები: {len(self.likes)}")

        if self.likes:
            print(f"მოიწონეს: {', '.join([user.name for user in self.likes])}")

        if self.comments:
            print(f"კომენტარები ({len(self.comments)}):")
            for comment in self.comments:
                print(f"  - {comment.author.name}: {comment.content}")
        print(f"{'=' * 50}\n")

class Comment:
    def __init__(self, content, author):
        self.content = content
        self.author = author

    def __str__(self):
        return f"{self.author.name}: {self.content}"

if __name__ == "__main__":
    print("სოციალური ქსელის სიმულაცია")

    user1 = User("ლუკა")
    user2 = User("მარი")
    user1.add_friend(user2)
    print()

    post1 = user1.create_post("გამარჯობა, ეს არის ჩემი პირველი პოსტი!")
    print()

    user2.comment_on_post(post1, "გილოცავ პირველ პოსტს!")
    print()

    user1.like_post(post1)
    print()
    post1.display_post()


    post2 = user1.create_post("დღეს ძალიან კარგი ამინდია!")
    print()

    user2.like_post(post2)
    print()

    post2.display_post()
