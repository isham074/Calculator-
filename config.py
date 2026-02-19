"""
Configuration file for the Calculator Bot
Loads environment variables and bot settings
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Bot configuration
BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    raise ValueError("No BOT_TOKEN found in environment variables!")

# Bot settings
BOT_USERNAME = "CalculatorBot"
BOT_VERSION = "1.0.0"

# Calculator settings
MAX_EXPRESSION_LENGTH = 100  # Maximum characters in expression
DEFAULT_EXPRESSION = "0"      # Default display value

# Message templates
WELCOME_MESSAGE = """
🧮 *Welcome to Calculator Bot!*

I'm your personal calculator bot. You can perform basic and scientific calculations right here in Telegram!

*Commands:*
/calc - Open calculator
/help - Show instructions
/clear - Reset current expression

*Features:*
• Basic operations: +, -, *, /, %, ^
• Scientific functions: sin, cos, tan, log, ln, !
• Constants: π (pi), e
• Parentheses support
• Error handling

Press /calc to start calculating!
"""

HELP_MESSAGE = """
📚 *Calculator Bot Help*

*Basic Operations:*
• Addition: 5 + 3
• Subtraction: 10 - 4
• Multiplication: 6 × 3
• Division: 15 ÷ 3
• Modulo: 10 % 3
• Power: 2 ^ 3 (equals 8)

*Scientific Functions:*
• sin(30), cos(60), tan(45)
• log(100) - base 10 logarithm
• ln(10) - natural logarithm
• 5! - factorial

*Constants:*
• pi = 3.14159...
• e = 2.71828...

*Button Functions:*
• C - Clear last entry
• AC - Clear all (reset)
• ⌫ - Backspace
• = - Calculate result

*Tips:*
• You can type expressions directly
• Use parentheses: (5+3)*2
• The bot remembers your expression
• Use /clear to reset if needed

*Examples:*
• 2+2 = 4
• sin(30) = 0.5
• 5! = 120
• sqrt(25) = 5
• 2^3 = 8
• pi*2 = 6.28318...
"""

ERROR_MESSAGES = {
    'division_by_zero': "❌ Error: Division by zero!",
    'invalid_syntax': "❌ Error: Invalid expression!",
    'math_domain': "❌ Error: Math domain error!",
    'too_long': f"❌ Error: Expression too long! Max {MAX_EXPRESSION_LENGTH} characters",
    'calculation_error': "❌ Error: Could not calculate!",
}
