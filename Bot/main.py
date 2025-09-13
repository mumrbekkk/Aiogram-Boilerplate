import asyncio

from .core.bot import main


if __name__ == "__main__":
    try:
        print("Bot started...")
        asyncio.run(main())

    except (KeyboardInterrupt, SystemExit):
        print("Exit")

