
class FizzBuzz:
    @staticmethod
    def generate(n):
        values = []
        for i in range(1,n+1):
            to_append = ""
            if i % 3 == 0:
                to_append += "Fizz"
            if i % 5 == 0:
                to_append += "Buzz"
            values.append(to_append or str(i))
        return '\n'.join(values)
            
