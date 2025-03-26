import pytest
from text_analyzer import count_words_and_sentences

@pytest.fixture
def sample_text(tmp_path):
    file = tmp_path / "sample.txt"
    file.write_text("Привіт, світ! Це тестовий файл. Він містить три речення? Так...")
    return str(file)

@pytest.mark.parametrize("text, expected_words, expected_sentences", [
    ("Привіт, світ!", 2, 1),
    ("Це перше речення. А це друге! І ще третє?", 8, 3),
    ("Один... Два... Три...", 3, 3)
])
def test_count_words_and_sentences(tmp_path, text, expected_words, expected_sentences):
    file = tmp_path / "test.txt"
    file.write_text(text)

    words, sentences = count_words_and_sentences(str(file))
    assert words == expected_words
    assert sentences == expected_sentences
