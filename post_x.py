import asyncio
import os

from twikit import Client


async def main():
    text = os.environ["POST_TEXT"].strip()

    if not text:
        raise ValueError("投稿本文が空です")

    username = os.environ["X_USERNAME"]
    email = os.environ.get("X_EMAIL", "").strip()
    password = os.environ["X_PASSWORD"]
    totp_secret = os.environ.get("X_TOTP_SECRET", "").strip()

    client = Client("ja-JP")

    login_args = {
        "auth_info_1": username,
        "password": password,
        "enable_ui_metrics": True,
    }

    if email:
        login_args["auth_info_2"] = email

    if totp_secret:
        login_args["totp_secret"] = totp_secret

    await client.login(**login_args)

    tweet = await client.create_tweet(text=text)

    print(f"POSTED: {tweet.id}")


if __name__ == "__main__":
    asyncio.run(main())
