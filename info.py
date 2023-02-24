import re
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '2229357'))
API_HASH = environ.get('API_HASH', '31f183a5a075fd4996cb8ad59e7b794f')
BOT_TOKEN = environ.get('BOT_TOKEN', '5425847881:AAF-vNcW1Hjl_s8THDUurrcjS9ePMEfPb_I')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://te.legra.ph/file/afe7846d7d160b683c257.jpg https://te.legra.ph/file/d835c62acb9fcc5b6b712.jpg https://te.legra.ph/file/49499d4c2c185ae003f3f.jpg https://te.legra.ph/file/ba12e6ef4e4b285376d16.jpg https://te.legra.ph/file/2b397c4cc8f85dce1cd7e.jpg https://te.legra.ph/file/5126b3dfa16dd201d04e0.jpg https://te.legra.ph/file/418f0b2c328bb341071cd.jpg https://te.legra.ph/file/5bb2c5cafba261ad35e1b.jpg https://te.legra.ph/file/e895ff7a3a0b42e2721f5.jpg https://te.legra.ph/file/3d66c637d7b40d42d687e.jpg https://te.legra.ph/file/f65a9cc09661486226d90.jpg https://te.legra.ph/file/ddd9ea9ed66462b5e97dd.jpg https://te.legra.ph/file/e93ed79078f9c28ca1348.jpg https://te.legra.ph/file/b2fdcf08ad674e305e826.jpg https://te.legra.ph/file/69c7de30fd9d79ccec8a3.jpg https://te.legra.ph/file/f55b75223dc49faaa7726.jpg https://te.legra.ph/file/fe7967e76862d02821571.jpg https://te.legra.ph/file/a2c7b64c302831bcd5338.jpg https://te.legra.ph/file/ee4c8e2e77aa155d0df4b.jpg https://te.legra.ph/file/dbce8ce8d63468e6e1dec.jpg  https://te.legra.ph/file/dfcf3c688420ef8dae25b.jpg https://te.legra.ph/file/ed71128076240da39e0cf.jpg https://te.legra.ph/file/6673e06a3c021e92be713.jpg https://te.legra.ph/file/b61b3560e4de1f3c361f3.jpg https://te.legra.ph/file/cacc469a54bf111458946.jpg https://te.legra.ph/file/0498043c465bf9c46b80f.jpghttps://te.legra.ph/file/d1cce58e7c58562793741.jpg https://te.legra.ph/file/78210809e5530320eb53d.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://te.legra.ph/file/c4fd9a3e87088868bbff5.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://te.legra.ph/file/364204ddcd64180a7c7dc.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/229b746a9efacb4245b53.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '794968418').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '794968418').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', "")
reqst_channel = environ.get('REQST_CHANNEL_ID', "")
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://shieldbot:Karuna100@cluster0.kx6zz.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Adult_files')

# Others

VERIFY = bool(environ.get('VERIFY', True))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'tnlink.in')
SHORTLINK_API = environ.get('SHORTLINK_API', '546326320a3c0a8fdc061f56ca40972e1e35682f')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', True))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-1001890570731').split()]
PORT = environ.get("PORT", "8080")
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+VzRu2EnECnIzMDk1')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/HeavenOfXXX')
MSG_ALRT = environ.get('MSG_ALRT', '🚩 @TVSeriesCW Best Channel In Telegram')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001500025641'))
REQUEST_LOGS = int(environ.get('REQUEST_LOGS', '-1001820924316'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'tvseriescw_group')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1001500025641')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
