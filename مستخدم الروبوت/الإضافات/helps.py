# commands for 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 by ~ @MFMVIP


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "الاوامر":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **↯ اهلاً بك عزيزي اختر الاوامر الاتيه :** \n ⪼ اوامر الادمن ~ م1 \n ⪼ اوامر التسليه ~ م2\n ⪼ اوامر الترحيب ~ م3\n ⪼ اوامر الردود ~ م4\n ⪼ اوامر الرفع ~ م5\n ⪼ اوامر الحمايه ~ م6\n ⪼ اوامر التلكراف ~ م7\n ⪼ اوامر الملصقات ~ م8\n ⪼ اوامر التاك ~ م9\n ⪼ اوامر الكشف ~ م10\n ⪼ اوامر المجموعه ~ م11\n ⪼ اوامر الترجمه ~ م12\n ⪼ اوامر البحث ~ م13\n ⪼ اوامر الانتحال ~ 14\n ⪼ اوامر النت ~ م15\n ⪼ اوامر البوت ~ م16\n ⪼ اوامر الحساب ~ م17\n ⪼ اوامر السورس ~ م18\n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP)𓆪"
            )
        else:
            await event.edit(
                "ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **↯ اهلاً بك عزيزي اختر الاوامر الاتيه :** \n ⪼ اوامر الادمن ~ م1 \n ⪼ اوامر التسليه ~ م2\n ⪼ اوامر الترحيب ~ م3\n ⪼ اوامر الردود ~ م4\n ⪼ اوامر الرفع ~ م5\n ⪼ اوامر الحمايه ~ م6\n ⪼ اوامر التلكراف ~ م7\n ⪼ اوامر الملصقات ~ م8\n ⪼ اوامر التاك ~ م9\n ⪼ اوامر الكشف ~ م10\n ⪼ اوامر المجموعه ~ م11\n ⪼ اوامر الترجمه ~ م12\n ⪼ اوامر البحث ~ م13\n ⪼ اوامر الانتحال ~ 14\n ⪼ اوامر النت ~ م15\n ⪼ اوامر البوت ~ م16\n ⪼ اوامر الحساب ~ م17\n ⪼ اوامر السورس ~ م18\n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP)𓆪"
            )


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م1":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر الادمن :** \n⪼ `.حظر` \n⪼ `.الغاء حظر` \n⪼ `.تقيد` \n⪼ `.الغاء تقيد` \n⪼ `.رفع القيود` \n⪼ `.كتم` \n⪼ `.الغاء كتم` \n⪼ `.تثبيت` \n⪼ `.الغاء التثبيت` \n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر الادمن :** \n⪼ `.حظر` \n⪼ `.الغاء حظر` \n⪼ `.تقيد` \n⪼ `.الغاء تقيد` \n⪼ `.رفع القيود` \n⪼ `.كتم` \n⪼ `.الغاء كتم` \n⪼ `.تثبيت` \n⪼ `.الغاء التثبيت` \n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )


########################  𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 ~ BY: MUSTAFA (@MFMVIP)  ########################


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م2":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر التسليه :** \n⪼ `.قمر` \n⪼ `.اقمار` \n⪼ `.قمور` \n⪼ `.قلوب` \n⪼ `.قلب ` \n⪼ `.جيم` \n⪼ `.افكر` \n⪼ `.افكرر` \n⪼ `.شنوو ` \n⪼ `.مح ` \n⪼ `.متت ` \n⪼ `.النضام الشمسي ` \n⪼ `.موسيقى ` \n⪼ `.قنبله ` \n⪼ `.مكبعات ` \n⪼ `.افعى ` \n⪼ `.طائره ` \n⪼ `.نجمه ` \n⪼ `.دائره ` \n⪼ `.شرطه ` \n⪼ `.فايروس ` \n⪼ `.غبي ` \n⪼ `.العد التنازلي`\n⪼ `.يد`\n⪼ `.تهكير`\n⪼ `.قرد `\n⪼ `.بشره `\n⪼ `.انيم `\n⪼ `.نيكول `\n⪼ `.مربع`\n⪼ `.قاتل `\n⪼ `.تحميل`\n⪼ `.رجل `\n⪼ `.شنوو `\n⪼ `.ريبي `\n⪼ `.تفريغ `\n⪼ `.حلويات `\n⪼ `.فليم`\n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر التسليه :** \n⪼ `.قمر` \n⪼ `.اقمار` \n⪼ `.قمور` \n⪼ `.قلوب` \n⪼ `.قلب ` \n⪼ `.جيم` \n⪼ `.افكر` \n⪼ `.افكرر` \n⪼ `.شنوو ` \n⪼ `.مح ` \n⪼ `.متت ` \n⪼ `.النضام الشمسي ` \n⪼ `.موسيقى ` \n⪼ `.قنبله ` \n⪼ `.مكبعات ` \n⪼ `.افعى ` \n⪼ `.طائره ` \n⪼ `.نجمه ` \n⪼ `.دائره ` \n⪼ `.شرطه ` \n⪼ `.فايروس ` \n⪼ `.غبي ` \n⪼ `.العد التنازلي`\n⪼ `.يد`\n⪼ `.تهكير`\n⪼ `.قرد `\n⪼ `.بشره `\n⪼ `.انيم `\n⪼ `.نيكول `\n⪼ `.مربع`\n⪼ `.قاتل `\n⪼ `.تحميل`\n⪼ `.رجل `\n⪼ `.شنوو `\n⪼ `.ريبي `\n⪼ `.تفريغ `\n⪼ `.حلويات `\n⪼ `.فليم`\n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )


########################  𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 ~ BY: MUSTAFA (@MFMVIP)  ########################


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م3":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫   قائـمه اوامر الترحيب + اوامر الساعه :** \n⪼ `.ترحيب ` \n⪼ `.حذف ترحيب ` \n⪼ `.الترحيب `\n`.اوتونيم `\n`.اوتوبايو `\n`.اينداوتونيم `\n`.ايندالبايو التلقائي `\n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩 `.الترحيب `\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر الترحيب :** \n⪼ `.ترحيب ` \n⪼ `.حذف ترحيب ` \n⪼ `.الترحيب `\n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )


########################  𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 ~ BY: MUSTAFA (@MFMVIP)  ########################


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م4":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر الردود :** \n⪼ `.اضف رد ` \n⪼ `.حذف رد ` \n⪼ `.حذف الردود `\n⪼ `.الردود `\n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر الردود :** \n⪼ `.اضف رد ` \n⪼ `.حذف رد ` \n⪼ `.حذف الردود `\n⪼ `.الردود `\n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )


########################  𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 ~ BY: MUSTAFA (@MFMVIP)  ########################


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م5":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر الرفع :** \n⪼ `.رفع مطي ` \n⪼ `.رفع جلب ` \n⪼ `.رفع بكلبي `\n⪼ `.رفع مرتي ` \n⪼ `.رفع تاج ` \n⪼ `.رفع جريذي `\n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر الرفع :** \n⪼ `.رفع مطي ` \n⪼ `.رفع جلب ` \n⪼ `.رفع بكلبي `\n⪼ `.رفع مرتي ` \n⪼ `.رفع تاج ` \n⪼ `.رفع جريذي `\n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )


########################  𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 ~ BY: MUSTAFA (@MFMVIP)  ########################


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م6":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر الحمايه :** \n⪼ `.الكل ` \n⪼ `.المسموح لهم ` \n⪼ `.سماح `\n⪼ `.رفض ` \n⪼ `.بلوك ` \n⪼ `.انبلوك `\n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر الحمايه :** \n⪼ `.الكل ` \n⪼ `.المسموح لهم ` \n⪼ `.سماح `\n⪼ `.رفض ` \n⪼ `.بلوك ` \n⪼ `.انبلوك `\n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )


########################  𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 ~ BY: MUSTAFA (@MFMVIP)  ########################


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م7":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر التلكراف :** \n⪼ `.تلكراف ميديا ` \n⪼ `.تلكراف نص ` \n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر التلكراف :** \n⪼ `.تلكراف ميديا ` \n⪼ `.تلكراف نص ` \n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )


########################  𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 ~ BY: MUSTAFA (@MFMVIP)  ########################


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م8":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر الملصقات :** \n⪼ `.ملصق ` \n⪼ `.معلومات الملصق ` \n⪼ `.حزمه ` \n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر الملصقات :** \n⪼ `.ملصق ` \n⪼ `.معلومات الملصق ` \n⪼ `.حزمه ` \n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )


########################  𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 ~ BY: MUSTAFA (@MFMVIP)  ########################


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م9":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر التاك :** \n⪼ `.تاك ` \n⪼ `.للكل ` + الكلام \n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر التاك :** \n⪼ `.تاك ` \n⪼ `.للكل ` + الكلام \n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )


########################  𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 ~ BY: MUSTAFA (@MFMVIP)  ########################


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م10":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر الكشف :** \n⪼ `.الايدي ` \n⪼ `.ايدي ` \n⪼ `.رابط الحساب ` \n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر الكشف :** \n⪼ `.الايدي ` \n⪼ `.ايدي ` \n⪼ `.رابط الحساب ` \n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )


########### for 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 by ~ @MFMVIP ###########


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م11":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر المجموعه :** \n⪼ `.المجموعه ` \n⪼ `.رفع مشرف ` \n⪼ `.رفع مالك ` \n⪼ `.تك ` \n⪼ `.الاحصائيات ` \n⪼ `.تنظيف الحسابات ` \n⪼ `.الاعضاء ` \n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر المجموعه :** \n⪼ `.المجموعه ` \n⪼ `.رفع مشرف ` \n⪼ `.رفع مالك ` \n⪼ `.تك ` \n⪼ `.الاحصائيات ` \n⪼ `.تنظيف الحسابات ` \n⪼ `.الاعضاء ` \n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )


########################  𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 ~ BY: MUSTAFA (@MFMVIP)  ########################


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م12":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر الترجمه :** \n⪼ `.ترجمه ar` لترجمه من اي لغه الى العربيه \n⪼ `.ترجمه en` لترجمه من اي لغه الى الانكليزيه \n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر الترجمه :** \n⪼ `.ترجمه ar` لترجمه من اي لغه الى العربيه \n⪼ `.ترجمه en` لترجمه من اي لغه الى الانكليزيه \n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )


########################  𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 ~ BY: MUSTAFA (@MFMVIP)  ########################


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م13":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر البحث :** \n⪼ `.بحث` للبحث عن اغنيه + .بحث عشق \n⪼ `.صوره` \n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر البحث :** \n⪼ `.بحث` للبحث عن اغنيه + .بحث عشق \n⪼ `.صوره` \n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )


########### for 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 by ~ @MFMVIP ###########


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م14":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر الانتحال :** \n⪼ `.نسخ`  \n⪼ `.اعاده` \n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر الانتحال :** \n⪼ `.نسخ`  \n⪼ `.اعاده` \n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )


########################  𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 ~ BY: MUSTAFA (@MFMVIP)  ########################


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م15":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر النت :** \n⪼ `.بنك`  \n⪼ `.سرعه النت` \n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر النت :** \n⪼ `.بنك`  \n⪼ `.سرعه النت` \n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )


########################  𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 ~ BY: MUSTAFA (@MFMVIP)  ########################


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م16":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر البوت :** \n⪼ `.اعاده تشغيل`  \n⪼ `.ايقاف ` \n⪼ `.تحديث ` \n⪼ `.تحديث الان `\n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر البوت :** \n⪼ `.اعاده تشغيل`  \n⪼ `.ايقاف ` \n⪼ `.تحديث ` \n⪼ `.تحديث الان `\n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )


########################  𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 ~ BY: MUSTAFA (@MFMVIP)  ########################

import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م17":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر الحساب :** \n⪼ `.اسم` لتغير اسم حسابك \n⪼ `.صوره` لتغير صوره حسابك \n⪼ `.معرف ` لتغير معرف حسابك \n⪼ `.كروباتي ` لعرض المجموعات التي انشأتها \n⪼ `.مسح الصور ` لحذف جميع صور حسابك \n⪼ `.مسح ` لحذف صوره واحده من حسابك \n⪼ `.الحساب ` لعرض معلومات الحساب \n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر الحساب :** \n⪼ `.اسم` لتغير اسم حسابك \n⪼ `.صوره` لتغير صوره حسابك \n⪼ `.معرف ` لتغير معرف حسابك \n⪼ `.كروباتي ` لعرض المجموعات التي انشأتها \n⪼ `.مسح الصور ` لحذف جميع صور حسابك \n⪼ `.مسح ` لحذف صوره واحده من حسابك \n⪼ `.الحساب ` لعرض معلومات الحساب \n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )


########### for 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 by ~ @MFMVIP ###########


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م18":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر السورس :** \n⪼ `.السورس ` لعرض معلومات السورس \n⪼ `.المطور` \n⪼ `.المده ` لعرض مدة استخدام السورس \n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )
        else:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n **✘ ∫  قائـمه اوامر السورس :** \n⪼ `.السورس ` لعرض معلومات السورس \n⪼ `.المطور` \n⪼ `.المده ` لعرض مدة استخدام السورس \n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪"
            )


########################  𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 ~ BY: MUSTAFA (@MFMVIP)  ########################


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "قائمه":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n⪼ **قائمه اوامر طوكيو قم بضغط على الامر لنسخه :**\n⪼ `.ترحيب` \n⪼ `.مسح ترحيب` \n⪼ `.الترحيب ` \n⪼ `.حظر` \n⪼ `.الغاء حظر` \n⪼ `.المحظورين` \n⪼ `.كتم` \n⪼ `.الغاء كتم` \n⪼ `.تقيد` \n⪼ `.الغاء تقيد` \n⪼ `.رفع القيود` \n⪼ `.رفع` - مطي ، جلب \n⪼ `.تثبيت` \n⪼ `.الغاء تثبيت` \n⪼ `.الغاء تثبيت الكل` \n⪼ `.منع كلمه` \n⪼ `.الغاء منع` \n⪼ `.رفع مشرف` \n⪼ `.رفع مالك` \n⪼ `.تنظيف`  》》 يستخدم بالرد على الرساله \n⪼ `.نسخ`  》》لنسخ بروفايل الشخص \n⪼ `.اعاده` 》》لاعاده حسابك بعد نسخ الصوره.. الخ \n⪼ `نسبه الانوثه` \n⪼ `.اعادة التشغيل` \n⪼ `.ايقاف التشغيل` \n⪼ `.تحديث`  》 لتحديث السورس \n⪼ `.بحث` 》 مثلا  `.بحث عشك` \n⪼ `.صوره` 》 مثلا  .صوره طياره \n⪼ `.ايدي` 》 لعرض معلومات البوت \n⪼ `.بنك`  》 يعرض البنك \n⪼ `.سرعه النت` 》 قياس سرعه النت \n⪼ `.ترجمه ar` \n⪼ `.ترجمه en`  \n⪼ `.تكرار`+الرقم + الكلمه \n⪼ `.سبام`  》 كذالك نفس التكرار \n⪼ `.سماح` 》الامر فقط لميزه  حمايه الخاص \n⪼ `.رفض` 》 كذالك \n⪼ `.الكل` 》 لرفض الكل وتشغيل الحمايه \n⪼ `.بلوك` 》 من الخاص \n⪼ `.انبلوك` 》》لرفع الحظر من الخاص  \n⪼ `.المسموح لهم` 》لعرض قائمه السماح \n⪼ `.ايدي` 》 لعرض معلومات المستخدم \n⪼ `.الايدي` \n⪼ `.المجموعه 》》لعرض معلومات المجموعه ` \n⪼ `.السورس 》》 لعرض معلومات السورس ` \n⪼ `.مغادره` 》 تستخدم  لمغادره الكروب \n⪼ `.تاك` 》 لعمل تاك للكل \n⪼ `.للكل` + الكلام 》 لعمل تاك \n⪼ `.تلكراف ميديا` 》 يستخدم بالرد على الصوره \n⪼ `.تلكراف نص` 》 بالرد على الكتابه\n⪼ `.المطور` \nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪 "
            )
        else:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𓆪\n ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n⪼ **قائمه اوامر طوكيو قم بضغط على الامر لنسخه :**\n⪼ `.ترحيب` \n⪼ `.مسح ترحيب` \n⪼ `.الترحيب ` \n⪼ `.حظر` \n⪼ `.الغاء حظر` \n⪼ `.المحظورين` \n⪼ `.كتم` \n⪼ `.الغاء كتم` \n⪼ `.تقيد` \n⪼ `.الغاء تقيد` \n⪼ `.رفع القيود` \n⪼ `.رفع` - مطي ، جلب \n⪼ `.تثبيت` \n⪼ `.الغاء تثبيت` \n⪼ `.الغاء تثبيت الكل` \n⪼ `.منع كلمه` \n⪼ `.الغاء منع` \n⪼ `.رفع مشرف` \n⪼ `.رفع مالك` \n⪼ `.تنظيف`  》》 يستخدم بالرد على الرساله \n⪼ `.نسخ`  》》لنسخ بروفايل الشخص \n⪼ `.اعاده` 》》لاعاده حسابك بعد نسخ الصوره.. الخ \n⪼ `نسبه الانوثه` \n⪼ `.اعادة التشغيل` \n⪼ `.ايقاف التشغيل` \n⪼ `.تحديث`  》 لتحديث السورس \n⪼ `.بحث` 》 مثلا  `.بحث عشك` \n⪼ `.صوره` 》 مثلا  .صوره طياره \n⪼ `.ايدي` 》 لعرض معلومات البوت \n⪼ `.بنك`  》 يعرض البنك \n⪼ `.سرعه النت` 》 قياس سرعه النت \n⪼ `.ترجمه ar` \n⪼ `.ترجمه en`  \n⪼ `.تكرار`+الرقم + الكلمه \n⪼ `.سبام`  》 كذالك نفس التكرار \n⪼ `.سماح` 》الامر فقط لميزه  حمايه الخاص \n⪼ `.رفض` 》 كذالك \n⪼ `.الكل` 》 لرفض الكل وتشغيل الحمايه \n⪼ `.بلوك` 》 من الخاص \n⪼ `.انبلوك` 》》لرفع الحظر من الخاص  \n⪼ `.المسموح لهم` 》لعرض قائمه السماح \n⪼ `.ايدي` 》 لعرض معلومات المستخدم \n⪼ `.الايدي` \n⪼ `.المجموعه 》》لعرض معلومات المجموعه ` \n⪼ `.السورس 》》 لعرض معلومات السورس ` \n⪼ `.مغادره` 》 تستخدم  لمغادره الكروب \n⪼ `.تاك` 》 لعمل تاك للكل \n⪼ `.للكل` + الكلام 》 لعمل تاك \n⪼ `.تلكراف ميديا` 》 يستخدم بالرد على الصوره \n⪼ `.تلكراف نص` 》 بالرد على الكتابه\n⪼ `.المطور` \nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n 𓆩[𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤](t.me/TOKYO_TEAM)𓆪\n 𓆩[𝙈𝙐𝙎𝙏𝘼𝙁𝘼](t.me/MFMVIP) 𓆪 "
            )


########################  𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 ~ BY: MUSTAFA (@MFMVIP)  ########################


import random

from telethon import events


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "ديڤ":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝑫𝑬𝑽𝑬𝑳𝑶𝑷𝑬𝑹 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n ✘ ∫ 𝑫𝑬𝑽 𝑼𝑺𝑬𝑹 ↬ @MFMVIP \n  ✘ ∫ 𝑫𝑬𝑽 𝑰𝑫 ↬ 911945965"
            )
        else:
            await event.edit(
                "𓆰 𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 - 𝑫𝑬𝑽𝑬𝑳𝑶𝑷𝑬𝑹 𓆪\nٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n ✘ ∫ 𝑫𝑬𝑽 𝑼𝑺𝑬𝑹 ↬ @MFMVIP \n  ✘ ∫ 𝑫𝑬𝑽 𝑰𝑫 ↬ 911945965"
            )


########################  𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 ~ BY: MUSTAFA (@MFMVIP)  ########################


from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع جلب(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع جلب(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """For .link command, generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"✘ ∫  المستخدم [{custom}](tg://user?id={user.id}) \n ✘ ∫ تم رفعه جلب في طوكيو",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"✘ ∫  المستخدم [{tag}](tg://user?id={user.id}) \n ✘ ∫ تم رفعه جلب في طوكيو",
        )


async def get_user_from_event(event):
    """Get the user from argument or replied message."""
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and len(args) != 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_obj, extra


async def ge(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


########################  𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 ~ BY: MUSTAFA (@MFMVIP)  ########################


from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع مطي(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع مطي(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """For .link command, generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"✘ ∫  المستخدم [{custom}](tg://user?id={user.id}) \n ✘ ∫  تم رفعه مطي هنا ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"✘ ∫  المستخدم [{tag}](tg://user?id={user.id}) \n ✘ ∫  تم رفعه مطي هنا ",
        )


async def get_user_from_event(event):
    """Get the user from argument or replied message."""
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and len(args) != 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_obj, extra


async def ge(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


########################  𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 ~ BY: MUSTAFA (@MFMVIP)  ########################


from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع مرتي(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع مرتي(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """For .link command, generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"✘ ∫  المستخدم [{custom}](tg://user?id={user.id}) \n ✘ ∫  تـم رفعـه مـࢪتك مـشي نخـلف 😹🤤",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"✘ ∫  المستخدم [{tag}](tg://user?id={user.id}) \n ✘ ∫  تـم رفعـه مـࢪتك مـشي نخـلف 😹🤤",
        )


########################  𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 ~ BY: MUSTAFA (@MFMVIP)  ########################

from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع تاج(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع تاج(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """For .link command, generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"✘ ∫  المستخدم [{custom}](tg://user?id={user.id}) \n ✘ ∫  تـم رفعـه تـاج 👑🔥 ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"✘ ∫  المستخدم [{tag}](tg://user?id={user.id}) \n ✘ ∫  تـم رفعـه تـاج 👑🔥 ",
        )


########################  𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 ~ BY: MUSTAFA (@MFMVIP)  ########################


from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع بكلبي(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع بكلبي(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """For .link command, generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"✘ ∫  المستخدم [{custom}](tg://user?id={user.id}) \n ✘ ∫  تـم رفعـه بڪلبك 🖤 ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"✘ ∫  المستخدم [{tag}](tg://user?id={user.id}) \n ✘ ∫  تـم رفعـه بڪلبك 🖤 ",
        )


########################  𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 ~ BY: MUSTAFA (@MFMVIP)  ########################


from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع جريذي(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع جريذي(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """For .link command, generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"✘ ∫  المستخدم [{custom}](tg://user?id={user.id}) \n ✘ ∫  تـم رفعـه جـࢪيذي ۿنـا 😹🐀 ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"✘ ∫  المستخدم [{tag}](tg://user?id={user.id}) \n ✘ ∫  تـم رفعـه جـࢪيذي ۿنـا 😹🐀 ",
        )


########################  𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 ~ BY: MUSTAFA (@MFMVIP)  ########################


from telethon.tl.types import MessageEntityMentionName

TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY


@bot.on(admin_cmd(pattern="رفع فرخ(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="رفع فرخ(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    """For .link command, generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"✘ ∫  المستخدم [{custom}](tg://user?id={user.id}) \n ✘ ∫  تم رفعه فرخ هنا ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"✘ ∫  المستخدم [{tag}](tg://user?id={user.id}) \n ✘ ∫  تم رفعه فرخ هنا ",
        )


async def get_user_from_event(event):
    """Get the user from argument or replied message."""
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and len(args) != 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_obj, extra


async def ge(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


########################  𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 ~ BY: MUSTAFA (@MFMVIP)  ########################


import random

from telethon.tl.types import MessageEntityMentionName

ppp = [
    "100% 🔱💕.",
    "90%",
    "80%",
    "70%",
    "60%",
    "50%",
    "40%",
    "30%",
    "20%",
    "10%",
    "0%",
]


@bot.on(admin_cmd(pattern="نسبه الانوثه(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="نسبه الانوثه(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    ioi = random.choice(ppp)
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"✘ ∫  نسبه الانوثه لـ [{custom}](tg://user?id={user.id}) هيه {ioi} ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"✘ ∫  نسبه الانوثه لـ [{tag}](tg://user?id={user.id}) هيه {ioi} ",
        )


async def get_user_from_event(event):
    """Get the user from argument or replied message."""
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and len(args) != 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_obj, extra


async def ge(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


########################  𝙎𝙤𝙪𝙧𝙘𝙚 𝙏𝙤𝙠𝙔𝙤 ~ BY: MUSTAFA (@MFMVIP)  ########################


import time

from . import StartTime, get_readable_time, reply_id

DEFAULTUSER = "T0KY0˼༒࿅"
CAT_IMG = "https://telegra.ph/file/967209504b62689f5f770.jpg"
CUSTOM_ALIVE_TEXT = "𓆩 𝙎𝙤𝙪𝙧𝙘𝙚 -˹𝙏𝙤𝙠𝙔𝙤˼༒࿅ - 𝑫𝑬𝑽𝑬𝑳𝑶𝑷𝑬𝑹 𓆪"
EMOJI = "  𓄂† "


@bot.on(admin_cmd(outgoing=True, pattern="المبرمج$"))
@bot.on(sudo_cmd(pattern="المبرمج$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if CAT_IMG:
        cat_caption = f"**{CUSTOM_ALIVE_TEXT}**\n"
        cat_caption += f"ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n"
        cat_caption += f"**{EMOJI}** 𝑫𝑬𝑽 𝑼𝑺𝑬𝑹 ↬ @MFMVIP ༗\n"
        cat_caption += f"**{EMOJI}** 𝑫𝑬𝑽 𝑰𝑫 ↬ 911945965 ༗\n"
        cat_caption += f"ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷"
        await alive.client.send_file(
            alive.chat_id, CAT_IMG, caption=cat_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n"
            f"ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷\n"
            f"**{EMOJI}** 𝑫𝑬𝑽 𝑼𝑺𝑬𝑹 ↬ @MFMVIP ༗\n"
            f"**{EMOJI}** 𝑫𝑬𝑽 𝑰𝑫 ↬ 911945965 ༗\n"
            f"ٴ⊶─────≺ᴛᴏᴋʏᴏ≻─────⊷",
        )


def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = False
    output = "✾"
    if not Config.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "↫ "
        is_database_working = True
    return is_database_working, output
