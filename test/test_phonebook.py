import pytest

from src.phonebook import Phonebook


class TestPhonebook:



    #Validando o sucesso do método add
    def test_add_nome_sucesso(self):
        # SETUP
        phonebook = Phonebook()
        resultado_esperado = "Numero adicionado"

        # CHAMADA
        resultado = phonebook.add("Gildo", "12345678")

        # VALIDAÇÃO
        assert resultado == resultado_esperado

    # Validando a mensagem de nome invalido do método add
    @pytest.mark.parametrize("test_data", ["G#ildo", "Gild@", "G!ildo", "Gildo%", "Gildo$"])
    def test_add_nome_invalido(self, test_data):
        # SETUP
        phonebook = Phonebook()
        resultado_esperado = "Nome invalido"

        # CHAMADA
        resultado = phonebook.add(test_data, "(84)988974488")

        # VALIDAÇÃO
        assert resultado == resultado_esperado

    # Validando a mensagem de numero invalido do método add
    @pytest.mark.parametrize("test_data",["ABCDEFG", "----", None])
    def test_add_numero_invalido(self, test_data):
        # SETUP
        phonebook = Phonebook()
        resultado_esperado = "Numero invalido"

        # CHAMADA
        resultado = phonebook.add("Gildo", test_data)

        # VALIDAÇÃO
        assert resultado == resultado_esperado

    # Validando a mensagem de nome ja cadastrado metodo add
    def test_add_nomes_iguais(self):
        #SETUP
        phonebook = Phonebook()
        phonebook.add("Gildo", "12345678")
        resultado_esperado = "Nome ja cadastrado"

        #CHAMADA
        phonebook.add("Gildo", "12345678")
        resultado = phonebook.add("Gildo", "12345678")

        #VALIDAÇÃO
        assert resultado == resultado_esperado

#Validando o sucesso do método lookup
    def test_lookup_nome_sucesso(self):
        # SETUP
        phonebook = Phonebook()
        phonebook.add("Gildo", "12345678")
        resultado_esperado = "12345678"

        # CHAMADA
        resultado = phonebook.lookup("Gildo")

        # VALIDAÇÃO
        assert resultado == resultado_esperado

# Validando a mensagem de nome invalido do método lookup
    @pytest.mark.parametrize("test_data", ["G#ildo", "Gild@", "G!ildo", "Gildo%", "Gildo$"])
    def test_lookup_nome_invalido(self, test_data):
        # SETUP
        phonebook = Phonebook()
        phonebook.add("Gildo", "12345678")
        resultado_esperado = "Nome invalido"

        # CHAMADA
        resultado = phonebook.lookup(test_data)

        # VALIDAÇÃO
        assert resultado == resultado_esperado

    #Validando o sucesso do método get_names
    def test_get_names_sucesso(self):
        # SETUP
        phonebook = Phonebook()
        phonebook.add("Gildo", "12345678")
        resultado_esperado = ['POLICIA', 'Gildo']

        # CHAMADA
        resultado = phonebook.get_names()

        # VALIDAÇÃO
        assert resultado == resultado_esperado

    #Validando o sucesso do método get_numbers
    def test_get_numbers_sucesso(self):
        # SETUP
        phonebook = Phonebook()
        phonebook.add("Gildo", "1234567")
        resultado_esperado = ['190', '1234567']

        # CHAMADA
        resultado = phonebook.get_numbers()

        # VALIDAÇÃO
        assert resultado == resultado_esperado

    # Validando o sucesso do método clear
    def test_clear_sucesso(self):
        # SETUP
        phonebook = Phonebook()
        phonebook.add("Gildo", "12345678")
        resultado_esperado = "phonebook limpado"

        # CHAMADA
        resultado = phonebook.clear()

        # VALIDAÇÃO
        assert resultado == resultado_esperado

    # Validando o sucesso do método search
    def test_seach_sucesso(self):
        # SETUP
        phonebook = Phonebook()
        phonebook.add("Gildo", "12345678")
        resultado_esperado = [{'12345678', 'Gildo'}]

        # CHAMADA
        resultado = phonebook.search("Gildo")

        # VALIDAÇÃO
        assert resultado == resultado_esperado

    # Validando o sucesso do método sorted
    def test_sorted_sucesso(self):
        # SETUP
        phonebook = Phonebook()
        phonebook.add("Bruno", "12345678")
        phonebook.add("Alexandre", "1234567")
        phonebook.add("Claudio", "123456789")
        resultado_esperado = ['Alexandre', 'Bruno', 'Claudio','POLICIA']

        # CHAMADA
        resultado = phonebook.get_phonebook_sorted()

        # VALIDAÇÃO
        assert resultado == resultado_esperado


    # Validando o sucesso do método reverse
    def test_reverse_sucesso(self):
        # SETUP
        phonebook = Phonebook()
        phonebook.add("Bruno", "12345678")
        phonebook.add("Alexandre", "1234567")
        phonebook.add("Claudio", "123456789")
        resultado_esperado = ['POLICIA', 'Claudio', 'Bruno', 'Alexandre']

        # CHAMADA
        resultado = phonebook.get_phonebook_reverse()

        # VALIDAÇÃO
        assert resultado == resultado_esperado


    def test_delete_sucesso(self):
        # SETUP
        phonebook = Phonebook()
        phonebook.add("Gildo", "12345678")
        resultado_esperado = "Numero deletado"


        # CHAMADA
        resultado = phonebook.delete("Gildo")

        # VALIDAÇÃO
        assert resultado == resultado_esperado


