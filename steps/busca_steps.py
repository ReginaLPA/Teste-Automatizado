from behave import given, when, then
from utils import  Utils
from pages.header_page import HeaderPage
from pages.resultPage import ResultPage
from nose.tools import assert_equal


utils = Utils()
headerPage = HeaderPage()
resultPage = ResultPage()

@given(u'que acesso o site do Python')
def step_impl(context):
    utils.navegar('https://www.python.org/')



@given(u'preencho o input da pesquisa')
def step_impl(context):
    headerPage.preenche_input_busca('Python')

@when(u'clico no botão de pesquisar')
def step_impl(context):
    headerPage.click_btn_go()

@then(u'devo visualizar os resultados da pesquisa')
def step_impl(context):
    assert_equal(resultPage.get_text_title(),'Search Python.org')

