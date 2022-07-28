from telegram.ext.updater import Updater
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import bot


def main():
    updater = Updater("<bot_token>", use_context=True)
    updater.dispatcher.add_handler(CommandHandler('start', bot.start))
    updater.dispatcher.add_handler(CommandHandler('help', bot.help_command))
    updater.dispatcher.add_handler(CommandHandler('task', bot.task))
    updater.dispatcher.add_handler(MessageHandler(Filters.command, bot.unknown_command))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, bot.catch_text))
    updater.start_polling()


if __name__ == '__main__':
    main()
