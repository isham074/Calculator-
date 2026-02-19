"""
Safe mathematical expression parser using SymPy
Handles all calculations safely without eval()
"""

import sympy as sp
import math
from sympy.parsing.sympy_parser import (
    parse_expr, 
    standard_transformations, 
    implicit_multiplication_application,
    convert_xor
)
from config import ERROR_MESSAGES

# Configure SymPy transformations for better parsing
transformations = (
    standard_transformations + 
    (implicit_multiplication_application, convert_xor)
)

# Define allowed functions and constants
ALLOWED_FUNCTIONS = {
    'sin': sp.sin,
    'cos': sp.cos,
    'tan': sp.tan,
    'log': sp.log,
    'ln': sp.ln,
    'sqrt': sp.sqrt,
    'factorial': sp.factorial,
    'abs': sp.Abs,
}

ALLOWED_CONSTANTS = {
    'pi': sp.pi,
    'e': sp.E,
}

def safe_evaluate(expression):
    """
    Safely evaluate a mathematical expression using SymPy
    
    Args:
        expression (str): The mathematical expression to evaluate
        
    Returns:
        tuple: (success, result_or_error_message)
    """
    
    if not expression or expression == "0":
        return True, "0"
    
    try:
        # Replace calculator-specific symbols
        expression = expression.replace('×', '*').replace('÷', '/')
        expression = expression.replace('^', '**')
        
        # Handle factorial notation (5! -> factorial(5))
        expression = _handle_factorial(expression)
        
        # Handle percentage
        expression = _handle_percentage(expression)
        
        # Parse the expression safely
        parsed_expr = parse_expr(
            expression,
            transformations=transformations,
            local_dict={**ALLOWED_FUNCTIONS, **ALLOWED_CONSTANTS},
            evaluate=True
        )
        
        # Evaluate the expression
        result = parsed_expr.evalf()
        
        # Format the result
        formatted_result = _format_result(result)
        
        return True, formatted_result
        
    except (sp.SympifyError, TypeError, ValueError, ZeroDivisionError) as e:
        return _handle_error(e)
    except Exception as e:
        return False, ERROR_MESSAGES['calculation_error']

def _handle_factorial(expr):
    """Convert 5! notation to factorial(5)"""
    import re
    pattern = r'(\d+)!'
    return re.sub(pattern, r'factorial(\1)', expr)

def _handle_percentage(expr):
    """Convert percentage operations"""
    # This is a simple implementation - can be enhanced
    return expr.replace('%', '/100')

def _format_result(result):
    """Format the result nicely"""
    try:
        # Convert to float
        float_result = float(result)
        
        # If it's an integer, show as integer
        if float_result.is_integer():
            return str(int(float_result))
        
        # Otherwise, show with up to 10 decimal places
        return f"{float_result:.10f}".rstrip('0').rstrip('.')
    except:
        return str(result)

def _handle_error(error):
    """Handle different types of errors"""
    error_str = str(error).lower()
    
    if 'division by zero' in error_str:
        return False, ERROR_MESSAGES['division_by_zero']
    elif 'invalid syntax' in error_str:
        return False, ERROR_MESSAGES['invalid_syntax']
    elif 'math domain' in error_str:
        return False, ERROR_MESSAGES['math_domain']
    else:
        return False, ERROR_MESSAGES['calculation_error']

def validate_expression(expression):
    """
    Validate if the expression is safe and within limits
    """
    from config import MAX_EXPRESSION_LENGTH
    
    if len(expression) > MAX_EXPRESSION_LENGTH:
        return False, ERROR_MESSAGES['too_long']
    
    # Check for dangerous patterns
    dangerous = ['__', 'exec', 'eval', 'import', 'os', 'sys']
    for pattern in dangerous:
        if pattern in expression.lower():
            return False, ERROR_MESSAGES['invalid_syntax']
    
    return True, None
