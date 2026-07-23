import logging
from functools import wraps


# One-time logging setup
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)

# Prevent duplicate handlers if the file is run more than once
if not logger.handlers:
    file_handler = logging.FileHandler("./decorator.log", "a")
    logger.addHandler(file_handler)


def logger_decorator(func):
    """Log a decorated function's name, parameters, and return value."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Call the original function and save what it returns
        return_value = func(*args, **kwargs)

        # Display "none" when no arguments were supplied
        positional_parameters = list(args) if args else "none"
        keyword_parameters = kwargs if kwargs else "none"

        # Create one log entry for this function call
        log_message = (
            f"function: {func.__name__}\n"
            f"positional parameters: {positional_parameters}\n"
            f"keyword parameters: {keyword_parameters}\n"
            f"return: {return_value}\n"
        )

        logger.log(logging.INFO, log_message)

        # Return the original function's result
        return return_value

    return wrapper


@logger_decorator
def say_hello():
    """Take no parameters and return nothing."""
    print("Hello, World!")


@logger_decorator
def accept_positional_arguments(*args):
    """Take any number of positional arguments and return True."""
    return True


@logger_decorator
def accept_keyword_arguments(**kwargs):
    """Take any number of keyword arguments and return logger_decorator."""
    return logger_decorator


if __name__ == "__main__":
    say_hello()

    accept_positional_arguments("Python", 42, True)

    accept_keyword_arguments(
        name="Carla",
        course="Python",
        assignment=3,
    )




