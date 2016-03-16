
class UniqueElement:
    @staticmethod
    def find(input):
        count_map = {}
        for n in input:
            if not n in count_map:
                count_map[n] = 1
            else:
                count_map[n] += 1
        for key,value in count_map.iteritems():
            if value == 1:
                return key
        return -1
