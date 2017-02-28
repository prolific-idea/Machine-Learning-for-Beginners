class Chromosome:    
    def __init__(self, genes):
        self.genes = genes
        self.move_index = 0
        
    def get_move(self):
        if self.genes.size > self.move_index:
            gene = self.genes[self.move_index]
            self.move_index += 1
            return gene
        else:
            return False
