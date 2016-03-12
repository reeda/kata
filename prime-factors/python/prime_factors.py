
class PrimeFactors:
    @staticmethod
    def generate(n):
        primes = []
        candidate = 2
        while (n > 1):
            while (n % candidate == 0):
                primes.append(candidate)
                n = n / candidate
            candidate = candidate + 1
        return primes
