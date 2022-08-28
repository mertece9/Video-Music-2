from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from Yukki import db_mem


def others_markup(videoid, user_id):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 1
    buttons = [
        [
            InlineKeyboardButton(
                text="• ᴋᴇɴᴅɪ ᴘʟᴀʏʟɪsᴛɪɴᴇ ᴇᴋʟᴇ",
                callback_data=f"your_playlist {videoid}|{user_id}",
            ),
       ],
       [
            InlineKeyboardButton(
                text="• ɢʀᴜʙᴜɴ ᴘʟᴀʏʟɪsᴛɪɴᴇ ᴇᴋʟᴇ",
                callback_data=f"group_playlist {videoid}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="📥 sᴀʀᴋɪ | ᴠɪᴅᴇᴏ 📥",
                callback_data=f"audio_video_download {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(
                text="• ɢᴇʀɪ",
                callback_data=f"pr_go_back_timer {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="• ᴋᴀᴘᴀᴛ",
                callback_data=f"close",
            ),
        ],
    ]
    return buttons


def download_markup(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="🔎 sᴀʀᴋɪ ɪɴᴅɪʀ",
                callback_data=f"gets audio|{videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="🔎 ᴠɪᴅᴇᴏ ɪɴᴅɪʀ",
                callback_data=f"gets video|{videoid}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="• ɢᴇʀɪ", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="• ᴋᴀᴘᴀᴛ", callback_data=f"close"),
        ],
    ]
    return buttons

