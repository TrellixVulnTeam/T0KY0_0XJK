# Userbot module for fetching info about any user on Telegram(including you!).

import os

from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location

from . import get_user_from_event

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="ايدي(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="ايدي(?: |$)(.*)", allow_sudo=True))
async def who(event):
    cat = await edit_or_reply(event, "⇆")
    if not os.path.isdir(TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TMP_DOWNLOAD_DIRECTORY)
    replied_user = await get_user(event)
    if replied_user is None:
        return await edit_or_reply(cat, "☆:↫لايمكنني العثور ع المستخدم")
    try:
        photo, caption = await fetch_info(replied_user, event)
    except AttributeError:
        await edit_or_reply(cat, "`Could not fetch info of that user.`")
        return
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    try:
        await event.client.send_file(
            event.chat_id,
            photo,
            caption=caption,
            link_preview=False,
            force_document=False,
            reply_to=message_id_to_reply,
            parse_mode="html",
        )
        if not photo.startswith("http"):
            os.remove(photo)
        await cat.delete()
    except TypeError:
        await cat.edit(caption, parse_mode="html")


async def get_user(event):
    """Get the user from argument or replied message."""
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        previous_message = await event.get_reply_message()
        if previous_message.from_id is None and not event.is_private:
            return None
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
    else:
        user = event.pattern_match.group(1)
        if user.isnumeric():
            user = int(user)
        if not user:
            self_user = await event.client.get_me()
            user = self_user.id
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return replied_user


async def fetch_info(replied_user, event):
    """Get details from the User object."""
    replied_user_profile_photos = await event.client(
        GetUserPhotosRequest(
            user_id=replied_user.user.id, offset=42, max_id=0, limit=80
        )
    )
    replied_user_profile_photos_count = "  ☆:↫ لاتوجد صوره بروفايل"
    try:
        replied_user_profile_photos_count = replied_user_profile_photos.count
    except AttributeError:
        pass
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    last_name = replied_user.user.last_name
    try:
        dc_id, location = get_input_location(replied_user.profile_photo)
    except Exception:
        pass
    replied_user.common_chats_count
    username = replied_user.user.username
    user_bio = replied_user.about
    replied_user.user.bot
    replied_user.user.restricted
    replied_user.user.verified
    photo = await event.client.download_profile_photo(
        user_id, TMP_DOWNLOAD_DIRECTORY + str(user_id) + ".jpg", download_big=True
    )
    first_name = (
        first_name.replace("\u2060", "")
        if first_name
        else ("هذا المستخدم ليس له اسم أول")
    )
    last_name = last_name.replace("\u2060", "") if last_name else (" ")
    username = "@{}".format(username) if username else ("لايوجد معرف")
    user_bio = "لاتوجد نبذه" if not user_bio else user_bio
    caption = "<b><i> 𓆩𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝙋𝙍𝙊 𝘿𝘼𝙏𝘼𓆪 </i></b>\n"
    caption += f"<b> ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷ </b>\n"
    caption += f"<b> • 🖤 | FIRST NAME 𓆪</b> {first_name} {last_name}\n"
    caption += f"<b> • 🖤 | USR 𓆪</b> {username}\n"
    caption += f"<b> • 🖤 | ID 𓆪</b> <code>{user_id}</code>\n"
    caption += f"<b> • 🖤 | NUMBR OF PRO PIC 𓆪</b> {replied_user_profile_photos_count}\n"
    caption += f"<b> • 🖤 | BIO ↬ </b> \n {user_bio} \n"
    caption += f"<b> • 🖤 | MY PRO LINK 𓆪</b> "
    caption += f'<a href="tg://user?id={user_id}">{first_name}</a>'
    caption += f"<b> ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷ </b>\n"
    caption += f"<b> 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪 </b>\n"
    caption += f"<b> 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP)𓆪 "
    return photo, caption


@bot.on(admin_cmd(pattern="رابط الحساب(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رابط الحساب(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """For .link command, generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(mention, f"[{tag}](tg://user?id={user.id})")


async def ge(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


CMD_HELP.update(
    {
        "whois": "**Plugin : **`whois`\
    \n\n  •  **Syntax : **`.whois <username> or reply to someones text with .whois`\
    \n  •  **Function : **__Gets info of an user.__\
    \n\n  •  **Syntax : **`.userinfo <username> or reply to someones text with .userinfo`\
    \n  •  **Function : **__Gets information of an user such as restrictions ban by spamwatch or cas__\
    \n\n  •  **Syntax : **`.link id/username/reply`\
    \n  •  **Function : **__Generates a link to the user's PM .__"
    }
)
