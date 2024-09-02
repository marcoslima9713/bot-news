import requests
from translate import Translator
from telegram import Bot
import asyncio

# Configurações
NEWS_API_KEY = '0680a4faaad246109b1fecf383fc95d8'  # Substitua pela sua chave da NewsAPI
TELEGRAM_TOKEN = '7278339227:AAHFPdZzruGLNPDT19xFLIxa9RdP2vTxi0I'  # Substitua pelo seu token do Telegram Bot
TELEGRAM_CHAT_ID = '-1001855762346'  # Substitua pelo chat_id do seu grupo do Telegram
YOUTUBE_CHANNEL_URL = 'https://pay.kiwify.com.br/SZZmiti'  # Substitua pelo link do seu canal do YouTube

# Função para buscar notícias de criptomoedas
def get_crypto_news():
    url = f'https://newsapi.org/v2/everything?q=cryptocurrency&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    news_data = response.json()
    return news_data.get('articles', [])

# Função para traduzir texto para português
def translate_text(text, dest_language='pt'):
    translator = Translator(to_lang=dest_language)
    translated = translator.translate(text)
    return translated

# Função para enviar mensagem ao Telegram
async def send_telegram_message(bot, message):
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message, parse_mode='Markdown')

# Função principal para coletar, traduzir e postar notícias
async def main():
    bot = Bot(token=TELEGRAM_TOKEN)
    articles = get_crypto_news()
    
    for article in articles[:5]:  # Limite para as 5 primeiras notícias, ajuste conforme necessário
        title = translate_text(article['title'])
        description = translate_text(article['description'])
        url = article['url']

        # Mensagem padrão para chamar a pessoa para o canal do YouTube
        youtube_message = (
            "\n\n🔥 *Não perca!* \n"
            "Se torne membro do nosso canal do YouTube para mais atualizações e análises de criptomoedas!\n"
            f"[Acesse aqui]({YOUTUBE_CHANNEL_URL})"
        )

        # Construção da mensagem completa
        message = f"📰 *{title}*\n\n{description}\n\n[Leia mais]({url}){youtube_message}"
        await send_telegram_message(bot, message)

# Executar a função principal
if __name__ == "__main__":
    asyncio.run(main())
