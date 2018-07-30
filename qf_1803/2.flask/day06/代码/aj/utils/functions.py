
def get_sqlalchemy_uri(DATABASE):

    return '%s+%s://%s:%s@%s:%s/%s' % (DATABASE['ENGINE'],
                                       DATABASE['DRIVER'],
                                       DATABASE['USER'],
                                       DATABASE['PASSWORD'],
                                       DATABASE['HOST'],
                                       DATABASE['PORT'],
                                       DATABASE['DB']
                                       )
