import asyncio
import importlib
import os
import re

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytgcalls import idle
from rich.console import Console
from rich.table import Table
from youtubesearchpython import VideosSearch

from config import (LOG_GROUP_ID, LOG_SESSION, STRING1, STRING2, STRING3,
                    STRING4, STRING5)
from Yukki import (ASS_CLI_1, ASS_CLI_2, ASS_CLI_3, ASS_CLI_4, ASS_CLI_5,
                   ASSID1, ASSID2, ASSID3, ASSID4, ASSID5, ASSNAME1, ASSNAME2,
                   ASSNAME3, ASSNAME4, ASSNAME5, BOT_ID, BOT_NAME, LOG_CLIENT,
                   OWNER_ID, app)
from Yukki.Core.Clients.cli import LOG_CLIENT
from Yukki.Core.PyTgCalls.Yukki import (pytgcalls1, pytgcalls2, pytgcalls3,
                                        pytgcalls4, pytgcalls5)
from Yukki.Database import (get_active_chats, get_active_video_chats,
                            get_sudoers, is_on_off, remove_active_chat,
                            remove_active_video_chat)
from Yukki.Inline import private_panel
from Yukki.Plugins import ALL_MODULES
from Yukki.Utilities.inline import paginate_modules

loop = asyncio.get_event_loop()
console = Console()
HELPABLE = {}


async def initiate_bot():
    with console.status(
        "[magenta] Önyükleme Sonlandırılıyor...",
    ) as status:
        try:
            chats = await get_active_video_chats()
            for chat in chats:
                chat_id = int(chat["chat_id"])
                await remove_active_video_chat(chat_id)
        except Exception as e:
            pass
        try:
            chats = await get_active_chats()
            for chat in chats:
                chat_id = int(chat["chat_id"])
                await remove_active_chat(chat_id)
        except Exception as e:
            pass
        status.update(
            status="[bold blue]Scanning for Plugins", spinner="earth"
        )
        console.print("Found {} Plugins".format(len(ALL_MODULES)) + "\n")
        status.update(
            status="[bold red]Importing Plugins...",
            spinner="bouncingBall",
            spinner_style="yellow",
        )
        for all_module in ALL_MODULES:
            imported_module = importlib.import_module(
                "Yukki.Plugins." + all_module
            )
            if (
                hasattr(imported_module, "__MODULE__")
                and imported_module.__MODULE__
            ):
                imported_module.__MODULE__ = imported_module.__MODULE__
                if (
                    hasattr(imported_module, "__HELP__")
                    and imported_module.__HELP__
                ):
                    HELPABLE[
                        imported_module.__MODULE__.lower()
                    ] = imported_module
            console.print(
                f">> [bold cyan]Successfully imported: [green]{all_module}.py"
            )
        console.print("")
        status.update(
            status="[bold blue]Importation Completed!",
        )
    console.print(
        "[bold green]Congrats!! Yukki Music Bot başarıyla başladı!\n"
    )
    try:
        await app.send_message(
            LOG_GROUP_ID,
            "<b>🪧 Müzik Botu başarıyla başladı!</b>",
        )
    except Exception as e:
        print(
            "\nBot has failed to access the log Channel. Make sure that you have added your bot to your log channel and promoted as admin!"
        )
        console.print(f"\n[red]Stopping Bot")
        return
    a = await app.get_chat_member(LOG_GROUP_ID, BOT_ID)
    if a.status != "administrator":
        print("Promote Bot as Admin in Logger Channel")
        console.print(f"\n[red]Stopping Bot")
        return
    console.print(f"\n┌[red] Bot Started as {BOT_NAME}!")
    console.print(f"├[green] ID :- {BOT_ID}!")
    if STRING1 != "None":
        try:
            await ASS_CLI_1.send_message(
                LOG_GROUP_ID,
                "<b>Tebrikler!! Yardımcı İstemci 1 başarıyla başlatıldı!</b>",
            )
        except Exception as e:
            print(
                "\nYardımcı Hesap 1 günlük Kanalı'na erişemedi. Asistanınızı günlük kanalınıza eklediğinizden ve yönetici olarak terfi ettirdiğinizden emin olun!"
            )
            console.print(f"\n[red]Stopping Bot")
            return
        try:
            await ASS_CLI_1.join_chat("ProTubeSupport")
            await ASS_CLI_1.join_chat("sohbetmuhabbetw")
        except:
            pass
        console.print(f"├[red] Asistan 1 Olarak Başladı {ASSNAME1}!")
        console.print(f"├[green] ID :- {ASSID1}!")
    if STRING2 != "None":
        try:
            await ASS_CLI_2.send_message(
                LOG_GROUP_ID,
                "<b>Tebrikler!! Yardımcı İstemci 2 başarıyla başlatıldı!</b>",
            )
        except Exception as e:
            print(
                "\nYardımcı Hesap 2 günlük Kanalı'na erişemedi. Asistanınızı günlük kanalınıza eklediğinizden ve yönetici olarak terfi ettirdiğinizden emin olun!"
            )
            console.print(f"\n[red]Stopping Bot")
            return
        try:
            await ASS_CLI_2.join_chat("ProTubeSupport")
            await ASS_CLI_2.join_chat("sohbetmuhabbetw")
        except:
            pass
        console.print(f"├[red] Asistan 2 Olarak Başladı {ASSNAME2}!")
        console.print(f"├[green] ID :- {ASSID2}!")
    if STRING3 != "None":
        try:
            await ASS_CLI_3.send_message(
                LOG_GROUP_ID,
                "<b>Tebrikler!! Yardımcı İstemci 3 başarıyla başlatıldı!</b>",
            )
        except Exception as e:
            print(
                "\nYardımcı Hesap 3, Kanal günlüğüne erişemedi. Asistanınızı günlük kanalınıza eklediğinizden ve yönetici olarak terfi ettirdiğinizden emin olun!"
            )
            console.print(f"\n[red]Stopping Bot")
            return
        try:
            await ASS_CLI_3.join_chat("ProTubeSupport")
            await ASS_CLI_3.join_chat("sohbetmuhabbetw")
        except:
            pass
        console.print(f"├[red] Asistan 3 Olarak Başladı {ASSNAME3}!")
        console.print(f"├[green] ID :- {ASSID3}!")
    if STRING4 != "None":
        try:
            await ASS_CLI_4.send_message(
                LOG_GROUP_ID,
                "<b>Tebrikler!! Yardımcı İstemci 4 başarıyla başlatıldı!</b>",
            )
        except Exception as e:
            print(
                "\nYardımcı Hesap 4 günlük Kanalı'na erişemedi. Asistanınızı günlük kanalınıza eklediğinizden ve yönetici olarak terfi ettirdiğinizden emin olun!"
            )
            console.print(f"\n[red]Stopping Bot")
            return
        try:
            await ASS_CLI_4.join_chat("ProTubeSupport")
            await ASS_CLI_4.join_chat("sohbetmuhabbetw")
        except:
            pass
        console.print(f"├[red] Asistan 4 Olarak Başladı {ASSNAME4}!")
        console.print(f"├[green] ID :- {ASSID4}!")
    if STRING5 != "None":
        try:
            await ASS_CLI_5.send_message(
                LOG_GROUP_ID,
                "<b>Tebrikler!! Yardımcı İstemci 5 başarıyla başlatıldı!</b>",
            )
        except Exception as e:
            print(
                "\nYardımcı Hesap 5 günlük Kanalı'na erişemedi. Asistanınızı günlük kanalınıza eklediğinizden ve yönetici olarak terfi ettirdiğinizden emin olun!"
            )
            console.print(f"\n[red]Stopping Bot")
            return
        try:
            await ASS_CLI_5.join_chat("ProTubeSupport")
            await ASS_CLI_5.join_chat("sohbetmuhabbetw")
        except:
            pass
        console.print(f"├[red] Asistan 5 Olarak Başladı {ASSNAME5}!")
        console.print(f"├[green] ID :- {ASSID5}!")
    if LOG_SESSION != "None":
        try:
            await LOG_CLIENT.send_message(
                LOG_GROUP_ID,
                "<b>Tebrikler!! Günlükler İstemcisi başarıyla başlatıldı!</b>",
            )
        except Exception as e:
            print(
                "\nGünlük İstemci günlük kanalına erişemedi. Logger Hesabınızı günlük kanalınıza eklediğinizden ve yönetici olarak yükseltdiğinizden emin olun!"
            )
            console.print(f"\n[red]Stopping Bot")
            return
        try:
            await LOG_CLIENT.join_chat("ProTubeSupport")
            await LOG_CLIENT.join_chat("sohbetmuhabbetw")
        except:
            pass
    console.print(f"└[red] Vip Müzik Bot Önyükleme tamamlandı.")
    if STRING1 != "None":
        await pytgcalls1.start()
    if STRING2 != "None":
        await pytgcalls2.start()
    if STRING3 != "None":
        await pytgcalls3.start()
    if STRING4 != "None":
        await pytgcalls4.start()
    if STRING5 != "None":
        await pytgcalls5.start()
    await idle()
    console.print(f"\n[red]Stopping Bot")


home_text_pm = f"""🪧 𝗠𝗲𝗿𝗵𝗮𝗯𝗮 ,

🗯️ 𝗧𝗲𝗵𝗹𝗶𝗸𝗲𝗹𝗶 𝗼̈𝘇𝗲𝗹𝗹𝗶𝗸𝗹𝗲𝗿𝗲 𝘀𝗮𝗵𝗶𝗽 𝗯𝗶𝗿 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗠𝘂̈𝘇𝗶𝗸 + 𝗩𝗶𝗱𝗲𝗼 𝗔𝗸𝗶𝘀̧𝗶 𝗯𝗼𝘁𝘂𝘆𝘂𝗺.

💡 𝗞𝗼𝗺𝘂𝘁𝗹𝗮𝗿𝛊 𝗚𝗿𝘂𝗯𝗹𝗮𝗿𝗱𝗮 𝗞𝘂𝗹𝗹𝗮𝗻𝛊𝗻, 𝗕𝗼𝘁𝘂 𝗚𝗿𝘂𝗯𝗮 𝗘𝗸𝗹𝗲𝘆𝗶𝗽 𝗬𝗼̈𝗻𝗲𝘁𝗶𝗰𝗶 𝗬𝗮𝗽𝘁𝛊𝗸𝘁𝗮𝗻 𝗦𝗼𝗻𝗿𝗮 . . .

✅ 𝗧𝘂̈𝗺 𝗞𝗼𝗺𝘂𝘁𝗹𝗮𝗿 𝗕𝘂𝘁𝗼𝗻𝘂𝗻𝗮 𝗧𝛊𝗸𝗹𝗮𝘆𝛊𝗻 .


**sᴀʀᴋɪ ᴀᴄ̧ᴍᴀ ʟɪᴍɪᴛɪ : 30 ᴅᴋ**
**ᴠɪᴅᴇᴏ ᴀᴄᴍᴀ ʟɪᴍɪᴛɪ : 3 sᴀᴀᴛ**"""


@app.on_message(filters.command("help") & filters.private)
async def help_command(_, message):
    text, keyboard = await help_parser(message.from_user.mention)
    await app.send_message(message.chat.id, text, reply_markup=keyboard)


@app.on_message(filters.command("start") & filters.private)
async def start_command(_, message):
    if len(message.text.split()) > 1:
        name = (message.text.split(None, 1)[1]).lower()
        if name[0] == "s":
            sudoers = await get_sudoers()
            text = "⭐️<u> **Sahipler:**</u>\n"
            sex = 0
            for x in OWNER_ID:
                try:
                    user = await app.get_users(x)
                    user = (
                        user.first_name if not user.mention else user.mention
                    )
                    sex += 1
                except Exception:
                    continue
                text += f"{sex}➤ {user}\n"
            smex = 0
            for count, user_id in enumerate(sudoers, 1):
                if user_id not in OWNER_ID:
                    try:
                        user = await app.get_users(user_id)
                        user = (
                            user.first_name
                            if not user.mention
                            else user.mention
                        )
                        if smex == 0:
                            smex += 1
                            text += "\n⭐️<u> **Yönetici Kullanıcılar:**</u>\n"
                        sex += 1
                        text += f"{sex}➤ {user}\n"
                    except Exception:
                        continue
            if not text:
                await message.reply_text("Yardımcı Yönetici yok")
            else:
                await message.reply_text(text)
            if await is_on_off(5):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                umention = f"[{sender_name}](tg://user?id={int(sender_id)})"
                return await LOG_CLIENT.send_message(
                    LOG_GROUP_ID,
                    f"{message.from_user.mention} botu yeni başlattı.\n\n**KULLANICI KİMLİĞİ:** {sender_id}\n**KULLANICI adı:** {sender_name}",
                )
        if name == "help":
            text, keyboard = await help_parser(message.from_user.mention)
            await message.delete()
            return await app.send_text(
                message.chat.id,
                text,
                reply_markup=keyboard,
            )
        if name[0] == "i":
            m = await message.reply_text("🔎 𝗕𝗶𝗹𝗴𝗶 𝗔𝗹𝗶𝗻𝗶𝘆𝗼𝗿!")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in results.result()["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = f"""
❇️ 𝐈̇𝐬𝐢𝐦: {title}

⏳ 𝐒𝐮̈𝐫𝐞: {duration} Mins
🔗 𝐕𝐢𝐝𝐞𝐨 𝐁𝐚𝐠̆𝐥𝐚𝐧𝐭𝐢𝐬𝐢: [Link]({link})

"""
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="🎥 YouTube İzle", url=f"{link}"
                        ),
                        InlineKeyboardButton(
                            text="• Kapat", callback_data="close"
                        ),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                parse_mode="markdown",
                reply_markup=key,
            )
            if await is_on_off(5):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                umention = f"[{sender_name}](tg://user?id={int(sender_id)})"
                return await LOG_CLIENT.send_message(
                    LOG_GROUP_ID,
                    f"{message.from_user.mention} VİDEO bilgilerini kontrol etmek için botu yeni başlattı <code></code></code>\n\n**KULLANICI kimliği:** {sender_ıdname}\n**KULLANICI adı:** {sender_name}",
                )
            return
    out = private_panel()
    await message.reply_text(
        home_text_pm,
        reply_markup=InlineKeyboardMarkup(out[1]),
    )
    if await is_on_off(5):
        sender_id = message.from_user.id
        sender_name = message.from_user.first_name
        umention = f"[{sender_name}](tg://user?id={int(sender_id)})"
        return await LOG_CLIENT.send_message(
            LOG_GROUP_ID,
            f"{message.from_user.mention} botu yeni başlattı.\n\n**KULLANICI KİMLİĞİ:** {sender_id}\n**KULLANICI adı:** {sender_name}",
        )
    return


async def help_parser(name, keyboard=None):
    if not keyboard:
        keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    return (
        """🪧 𝐌𝐞𝐫𝐡𝐚𝐛𝐚 {first_name}

**sᴀʀᴋɪ ᴀᴄ̧ᴍᴀ ʟɪᴍɪᴛɪ : 30 ᴅᴋ**
**ᴠɪᴅᴇᴏ ᴀᴄᴍᴀ ʟɪᴍɪᴛɪ : 3 sᴀᴀᴛ**
""".format(
            first_name=name
        ),
        keyboard,
    )


@app.on_callback_query(filters.regex("shikhar"))
async def shikhar(_, CallbackQuery):
    text, keyboard = await help_parser(CallbackQuery.from_user.mention)
    await CallbackQuery.message.edit(text, reply_markup=keyboard)


@app.on_callback_query(filters.regex(r"help_(.*?)"))
async def help_button(client, query):
    home_match = re.match(r"help_home\((.+?)\)", query.data)
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)
    create_match = re.match(r"help_create", query.data)
    top_text = f"""🪧 𝐌𝐞𝐫𝐡𝐚𝐛𝐚 {query.from_user.first_name}

**sᴀʀᴋɪ ᴀᴄ̧ᴍᴀ ʟɪᴍɪᴛɪ : 30 ᴅᴋ**
**ᴠɪᴅᴇᴏ ᴀᴄᴍᴀ ʟɪᴍɪᴛɪ : 3 sᴀᴀᴛ**
"""
    if mod_match:
        module = mod_match.group(1)
        text = (
            "{} **{}**:\n".format(
                "𝗜̇𝘀̧𝘁𝗲 𝗯𝘂𝗻𝘂𝗻 𝗶𝗰̧𝗶𝗻 𝘆𝗮𝗿𝗱𝗶𝗺", HELPABLE[module].__MODULE__
            )
            + HELPABLE[module].__HELP__
        )
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="• Geri", callback_data="help_back"
                    ),
                    InlineKeyboardButton(
                        text="• Kapat", callback_data="close"
                    ),
                ],
            ]
        )

        await query.message.edit(
            text=text,
            reply_markup=key,
            disable_web_page_preview=True,
        )
    elif home_match:
        out = private_panel()
        await app.send_message(
            query.from_user.id,
            text=home_text_pm,
            reply_markup=InlineKeyboardMarkup(out[1]),
        )
        await query.message.delete()
    elif prev_match:
        curr_page = int(prev_match.group(1))
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(curr_page - 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif next_match:
        next_page = int(next_match.group(1))
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(next_page + 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif back_match:
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(0, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif create_match:
        text, keyboard = await help_parser(query)
        await query.message.edit(
            text=text,
            reply_markup=keyboard,
            disable_web_page_preview=True,
        )

    return await client.answer_callback_query(query.id)


if __name__ == "__main__":
    loop.run_until_complete(initiate_bot())
