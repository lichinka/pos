import locale


def format_float (value):
    """
    Returns the received formated in the current locale.
    """
    try:
        value = '%.2f' % float(value)
        value = value.replace ('.', locale.localeconv( )['decimal_point'])
        logging.debug ("value is %s" % value)
    except (TypeError, ValueError):
        pass

    finally:
        return value

