class script(object):
    START_TXT = """<b>HELLO {},
MY NAME IS <a href=https://t.me/{}>{}</a>, I PROVIDE SERIES. JUST ADD ME TO YOUR GROUP AND ENJOY!π</b>"""
    HELP_TXT = """{},
<b>HERE IS THE HELP FOR MY COMMANDS</b>"""
    ABOUT_TXT = """<b>β οΈ MY NAME: {}</b>
<b>β£οΈ OWNED BY:</b> <a href=https://t.me/JiC54_SERIES_Bot>Click Here!</a>
<b>β£οΈ LANGUAGE:</b> πΏπππ·πΎπ½ πΉ
<b>β£οΈ DATABASE:</b> πΌπΎπ½πΆπΎ
<b>β£οΈ BOT SERVER:</b> π·π΄ππΎπΊπ
<b>β£οΈ π±OT VERSION:</b> <code>5.1.0</code></b>"""
    SOURCE_TXT = """<b>JiC54 CHANNELS:</b> 
    
<a href=https://t.me/+H_6j47erCp44YjY0>Movies and Series 2022</a>
<a href=https://t.me/+uQBJ5JaaLpgyMWI0>House of Movies</a>
<a href=https://t.me/+EHBqUrMHnglmZWY8>Dax songs</a>
<a href=https://t.me/+8eC2YwzHZtUwZDg0>DC Series</a>
<a href=https://t.me/+GvVfP9p-YAsyMTY0>Marvel Movies</a>
<a href=https://t.me/+6QrMOpOVtKAxOGQ0>African Movies</a>
<a href=https://t.me/+LhZuWiqE21NiYzY0>WWE wrestling</a>

<b>JiC54 GROUPS:</b>
<a href=https://t.me/+dFGzJDTQWow2ZGY8>Request Movies</a>
<a href=https://t.me/+bCTNQn4-5TtkZmZk>Request Series</a>
<a href=https://t.me/+gTYFpj1ZBIIxZTQ0>Request Dax Songs</a>

<b>JiC54 BOTS:</b>
<a href=http://t.me/JiC54_MOVIES_Bot>Movies Bot</a>
<a href=http://t.me/JiC54SeriesBot>Series Bot</a>
<a href=http://t.me/JiC54filterBot>Filter Bot</a>
<a href=http://t.me/filestolinks1_bot>File to Links Bot</a>"""
    
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and this bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. <a href=https://t.me/JiC54_MOVIES_Bot>JiC54 Movies bot</a> should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
β’ /filter - <code>add a filter in chat</code>
β’ /filters - <code>list all the filters of a chat</code>
β’ /del - <code>delete a specific filter in chat</code>
β’ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- <a href=https://t.me/JiC54_MOVIES_Bot>JiC54 Movies bot</a> Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allow you to send buttons without any content, so content is mandatory.
2. <a href=https://t.me/JiC54_MOVIES_Bot>JiC54 Movies bot</a> supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/JiC54_MOVIES_Bot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make <a href=https://t.me/JiC54_MOVIES_Bot>JiC54 Movies bot</a> the admin of your channel if it's private.
2. make sure that your channel does not contains CAMRips, porn and fake files.
3. Forward the last message to <a href=https://t.me/JiC54_MOVIES_Bot>me</a> with quotes.
 I'll add all the files in that channel to my database."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting <a href=https://t.me/JiC54_MOVIES_Bot>me</a> to ur PM

<b>Commands and Usage:</b>
β’ /connect  - <code>connect a particular chat to your PM</code>
β’ /disconnect  - <code>disconnect from a chat</code>
β’ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
These are the extra features of <a href=https://t.me/JiC54_MOVIES_Bot>JiC54 MOVIES Bot</a>

<b>Commands and Usage:</b>
β’ /id - <code>get id of a specified user.</code>
β’ /info  - <code>get information about a user.</code>
β’ /imdb  - <code>get the film information from IMDb source.</code>
β’ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
β’ /logs - <code>to get the rescent errors</code>
β’ /stats - <code>to get status of files in db.</code>
β’ /delete - <code>to delete a specific file from db.</code>
β’ /users - <code>to get list of my users and ids.</code>
β’ /chats - <code>to get list of the my chats and ids </code>
β’ /leave  - <code>to leave from a chat.</code>
β’ /disable  -  <code>do disable a chat.</code>
β’ /ban  - <code>to ban a user.</code>
β’ /unban  - <code>to unban a user.</code>
β’ /channel - <code>to get list of total connected channels</code>
β’ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """β TOTAL USERS: <code>{}</code>
β TOTAL CHATS: <code>{}</code>
β TOTAL FILES <code>{}</code>
β USED RAM: <code>{}</code> 
β FREE RAM: <code>{}</code>
β TOTAL RAM: <code>512MB</code>"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
