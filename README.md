This is a simple welcome bot using python, created just to send automatic welcome messages :D

## How to use:
- 1 - Before **starting** the bot, make sure you have added **YOUR BOT TOKEN** on the `utils/config.json`:
  - ```json
    {
         "token": "YOUR_BOT_TOKEN"
    }
    ```
- 2 - The file `commands/welcome.py` have another **very important field to fill**, is the `"CHANNEL_ID"`. Replace both `CHANNEL_ID` parameters with the ID of the channel that the bot will send and delete the welcome message.
  - ```py
    @bot.event
    async def on_member_join(member):
        channel_id = "CHANNEL_ID" # <-- here
        channel = bot.get_channel(channel_id)
    ```
  - ```py
    @bot.event
    async def on_member_remove(member):
        channel_id = "CHANNEL_ID" # <-- here
        channel = bot.get_channel(channel_id)
    ```
- 3 - After that, customize the bot message in the same `commands/welcome.py` file. The places to customize the messages are already being indicated within the file. If you want to move a line down in your message, just use the `\n` function
  - Code:
    ```py
    print("line 1 \n line 2")
    ```
    Console:
    ```
    line 1
     line 2
    ```
- 4 - Now your bot is ready, just activate then!
    
## Note:
- You need to download the packages that are in the `requirements.txt` folder for the bot to work correctly.
  Use this on console:
  ```py
  pip install py-cord==2.4.1
  pip install NewFunctionsPYC==1.4.0
  ``` 
- This bot is using the **[py-cord](https://docs.pycord.dev)** library, not **[discord.py](https://discordpy.readthedocs.io)**. If you have the **[discord.py](https://discordpy.readthedocs.io)** library installed on your desktop, I recommend that you **uninstall** it and only use the **[py-cord](https://docs.pycord.dev)** library.
- Also check if you have **[python](https://www.python.org)** installed on your desktop.

If you want to place your bot on a host, I recommend that you place it on a host with **75Mb RAM** or more. These are the hosts that I recommend you use to host the bot:
- **[DisCloud](https://discloudbot.com)**.
- **[SquareCloud](https://squarecloud.app)**.
