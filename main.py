from telegram import Update
from telegram.ext import ApplicationBuilder,CommandHandler,MessageHandler,ContextTypes,filters
BOT_TOKEN="YOUR_BOT_TOKEN"
questions=[
    {"q":"Question 1?","options":["A","B","C","D"],"answer":"A"},
    {"q":"Question 2?","options":["A","B","C","D"],"answer":"A"},
    {"q":"Question 3?","options":["A","B","C","D"],"answer":"A"},
    {"q":"Question 4?","options":["A","B","C","D"],"answer":"A"},
    {"q":"Question 5?","options":["A","B","C","D"],"answer":"A"},
    {"q":"Question 6?","options":["A","B","C","D"],"answer":"A"},
    {"q":"Question 7?","options":["A","B","C","D"],"answer":"A"},
    {"q":"Question 8?","options":["A","B","C","D"],"answer":"A"},
    {"q":"Question 9?","options":["A","B","C","D"],"answer":"A"},
    {"q":"Question 10?","options":["A","B","C","D"],"answer":"A"},
    {"q":"Question 11?","options":["A","B","C","D"],"answer":"A"},
    {"q":"Question 12?","options":["A","B","C","D"],"answer":"A"},
    {"q":"Question 13?","options":["A","B","C","D"],"answer":"A"},
    {"q":"Question 14?","options":["A","B","C","D"],"answer":"A"},
    {"q":"Question 15?","options":["A","B","C","D"],"answer":"A"},
    {"q":"Question 16?","options":["A","B","C","D"],"answer":"A"},
    {"q":"Question 17?","options":["A","B","C","D"],"answer":"A"},
    {"q":"Question 18?","options":["A","B","C","D"],"answer":"A"},
    {"q":"Question 19?","options":["A","B","C","D"],"answer":"A"},
    {"q":"Question 20?","options":["A","B","C","D"],"answer":"A"},
    {"q":"Question 21?","options":["A","B","C","D"],"answer":"A"},
    {"q":"Question 22?","options":["A","B","C","D"],"answer":"A"},
    {"q":"Question 23?","options":["A","B","C","D"],"answer":"A"},
    {"q":"Question 24?","options":["A","B","C","D"],"answer":"A"},
    {"q":"Question 25?","options":["A","B","C","D"],"answer":"A"},
    {"q":"Question 26?","options":["A","B","C","D"],"answer":"A"},
    {"q":"Question 27?","options":["A","B","C","D"],"answer":"A"},
    {"q":"Question 28?","options":["A","B","C","D"],"answer":"A"},
    {"q":"Question 29?","options":["A","B","C","D"],"answer":"A"},
    {"q":"Question 30?","options":["A","B","C","D"],"answer":"A"},
]
progress={}
async def sendq(update):
 u=update.effective_user.id;i=progress.get(u,0)
 if i>=len(questions):
  await update.message.reply_text("Quiz completed!");return
 q=questions[i]
 t=f"{i+1}. {q['q']}\n"+"\n".join(q["options"])
 await update.message.reply_text(t)
async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):
 progress[update.effective_user.id]=0;await sendq(update)
async def ans(update:Update,context:ContextTypes.DEFAULT_TYPE):
 u=update.effective_user.id;i=progress.get(u,0)
 if update.message.text.strip().upper()==questions[i]["answer"]:
  await update.message.reply_text("Correct")
 else:
  await update.message.reply_text("Wrong")
 progress[u]=i+1;await sendq(update)
app=ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start",start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,ans))
app.run_polling()
