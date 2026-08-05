from telegram import Update
from telegram.ext import ApplicationBuilder,CommandHandler,MessageHandler,ContextTypes,filters
BOT_TOKEN="os.getenv("BOT_TOKEN")"
questions = [
    {"q":"What is the capital of Nigeria?","options":["Lagos","Abuja","Kano","Port Harcourt"],"answer":"Abuja"},
    {"q":"Which planet is known as the Red Planet?","options":["Earth","Mars","Venus","Jupiter"],"answer":"Mars"},
    {"q":"What is the largest ocean?","options":["Atlantic","Indian","Pacific","Arctic"],"answer":"Pacific"},
    {"q":"How many continents are there?","options":["5","6","7","8"],"answer":"7"},
    {"q":"Who invented the light bulb?","options":["Thomas Edison","Isaac Newton","Albert Einstein","Nikola Tesla"],"answer":"Thomas Edison"},
    {"q":"What is H2O commonly known as?","options":["Hydrogen","Water","Oxygen","Salt"],"answer":"Water"},
    {"q":"Which country has the Eiffel Tower?","options":["Italy","France","Spain","Germany"],"answer":"France"},
    {"q":"How many days are in a leap year?","options":["365","366","364","360"],"answer":"366"},
    {"q":"Which animal is called the King of the Jungle?","options":["Tiger","Lion","Elephant","Leopard"],"answer":"Lion"},
    {"q":"What is 9 × 9?","options":["72","81","99","90"],"answer":"81"},
    {"q":"Which planet is the largest?","options":["Earth","Mars","Jupiter","Venus"],"answer":"Jupiter"},
    {"q":"Which gas do plants absorb?","options":["Oxygen","Carbon Dioxide","Nitrogen","Hydrogen"],"answer":"Carbon Dioxide"},
    {"q":"What is the currency of Nigeria?","options":["Dollar","Naira","Cedi","Rand"],"answer":"Naira"},
    {"q":"How many hours are in a day?","options":["12","24","36","48"],"answer":"24"},
    {"q":"Which continent is Nigeria in?","options":["Asia","Europe","Africa","Australia"],"answer":"Africa"},
    {"q":"Who wrote Romeo and Juliet?","options":["William Shakespeare","Charles Dickens","Mark Twain","Jane Austen"],"answer":"William Shakespeare"},
    {"q":"What is the square root of 64?","options":["6","7","8","9"],"answer":"8"},
    {"q":"Which bird cannot fly?","options":["Parrot","Penguin","Eagle","Crow"],"answer":"Penguin"},
    {"q":"Which organ pumps blood?","options":["Brain","Heart","Kidney","Liver"],"answer":"Heart"},
    {"q":"How many months are in a year?","options":["10","11","12","13"],"answer":"12"},
    {"q":"What is the tallest animal?","options":["Elephant","Horse","Giraffe","Camel"],"answer":"Giraffe"},
    {"q":"Which is the smallest continent?","options":["Africa","Europe","Australia","Asia"],"answer":"Australia"},
    {"q":"Which language is mainly spoken in Brazil?","options":["Spanish","Portuguese","French","English"],"answer":"Portuguese"},
    {"q":"What is the capital of Ghana?","options":["Lagos","Accra","Nairobi","Abuja"],"answer":"Accra"},
    {"q":"Which instrument has 88 keys?","options":["Guitar","Drums","Piano","Violin"],"answer":"Piano"},
    {"q":"What is the largest mammal?","options":["Elephant","Blue Whale","Hippo","Giraffe"],"answer":"Blue Whale"},
    {"q":"Which planet has rings?","options":["Earth","Mars","Saturn","Mercury"],"answer":"Saturn"},
    {"q":"What is the boiling point of water?","options":["90°C","100°C","110°C","120°C"],"answer":"100°C"},
    {"q":"Which is the fastest land animal?","options":["Horse","Lion","Cheetah","Tiger"],"answer":"Cheetah"},
    {"q":"Which is the largest continent?","options":["Africa","Europe","Asia","Australia"],"answer":"Asia"},
]
progress = {}

async def sendq(update):
    u = update.effective_user.id
    i = progress.get(u, 0)

    if i >= len(questions):
        await update.message.reply_text("🎉 Quiz Finished!")
        return

    q = questions[i]

    text = (
        f"Question {i+1}/{len(questions)}\n\n"
        f"{q['q']}\n\n"
        f"1. {q['options'][0]}\n"
        f"2. {q['options'][1]}\n"
        f"3. {q['options'][2]}\n"
        f"4. {q['options'][3]}\n\n"
        "Reply with 1, 2, 3 or 4."
    )

    await update.message.reply_text(text)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    progress[update.effective_user.id] = 0
    await sendq(update)


async def ans(update: Update, context: ContextTypes.DEFAULT_TYPE):
    u = update.effective_user.id
    i = progress.get(u, 0)

    if i >= len(questions):
        await update.message.reply_text("🎉 Quiz Finished!")
        return

    try:
        choice = int(update.message.text.strip())
    except ValueError:
        await update.message.reply_text("Please reply with 1, 2, 3 or 4.")
        return

    if choice < 1 or choice > 4:
        await update.message.reply_text("Please choose a number between 1 and 4.")
        return

    q = questions[i]

    if q["options"][choice - 1] == q["answer"]:
        await update.message.reply_text("✅ Correct!")
    else:
        await update.message.reply_text(
            f"❌ Wrong!\nCorrect answer: {q['answer']}"
        )

    progress[u] = i + 1
    await sendq(update)


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, ans))

print("Bot is running...")
app.run_polling()
