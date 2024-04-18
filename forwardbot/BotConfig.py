from os import environ
class Config(object):
    API_ID = environ.get("API_ID", "12606917")
    API_HASH = environ.get("API_HASH", "f25113b8c17dca6fa7abda53a86bd4f7")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6608265446:AAGbs7WKURen7ED8kWRLN_pqy1Fbo5WuBag")
    STRING_SESSION = environ.get("STRING_SESSION", "AQDAXcUAXmnryuixZKCwPpcN6hEyK6Ur9qpu2v2Kf5doV38K4h8_lsAnRhYDx2RnZO-tJpZbfbPgESAcg8-scSsHScdq3iFr-MpIgezLacpTT-vjHWryOwqNzpjRbo8d9i5BnVEuM1_DlXEDtB85eOiK-1GXd-9gt3aQr8iBBE10wLZXZvY-2j68XCYVRoXKxzuOjzfxwN07dRepJG1CwjPb7D8s3eUwH_uRL2GCooUxD-G_3duWY58XaMuVArFgnA_TnN-0SVi8Iv3GgcqV0peG8I0ueD8YLc5hlQzTKPu6qLjbl1yxv69O6NqLnyWsxVW0MX9k11xpxDSOMh8HJOKzeas2nQAAAAE8_fPSAA")
    SUDO_USERS = environ.get("SUDO_USERS", "5318243282")
    COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "^/")
    HELP_MSG = """
    💢 **ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ɪɴ ᴛʜᴇ ʙᴏᴛ ᴀʀᴇ:**
    
    🔻 **Command :** /forward
    **Usage : ** Forwards messages from a channel to other.
    🔻 **Command :** /count
    **Usage : ** Returns the Total message sent using the bot.
    🔻 **Command :** /reset
    **Usage : ** Resets the message count to 0.
    🔻 **Command :** /restart
    **Usage : ** Updates and Restarts the Bot.
    🔻 **Command :** /join
    **Usage : ** Joins the channel.
    🔻 **Command :** /help
    **Usage : ** Get the help of this bot.
    🔻 **Command :** /status
    **Usage :** Check current status of Bot.
    🔻 **Command :** /uptime
    **Usage :** Check uptime of Bot.
    
    ⭕ **ʙᴏᴛ ɪs ᴄʀᴇᴀᴛᴇᴅ ʙʏ** **@KingVJ01**
    """
