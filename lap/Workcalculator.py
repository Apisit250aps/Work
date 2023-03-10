import pandas as pd
import xlrd

class Workcalculator:
    def __init__(self, file: str, sheet: str, weights : int, trees : int):
        self.sheet = sheet.capitalize()
        self._WPB = weights
        self._TPB = trees
        self.sum_of_weight = 0
        self.sum_of_tree = 0
        

        try:
            self.db = pd.read_excel(
                f'{file}', sheet_name=self.sheet, index_col='Name')
        except Exception as err:
            return err
        
        self.salary = self.db['money']

    def Normal_case(self, weight: int):
        try:
            self.col = self.data
            for i in range(len(weight)):
                self.round = f'{self.sheet}{i+1}'
                self.worker = self.db[self.round]
                self.weight_cal = (
                    (weight[i]/1000)*self._WPB)/(self.worker.sum())
                print(self.weight_cal)
                self.final_cal = (self.worker*(int(self.weight_cal)))
                self.salary += self.final_cal
    
            return self.salary
        except:
            return
        
   
 
        
    