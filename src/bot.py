from selenium.webdriver import Chrome, ChromeService, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from os import getcwd
from time import sleep


class Bot:
    __instante = None
    __driver = None
    __tempoEspera = 3

    def __new__(cls, *args, **kargs):
        if cls.__instante is None:
            cls.__instante = super().__new__(cls)
        return cls.__instante

    def __init__(self, categoria: str, quantLivros: int) -> None:
        self.categoria = categoria
        self.quantLivros = quantLivros

        opcoes = ["--start-maximized", "--lang=pt-BR", "--incognito"]
        self.__driver: Chrome = self.__configurarDriver(*opcoes)
        self.__driver.get("https://www.amazon.com.br/amz-books/store?")

    def __configurarDriver(*opcoes: str) -> Chrome:
        verificarOpcoes = lambda x: (
            str(x).startswith("--") and isinstance(x, str) and x != ""
        )
        opcoesFiltradas = list(filter(verificarOpcoes, opcoes))
        chromeOptions = ChromeOptions()
        chromeService = ChromeService()

        if len(opcoesFiltradas) == 1:
            chromeOptions.add_argument(opcoesFiltradas[0])
        elif len(opcoesFiltradas) > 1:
            for opcao in opcoesFiltradas:
                chromeOptions.add_argument(opcao)
        chromeOptions.add_experimental_option(
            "prefs",
            {
                "download.default_directory": getcwd() + r"\imgs",
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True,
            },
        )

        return Chrome(options=chromeOptions, service=chromeService)

    def retornarInicio(self) -> None:
        self.__driver.get("https://www.amazon.com.br/amz-books/store?")
        sleep(self.__tempoEspera)

    def navegarPorCategoria(self) -> None:
        subNavegacaoElemento = self.__driver.find_element(By.ID, "nav-subnav")
        categoriaElemento = subNavegacaoElemento.find_elements(By.TAG_NAME, "a")[1]
        ActionChains(self.__driver).move_to_element(categoriaElemento).perform()
        caixaElemento = WebDriverWait(self.__driver, self.__tempoEspera * 2).until(
            EC.visibility_of_element_located(
                (By.ID, "nav-flyout-lt:subnav-flyout-index-1")
            )
        )

        for opcaoElemento in caixaElemento.find_elements(By.CLASS_NAME, "nav_a"):
            if opcaoElemento.text.lower() == self.categoria:
                opcaoElemento.click()
                break
            continue
        else:
            raise ValueError("Não existe essa categoria! Tente Novamente.")
        sleep(self.__tempoEspera)
    

if __name__ == "__main__":
    bot = Bot("romance", 10)
    bot.navegarPorCategoria()
    # bot.retornarInicio()
