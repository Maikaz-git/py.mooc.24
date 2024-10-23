# WRITE YOUR SOLUTION HERE:
class ExamResult:
    def __init__(self, name: str, grade1: int, grade2: int, grade3: int):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3

 

    def __str__(self):
        return (f'Name:{self.name}, grade1: {self.grade1}' +
            f', grade2: {self.grade2}, grade3: {self.grade3}')


def best_results(results: list) -> list:
        ## read challenge very cearfuly
        return [max(res.grade1, res.grade2, res.grade3) for res in results]

if __name__=="__main__":
    result1 = ExamResult("Peter",5,3,4)
    result2 = ExamResult("Pippa",3,4,1)
    result3 = ExamResult("Paul",2,1,3)
    results = [result1, result2, result3]
    awns = best_results(results)
    print(awns)