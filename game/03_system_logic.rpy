# Copyright 2026 Alenia Studios. All rights reserved.
# This code is the property of Alenia Studios and may not be used without permission.
# Developed for the project: Gatekeeper


init python:
    def get_time():
        return datetime.datetime.now().strftime("%H:%M")

    def update_trace(amount):
        store.trace_level += amount
        if store.trace_level >= 100:
            renpy.jump("game_over_traced")

    def window_dragged(drags, drop):
        drag = drags[0]
        if drag.drag_name == "browser_window":
            store.browser_x = drag.x
            store.browser_y = drag.y
        elif drag.drag_name == "cmd_window":
            store.cmd_x = drag.x
            store.cmd_y = drag.y
        elif drag.drag_name == "mail_window": 
            store.mail_x = drag.x
            store.mail_y = drag.y
        renpy.restart_interaction()

    def set_focus(window_name):
        store.active_window = window_name
        renpy.restart_interaction()

    def process_cmd():
        command = store.cmd_input.strip().upper()
        renpy.play("audio/typing.wav")
        store.cmd_history_text += _("\n\n> ") + command
        store.cmd_input = "" 
        
        # ==========================================
        # LISTA DE COMANDOS
        # ==========================================

        # --- COMANDO DE AYUDA ---
        if command == "HELP":
            store.cmd_history_text += _("\n[[COMANDOS DISPONIBLES]:\n- SCAN_NETWORK: Escaneo de nodos.\n- DIR / LS: Listar archivos descargados.\n- DECRYPT [[ARCHIVO] [[CLAVE]: Desencriptar archivos.\n- GATE_OPEN: Ejecutar protocolo de acceso.")
        
        # --- COMANDO DE INVENTARIO (DIR / LS) ---
        elif command == "DIR" or command == "LS":
            store.cmd_history_text += _("\n[[DIRECTORIO LOCAL - C:\\Users\\Admin\\Downloads]")
            
            # Verificación de seguridad
            if not hasattr(store, "downloaded_files"): 
                store.downloaded_files = []
            
            if not store.downloaded_files:
                store.cmd_history_text += _("\n[[VACÍO]")
            else:
                for f in store.downloaded_files:
                    if f == "subject_001": 
                        name = _("SUBJECT_001.DATA") 
                    elif f == "arlene_log": 
                        name = _("ARLENE_LOG.ENC")
                    else: 
                        name = f.upper()
                    
                    store.cmd_history_text += _("\n<FILE> ") + name

        # --- COMANDO DE DESENCRIPTACIÓN (DECRYPT) ---
        elif command.startswith(_("DECRYPT")):
            parts = command.split(" ")
            if len(parts) < 3:
                renpy.play("audio/error_buzz.mp3.wav")
                store.cmd_history_text += _("\n[[ERROR]: Sintaxis incorrecta. Uso: DECRYPT [[ARCHIVO] [[CLAVE]")
            
            elif "SUBJECT" in parts[1]:
                store.cmd_history_text += _("\n[[SYSTEM]: Este archivo ya fue procesado automáticamente.")
                
            elif "ARLENE" in parts[1]:
                if not hasattr(store, "downloaded_files") or "arlene_log" not in store.downloaded_files:
                    renpy.play("audio/error_buzz.mp3.wav")
                    store.cmd_history_text += _("\n[[ERROR]: Archivo no encontrado. Descárgalo primero del nodo Cradle.")
                
                elif parts[2] == "NUTRIENTES" or parts[2] == "NUTRIENT": 
                    renpy.play("audio/success_chime.wav")
                    store.cmd_history_text += _("\n[[SUCCESS]: Desencriptando...\n[[LOG]: 'Sujeto 44 escapó al Sótano 4... Código de puerta: VIGILANT'.")
                    renpy.notify(_(">> CLAVE FINAL OBTENIDA <<"))
                else:
                    renpy.play("audio/error_buzz.mp3.wav")
                    store.cmd_history_text += _("\n[[ERROR]: Clave incorrecta. Acceso denegado.")
                    update_trace(10) 
            else:
                 store.cmd_history_text += _("\n[[ERROR]: Archivo no reconocido.")
        
        # --- COMANDO: PURGE (ANTIVIRUS) ---
        elif command == "PURGE":
            if not store.virus_installed:
                store.cmd_history_text += _("\n> SISTEMA ESTABLE. NO SE REQUIERE PURGA.")
            else:
                store.virus_popups = []
                store.antivirus_timer = 20
                renpy.play("audio/success_chime.wav")
                store.cmd_history_text += _("\n> [[OK] VACIADO DE RAM COMPLETADO.\n> PROTECCIÓN ACTIVA: 20 SEGUNDOS.")

        # --- COMANDO: GATE_OPEN ---
        elif command == "GATE_OPEN":
            store.cmd_history_text += _("\n[[SYSTEM]: PROTOCOL INITIATED.\n[[SYSTEM]: ACCESS GRANTED.\n\n[[SECURITY]: ENTER PROJECT PASSWORD:")
        
        # --- COMANDO: SCAN_NETWORK ---
        elif command == "SCAN_NETWORK":
            renpy.play("audio/typing.wav")
            store.cmd_history_text += _("\n[[ESCANEANDO...]\n[[ENCONTRADO]: Nodo_Privado_Arke...\n[[ESTADO]: ENCRIPTADO")
            update_trace(15)
            
        # --- COMANDO: LAZARUS ---
        elif command == "LAZARUS" or command == "LAZARO":
            renpy.play("audio/success_chime.wav")
            store.cmd_history_text += _("\n[[SYSTEM]: PASSWORD ACCEPTED.\n[[SYSTEM]: UPLOADING...")
            renpy.jump("endgame_sequence")
        
        # --- COMANDO: ALENIA (EASTER EGG) ---
        elif command == "ALENIA":
            store.cmd_history_text += _("\n> HOLA CREADOR. GRACIAS POR JUGAR MI JUEGO.\n> ESPERO QUE TE HAYA GUSTADO EL JUEGO Y EL GUIÓN.\n> SALUDOS DESDE MEXICO. NUEVO JUEGO PRONTO. SIGUIENDO LA HISTORIA DE ECHO CORP.")

        # --- ERROR: COMANDO NO RECONOCIDO (ELSE FINAL) ---
        else:
            store.cmd_history_text += _("\nERROR: COMANDO O SINTAXIS DESCONOCIDA. ESCRIBE 'HELP'.")
            renpy.play("audio/error_buzz.mp3.wav")
            
        renpy.restart_interaction()

    # --- Pega aquí trigger_delayed_email, download_file, check_incoming_mail, add_email ---
    def trigger_delayed_email(mission_code, delay=10.0):
        store.pending_mission_code = mission_code
        store.next_mail_time = time.time() + delay
        store.waiting_for_mail = True
    
    def download_file(file_id):
        if not hasattr(store, "downloaded_files"): store.downloaded_files = []

        if file_id == "subject_001":
            if file_id not in store.downloaded_files:
                store.downloaded_files.append(file_id)
            
            # CAMBIO: Ahora activa la misión 4 (Black Moth)
            if store.current_mission == 3:
                trigger_delayed_email("mission_4", delay=5.0) # <--- CAMBIO AQUÍ
                store.current_mission = 4
                renpy.notify(_("ALARMA SILENCIOSA ACTIVADA."))
            
            renpy.notify(_("Descarga completada."))

        elif file_id == "arlene_log":
             if file_id not in store.downloaded_files:
                store.downloaded_files.append(file_id)
                renpy.notify(_("Log encriptado obtenido."))
             else:
                renpy.notify(_("Archivo ya existe."))

        renpy.restart_interaction()
    def check_incoming_mail():
        if store.waiting_for_mail and time.time() >= store.next_mail_time:
            store.waiting_for_mail = False
            add_email(store.pending_mission_code)
            renpy.play("audio/mail.mp3")  # 🔔 sonido de correo
            renpy.notify(_("NUEVO CORREO RECIBIDO"))
            renpy.restart_interaction()

    def add_email(mission_code):
        # MISION 1: CEO
        if mission_code == "welcome":
            e = Email("Handler_X", _("CONTRATO: Echo Corp"), 
                _("Agente, necesitamos el nombre del CEO de Echo Corp.\nBusca noticias financieras y RESPONDE."),
                mission_id=1, correct_answer=1,
                options=[_("CEO: Elon Musk"), _("CEO: Julius Vax"), _("CEO: Bill Gates")])
            inbox.insert(0, e)

        # MISION 2: ARCHIVO
        elif mission_code == "mission_2":
            e = Email("Handler_X", _("RE: Objetivo Identificado"), 
                _("Bien. Vax está ocultando algo.\nBusca en los foros de conspiración el nombre del archivo filtrado."),
                mission_id=2, correct_answer=0,
                options=[_("Archivo: 'Subject_001.data'"), _("Archivo: 'Half Life 3'"), _("Nada relevante")])
            inbox.insert(0, e)

        # MISION 3: DESCARGA (Sin respuesta, acción física)
        elif mission_code == "mission_3":
            e = Email("Handler_X", _("RE: Extracción"), 
                _("El archivo 'Subject_001.data' es la clave.\nBúscalo en Ghoogle por su nombre exacto y DESCÁRGALO.\n\n(Requiere Deep Web)."),
                mission_id=3)
            inbox.insert(0, e)

        # MISION 4: LOS LIMPIADORES (NUEVA)
        elif mission_code == "mission_4":
            e = Email("Handler_X", _("ALERTA: Black Moth"), 
                _("Al descargar el archivo, activaste una alarma silenciosa.\nUna unidad llamada 'Black Moth' ha sido desplegada.\n\nNecesito saber qué equipo compraron recientemente en el Mercado Negro ('market') para saber a qué nos enfrentamos."),
                mission_id=4, correct_answer=1,
                options=[_("Compraron: Servidores"), _("Compraron: Napalm y Sierras"), _("Compraron: Bitcoins")])
            inbox.insert(0, e)


        # MISION 5: EL PACIENTE (Ya la tienes, la dejamos igual)
        elif mission_code == "mission_5":
            e = Email("Handler_X", _("RE: Brutalidad"), 
                _("El Napalm no fue suficiente.\n\nHay un superviviente: un guardia llamado 'Martinez'.\nBusca en la base de datos del Psiquiátrico St. Jude ('st jude') y dime qué vio."),
                mission_id=5, correct_answer=1,
                options=[_("Vio a Julius Vax"), _("Vio a 'El Tejedor' (The Weaver)"), _("Vio estática pura")])
            inbox.insert(0, e)

        # MISION 6: EL RASTRO DE ROSSI (NUEVA)
        elif mission_code == "mission_6":
            e = Email("Handler_X", _("INTELIGENCIA: Acceso Interno"), 
                _("Hemos encontrado un ID de empleado antiguo: '#IT-440' (Marcus Rossi).\n\nIntrodúcelo en el buscador de Torion para acceder a su perfil en la Intranet de Echo Corp.\n\n¿Qué ID de seguridad menciona en su último log?"),
                mission_id=6, correct_answer=1,
                options=[_("ID: #GUEST-000"), _("ID: #SEC-221"), _("ID: #ADMIN-1")])
            inbox.insert(0, e)

        # MISION 7: EL GUARDIA (NUEVA)
        elif mission_code == "mission_7":
            e = Email("Handler_X", _("RE: Martinez"), 
                _("Bien. El ID #SEC-221 pertenece a J. Martinez.\n\nÚsalo en el buscador ('#SEC-221') para ver su expediente.\n¿A dónde enviaron a Martinez tras el incidente?"),
                mission_id=7, correct_answer=2,
                options=[_("A su casa"), _("A la morgue"), _("Al Psiquiátrico St. Jude")])
            inbox.insert(0, e)

        # MISION 8: LA LLAVE MAESTRA (AQUÍ DAMOS EL ID DE ARLENE)
        elif mission_code == "mission_8":
            e = Email("Handler_X", _("OBJETIVO: Nivel 4"), 
                _("Martinez vio cosas clasificadas. Su reporte menciona que se necesita autorización de NIVEL 4.\n\nHe hackeado la nómina de RRHH. La Jefa de Bio-Ingeniería es la Dra. Arlene.\n\nSu ID es: #RD-892\n\nÚsalo para entrar a su perfil y dime el CÓDIGO del Proyecto 'The Weaver'."),
                mission_id=8, correct_answer=0,
                options=[_("Código: E-01"), _("Código: 404"), _("Código: X-FILE")])
            inbox.insert(0, e)

        # MISION 9: UBICACIÓN
        elif mission_code == "mission_9":
            e = Email("Handler_X", _("GEOLOCALIZACIÓN"), 
                _("El Tejedor (E-01) es un sistema nervioso humano usado como servidor...\nQué horror.\n\nEl archivo menciona que está en la 'Sede Oculta'. Busca las coordenadas en el 'Echo-Tracker' (Maps) y confirma la ciudad."),
                mission_id=9, correct_answer=2,
                options=[_("Nueva York"), _("Londres"), _("Pripyat, Ucrania")])
            inbox.insert(0, e)

        # MISION 10: FINAL
        elif mission_code == "mission_10":
            e = Email("Handler_X", _("OBJETIVO FINAL: Arlene"), 
                _("Arlene está huyendo. Sabemos quién es, sabemos dónde está (Pripyat) y sabemos qué hizo.\n\nUsa 'SCAN_NETWORK' en el CMD. Encuentra su servidor personal y destrúyelo."),
                mission_id=10, correct_answer=0, 
                options=[_("Iniciando ataque final."), _("..."), _("Ayuda.")])
            inbox.insert(0, e)
    
    # --- Pega aquí select_email, open_reply_menu, submit_reply ---
    def select_email(idx):
        store.selected_email_index = idx
        store.inbox[idx].is_read = True
        renpy.restart_interaction()

    def open_reply_menu(email):
        store.replying_email = email
        store.reply_menu_visible = True
        renpy.restart_interaction()
    
    def submit_reply(option_id):
        # 1. Verificamos si la respuesta es correcta
        if store.replying_email and option_id == store.replying_email.correct_answer:
            renpy.play("audio/success_chime.wav") 
            
            # Marcamos como respondido
            store.replying_email.is_replied = True
            store.reply_menu_visible = False
            
            # --- LÓGICA DE MISIONES (CORRECTO) ---
            if store.replying_email.mission_id == 1:
                # CORREGIDO: El nombre va fuera, la traducción _() solo envuelve el texto
                receive_chat("Handler_X", _("Correcto. Julius Vax. Ese tipo es un fantasma."))
                trigger_delayed_email("mission_2", delay=4.0)
                store.current_mission = 2

            elif store.replying_email.mission_id == 2:
                receive_chat("Handler_X", _("Subject_001... Descárgalo, pero no lo abras."))
                store.current_mission = 3

            elif store.replying_email.mission_id == 4: 
                receive_chat("Handler_X", _("Napalm y Sierras... Están limpiando evidencia biológica."))
                trigger_delayed_email("mission_5", delay=5.0) 
                store.current_mission = 5

            elif store.replying_email.mission_id == 5: 
                receive_chat("Handler_X", _("¿'El Tejedor'? Suena a pesadilla. Sigamos."))
                trigger_delayed_email("mission_6", delay=5.0)
                store.current_mission = 6

            elif store.replying_email.mission_id == 6: 
                receive_chat("Handler_X", _("Bien hecho. Rossi nos dio la llave sin saberlo."))
                trigger_delayed_email("mission_7", delay=5.0)
                store.current_mission = 7

            elif store.replying_email.mission_id == 7: 
                receive_chat("Handler_X", _("St. Jude... Típico. Encierran a los testigos."))
                trigger_delayed_email("mission_8", delay=6.0)
                store.current_mission = 8

            elif store.replying_email.mission_id == 8: 
                receive_chat("Handler_X", _("E-01. Confirmado. Rastreo iniciado."))
                trigger_delayed_email("mission_9", delay=5.0)
                store.current_mission = 9

            elif store.replying_email.mission_id == 9: 
                receive_chat("Handler_X", _("Pripyat. Zona de exclusión. Nadie buscaría ahí."))
                trigger_delayed_email("mission_10", delay=4.0)
                store.current_mission = 10

            elif store.replying_email.mission_id == 10: 
                receive_chat("Handler_X", _("Hazlo. GATE_OPEN. Que se caiga el cielo."))

        # ==========================================================
        # 2. SISTEMA DE ERROR REACTIVO
        # ==========================================================
        else:
            renpy.play("audio/error_buzz.mp3.wav")
            renpy.invoke_in_new_context(renpy.with_statement, hpunch)
            
            # Penalización
            update_trace(10)
            
            # Handler reacciona al error ESPECÍFICO
            m_id = store.replying_email.mission_id
            
            if m_id == 1: # Falló el nombre del CEO
                receive_chat("Handler_X", _("¡No! Ese no es el CEO. Busca noticias financieras sobre Echo Corp."))
                
            elif m_id == 2: # Falló el nombre del archivo
                receive_chat("Handler_X", _("¿Qué? No busques videojuegos. Busca el nombre del archivo filtrado en los foros."))
                
            elif m_id == 4: # Falló las armas/compras
                receive_chat("Handler_X", _("Concéntrate. Mira el historial del Mercado Negro (Deep Market). ¿Qué compraron?"))
                
            elif m_id == 5: # Falló lo que vio Martinez
                receive_chat("Handler_X", _("Dato erróneo. Lee el expediente de St. Jude otra vez. ¿Qué vio exactamente?"))
                
            elif m_id == 6: # Falló el ID de seguridad
                receive_chat("Handler_X", _("Ese ID no sirve. Revisa el último log de Rossi en la Intranet."))
                
            elif m_id == 7: # Falló el destino de Martinez
                receive_chat("Handler_X", _("Negativo. No lo enviaron a casa. ¿A qué institución médica fue?"))
                
            elif m_id == 8: # Falló el código de Arlene
                receive_chat("Handler_X", _("Código rechazado. Entra al perfil de Arlene (#RD-892) y busca 'Project Weaver'."))
                
            elif m_id == 9: # Falló la ubicación
                receive_chat("Handler_X", _("No, esa ciudad está limpia. Busca las coordenadas del HQ en el mapa de la Deep Web."))
                
            else:
                # Regaño genérico
                mensajes_error = [
                    _("¡Dato inválido! Nos vas a delatar."),
                    _("¿Estás adivinando? Necesito precisión."),
                    _("Sistema rechazó la respuesta. Inténtalo de nuevo."),
                    _("Concéntrate. Lee bien la información."),
                    _("No podemos permitir errores ahora mismo."),
                    _("Cada error nos acerca al rastreo. Cuidado."),
                    _("¡Eso no es correcto! Revisa los datos otra vez."),
                    _("¡Error! Necesitamos respuestas fiables."),
                    _("¡Cuidado! Cada fallo aumenta el riesgo de rastreo."),
                    _("¡No podemos permitirnos errores"),
                    _("!Deja de jugar y concéntrate."),
                    _("¡Eso no es lo que necesitamos saber!")
                ]
                import random
                msg = random.choice(mensajes_error)
                receive_chat("Handler_X", msg)
        
        renpy.restart_interaction()

    # --- Funciones de control de ventanas UI ---
    def toggle_browser():
        if store.browser_visible and not store.browser_minimized: store.browser_minimized = True
        elif store.browser_visible: store.browser_minimized = False
        else: store.browser_visible = True; store.browser_minimized = False; set_focus("browser")
    def close_browser(): store.browser_visible = False; store.current_site_id = "home"
    
    def toggle_mail():
        if store.mail_visible and not store.mail_minimized: store.mail_minimized = True
        elif store.mail_visible: store.mail_minimized = False
        else: store.mail_visible = True; store.mail_minimized = False; set_focus("mail")
    def close_mail(): store.mail_visible = False
    
    def toggle_cmd():
        if store.cmd_visible and not store.cmd_minimized: store.cmd_minimized = True
        elif store.cmd_visible: store.cmd_minimized = False
        else: store.cmd_visible = True; store.cmd_minimized = False; set_focus("cmd")