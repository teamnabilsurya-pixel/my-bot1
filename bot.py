import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# القائمة الرئيسية
def menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("📸 انستغرام"))
    kb.add(KeyboardButton("📢 تليجرام"))
    kb.add(KeyboardButton("🎵 تيك توك"))
    kb.add(KeyboardButton("💳 الدفع"))
    return kb

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "🔥 أهلاً بك في متجر الخدمات", reply_markup=menu())

# انستغرام
@bot.message_handler(func=lambda m: m.text == "📸 انستغرام")
def insta(message):
    bot.send_message(message.chat.id,
"""
📸 خدمات انستغرام:

1000 متابع = 5$
5000 متابع = 20$
10000 متابع = 35$

✍️ أرسل طلبك بهذه الصيغة:
عدد + يوزر
""")

# تليجرام
@bot.message_handler(func=lambda m: m.text == "📢 تليجرام")
def telegram(message):
    bot.send_message(message.chat.id,
"""
📢 خدمات تليجرام:

1000 مشترك = 4$
5000 مشترك = 18$

✍️ أرسل:
عدد + رابط القناة
""")

# تيك توك
@bot.message_handler(func=lambda m: m.text == "🎵 تيك توك")
def tiktok(message):
    bot.send_message(message.chat.id,
"""
🎵 خدمات تيك توك:

1000 مشاهدة = 2$
1000 لايك = 3$

✍️ أرسل:
عدد + رابط الفيديو
""")

# الدفع
@bot.message_handler(func=lambda m: m.text == "💳 الدفع")
def pay(message):
    bot.send_message(message.chat.id,
"""
💳 طرق الدفع:

- تحويل اسيا

📞 رقم التواصل:
07756650525
""")

# استقبال الطلبات
@bot.message_handler(func=lambda m: True)
def order(message):
    bot.send_message(message.chat.id, "✅ تم استلام طلبك، سيتم التواصل معك قريباً")

bot.infinity_polling()