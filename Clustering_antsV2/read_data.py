from data import Data

class Read_data:
    def __init__(self, name_data):
        self.name_data = name_data
        self.data = []

    def read(self):
        with open(self.name_data, 'r') as archive:
            lines = archive.readlines()

            first_line = lines[0].strip()
            first_line = first_line.split(', ')

            self.n = int(first_line[0].split('=')[1])
            self.k = int(first_line[1].split('=')[1])
            self.d = int(first_line[2].split('=')[1])

            i = 0
            for line in lines:
                line_plit = line.strip().split('\t')
                if len(line_plit) == 3:
                    name = line_plit[2]
                    x = float(line_plit[0])
                    y = float(line_plit[1])
                    self.data.append(Data(name, x, y))
    
    def creat_matrix(self):
        
