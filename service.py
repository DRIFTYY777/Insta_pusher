



class FilesService:

    def write_file(path, data):
        with open(path, 'w') as f:
            f.write(data)
            return True

    def write_file(data):
        with open('file.txt', 'w') as f:
            f.write(data)
            return True

    def read_file(path):
        with open(path, 'r') as f:
            return f.read()
        
class InstagramService:
    

    def get_hashtag_medias(self, hashtag):
        return self.client.feed_tag(hashtag)

    def like_media(self, media_id):
        self.client.post_like(media_id)

    def follow_user(self, user_id):
        self.client.user_follow(user_id)

    def unfollow_user(self, user_id):
        self.client.user_unfollow(user_id)

    def get_user_medias(self, user_id):
        return self.client.user_medias(user_id)

    def get_user_followers(self, user_id):
        return self.client.user_followers(user_id)

    def get_user_followings(self, user_id):
        return self.client.user_followings(user_id)

    def get_user_info(self, user_id):
        return self.client.user_info(user_id)

    def get_user_followers(self, user_id):
        return self.client.user_followers(user_id)

    def get_user_followings(self, user_id):
        return self.client.user_followings(user_id)

    def get_user_info(self, user_id):
        return self.client.user_info(user_id)

    def get_user_followers(self, user_id):
        return self.client.user_followers(user_id)

    def get_user_followings(self, user_id):
        return self.client.user_followings(user_id)

    def get_user_info(self, user_id):
        return self.client.user_info(user_id)

    def get_user_followers(self, user_id):
        return self.client.user_followers(user_id)

    def get_user_followings(self, user_id):
        return self.client.user_followings(user_id)

    def get_user_info(self, user_id):
        return self.client.user_info(user_id)

    def get_user_followers(self, user_id):
        return self.client.user_followers(user_id)

    def get_user_followings(self, user_id):
        return self.client.user_followings(user_id)

    def get_user_info(self, user_id):
        return self.client.user_info(user_id)

    

        