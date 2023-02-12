from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, ChatJoinRequestHandler

WELCOME_MESSAGE = """
<b>
❤️ Thanks {first} for requesting {cname}

🤩Your request will be accepted by our Admins as soon as Possible

💎You Don't have to leave after you are being approved to join because it's one of the best decisions you have ever made on telegram. 

🌀Enjoy your stay with us❤️

✅ Until you get approved, Join Our Other Channels 🙏

🔞 https://t.me/+5i3EGAvgCflmMmZl

🔞 https://t.me/+UJpw1jQBFrUwNGI1

🔞 https://t.me/+ld84Qdzda8QyYWU9
</b>
"""


async def start(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
  """Send a message when the command /start is issued."""

  await update.message.reply_html("I welcome new users.")


import html


async def cjr(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """handles welcomes."""
  user = update.effective_user
  await context.bot.send_animation(
    user.id,
    "https://te.legra.ph/file/63ae10f6a0e79168f072f.mp4",
    caption=WELCOME_MESSAGE.format(first=html.escape(user.first_name),
                                   cname=html.escape(
                                     update.effective_chat.title)),
    parse_mode="html",
  )
  # await update.chat_join_request.approve()


def main() -> None:
  """Start the bot."""
  # Create the Application and pass it your bot's token.
  application = Application.builder().token(
    "6138438487:AAEwfXS7Uqnw_8K_tedXY523EtkwifAdBq0").build()

  # on different commands - answer in Telegram
  application.add_handler(CommandHandler("start", start))
  application.add_handler(ChatJoinRequestHandler(cjr))

  # Run the bot until the user presses Ctrl-C
  application.run_polling()


main()
