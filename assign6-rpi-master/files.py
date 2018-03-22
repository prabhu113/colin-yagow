# Donovan Dobler

"""
Object to load media files into the game
"""
import csv

class File():
    def __init__(self,file_name):
        self._file_list=[]
        self._file_reader= open(file_name, "rt", encoding='UTF-8')
        self._read = csv.reader(self._file_reader)
        for row in self._read:
            self._file_list.append(row)

    def getData(self,row_number,column_number):
        return self._file_list[row_number][column_number]

    def getAll(self):
        return self._file_list
    def hashList(self):
        self.multi_list = self.getAll()
        self.dictionary = {}
        counter = 0
        key = ""
        for single_list in self.multi_list:
            for item in single_list:
                if counter % 2 == 0:
                    key = item
                    counter += 1
                else:
                    self.dictionary.update({key:item})
                    counter += 1
        return self.dictionary

