from flask import Flask, render_template, request, redirect, url_for  # type: ignore[import]
from supabase import create_client, Client  # type: ignore[import]

app = Flask(__name__)

# Configuración de base de datos de Supabase
SUPABASE_URL = "https://wpcgokuvaesnppswmbnp.supabase.co"
SUPABASE_KEY = "sb_publishable_QZwfFqptKInsC7-S1m5WLA_OHurWqfM"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)



# JURISDICCIÓN: INICIO E INSTITUCIONES

@app.route('/')
def inicio():
    return redirect(url_for('gestionar_instituciones'))

# Pantalla de Instituciones
@app.route('/instituciones', methods=['GET', 'POST'])
def gestionar_instituciones():
    if request.method == 'POST':
        # 1. CAPTURAR DATOS DEL FORMULARIO HTML
        nombre_centro = request.form.get('nombre')
        zona_centro = request.form.get('zona')
        
        try:
            # 2. INSERTAR EN BASE DE DATOS
            supabase.table('centros_salud').insert({
                "nombre": nombre_centro, 
                "zona": zona_centro
            }).execute()
            
            return redirect(url_for('gestionar_instituciones'))
        except Exception as e:
            return f"Error al guardar en base de datos: {str(e)}"

    # SI ES GET: TRAER LOS DATOS DESDE SUPABASE
    try:
        response = supabase.table('centros_salud').select('*').order('id_centros').execute()
        listado_centros = response.data 
    except Exception as e:
        listado_centros = []
        print(f"Error al conectar con Supabase: {e}")
        
    return render_template('instituciones.html', centros=listado_centros)


# JURISDICCIÓN: MAESTRO DE PACIENTES (ABM)

# Vista de Pacientes (Maneja el listado general, la edición y la ficha médica)
@app.route('/pacientes', methods=['GET'])
def gestionar_pacientes():
    id_ver = request.args.get('ver')
    id_editar = request.args.get('editar')
    
    paciente_seleccionado = None
    paciente_editar = None
    historial_turnos = []

    # 1. Trae todos los pacientes de la base de datos para armar la tabla
    try:
        res_pacientes = supabase.table('pacientes').select('*').order('nombre_apellido').execute()
        lista_pacientes = res_pacientes.data
    except Exception as e:
        lista_pacientes = []
        print(f"Error al listar pacientes: {e}")

    # 2. MODO VER FICHA: Si viene '?ver=ID', traemos sus datos y su historial clínico relacional
    if id_ver:
        try:
            res_sel = supabase.table('pacientes').select('*').eq('id_paciente', int(id_ver)).single().execute()
            paciente_seleccionado = res_sel.data
            
            # Traemos sus solicitudes vinculadas con el nombre del efector de origen
            res_turnos = supabase.table('solicitudes_turnos').select(
                'id_solicitud, created_at, especialidad, estado, observaciones, centros_salud(nombre)'
            ).eq('id_paciente', int(id_ver)).execute()
            historial_turnos = res_turnos.data
        except Exception as e:
            print(f"Error al abrir ficha: {e}")

    # 3. MODO EDITAR: Si viene '?editar=ID', cargamos sus datos en el formulario
    if id_editar:
        try:
            res_edit = supabase.table('pacientes').select('*').eq('id_paciente', int(id_editar)).single().execute()
            paciente_editar = res_edit.data
        except Exception as e:
            print(f"Error al cargar edición: {e}")

    return render_template(
        'pacientes.html', 
        lista_pacientes=lista_pacientes, 
        paciente_seleccionado=paciente_seleccionado, 
        paciente_editar=paciente_editar,
        historial_turnos=historial_turnos
    )

# Guardar Paciente (Procesa tanto el INSERT como el UPDATE)
@app.route('/pacientes/guardar', methods=['POST'])
def guardar_paciente():
    id_paciente = request.form.get('id_paciente') # Viene solo si estamos modificando
    
    datos = {
        "nombre_apellido": request.form.get('nombre_apellido'),
        "dni": request.form.get('dni'),
        "fecha_nacimiento": request.form.get('fecha_nacimiento'),
        "telefono": request.form.get('telefono'),
        "nro_hc": request.form.get('nro_hc'),
        "obra_social": request.form.get('obra_social')
    }

    try:
        if id_paciente:
            # Es una MODIFICACIÓN (UPDATE)
            supabase.table('pacientes').update(datos).eq('id_paciente', int(id_paciente)).execute()
        else:
            # Es un ALTA NUEVA (INSERT)
            supabase.table('pacientes').insert(datos).execute()
            
        return redirect(url_for('gestionar_pacientes'))
    except Exception as e:
        return f"Error al guardar paciente: {str(e)}"

# Eliminar Paciente (Maneja las restricciones de integridad relacional)
@app.route('/pacientes/eliminar/<id>', methods=['GET'])
def eliminar_paciente(id):
    try:
        supabase.table('pacientes').delete().eq('id_paciente', int(id)).execute()
        return redirect(url_for('gestionar_pacientes'))
    except Exception as e:
        return "<h3> No se puede eliminar: el paciente posee solicitudes de turnos históricos asociados en el hospital central.</h3><br><a href='/pacientes'>Volver al ABM</a>"

# JURISDICCIÓN: AGENTE SANITARIO (SOLICITUD)

#  Pantalla de Carga de Solicitudes (Trae centros y pacientes para el buscador)
@app.route('/solicitud', methods=['GET'])
def cargar_formulario_solicitud():
    try:
        # Traemos efectores de origen
        res_centros = supabase.table('centros_salud').select('*').order('id_centros').execute()
        centros = res_centros.data
        
        # Traemos lista de pacientes reducida para el autocompletado en JS
        res_pacientes = supabase.table('pacientes').select('id_paciente, nombre_apellido, dni, nro_hc').order('nombre_apellido').execute()
        lista_pacientes = res_pacientes.data
    except Exception as e:
        centros = []
        lista_pacientes = []
        print(f"Error al inicializar formulario: {e}")

    return render_template('solicitud.html', centros=centros, lista_pacientes=lista_pacientes)

# Guardar Solicitud (Lógica de inserción simple o combinada si crea paciente nuevo)
@app.route('/solicitud/guardar', methods=['POST'])
def guardar_solicitud():
    es_nuevo = request.form.get('es_nuevo') == "true"
    
    try:
        # OPCIÓN A: Si el Agente cargó un paciente nuevo, lo insertamos primero
        if es_nuevo:
            datos_paciente = {
                "nombre_apellido": request.form.get('nombre_apellido'),
                "dni": request.form.get('dni'),
                "fecha_nacimiento": request.form.get('fecha_nacimiento'),
                "telefono": request.form.get('telefono'),
                "nro_hc": request.form.get('nro_hc'),
                "obra_social": request.form.get('obra_social')
            }
            # Insertamos y capturamos el ID asignado automáticamente
            res_nuevo_pac = supabase.table('pacientes').insert(datos_paciente).execute()
            id_paciente = res_nuevo_pac.data[0]['id_paciente']
        else:
            # OPCIÓN B: Si ya existía, agarramos el ID que inyectó el buscador predictivo
            id_paciente = int(request.form.get('id_paciente'))

        # Armamos el registro de la solicitud de turno diferido
        datos_solicitud = {
            "id_paciente": id_paciente,
            "id_centros": int(request.form.get('id_centros')),
            "especialidad": request.form.get('especialidad'),
            "diagnostico_motivo": request.form.get('diagnostico_motivo'),
            "estado": "pendiente" # Toda solicitud nueva entra en revisión
        }

        # Insertamos el turno en la base
        supabase.table('solicitudes_turnos').insert(datos_solicitud).execute()
        
        # Redirigimos de vuelta a la pantalla de carga limpia
        return redirect(url_for('cargar_formulario_solicitud'))

    except Exception as e:
        return f"<h3>Error al procesar la solicitud médica: {str(e)}</h3><br><a href='/solicitud'>Volver a intentar</a>"

# JURISDICCIÓN: MONITOR DE SEGUIMIENTO (ESTADO)

# Ver el estado de todas las solicitudes con formato de fecha regional
from datetime import datetime

@app.route('/estado', methods=['GET'])
def ver_estado_solicitudes():
    try:
        res = supabase.table('solicitudes_turnos').select(
            'id_solicitud, created_at, especialidad, diagnostico_motivo, estado, observaciones, '
            'pacientes(nombre_apellido, dni, nro_hc), centros_salud(nombre)'
        ).order('created_at', desc=True).execute()
        
        solicitudes_raw = res.data or []
        
        for s in solicitudes_raw:
            try:
                if s.get('created_at'):
                    fecha_limpia = s['created_at'].split('.')[0].replace('Z', '').replace('+00:00', '')
                    dt = datetime.fromisoformat(fecha_limpia)
                    s['fecha_corta'] = dt.strftime('%d/%m/%Y')
                    s['hora_corta'] = dt.strftime('%H:%M')
                else:
                    s['fecha_corta'] = '--/--/----'
                    s['hora_corta'] = '--:--'
            except Exception:
                s['fecha_corta'] = 'Reciente'
                s['hora_corta'] = '--:--'
                
    except Exception as e:
        solicitudes_raw = []
        print(f"Error en panel de estados: {e}")

    return render_template('estado.html', solicitudes=solicitudes_raw)

# Procesar Aceptación (Asignar Turno con Calendario)
@app.route('/gestion/aceptar', methods=['POST'])
def procesar_aceptacion_turno():
    id_solicitud = request.form.get('id_solicitud')
    fecha_hora_raw = request.form.get('fecha_hora') # Viene en formato 'AAAA-MM-DDTHH:MM'
    
    try:
        # Convertimos la fecha del input a formato regional prolijo
        dt = datetime.strptime(fecha_hora_raw, '%Y-%m-%dT%H:%M')
        fecha_formateada = dt.strftime('%d/%m/%Y a las %H:%M')
        
        supabase.table('solicitudes_turnos').update({
            "estado": "asignado",
            "observaciones": f"Turno otorgado para el día: {fecha_formateada} hs.",
            "fecha_modif": datetime.utcnow().isoformat()
        }).eq('id_solicitud', int(id_solicitud)).execute()
        
        return redirect(url_for('bandeja_gestion_turnos'))
    except Exception as e:
        return f"<h3>❌ Error al agendar cita médica: {str(e)}</h3><br><a href='/gestion'>Volver</a>"

# Procesar Rechazo (Cargar justificación de auditoría)
@app.route('/gestion/rechazar', methods=['POST'])
def procesar_rechazo_turno():
    id_solicitud = request.form.get('id_solicitud')
    motivo = request.form.get('motivo')
    
    try:
        supabase.table('solicitudes_turnos').update({
            "estado": "rechazado",
            "observaciones": f"Rechazado por Auditoría: {motivo}",
            "fecha_modif": datetime.utcnow().isoformat()
        }).eq('id_solicitud', int(id_solicitud)).execute()
        
        return redirect(url_for('bandeja_gestion_turnos'))
    except Exception as e:
        return f"<h3>❌ Error al procesar rechazo técnico: {str(e)}</h3><br><a href='/gestion'>Volver</a>"
    
# JURISDICCIÓN: AUDITORÍA CENTRAL (GESTIÓN)

@app.route('/gestion', methods=['GET'])
def bandeja_gestion_turnos():
    try:
        # 🔥 CORREGIDO: Se cambió 'descending=False' por 'desc=False'
        res = supabase.table('solicitudes_turnos').select(
            'id_solicitud, created_at, especialidad, diagnostico_motivo, estado, observaciones, '
            'pacientes(nombre_apellido, dni, nro_hc), centros_salud(nombre)'
        ).order('id_solicitud', desc=False).execute()
        
        solicitudes_raw = res.data or []
        
        for s in solicitudes_raw:
            if s.get('created_at'):
                fecha_limpia = s['created_at'].split('.')[0].replace('Z', '').replace('+00:00', '')
                dt = datetime.fromisoformat(fecha_limpia)
                s['fecha_corta'] = dt.strftime('%d/%m/%Y')
                s['hora_corta'] = dt.strftime('%H:%M')
            else:
                s['fecha_corta'] = '--/--/----'
                s['hora_corta'] = '--:--'
    except Exception as e:
        solicitudes_raw = []
        print(f"Error en bandeja de auditoría: {e}")

    return render_template('gestion.html', solicitudes=solicitudes_raw)

# ENTORNO DE ARRANQUE (SIEMPRE AL FINAL)

if __name__ == '__main__':
    app.run(debug=True, port=5000)