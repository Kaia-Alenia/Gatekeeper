# Copyright 2026 Alenia Studios. All rights reserved.
# This code is the property of Alenia Studios and may not be used without permission.
# Developed for the project: Gatekeeper


# --- VARIABLES ---
default mypc_visible = False
default mypc_minimized = False
default mypc_locked = True
default mypc_password_attempt = ""
# Inicializamos las notas vacías o con un template genérico
default user_notes = _("BLOC DE NOTAS DEL SISTEMA\n-------------------------\n\n(Escribe aquí tus descubrimientos...)")

init python:
    import os # Necesario para guardar archivos en el sistema real

    # Función para guardar las notas en un archivo .txt real
    def export_notes_to_txt():
        # Definimos la ruta: Se guardará en la misma carpeta que el ejecutable del juego
        file_name = "GATEKEEPER_NOTES.txt"
        file_path = os.path.join(config.basedir, file_name)
        
        try:
            # Escribimos el contenido de la variable user_notes en el archivo
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(store.user_notes)
            renpy.notify(_("Notas guardadas en: ") + file_path)
        except:
            renpy.notify(_("Error al escribir en disco."))

    # Función para abrir Mi PC
    def open_mypc():
        store.browser_visible = False
        store.mail_visible = False
        store.cmd_visible = False
        clear_all_popups()
        
        if store.mypc_visible and not store.mypc_minimized:
            store.mypc_minimized = True
            # Guardamos también al minimizar por seguridad
            export_notes_to_txt() 
        elif store.mypc_visible:
            store.mypc_minimized = False
        else:
            store.mypc_visible = True
            store.mypc_minimized = False
            store.active_window = "mypc"
        
        renpy.play("audio/click.wav") 
        renpy.restart_interaction()

    # Función para cerrar Mi PC
    def close_mypc():
        # Antes de cerrar, guardamos el archivo en la PC real
        export_notes_to_txt()
        
        store.mypc_visible = False
        renpy.restart_interaction()

    def check_mypc_login():
        attempt = store.mypc_password_attempt.strip().lower()
        real_user = store.pc_user.strip().lower()
        
        if attempt == real_user or attempt == "ad_min":
            store.mypc_locked = False
            renpy.play("audio/success_chime.wav")
            renpy.notify(_("ACCESO CONCEDIDO: " + real_user.upper()))
        else:
            renpy.play("audio/error_buzz.mp3.wav")
            renpy.notify(_("ERROR: USUARIO DESCONOCIDO."))
            store.mypc_password_attempt = "" 
            update_trace(5) 
        
        renpy.restart_interaction()

screen mypc_window():
    if mypc_visible and not mypc_minimized:
        drag:
            drag_name "mypc_window"
            xpos 100 ypos 80 draggable True drag_handle (0, 0, 500, 30) drag_raise True
            
            frame:
                xsize 500 ysize 400 background "#c0c0c0"
                
                # BARRA DE TÍTULO
                frame:
                    xpos 4 ypos 4 xsize 492 ysize 26 background "#000080"
                    # Usamos el nombre real solo en la barra de título una vez desbloqueado, o "SYSTEM" si está bloqueado
                    if mypc_locked:
                         text "SYSTEM LOCKED // GUEST MODE" color "#fff" bold True size 14 align (0.02, 0.5)
                    else:
                         text "SYSTEM PROPERTIES // " + pc_user.upper() color "#fff" bold True size 14 align (0.02, 0.5)

                    hbox:
                        align (0.98, 0.5) spacing 2
                        button:
                            xsize 20 ysize 18 background "#c0c0c0" action Function(open_mypc)
                            text "_" color "#000" size 12 align (0.5, 0.0) bold True
                        button:
                            xsize 20 ysize 18 background "#c0c0c0" action Function(close_mypc)
                            text "X" color "#000" size 12 align (0.5, 0.5) bold True

                # CONTENIDO PRINCIPAL
                frame:
                    xpos 10 ypos 40 xsize 480 ysize 350 background "#fff"
                    
                    # --- PANTALLA DE BLOQUEO (LOGIN) ---
                    if mypc_locked:
                        vbox:
                            align (0.5, 0.4) spacing 20
                            
                            # Feedback visual de error/bloqueo
                            text _("⚠ ACCESO RESTRINGIDO ⚠") color "#f00" bold True size 18 xalign 0.5
                            
                            null height 5
                            
                            # ID DEL JUGADOR (LORE)
                            text _("ID DE SESIÓN ACTUAL:") color "#555" size 12 xalign 0.5
                            text "{b}#GUEST-000{/b}" color "#000080" size 30 bold True xalign 0.5
                            
                            null height 15
                            
                            # PISTA CRÍPTICA (El puzle)
                            text _("SOLICITUD DE SEGURIDAD:") color "#000" size 14 xalign 0.5
                            text _("Introduzca credenciales del ADMINISTRADOR HOST") color "#555" size 12 xalign 0.5
                            text _("(Pista: Nombre de usuario del entorno local)") color "#aaa" size 10 xalign 0.5 italic True
                            
                            # Campo de contraseña
                            frame:
                                background "#eee" xsize 220 ysize 35 xalign 0.5
                                input value VariableInputValue("mypc_password_attempt", returnable=False) length 20 color "#000" align (0.5, 0.5)
                            
                            textbutton _("[[ AUTENTICAR ]"):
                                xalign 0.5
                                text_color "#fff" background "#000080" padding (30, 8)
                                text_hover_color "#0f0"
                                action Function(check_mypc_login)

                    # --- PANTALLA DESBLOQUEADA (ARCHIVOS Y NOTAS) ---
                    else:
                        hbox:
                            spacing 10 xfill True
                            
                            # COLUMNA IZQUIERDA: ARCHIVOS
                            vbox:
                                xsize 150 spacing 10
                                text _("ALMACENAMIENTO") color "#000" bold True size 14 underline True
                                
                                if not downloaded_files:
                                    text _("Disco Vacío") color "#888" size 12 italic True
                                else:
                                    for f in downloaded_files:
                                        hbox:
                                            spacing 5
                                            text "💾" color "#000" size 12
                                            if f == "subject_001":
                                                text "Subject_001.dat" color "#000" size 12
                                            elif f == "arlene_log":
                                                text "Arlene_Log.enc" color "#000" size 12
                                            else:
                                                text f.upper() color "#000" size 12
                            
                            # SEPARADOR VERTICAL
                            frame:
                                xsize 2 yfill True background "#ccc"

                            # COLUMNA DERECHA: BLOC DE NOTAS + AVISO
                            vbox:
                                xsize 300 spacing 5
                                text _("NOTAS DE USUARIO") color "#000" bold True size 14 underline True
                                text _("(Persistente en sesión)") color "#888" size 10
                                
                                # Área de texto editable (Block de notas)
                                frame:
                                    # Definimos el tamaño del post-it amarillo
                                    ysize 250 background "#ffffcc" xfill True 
                                    
                                    # AGREGAMOS UN VIEWPORT (Caja con Scroll)
                                    # Esto evita que el texto se salga de la ventana si escriben mucho
                                    viewport:
                                        mousewheel True   # Permite usar la rueda del ratón
                                        draggable True    # Permite arrastrar en móviles/touch
                                        scrollbars "both" # Pone barras de scroll (Vertical y Horizontal)
                                        
                                        # EL INPUT CONFIGURADO PARA ESCRIBIR MUCHO
                                        input:
                                            value VariableInputValue("user_notes") 
                                            color "#000" 
                                            size 14 
                                            # CAMBIO CLAVE 1: Permite usar ENTER para bajar línea
                                            multiline True 
                                            # CAMBIO CLAVE 2: Define un ancho máximo para intentar ajustar el texto
                                            xsize 270 
                                
                                # --- AVISO MODO SEGURO (CORREGIDO) ---
                                null height 5
                                frame:
                                    background "#ffffe0" xfill True ysize 35 padding (5, 2)
                                    hbox:
                                        spacing 5 align (0.5, 0.5) # Centrado vertical y horizontalmente
                                        text "⚠" color "#d00" size 12 bold True
                                        # Texto más pequeño y conciso
                                        text _("MODO SEGURO: Cierra esta ventana para conectar a la red.") color "#d00" size 9