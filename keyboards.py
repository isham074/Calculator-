"""
Keyboard layouts for the Calculator Bot
Contains all inline keyboard definitions
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def get_calculator_keyboard():
    """
    Creates the main calculator keyboard layout
    Returns an InlineKeyboardMarkup object
    """
    
    # Button layout - 4 columns
    keyboard = [
        # Row 1: Scientific functions
        [
            InlineKeyboardButton("sin", callback_data="func_sin"),
            InlineKeyboardButton("cos", callback_data="func_cos"),
            InlineKeyboardButton("tan", callback_data="func_tan"),
            InlineKeyboardButton("log", callback_data="func_log"),
        ],
        # Row 2: More functions
        [
            InlineKeyboardButton("ln", callback_data="func_ln"),
            InlineKeyboardButton("√", callback_data="func_sqrt"),
            InlineKeyboardButton("!", callback_data="func_fact"),
            InlineKeyboardButton("^", callback_data="op_pow"),
        ],
        # Row 3: Constants
        [
            InlineKeyboardButton("π", callback_data="const_pi"),
            InlineKeyboardButton("e", callback_data="const_e"),
            InlineKeyboardButton("(", callback_data="paren_open"),
            InlineKeyboardButton(")", callback_data="paren_close"),
        ],
        # Row 4: Numbers 7-9 and operators
        [
            InlineKeyboardButton("7", callback_data="num_7"),
            InlineKeyboardButton("8", callback_data="num_8"),
            InlineKeyboardButton("9", callback_data="num_9"),
            InlineKeyboardButton("÷", callback_data="op_div"),
        ],
        # Row 5: Numbers 4-6 and operators
        [
            InlineKeyboardButton("4", callback_data="num_4"),
            InlineKeyboardButton("5", callback_data="num_5"),
            InlineKeyboardButton("6", callback_data="num_6"),
            InlineKeyboardButton("×", callback_data="op_mul"),
        ],
        # Row 6: Numbers 1-3 and operators
        [
            InlineKeyboardButton("1", callback_data="num_1"),
            InlineKeyboardButton("2", callback_data="num_2"),
            InlineKeyboardButton("3", callback_data="num_3"),
            InlineKeyboardButton("-", callback_data="op_sub"),
        ],
        # Row 7: Special buttons
        [
            InlineKeyboardButton("0", callback_data="num_0"),
            InlineKeyboardButton(".", callback_data="num_dot"),
            InlineKeyboardButton("%", callback_data="op_mod"),
            InlineKeyboardButton("+", callback_data="op_add"),
        ],
        # Row 8: Clear buttons
        [
            InlineKeyboardButton("C", callback_data="clear_entry"),
            InlineKeyboardButton("AC", callback_data="clear_all"),
            InlineKeyboardButton("⌫", callback_data="backspace"),
            InlineKeyboardButton("=", callback_data="calculate"),
        ],
        # Row 9: Navigation
        [
            InlineKeyboardButton("🏠 Home", callback_data="home"),
            InlineKeyboardButton("❓ Help", callback_data="help"),
        ],
    ]
    
    return InlineKeyboardMarkup(keyboard)

def get_home_keyboard():
    """
    Creates the home screen keyboard
    """
    keyboard = [
        [
            InlineKeyboardButton("🧮 Open Calculator", callback_data="open_calc"),
            InlineKeyboardButton("❓ Help", callback_data="help"),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
