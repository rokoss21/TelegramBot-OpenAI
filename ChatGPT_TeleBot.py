import openai
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


# Set up OpenAI API key
openai.api_key = "OPENAI TOKEN"

# Set up Telegram bot token
bot_token = "TELEGRAM BOT TOKEN"
bot = telegram.Bot(token=bot_token)


# Define a command handler to respond to the /start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hi! I'm a bot that can help you with anything. What can I do for you?")


# Define a message handler to respond to user messages
def message_handler(update: Update, context: CallbackContext):
    # Get the user's message
    message = update.message.text

    # Use OpenAI to generate a response to the user's message
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message,
        max_tokens=2048
    )

    # Send the response back to the user
    bot.send_message(chat_id=update.message.chat_id, text=response.choices[0].text)


# Set up the Telegram bot with the command and message handlers
updater = Updater(bot_token)

# Add handlers for the /start command and user messages
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, message_handler))

# Start the bot
updater.start_polling()
updater.idle()
