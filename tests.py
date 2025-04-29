from main import BooksCollector
import  pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_book_genre_dictionary_true(self):
        dictionary = BooksCollector()
        assert dictionary.books_genre == {}

    def test_favorites_list_true(self):
        list = BooksCollector()
        assert list.favorites == []

    def test_genre_list_true(self):
        genre_list = BooksCollector()
        assert genre_list.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_genre_age_rating_list_true(self):
        genre_age_rating_list = BooksCollector()
        assert genre_age_rating_list.genre_age_rating == ['Ужасы', 'Детективы']

    def test_add_new_book_duplicate(self):
        duplicate = BooksCollector()
        duplicate.add_new_book('Зов Ктулху')
        duplicate.add_new_book('Зов Ктулху')
        assert len(duplicate.books_genre) == 1

    def test_set_book_genre_true(self):
        new_genre = BooksCollector()
        new_genre.add_new_book('Зов Ктулху')
        new_genre.set_book_genre('Зов Ктулху', 'Ужасы')
        assert new_genre.get_books_genre()['Зов Ктулху'] == 'Ужасы'

    def test_set_book_genre_false(self):
        unknown_boom = BooksCollector()
        unknown_boom.set_book_genre('Сёгун', 'Детективы')
        assert unknown_boom.get_book_genre('Сёгун') is None

    def test_get_book_genre_true(self):
        genre_name = BooksCollector()
        genre_name.add_new_book('Зов Ктулху')
        genre_name.set_book_genre('Зов Ктулху', 'Ужасы')
        assert genre_name.get_book_genre('Зов Ктулху') == 'Ужасы'

    def test_get_books_with_specific_genre_true(self):
        specific_genre = BooksCollector()
        specific_genre.add_new_book('Властелин колец')
        specific_genre.set_book_genre('Властелин колец', 'Фантастика')
        result = specific_genre.get_books_with_specific_genre('Фантастика')
        assert len(result) == 1

    def test_get_books_for_children_true(self):
        children_book = BooksCollector()
        children_book.add_new_book('Карлсон')
        children_book.set_book_genre('Карлсон', 'Мультфильмы')
        adult_book = BooksCollector()
        adult_book.add_new_book('Оно')
        adult_book.set_book_genre('Оно', 'Ужасы')
        children_book = children_book.get_books_for_children()
        assert children_book != adult_book

    def test_add_book_in_faivorites_true(self):
        faivorites_book = BooksCollector()
        faivorites_book.add_new_book('Граф Монте-Кристо')
        faivorites_book.add_book_in_favorites('Граф Монте-Кристо')
        assert 'Граф Монте-Кристо' in faivorites_book.favorites

    def test_add_book_in_faivorites_duplicate_not_add(self):
        duplicate_faivor_bool = BooksCollector()
        duplicate_faivor_bool.add_new_book('Граф Монте-Кристо')
        duplicate_faivor_bool.add_book_in_favorites('Граф Монте-Кристо')
        duplicate_faivor_bool.add_book_in_favorites('Граф Монте-Кристо')
        assert duplicate_faivor_bool.favorites.count('Граф Монте-Кристо') == 1

    def test_delete_book_from_favorites_true(self):
        delete_book = BooksCollector()
        delete_book.add_new_book('Ведьмак')
        delete_book.add_book_in_favorites('Ведьмак')
        delete_book.delete_book_from_favorites('Ведьмак')
        assert 'Ведьмак' not in delete_book.favorites

    def test_get_list_of_favorites_books_true(self):
        list_of_favorites = BooksCollector()
        list_of_favorites.add_new_book('Мастер и Маргарита')
        list_of_favorites.add_book_in_favorites('Мастер и Маргарита')
        assert list_of_favorites.get_list_of_favorites_books() == list_of_favorites.favorites




