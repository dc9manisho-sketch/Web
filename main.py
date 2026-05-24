from flask import Flask, request
from threading import Thread
from discord.ext import commands
import discord
import os
import asyncio

# ================= CONFIG =================
TOKEN = os.getenv("TOKEN")
PREFIX = os.getenv("PREFIX", "!")

# ================= DISCORD BOT =================
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# ================= FLASK WEBHOOK =================
app = Flask(__name__)

@app.route("/")
def home():
    return "PrimeX Casino Bot Online!"

@app.route("/webhook/nowpayments", methods=["POST"])
def webhook():
    print(f"Webhook received: {request.json}")
    return "OK", 200

def run_flask():
    app.run(host="0.0.0.0", port=3000, debug=False)

Thread(target=run_flask, daemon=True).start()

# ================= COMMANDS =================
@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

@bot.command()
async def balance(ctx):
    await ctx.send(f"💰 {ctx.author.mention}: $100 (Demo)")

@bot.event
async def on_ready():
    print(f"✅ Bot online: {bot.user}")
    print(f"🌐 Webhook URL: https://web.onrender.com/webhook/nowpayments")

# ================= RUN =================
if __name__ == "__main__":
    bot.run(TOKEN)
