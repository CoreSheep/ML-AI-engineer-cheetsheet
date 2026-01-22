

def is_valid_tweet(tweet: str) -> bool:
    if len(tweet.split("@")) - 1 > 3:
        return False
    return True


if __name__ == "__main__":
    print(is_valid_tweet("Hello @world"))
    print(is_valid_tweet("Hello @world @world"))
    print(is_valid_tweet("Hello @world @world @world"))
    print(is_valid_tweet("Hello @world @world @world @world"))