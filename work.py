import pandas as pd
import xlrd


class Work:

    def __init__(self, file: str, sheet: str, weights, trees):
        try:

            self.data = pd.read_excel(file, sheet, index_col=None)
            self.wpb = weights
            self.tpb = trees
            self.salary = self.data
        except ValueError as err:
            print(err)

    def show(self):
        return self.data

    def single_case(self, *weight):
        try:
            col = self.data.columns[2:]
            for i in range(len(weight)):
                self.worker = self.data[col[i]]
                self.weight_cal = (
                    (weight[i]/1000)*self.wpb)/(self.worker.sum())
                self.final_cal = (self.worker*(int(self.weight_cal)))
                self.salary[col[i]] += int(self.weight_cal)
                self.salary['money'] += self.final_cal

            return self.salary

        except TypeError as err:
            return err
