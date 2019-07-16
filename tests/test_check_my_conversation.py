

def test_check_my_conversation(app):
    tariff = 'мой'
    price = 200
    url = '/tariff/my-conversation'
    app.open_homepage()
    app.homepage.open_searchpage()
    app.homepage.search_tariff(tariff)
    app.homepage.select_my_conversation_tariff()
    my_conversation_price = app.tariff.get_tariff_price()
    current_url = app.homepage.get_current_url()
    assert my_conversation_price == price
    assert current_url == url
