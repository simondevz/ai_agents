import asyncio
from search_agent.agent import search_agent
from search_agent.utils import generate_random_string


async def main():
    INIT = True  # Indicator for if this is the start of the convo.
    AGENT_CALLED = False
    chat_id = ""
    user_input = ""

    while True:
        if INIT:
            print("WELCOME TO THE SEARCH BOT...")
            print("Press ctrl + C to Quit.")
            print("")

            start_old_converation = (
                input("Would you like to continue an Old Converstation? (y/N) ")
                .strip()
                .lower()
            ) == "y"

            if start_old_converation:
                chat_id = input("provide your chat id: ").strip().lower()
            else:
                chat_id = generate_random_string()
                print(
                    f"Your current chat id is {chat_id.upper()}. Copy for future refrence."
                )

            INIT = False

        print("")
        if AGENT_CALLED:
            user_input = input("you> ")
        else:
            print("Hi there, what would you like to know today?")
            user_input = input("you> ")

        await search_agent(chat_id, user_input)
        AGENT_CALLED = True


if __name__ == "__main__":
    asyncio.run(main())
