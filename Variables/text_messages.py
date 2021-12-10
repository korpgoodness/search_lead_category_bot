TIME_SLEEP_MAILING_START_1 = 300
TIME_SLEEP_MAILING_START_2 = 1200
TIME_SLEEP_MAILING_FREE = 21600
TIME_SLEEP_MAILING_PAYMENT = 43200
TIME_SLEEP_CHECK_TARIFFS = 3540
TIME_SLEEP_CHECK_CHANNELS = 100

FREE_TERM = 12
PRICE_ONE_TARIFF = 390
PRICE_TWO_TARIFF = 590
PRICE_THREE_TARIFF = 990

SALE_PRICE_ONE_TARIFF = 312
SALE_PRICE_TWO_TARIFF = 472
SALE_PRICE_THREE_TARIFF = 792

TEXT_ONE_TARIFF = "1 неделя"
TEXT_TWO_TARIFF = "2 недели"
TEXT_THREE_TARIFF = "1 месяц"

COMMAND_FREE_TARIFF = 'free'
COMMAND_ONE_TARIFF = 'one_week'
COMMAND_TWO_TARIFF = 'two_week'
COMMAND_THREE_TARIFF = 'one_month'

TARIFFS = {
	COMMAND_ONE_TARIFF: TEXT_ONE_TARIFF,
	COMMAND_TWO_TARIFF: TEXT_TWO_TARIFF,
	COMMAND_THREE_TARIFF: TEXT_THREE_TARIFF
}

PRICES = {
	COMMAND_ONE_TARIFF: PRICE_ONE_TARIFF,
	COMMAND_TWO_TARIFF: PRICE_TWO_TARIFF,
	COMMAND_THREE_TARIFF: PRICE_THREE_TARIFF
}

SALE_PRICES = {
	COMMAND_ONE_TARIFF: SALE_PRICE_ONE_TARIFF,
	COMMAND_TWO_TARIFF: SALE_PRICE_TWO_TARIFF,
	COMMAND_THREE_TARIFF: SALE_PRICE_THREE_TARIFF
}

DEADLINES_TARIFFS = {
	COMMAND_ONE_TARIFF: 7,
	COMMAND_TWO_TARIFF: 14,
	COMMAND_THREE_TARIFF: 30
}

LINK_CHANNEL = 'https://t.me/Leadscrollinfo'
USERNAME_CHANNEl = '@Leadscrollinfo'
LINK_MANAGER = 'https://t.me/leadscroll'
USERNAME_MANAGER = '@leadscroll'


BUTTON_TARIF_ONE = f"{FREE_TERM} часов free + подарок 🎁"
BUTTON_TARIF_TWO = f"{TEXT_ONE_TARIFF} - {PRICE_ONE_TARIFF}₽ 📕"
BUTTON_TARIF_THREE = f"{TEXT_TWO_TARIFF} - {PRICE_TWO_TARIFF}₽ 📗"
BUTTON_TARIF_FOUR = f"{TEXT_THREE_TARIFF} - {PRICE_THREE_TARIFF}₽ 📘"

SALE_BUTTON_TARIF_TWO = f"{TEXT_ONE_TARIFF} - {SALE_PRICE_ONE_TARIFF}₽ 📕"
SALE_BUTTON_TARIF_THREE = f"{TEXT_TWO_TARIFF} - {SALE_PRICE_TWO_TARIFF}₽ 📗"
SALE_BUTTON_TARIF_FOUR = f"{TEXT_THREE_TARIFF} - {SALE_PRICE_THREE_TARIFF}₽ 📘"

BUTTON_PAYMENT_ONE = "Оплатить в боте 🤖"
BUTTON_PAYMENT_TWO = "Оплатить напрямую 🙋‍♂️"

REPLACE_SYMBOLS = "###"
REPLACE_SYMBOLS_1 = "$$$"
REPLACE_SYMBOLS_2 = "@@@"


start_message_1 = """
Привет! 👋

Как все работает? 🤔: 
🔸 Наш бот ищет заявки по 500+ чатам в Telegram и присылает их в бота, распределяя между вами, что бы не создавать конкуренции, а так же подбирает актуальные вакансии с бирж фриланса.

🔸 Всё что нужно:
 - Подключить бесплатный тариф
 - Получить подарок
 - Начать получать заявки и зарабатывать деньги
"""

start_message_2 = f"""
⚡️Получи бесплатную подписку на 12 часов + подарок 🎁 от нашего сервиса.

Для этого нажимай на кнопку «12 часов бесплатно» 

Подробнее о подписке и других возможностях бота -> "добавим позже" 💬
"""

MAILING_MESSAGE_START_1 = """
Тебе дана уникальная возможность опробовать нашего бота на практике 😨

Всего 3 простых действия:
  - Нажать кнопку "Активировать подписку 🎁"
  - Выбрать интересующие тебя категории
  - Отвечать на новые заявки

Так чего же ты ждешь?!🧐
"""

MAILING_MESSAGE_START_2 = """
Ты ещё не попробовал нашего бота в действии? 🧐

Обрабатывай заявки уже сейчас и получи бесплатный подарок, который поможет тебе максимально эффективно забирать заказы 🤝🔥
"""

CHOOSING_CATEGORY = f"""
✅ После оплаты тарифа {REPLACE_SYMBOLS}, вы получите:

✔️ Чек-лист по составлению правильного отклика на заявки.
Мы собрали примеры и разобрали отклик на 3 части, каждую из которых подробно расписали, чтобы вы могли составить правильное обращение.
———
🎁 Доступно в бесплатной версии

✔️ Качественные и целевые заявки по тарифу {REPLACE_SYMBOLS}
• Бот сначала отправляет заявки людям с подпиской, после чего пользователям на бесплатном тарифе.
"""

SUPPORT = f"""
❗️Если у вас возник вопрос или проблема с использованием бота 🤖, то напишите в тех.поддержку или спросите у нашего менеджера напрямую.
💬 Контакт менеджера - {USERNAME_MANAGER}
"""

INFORMATION = f"""
ℹ️ Подробнее о боте и его фишках вы можете прочитать в нашем [Инфо канале]({LINK_CHANNEL}) 💬
"""

FREE_TARIFF = f"""
Вы выбрали тариф «{REPLACE_SYMBOLS} часов бесплатно»

Бот отправит вам заявки, как только они появятся в каналах.

На бесплатном тарифе мы скрываем контакты. Это нужно, чтобы клиенты оформившие платную подписку, не теряли заказчиков ❗️
"""

FREE_TARIFF_MAILING = """
Забери свой подарок! 🎁
- Специальный чек-лист по составлению правильного отклика на заявки.
👇
https://clck.ru/YvTjG
"""

ALREADY_USING_FREE = f"""
У вас уже подключен бесплатный тариф ☺️
До окончания тарифа: {REPLACE_SYMBOLS}
"""

ALREADY_PURCHASED_TARIFF = f"""
✔️ Вы уже приобрели тариф «{REPLACE_SYMBOLS}»
До окончания тарифа: {REPLACE_SYMBOLS}
Количество присланных заявок: {REPLACE_SYMBOLS}
"""

ALREADY_USED_FREE = f"""
❗️Вы уже использовали бесплатный тариф 
Посмотрите другой раздел или попробуйте наши другие тарифы в данной категории ☺️
"""

ENDED_FREE_TARIFF = f"""
ℹ️ Ваша бесплатная подписка закончилась. 

Количество присланных заявок: {REPLACE_SYMBOLS}

Мы предлагаем сотрудничать дальше вместе с нами и ежедневно получать заказы. Благодаря нам 92% специалистов находят своих заказчиков за первые три дня 🤝

Так же, специально для вас мы дарим скидку на любой наш тариф в размере 20% 🔥
"""

MAILING_MESSAGE_AFTER_FREE = f"""
Все еще думаешь? 🧐

А что будет, если я тебе скажу, что ты получишь 20% скидку на любой платный тариф и 3 дня использования в подарок? 🎁

Пиши мне в личные сообщения промокод «SALE» и подключай данное предложение! ⚡️

Внимание: Акция работает только на одном тарифе 
"""

PAYMENT_TITLE = 'Оплата тарифа'

PAID_TARIFF = """
Если у вас возникли трудности во время оплаты, обращайтесь в поддержку - @Leadscroll
"""

ENABLING_TARIFF = f"""
✅ Вы успешно оформили подписку! 

Подождите первые заявки и приступайте к работе!  📲
"""

STOP_TARIFF = f"""
❌ Ваша подписка закончилась
Количество присланных заявок: {REPLACE_SYMBOLS}
"""

END_WARNING_PAYMENT_TARIFF = f"""
Ваша подписка истекает ровно через 24 часа ❗️
"""

MAILING_MESSAGE_AFTER_PAYMENT = f"""
Продли свою подписку со скидкой 40% ⚡️

Предложение действует только 12 часов ❗️
"""

APPLICATION = f"""
<b>Заявка №{REPLACE_SYMBOLS_1} 🚀 | {REPLACE_SYMBOLS_2}</b>

{REPLACE_SYMBOLS}
"""

HIDE_CONTACT = """

Контакты: *****"""

APPLICATION_FREE = f"""
_________

📚 Почему мы скрываем контакты на бесплатном периоде ❓ -  https://clck.ru/YjYAs

По вопросам бота - {USERNAME_MANAGER}
"""

STATISTIC = f"""
<b>Статистика:</b>
Всего пользователей - {REPLACE_SYMBOLS}
Пользователей с бесплатной подпиской - {REPLACE_SYMBOLS}
Пользователей с платной подпиской - {REPLACE_SYMBOLS}
Не активных пользователей - {REPLACE_SYMBOLS}
"""


CATEGORY = "target"
CATEGODIES = {
	CATEGORY: 'Таргет'
}

target = ["таргетолог", "таргетинг", "таргет"]
target_phrases = ["настроить таргет"]

no = ['дизайн', "дизайнер"]

advertisement = [
	"внимание, читай до конца", 
	"в наличии кypcы блогеров", 
	"внимательно почитайте", 
	"внимательно прочитайте",
	"внимательно читайте", 
	"читай до конца",
	"что входит в мою работу",
	"меня зовут",
	"чем я могу быть вам полезна", 
	"чем я могу быть вам полезен", 
	"всем привет",
	"здравствуйте",
	'массовая рассылка',
	"я вам помогу",
	"супер акция",
	"я начинающий",
	"добрый вечер",
	"добрый день",
	"доброе утро",
	"#ишуклиента",
	"#помогy"
]