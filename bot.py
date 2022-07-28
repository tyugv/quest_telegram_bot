from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from quest import Quest
from random import randint
from time import sleep

quest = Quest(file_path='example_quest.txt')


def start(update: Update, context: CallbackContext):
    if not quest.is_done:
        update.message.reply_text("Hello! For first task print /task")


def help_command(update: Update, context: CallbackContext):
    if not quest.is_done:
        update.message.reply_text("To read task again print /task")


def task(update: Update, context: CallbackContext):
    if not quest.is_done:
        if quest.current_task.photo != '0':
            update.message.reply_photo(quest.current_task.photo)
        update.message.reply_text(quest.print_task())


def catch_text(update: Update, context: CallbackContext):
    if not quest.is_done:
        is_right, text = quest.check_password(update.message.text)
        update.message.reply_text(text)
        if is_right:
            sleep(1)
            task(update, context)
            if quest.is_done:
                update.message.reply_text('You found all presents! Happy birthday! ❤')
    else:
        random_phrases = ['Happy birthday!', 'Congratulations!']

        update.message.reply_text(random_phrases[randint(0, len(random_phrases) - 1)])


def unknown_command(update: Update, context: CallbackContext):
    update.message.reply_text(f"Sorry {update.message.text} is not a valid command")
