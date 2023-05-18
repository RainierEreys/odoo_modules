# -*- coding: utf-8 -*-
#IMPORTACION DE LIBRERIA PARA OBTENER LA FECHA DE HOY
from datetime import datetime
import logging
#IMPORTACION DE FUNCION QUE OPERA CON FECHAS (SUMA, RESTA)
from dateutil.relativedelta import relativedelta
from odoo import models,fields,api,_
from odoo.exceptions import UserError, ValidationError





class PartnerHb(models.Model):
    #HERENCIA DEL MODELO QUE ALMACENA LOS CONTACTOS
    _inherit = 'res.partner'

    #CAMPO COMPUTADO QUE CALCULA LA EDAD PARA ALMACENARLA EN EL CAMPO 'EDAD'
    @api.depends('birthday_date')
    #SIEMPRE SE DEFINEN ESTAS FUNCIONES CON SELF
    def onchange_age(self):
        #SE RECORRE ÉL MISMO PARA LLENARSE
        for rp in self:
            #SI HAY UNA FECHA REGISTRADA HACE ESTO
            if rp.birthday_date:
                #VARIABLE QUE GUARDA LA FECHA QUE INGRESO EN EL CAMPO 'FECHA DE CUMPLEAÑIS'
                v1 = rp.birthday_date
                #VARIABLE QUE ALMACENA LA FECHA DE HOY CON DATETIME (HAY QUE IMPORTARLA)
                v2 = datetime.today().date()
                #FUNCION QUE OPERA CON FECHAS [RELATIVEDELTA (HAY QUE IMPORTARLA)]
                result = relativedelta(v2, v1)
                print(result)
                logging.info(result)
                if result.month == 'None':
                    result.month = 0
                
                rp.age = str(result.years) + " Años, " + str(result.months) + " Meses, " + str(result.days) + " Días"
                
            #SI NO CONSIGUE UNA FECHA REGISTRADA HACE ESTO    
            else:
                rp.age = 'Sin fecha de nacimiento'
                
    #INSERCIÓN DE CAMPOS           
    birthday_date = fields.Date(string='Fecha de cumpleaños', track_visibility='onchange')
    sex = fields.Selection([('Masculino', 'Masculino'),('Femenino', 'Femenino'),('ND', 'No Definido')], string="Género", track_visibility='onchange')
    passport = fields.Char(string=u'Pasaporte', default='=000-000', help="Debe contener 8 dígitos", track_visibility='onchange')
    extranjero = fields.Boolean(string='Extranjero', default=True, track_visibility='onchange')
    age = fields.Char('Edad', compute=onchange_age)
    #VALIDACIÓN DE VALOR INTRODUCIDO EN EL CAMPO
    @api.constrains('birthday_date')
    def limitar_fecha(self):
        
        v1 = self.birthday_date
        v2 = datetime.today().date()
        
        if v1 > v2:
            raise ValidationError(_('La fecha de cumpleaños no puede ser después del dia de hoy'))
    
    