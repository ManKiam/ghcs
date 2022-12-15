"""install:
set max idle timeout in https://github.com/settings/codespaces
create codespace https://github.com/ManKiam/ghcs
rename codespace name to `big bang`
"""
import asyncio, time
from playwright.async_api import async_playwright
from telebot.async_telebot import AsyncTeleBot

time.sleep(5)
sessions = [    # user_session, next_index
    ["WXswTl0t2OLEHu3uybq2fxOxHi2mTU3RepfahPjMa2dN799T", 1],  # assdf43gqs@gmail.com:Qwe123!@#2
    ["q8u0h2WM9chKX7xlRXHeg-a6C5aP89r5BAY4Rgmk9RQcJn2Q", 2],  # mmadtqi125@protonmail.com:asjtp77nbby8tv6
    ["wHg0E4whbRAuwgVNwEpzVhs7MuaIyk9QKYap29Hn8Vjts4SU", 3],
    ["wHg0E4whbRAuwgVNwEpzVhs7MuaIyk9QKYap29Hn8Vjts4SU", 4],
    ["wHg0E4whbRAuwgVNwEpzVhs7MuaIyk9QKYap29Hn8Vjts4SU", 5],
    ["wHg0E4whbRAuwgVNwEpzVhs7MuaIyk9QKYap29Hn8Vjts4SU", 6],
    ["wHg0E4whbRAuwgVNwEpzVhs7MuaIyk9QKYap29Hn8Vjts4SU", 7],
    ["wHg0E4whbRAuwgVNwEpzVhs7MuaIyk9QKYap29Hn8Vjts4SU", 8],
    ["wHg0E4whbRAuwgVNwEpzVhs7MuaIyk9QKYap29Hn8Vjts4SU", 0]
]

cur_index = int(open('cur').read().strip())
last_expire = int(open('ex').read().strip())
if last_expire < time.time():
    cur_ex = int(time.time() + (60*60*24*19))
    open('ex', 'w').write(str(cur_ex))
else:
    cur_ex = last_expire

bot = AsyncTeleBot('5965228241:AAHAc0C_PUYEY3f8weXdL-Eqnc0dnaMbLE8')
chat = 5927280615

async def func():
    msg = (await bot.send_message(chat, str(int(time.time())))).message_id
    await asyncio.sleep(2)
    while 1:
        await bot.edit_message_text(str(int(time.time())), chat, msg)
        await asyncio.sleep(60*1)


async def main():
    asyncio.create_task(func())
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        context = await browser.new_context(storage_state={"cookies": [{
            "name": "user_session", "value": sessions[cur_index][0], "url": "https://github.com"
        }]})
        page = await context.new_page()
        await page.goto("https://github.com/codespaces")
        await page.get_by_role("link", name="big bang").click()

        now = time.time()
        while now < cur_ex:
            await page.mouse.click(0, 0)
            await page.wait_for_timeout(1*60*1000)
            now = time.time()

        await context.close()
        await browser.close()

    next_index = sessions[cur_index][1]
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        context = await browser.new_context(storage_state={"cookies": [{
            "name": "user_session", "value": sessions[next_index][0], "url": "https://github.com"
        }]})
        page = await context.new_page()
        await page.goto("https://github.com/codespaces")
        await page.get_by_role("link", name="big bang").click()
        await page.wait_for_timeout(5000)

        await context.close()
        await browser.close()


asyncio.run(main())
# from playwright.sync_api import sync_playwright
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("http://github.com")
#     print(page.title())
#     browser.close()
