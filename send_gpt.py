import g4f

providers = [
    g4f.Provider.Liaobots,
    g4f.Provider.ChatgptNext,
    g4f.Provider.FlowGpt
]


def ask(q, provider):
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": q}],
        provider=provider
    )
    return response


current_provider = 0
response = ''
while response == '':
    try:
        response = ask(
            """К какой из трёх тем (экология, социология, управление) относится следующая статья статья? Напиши только одно слово. МОСКВА, 29 ноя - РИА Новости. Сбербанк вплотную занялся экологией и разработал проекты по "умному" использованию мусора: из пластиковых стаканчиков уже создает ручки, а из старых или невостребованных карт будет делать окна, рассказал в интервью РИА Новости первый зампред правления Сбербанка Александр Ведяхин. "Сотрудники "Сбера" генерируют огромное количество разных креативных идей, многие из которых "Сбер" поддерживает, и те превращаются в проекты. Только в сфере экологии у нас более 150 проектов. Приведу пример. В отделениях банка в большом количестве выбрасываются пластиковые стаканчики у кулеров. Наши сотрудники предложили делать из них шариковые ручки, и мы запустили такой проект: из пяти стаканчиков получается одна ручка", - поделился он. При этом у банка есть и более амбициозный проект. "Мы пошли дальше и стали думать, что делать с использованными или невостребованными банковскими картами. Сейчас мы начинаем проект по их переработке в оконный профиль для наших отделений", - добавил первый зампред правления Сбербанка. Ведяхин подчеркнул, что в настоящее время наблюдается сильный запрос на решение ESG-вопросов со стороны клиентов, сотрудников, акционеров и инвесторов Сбербанка. ESG (ecological, social and corporate governance) - это подход к управлению, который стремится включить факторы окружающей среды, социальные факторы и факторы управления в процесс принятия решений для лучшего управления рисками и устойчивого развития компании. Структура природного цеолита, увеличеная в 2000 раз - РИА Новости, 1920, 31.07.2020 Создан материал для переработки пластика и поглощения углекислого газа 31 июля 2020, 13:55 "Это стало особенно заметно в пандемию. Люди испытывают тревогу за своё будущее и ожидают от бизнеса участия в решении социально значимых проблем. Кроме того, сегодня невозможно быть успешной компанией без соблюдения критериев ESG, иначе потребители просто объявят бойкот вашим товарам или услугам, а инвесторы перестанут покупать ваши акции", - заключил он.""",
            providers[current_provider])
    except Exception as e:
        if current_provider == len(providers) - 1:
            current_provider = 0
        else:
            current_provider += 1

print(response)
