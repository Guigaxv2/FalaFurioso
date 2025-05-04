from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

TOKEN =  123456789:ABCDefGhIJKlmNoPQRstuVWXyz123456789

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salve, fã da FURIA! Use /ajuda para ver os comandos!")

async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
Comandos:
/noticias – Últimas notícias
/elenco – Quem tá no time?
/proximo_jogo – Quando a FURIA joga?
/curiosidade – Sabia disso?
/quiz – Teste seu conhecimento
""")

async def noticias(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("FURIA classificada pro Major 2025! Próxima parada: vitória!")

async def elenco(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
Elenco Atual:
- FalleN
- yuurih
- KSCERATO
- chelo
- arT
""")

async def proximo_jogo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Próximo jogo: FURIA x NAVI - 10/05/2025 às 17h (BLAST Premier)")

async def curiosidade(update: Update, context: ContextTypes.DEFAULT_TYPE):
    fatos = [
        "A FURIA foi fundada em 2017 e já disputou Majors internacionais.",
        "FalleN entrou na FURIA em 2023, trazendo experiência e liderança.",
        "O nome FURIA representa a intensidade brasileira no CS!"
    ]
    await update.message.reply_text(random.choice(fatos))

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Quiz: Quem é o IGL da FURIA? Responda aí!")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ajuda", ajuda))
    app.add_handler(CommandHandler("noticias", noticias))
    app.add_handler(CommandHandler("elenco", elenco))
    app.add_handler(CommandHandler("proximo_jogo", proximo_jogo))
    app.add_handler(CommandHandler("curiosidade", curiosidade))
    app.add_handler(CommandHandler("quiz", quiz))

    print("Bot da FURIA ativo!")
    await app.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
