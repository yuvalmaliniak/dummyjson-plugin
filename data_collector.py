class EvidenceCollector:
    def __init__(self, client):
        self.client = client

    def collect_e1(self):
        return self.client.get("auth/me")

    def collect_e2(self):
        return self.client.get("posts?limit=60")

    def collect_e3(self):
        posts = self.client.get("posts?limit=60")["posts"]
        for post in posts:
            post_id = post["id"]
            comments = self.client.get(f"posts/{post_id}/comments")
            post["comments"] = comments.get("comments", [])
        return posts
