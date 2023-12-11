import os
import string
from typing import Iterable


class TextLoader:
    def init(self, folder_path):
        self.folder_path = folder_path
        self.text_files = [file for file in os.listdir(folder_path)]
        self.index = 0

    def len(self):
        return len(self.text_files)

    def getitem(self, index):
        if isinstance(index, int):
            if index < 0 or index >= len(self):
                raise IndexError("Index out of range")
            filename = os.path.join(self.folder_path, self.text_files[index])
            with open(filename, 'r', encoding='utf-8') as file:
                text = file.read()
            return self._preprocess_text(text)
        elif isinstance(index, Iterable):
            return [self.getitem(i) for i in index]
        else:
            raise TypeError("Index must be an integer or iterable of ones")

    def _preprocess_text(self, text):
        text = text.lower()
        translator = str.maketrans('', '', string.punctuation)
        text = text.translate(translator)
        return text

    def iter(self):
        self.index = 0
        return self

    def next(self):
        if self.index < len(self):
            text = self.getitem(self.index)
            self.index += 1
            return text
        else:
            raise StopIteration


data_folder = "./8/sample/"
text_loader = TextLoader(data_folder)

print("Возвращаю количество текстов в папке:", len(text_loader))

for text in text_loader:
    print(text)
