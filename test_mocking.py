import pytest

import for_mocking

"""
1. Реализовать программу на Python. Программа может содержать любое количество методов и классов (>0), но обязательно должна иметь класс main.
2. Имитировать:
    a. Метод созданного класса (метод не должен являться генератором).
    b. Параметр внутри метода класса.
    c. Класс.
3. Спровоцировать имитированную ошибку.
4. Применить декоратор @patch на любом имитируемом объекте (классе, методе и т.д.). 
Выбирается студентом самостоятельно.
5. Имитировать объект-генератор (см.пр. 26.6.3.3.[1]).
"""


def test_format_status(mocker):
    main_object = for_mocking.Main('Not OK')
    mocker.patch.object(main_object, 'format_status',
                        return_value=['Status: OK;'])
    assert main_object.format_status() == ['Status: OK;']
    assert main_object.status == 'Not OK'


def test_property_mocking(mocker):
    main_object = for_mocking.Main('Not OK')
    main_object = mocker.patch.object(main_object, 'format_status')
    main_object.format_status(mocker.ANY)
    main_object.format_status.assert_called_once_with(mocker.ANY)


def test_class_mocking(mocker):
    mocker.patch.object(for_mocking, 'Main')
    for_mocking.Main.format_status.return_value = 123
    mocked_instance = for_mocking.Main('wow')
    mocked_instance.format_status()
    mocked_instance.format_status.assert_called_once_with()  # pylint: disable=no-member


@pytest.mark.xfail(raises=Exception)
def test_generator(mocker):
    main_object = for_mocking.Main('Not OK')
    main_object = mocker.patch.object(main_object, 'format_status')
    main_object.format_status(123)


def test_letter_generator(mocker):
    main_object = for_mocking.Main('Not OK')
    mocker.patch.object(main_object, 'letter_generator',
                        return_value=iter('Status: OK;'))
    assert list(main_object.letter_generator()) == list('Status: OK;')
