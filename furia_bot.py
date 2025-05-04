from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

# --- Dados do Bot ---
proximos_jogos = [
    "🗓️ **FURIA x NAVI** — 27/04 às 14h _(ESL Pro League)_",
    "🗓️ **FURIA x Vitality** — 30/04 às 16h _(Blast Premier)_",
    "🗓️ **FURIA x Team Liquid** — 03/05 às 18h _(IEM Cologne)_",
]

historico_jogos = [
    "✅ **FURIA 2x1 Team Liquid** — 21/04 _(Vitória)_",
    "❌ **FURIA 0x2 Astralis** — 15/04 _(Derrota)_",
]

# --- Stats e Records ---
stats_e_records = [
    "🎯 **FURIA - Maior Vitória:** 16-0 (Contra a equipe X, em 2020).",
    "🎯 **FURIA - Maior Perda:** 0-16 (Contra a equipe Y, em 2021).",
    "🎯 **FalleN - Recorde de Kills:** 40 kills em uma única partida.",
    "🎯 **KSCERATO - Maior Ace:** 5 kills em uma rodada decisiva."
]

# --- Textos prontos de jogadores ---
respostas_jogadores = {
    "art": (
        "🎯 *arT* — In-Game Leader da FURIA.\n\n"
        "Conhecido pelo seu estilo *extremamente agressivo*, liderando com rushs ousados e estratégias únicas. 🧠💥"
    ),
    "yuurih": (
        "🎯 *yuurih* — Rifler.\n\n"
        "*Consistência e precisão!* yuurih é o pilar da FURIA nas trocas e momentos decisivos. 🏆"
    ),
    "kscerato": (
        "🎯 *KSCERATO* — Rifler.\n\n"
        "Reconhecido mundialmente pela *frieza nos clutches* e mira mortal. Um dos melhores do mundo! 🌍🎯"
    ),
    "chelo": (
        "🎯 *chelo* — Rifler.\n\n"
        "*Explosão e energia!* chelo traz agressividade e carisma tanto dentro quanto fora dos servidores! 🔥🎉"
    ),
    "fallen": (
        "🎯 *FalleN* — AWPer e Lenda Brasileira.\n\n"
        "*O Professor!* Campeão mundial, referência tática e agora liderando a FURIA com experiência e maestria. 🧠🏆"
    ),
}

# --- Texto do time ---
resposta_time = (
    "🔥 *FURIA Esports* é uma das maiores organizações de esports do Brasil! 🏆\n"
    "Atuando no cenário competitivo de CS:GO, a FURIA se destaca pelo seu estilo agressivo e tático.\n"
    "A equipe é composta por jogadores talentosos, como arT, yuurih, KSCERATO, chelo e FalleN. 🚀\n"
    "Sua trajetória inclui grandes vitórias e participações em torneios internacionais de CS:GO."
)

# --- Links para Redes Sociais ---
redes_sociais = {
    "Twitter": "https://x.com/FURIA",
    "Instagram": "https://www.instagram.com/furiagg/",
    "Facebook": "https://www.facebook.com/furiagg/following/",
    "YouTube": "https://www.youtube.com/@FURIAgg"
}

# --- Mensagem Inicial com Botão para Menu ---
mensagem_inicial = (
    "🔥 *BEM-VINDO À FAMÍLIA FURIA!* 🔥\n\n"
    "Aqui você vive a paixão pelo CS:GO como nunca! 🏴\n\n"
    "💬 *Como conversar com o bot:*\n"
    "- Pergunte sobre jogadores (ex: *Fala do KSCERATO*, *Quem é o arT?*)\n"
    "- Pergunte sobre o *time*, *próximos jogos*, *histórico*, *stats e records* *ou redes sociais*\n"
    "- Interaja como um verdadeiro fã! 🚀\n\n"
    "*Vamos juntos pelo #FURIAway!* 🏴‍☠️"
)

# --- Funções do Bot ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Criar o botão do menu
    keyboard = [
        [
            InlineKeyboardButton("Menu de Opções", callback_data='menu')
        ],
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Enviar imagem de fundo e a mensagem inicial
    media = "https://upload.wikimedia.org/wikipedia/pt/f/f9/Furia_Esports_logo.png"  # Link da imagem
    await update.message.reply_photo(media)  # Envia a imagem diretamente
    await update.message.reply_text(mensagem_inicial, reply_markup=reply_markup, parse_mode="Markdown")

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto_usuario = update.message.text.lower()

    # Checar por jogador específico
    for jogador in respostas_jogadores:
        if jogador in texto_usuario:
            await update.message.reply_text(respostas_jogadores[jogador], parse_mode="Markdown")
            return

    # Checar por palavras-chave sobre o time ou jogos
    if "time" in texto_usuario:
        await update.message.reply_text(resposta_time, parse_mode="Markdown")
    elif "jogos" in texto_usuario or "próximos" in texto_usuario:
        await update.message.reply_text("🎯 *Próximos jogos da FURIA:*\n\n" + "\n".join(proximos_jogos), parse_mode="Markdown")
    elif "histórico" in texto_usuario:
        await update.message.reply_text("📜 *Histórico recente da FURIA:*\n\n" + "\n".join(historico_jogos), parse_mode="Markdown")
    elif "stats" in texto_usuario or "records" in texto_usuario:
        await update.message.reply_text("🎯 *Stats e Records da FURIA:*\n\n" + "\n".join(stats_e_records), parse_mode="Markdown")
    elif "redes sociais" in texto_usuario:
        await update.message.reply_text(
            "🌐 *Siga a FURIA nas redes sociais!*\n\n"
            f"🔹 [Twitter](https://x.com/FURIA)\n"
            f"🔹 [Instagram](https://www.instagram.com/furiagg/)\n"
            f"🔹 [Facebook](https://www.facebook.com/furiagg/following/)\n"
            f"🔹 [YouTube](https://www.youtube.com/@FURIAgg)", 
            parse_mode="Markdown"
        )
    else:
        # Resposta padrão para mensagens que não correspondem a nada
        await update.message.reply_text(
            "⚡ Não entendi muito bem... Você pode perguntar sobre um jogador, o *time*, *redes sociais* ou pedir os *próximos jogos*! 🏴",
            parse_mode="Markdown"
        )

# --- Respostas aos botões do Menu ---

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Respostas para as opções de menu
    if query.data == 'menu':
        # Criar o menu de opções
        keyboard = [
            [
                InlineKeyboardButton("Sobre o Time", callback_data='time'),
                InlineKeyboardButton("Próximos Jogos", callback_data='jogos'),
            ],
            [
                InlineKeyboardButton("Histórico de Jogos", callback_data='historico'),
                InlineKeyboardButton("Stats & Records", callback_data='stats'),
            ],
            [
                InlineKeyboardButton("Redes Sociais", callback_data='redes')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Escolha uma opção:", reply_markup=reply_markup)
    elif query.data == 'time':
        # Criar botão de voltar
        keyboard = [
            [InlineKeyboardButton("Voltar ao Menu", callback_data='menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=resposta_time, reply_markup=reply_markup, parse_mode="Markdown")
    elif query.data == 'jogos':
        # Criar botão de voltar
        keyboard = [
            [InlineKeyboardButton("Voltar ao Menu", callback_data='menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="🎯 *Próximos jogos da FURIA:*\n\n" + "\n".join(proximos_jogos), reply_markup=reply_markup, parse_mode="Markdown")
    elif query.data == 'historico':
        # Criar botão de voltar
        keyboard = [
            [InlineKeyboardButton("Voltar ao Menu", callback_data='menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="📜 *Histórico recente da FURIA:*\n\n" + "\n".join(historico_jogos), reply_markup=reply_markup, parse_mode="Markdown")
    elif query.data == 'stats':
        # Criar botão de voltar
        keyboard = [
            [InlineKeyboardButton("Voltar ao Menu", callback_data='menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="🎯 *Stats e Records da FURIA:*\n\n" + "\n".join(stats_e_records), reply_markup=reply_markup, parse_mode="Markdown")
    elif query.data == 'redes':
        # Criar botão de voltar
        keyboard = [
            [InlineKeyboardButton("Voltar ao Menu", callback_data='menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🌐 *Siga a FURIA nas redes sociais!*\n\n"
            f"🔹 [Twitter](https://x.com/FURIA)\n"
            f"🔹 [Instagram](https://www.instagram.com/furiagg/)\n"
            f"🔹 [Facebook](https://www.facebook.com/furiagg/following/)\n"
            f"🔹 [YouTube](https://www.youtube.com/@FURIAgg)", 
            reply_markup=reply_markup, parse_mode="Markdown"
        )

# --- Iniciar o Bot ---
app = ApplicationBuilder().token('7489071306:AAFGHcslJfwyyPD2eu9GJpaErAF6JYA4ae4').build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))
app.add_handler(CallbackQueryHandler(button))  # Adicione esse manipulador para os botões

app.run_polling()
