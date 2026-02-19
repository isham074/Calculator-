"""
Calculator session management
Handles user sessions and expression building
"""

from config import DEFAULT_EXPRESSION

class CalculatorSession:
    """
    Manages a user's calculator session
    Stores current expression in memory (RAM only)
    """
    
    def __init__(self, user_id):
        self.user_id = user_id
        self.expression = DEFAULT_EXPRESSION
        self.last_result = None
    
    def add_to_expression(self, value):
        """Add a value to the current expression"""
        if self.expression == "0" and value not in ['+', '-', '*', '/', '(', ')']:
            self.expression = value
        else:
            self.expression += value
    
    def clear_entry(self):
        """Clear the last entry (C button)"""
        # Simple implementation - removes last character
        if len(self.expression) > 1:
            self.expression = self.expression[:-1]
        else:
            self.expression = "0"
    
    def clear_all(self):
        """Clear everything (AC button)"""
        self.expression = "0"
        self.last_result = None
    
    def backspace(self):
        """Remove last character"""
        if len(self.expression) > 1:
            self.expression = self.expression[:-1]
        else:
            self.expression = "0"
    
    def set_result(self, result):
        """Set the result of a calculation"""
        self.expression = result
        self.last_result = result
    
    def get_display_text(self):
        """Get the text to display"""
        return f"`{self.expression}`"
    
    def handle_function(self, func_name):
        """Handle scientific function buttons"""
        if func_name == 'sin':
            self.expression += "sin("
        elif func_name == 'cos':
            self.expression += "cos("
        elif func_name == 'tan':
            self.expression += "tan("
        elif func_name == 'log':
            self.expression += "log("
        elif func_name == 'ln':
            self.expression += "ln("
        elif func_name == 'sqrt':
            self.expression += "sqrt("
        elif func_name == 'fact':
            self.expression += "!"
    
    def handle_constant(self, const_name):
        """Handle constant buttons"""
        if const_name == 'pi':
            self.expression += "pi"
        elif const_name == 'e':
            self.expression += "e"
    
    def handle_operator(self, op_name):
        """Handle operator buttons"""
        operators = {
            'add': '+',
            'sub': '-',
            'mul': '×',
            'div': '÷',
            'mod': '%',
            'pow': '^'
        }
        if op_name in operators:
            self.expression += operators[op_name]

# Global dictionary to store user sessions (RAM only)
# This is cleared when the bot restarts
user_sessions = {}

def get_user_session(user_id):
    """
    Get or create a calculator session for a user
    """
    if user_id not in user_sessions:
        user_sessions[user_id] = CalculatorSession(user_id)
    return user_sessions[user_id]

def clear_user_session(user_id):
    """
    Clear a user's session
    """
    if user_id in user_sessions:
        del user_sessions[user_id]
