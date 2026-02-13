# Copyright 2026 Alenia Studios. All rights reserved.
# This code is the property of Alenia Studios and may not be used without permission.
# Developed for the project: Gatekeeper

label start:
    # --- 1. LIMPIEZA TOTAL DE VARIABLES (RESET) ---
    # Esto asegura que no queden restos de partidas anteriores al probar
    $ trace_level = 0
    $ deep_mode = False
    $ virus_installed = False        
    $ is_downloading = False
    $ downloaded_files = []          
    
    # Reset de Ventanas y Apps
    $ browser_visible = False
    $ mail_visible = False
    $ cmd_visible = False
    $ mypc_visible = False
    $ mypc_locked = True             
    $ mypc_password_attempt = ""
    $ antivirus_timer = 0          # Temporizador del antivirus (0 = apagado)
    # Variables de Misión
    $ current_mission = 1
    $ inbox = []                     
    $ history = ["home"]
    $ current_site_id = "home"
    
    # --- 2. INICIO DEL JUEGO ---
    play music "audio/ambiente.mp3" loop
    scene bg desktop
    
    "SYSTEM" "Iniciando protocolos Gatekeeper..."
    
    # Enviamos el primer correo
    $ trigger_delayed_email("welcome", delay=2.0)
    $ receive_chat(_("Handler_X"), _("Bienvenido al sistema Gatekeeper. Tu misión es infiltrarte en el servidor de Echo Corp y obtener los datos sensibles. No te desesperes si todo parece confuso. Solo sigue las pistas que te dan los correos electrónicos."))
    $ cmd_history_text = _("Microsoft(R) Windows 98\nC:\\Users\\Admin> Subject_001.bat\n[[ERROR]: SISTEMA BLOQUEADO.\n[[PISTA]: INTRODUCE 'HELP' PARA COMENZAR.")
    
    # Iniciamos la pantalla
    call screen desktop

    return

label start_download:
    $ is_downloading = True
    $ terminal_log = []
    
    $ terminal_log.append(_("Conectando..."))
    show screen desktop 
    $ renpy.pause(0.5)
    $ terminal_log.append(_("Descargando Subject_001.data..."))
    show screen desktop 
    $ renpy.pause(0.5)
    $ terminal_log.append("[=====>              ] 25%")
    show screen desktop 
    $ renpy.pause(0.5)
    $ terminal_log.append("[==========>         ] 50%")
    show screen desktop 
    $ renpy.pause(0.5)
    $ terminal_log.append("[===============>    ] 75%")
    show screen desktop 
    $ renpy.pause(0.5)
    $ terminal_log.append("[===================>] 100%")
    show screen desktop 
    $ renpy.pause(1.0)
    
    $ is_downloading = False
    $ virus_installed = True
    # ACTIVA EL VIRUS
    
    # --- MOMENTO DRAMÁTICO ---
    play sound "audio/error_popup.wav"
    
    # 1. Handler reacciona al desastre
    $ receive_chat(_("Handler_X"), _("¡Mierda! ¡Es una trampa lógica! Tu pantalla se está llenando de basura."))
    
    # 2. Handler te da la solución (Tutorial integrado)
    $ receive_chat(_("Handler_X"), _("¡No puedo ver nada! Escucha: Abre la terminal y escribe 'PURGE'."))
    $ receive_chat(_("Handler_X"), _("Eso limpiará la RAM unos segundos. Úsalo para ganar tiempo y busca los datos."))
    # CRÍTICO: Esto activa la siguiente misión
    $ download_file(_("subject_001"))
    
    call screen desktop

label open_cursed_file:
    $ browser_visible = False
    $ mail_visible = False
    $ cmd_visible = True
    call screen desktop

label endgame_sequence:
    $ browser_visible = False
    $ mail_visible = False
    $ cmd_visible = False
    
    scene bg desktop at screen_shake_glitch
    play sound "audio/alarm.wav"
    
    # CORREGIDO: [[ Dobles corchetes al inicio
    centered "{color=#00ff00}[[CONEXIÓN SEGURA ESTABLECIDA]{/color}"
    centered "GATEKEEPER PROTOCOL V.1.0"
    centered "ADVERTENCIA: Se requiere autorización de Nivel 5."
    $ auth_code = renpy.input(_("INTRODUZCA CÓDIGO DE PROYECTO:"), length=20).strip().upper()

    if auth_code == "VIGILANT":
        jump true_ending
    else:
        # CORREGIDO: [[ERROR]
        centered "{color=#f00}[[ERROR]: CONTRASEÑA INCORRECTA.{/color}"
        centered "Reiniciando conexión..."
        $ cmd_visible = True
        call screen desktop

label true_ending:
    scene black with dissolve 
    # CORREGIDO: [[ACCESO]
    centered "{color=#00ff00}[[ACCESO CONCEDIDO]{/color}"
    centered "Has completado la operación de infiltración."
    centered "Ahora tienes las credenciales para acceder al servidor real."
    centered "{size=40}{color=#f00}USUARIO: #GUEST-000"
    
    centered "Haz clic para acceder al terminal maestro:"
    $ webbrowser.open("https://echo-corp.neocities.org/")
    
    centered "{b}FIN DE LA Busqueda. Iremos por Martinez{/b}"
    return

label game_over_traced:
    $ close_browser()
    $ close_mail()
    $ store.cmd_visible = True
    # CORREGIDO: [[ALERTA], [[SISTEMA], [[ESTADO]
    $ store.cmd_history_text += _("\n\n[[ALERTA]: RASTREO DE IP COMPLETADO.\n[[SISTEMA]: CONEXIÓN INTERCEPTADA POR ECHO CORP.\n[[ESTADO]: LOCALIZANDO DIRECCIÓN FÍSICA...")
    scene black with dissolve
    centered "{color=#f00}TE HAN ENCONTRADO.{/color}"
    centered "{color=#f00}No debiste profundizar tanto en los nodos de Arke.{/color}"
    $ renpy.quit()

label bad_ending:
    scene black with dissolve
    # CORREGIDO: [[ACCESO] y [[SISTEMA]
    centered "{color=#f00}[[ACCESO DENEGADO]{/color}"
    centered "{color=#f00}[[SISTEMA]: RASTREO DE IP INICIADO...{/color}"
    return