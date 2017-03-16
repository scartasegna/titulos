### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
#Tabla de titulos auditados (por dia)
########################################
db.define_table('t_titulos_auditados',
    Field('f_fecha', type='date',
          label=T('Fecha'), default=request.now, writable=False),
    Field('f_aceptados', type='integer',
          label=T('Aceptados'),default=0),
    Field('f_rechazados', type='integer',
          label=T('Rechazados'),default=0),
    Field('f_cargo', type='reference auth_user',
          label=T('Cargo'),default=auth.user_id,writable=False),
    auth.signature,
    format='%(f_fecha)s',
    migrate=settings.migrate)

db.define_table('t_titulos_auditados_archive',db.t_titulos_auditados,Field('current_record','reference t_titulos_auditados',readable=False,writable=False))

########################################
#Tabla de egresados (por anio)
########################################
db.define_table('t_egresados',
    Field('f_anio', type='integer',
          label=T('Año')),
    Field('f_egresados', type='integer',
          label=T('egresados')),
    Field('f_cargo', type='reference auth_user',
          label=T('Cargo'),default=auth.user_id,writable=False),
    auth.signature,
    format='%(f_anio)s',
    migrate=settings.migrate)

db.define_table('t_egresados_archive',db.t_egresados,Field('current_record','reference t_egresados',readable=False,writable=False))


########################################
#Tabla de titulos impresos por region
########################################
db.define_table('t_titulos_impresos',
    Field('f_fecha', type='date',
          label=T('Fecha'), default=request.now, writable=False),
    Field('f_region1', type='integer',
          label=T('Region 1'),default=0),
    Field('f_region2', type='integer',
          label=T('Region 2'),default=0),
    Field('f_region3', type='integer',
          label=T('Region 3'),default=0),
    Field('f_region4', type='integer',
          label=T('Region 4'),default=0),
    Field('f_region5', type='integer',
          label=T('Region 5'),default=0),
    Field('f_region6', type='integer',
          label=T('Region 6'),default=0),
    Field('f_region7', type='integer',
          label=T('Region 7'),default=0),
    Field('f_region8', type='integer',
          label=T('Region 8'),default=0),
    Field('f_region9', type='integer',
          label=T('Region 9'),default=0),
    Field('f_region10', type='integer',
          label=T('Region 10'),default=0),
    Field('f_region11', type='integer',
          label=T('Region 11'),default=0),
    Field('f_region12', type='integer',
          label=T('Region 12'),default=0),
    Field('f_region13', type='integer',
          label=T('Region 13'),default=0),
    Field('f_region14', type='integer',
          label=T('Region 14'),default=0),
    Field('f_region15', type='integer',
          label=T('Region 15'),default=0),
    Field('f_region16', type='integer',
          label=T('Region 16'),default=0),
    Field('f_region17', type='integer',
          label=T('Region 17'),default=0),
    Field('f_region18', type='integer',
          label=T('Region 18'),default=0),
    Field('f_region19', type='integer',
          label=T('Region 19'),default=0),
    Field('f_region20', type='integer',
          label=T('Region 20'),default=0),
    Field('f_region21', type='integer',
          label=T('Region 21'),default=0),
    Field('f_region22', type='integer',
          label=T('Region 22'),default=0),
    Field('f_region23', type='integer',
          label=T('Region 23'),default=0),
    Field('f_region24', type='integer',
          label=T('Region 24'),default=0),
    Field('f_region25', type='integer',
          label=T('Region 25'),default=0),
    Field('f_cargo', type='reference auth_user',
          label=T('Cargo'),default=auth.user_id,writable=False),
    auth.signature,
    format='%(f_fecha)s',
    migrate=settings.migrate)

db.define_table('t_titulos_impresos_archive',db.t_titulos_impresos,Field('current_record','reference t_titulos_impresos',readable=False,writable=False))

########################################
#Tabla de resumen de impresos.
# Esta tabla se carga mediante un SP, es calculada a dia vencido.
# El migrate = false es porque es inventada para que web2py la pueda ver
########################################
db.define_table('t_resumen_impresos',
    Field('f_fecha', type='date',
          label=T('Fecha'),default=request.now, writable=False),
    Field('f_impresos', type='integer',
          label=T('Impresos')),
    Field('f_sum_region1', type='integer',
          label=T('Region 1')),
    Field('f_sum_region2', type='integer',
          label=T('Region 2')),
    Field('f_sum_region3', type='integer',
          label=T('Region 3')),
    Field('f_sum_region4', type='integer',
          label=T('Region 4')),
    Field('f_sum_region5', type='integer',
          label=T('Region 5')),
    Field('f_sum_region6', type='integer',
          label=T('Region 6')),
    Field('f_sum_region7', type='integer',
          label=T('Region 7')),
    Field('f_sum_region8', type='integer',
          label=T('Region 8')),
    Field('f_sum_region9', type='integer',
          label=T('Region 9')),
    Field('f_sum_region10', type='integer',
          label=T('Region 10')),
    Field('f_sum_region11', type='integer',
          label=T('Region 11')),
    Field('f_sum_region12', type='integer',
          label=T('Region 12')),
    Field('f_sum_region13', type='integer',
          label=T('Region 13')),
    Field('f_sum_region14', type='integer',
          label=T('Region 14')),
    Field('f_sum_region15', type='integer',
          label=T('Region 15')),
    Field('f_sum_region16', type='integer',
          label=T('Region 16')),
    Field('f_sum_region17', type='integer',
          label=T('Region 17')),
    Field('f_sum_region18', type='integer',
          label=T('Region 18')),
    Field('f_sum_region19', type='integer',
          label=T('Region 19')),
    Field('f_sum_region20', type='integer',
          label=T('Region 20')),
    Field('f_sum_region21', type='integer',
          label=T('Region 21')),
    Field('f_sum_region22', type='integer',
          label=T('Region 22')),
    Field('f_sum_region23', type='integer',
          label=T('Region 23')),
    Field('f_sum_region24', type='integer',
          label=T('Region 24')),
    Field('f_sum_region25', type='integer',
          label=T('Region 25')),
               migrate=False)

########################################
#Tabla de resumen de Auditados.
# Esta tabla se carga mediante un SP, es calculada a dia vencido.
# El migrate = false es porque es inventada para que web2py la pueda ver
########################################

db.define_table('t_resumen_auditados',
    Field('f_fecha', type='date',
          label=T('Fecha'),default=request.now, writable=False),
    Field('f_auditados', type='integer',
          label=T('Auditados')),
    Field('f_aceptados', type='integer',
          label=T('Aceptados')),
    Field('f_rechazados', type='integer',
          label=T('Rechazados')),
                migrate=False)
