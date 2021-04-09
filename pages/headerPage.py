from browser import Browser

class HeaderPageElement(object):
    INPUT_BUSCA = '#id-search-field'
    BTN_SUBMIT = '#submit'

class HeaderPage(Browser):
    def preenche_input_busca(self, texto):
        self.driver.find_element_by_css_selector(HeaderPageElement.INPUT_BUSCA).send_keys(texto)

    def click_btn_go(self):
        self.driver.find_element_by_css_selector(HeaderPageElement.BTN_SUBMIT).click()


"""
para executar os testes com relatorio
behave --tags=@busca -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features

para visualizar os resultados do relatorio
$ allure serve %allure_result_folder%
"""