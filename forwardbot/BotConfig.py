from os import environ
class Config(object):
    API_ID = environ.get("API_ID", "12606917")
    API_HASH = environ.get("API_HASH", "f25113b8c17dca6fa7abda53a86bd4f7")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6608265446:AAGbs7WKURen7ED8kWRLN_pqy1Fbo5WuBag")
    STRING_SESSION = environ.get("STRING_SESSION", "AQDAXcUAXKhjhbpEJud3GzKQTv5NiYoz5wv2AkT2eDtljg2o41k2ZupXlp6D8CiXFN4jxSXXF9C3T8sM-G77lKoPJEFOAVwk1CW4NMD1H_uh_DHQ3EDkzLbk36swb_mrPK6HMRotgMSb2MfH9VVOlP8kJK84OAOSRHDwKf5O3q6JKKE6sbxMvafB883N4oLfePZFpDFS-xzKWef5e2NhWHHiRha3jQu9-EP0QID4xOeXaX4gvdl89Px3vHn3X7HSEPTDv3x0qCfKVU81Y0ItwjS_bxXWfrUma-Cr1eV41dACdR7sa5dcCE_ViwyVFdvHjRyzUw7BT72-pxCToP2_yRL1tK9TagAAAAE8_fPSAA")
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
