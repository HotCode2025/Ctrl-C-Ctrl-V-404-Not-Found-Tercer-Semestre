class Conexion:
    _DATABASE = 'test_bd'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MAX_CON = 5
    _pool = None


    #@classmethod
    #def obtenerConexion(cls):
    # if cls._conexion is None:
    # try:
    #       cls._conexion = bd.connect(host=cls._HOST,
    #                                    user=cls._USERNAME,
    #                                    password=cls._PASSWORD,
    #                                     port=cls._DB_PORT,
    #                                     database=cls._DATABASE)
    #         log.debug(f'Conexión Exitosa: {cls._conexion}')
    #          return cls._conexion
    #     except Exception as e:
    #           log.error(f'Ocurrió un error: {e}')
    #          sys.exit()
    #  else:
    #     return cls._conexion

    # @classmethod
    #  def obtenerCursor(cls):
    #   if cls._cursor is None:
    #      try:
    #          cls._cursor = cls.obtenerConexion().cursor()
    #         log.debug(f'Se abrió corectamente el cursor: {cls._cursor}')
    #          return cls._cursor
    #        except Exception as e:
    #            log.error(f'Ocurrió un error: {e}')
    #           sys.exit()
    #   else:
    #       return cls._cursor

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        return conexion

    @classmethod
    def obtenerCursor(cls):
        pass

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,
                                                      cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE)
                log.debug(f'creación del pool exitosa: {cls._pool}')
            except Exception as e:
                log.error(f'Ocurrió un error al obtener el pool: {e}')
                sys.exit()
        else:
            return cls._pool

        if __name__ == '__main__':
            conexion1 = Conexion.obtenerConexion()
            conexion2 = Conexion.obtenerConexion()
            conexion3 = Conexion.obtenerConexion()
            conexion4 = Conexion.obtenerConexion()
            conexion5 = Conexion.obtenerConexion()