"""Class 10/27/22: Object oriented programming."""


class Profile:
    handle: str 
    followers: int 
    is_private: bool 

    def __init__(self, handle: str):
        """Constructor for initializing atributes."""
        self.handle = handle 
        self.follwers = 0 
        self.is_private = False 

    def tweet(self, msg: str) -> None:
        """Example of a method."""
        print(f"@{self.handle} tweets {msg}")


my_profile: Profile = Profile("setyler")
my_profile.tweet("Hello, world.")