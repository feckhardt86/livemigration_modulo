def format_date(data):
    """
    Espera receber: Ex. '23/10/2018 10:20'
    Precisa retornar: YYYY-MM-DD HH:MM
    """
    if not data:
        return None

    time = data.split(' ')[1]
    date = data.split(' ')[0]
    res = date.split('/')[2] + '-' + \
          date.split('/')[1] + '-' + \
          date.split('/')[0] + ' ' + \
          time
    return res