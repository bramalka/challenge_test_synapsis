class GradeProcessor:
    """Class to process grade values and determine status"""
    
    def convertNumberToGrade(self, score):
        """Convert numeric score to letter grade"""
        # Check if input is not a number
        if not isinstance(score, (int, float)):
            return "Invalid"
        
        # Check range and convert to grade
        if score < 0 or score > 100:
            return "Invalid"
        elif score >= 80:  # 80-100
            return "A"
        elif score >= 65:  # 65-79
            return "B"
        elif score >= 50:  # 50-64
            return "C"
        elif score >= 35:  # 35-49
            return "D"
        else:  # 0-34
            return "E"

    def determineStatus(self, grade):
        """Determine pass/fail status based on grade"""
        if grade in ["A", "B", "C"]:
            return "lulus"
        else:  # D, E, Invalid
            return "tidak lulus"

    def processGradeData(self, data, candidate_name):
        """Process grade data and return formatted result"""
        # Check if data exists and is a dictionary
        if not data or not isinstance(data, dict):
            return {
                "nama": candidate_name,
                "nilai": "Invalid",
                "status": "tidak lulus"
            }
        
        # Check if 'nilai' key exists
        if "nilai" not in data:
            return {
                "nama": candidate_name,
                "nilai": "Invalid",
                "status": "tidak lulus"
            }
        
        # Get the score value
        score = data["nilai"]
        
        # Convert score to grade
        grade = self.convertNumberToGrade(score)
        
        # Determine status
        status = self.determineStatus(grade)
        
        return {
            "nama": candidate_name,
            "nilai": grade,
            "status": status
        }