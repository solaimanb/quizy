class ScoreManager:
    def __init__(self):
        self.score = 0
        self.total_questions = 0
        
    def increase_score(self, points=1):
        self.score += points
        
    def reset(self):
        self.score = 0
        self.total_questions = 0
        
    def get_score(self):
        return self.score
    
    def increment_total_questions(self):
        self.total_questions += 1
        
    def get_total_questions(self):
        return self.total_questions