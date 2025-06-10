from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from openai import OpenAI

BOT_TOKEN = "7807724167:AAGYYVtgNonmFf_gWY23awKTm19ss-GiVmw"

# Command: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your bot 😎")

# Echo other messages



async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # await update.message.reply_text(update.messageAI)
    message_user = update.message.text
    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
    )

    completion = client.chat.completions.create(
    extra_headers={
        "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    model="deepseek/deepseek-r1-0528:free",
    # model="deepseek/deepseek-prover-v2:free",
        # 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
    messages=[
        {
        "role": "user",
        "content": message_user
        }
    ]
    )
    messageAI = completion.choices[0].message
    await update.message.reply_text(messageAI.content)


# Main function
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
