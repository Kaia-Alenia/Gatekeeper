# Copyright 2026 Alenia Studios. All rights reserved.
# This code is the property of Alenia Studios and may not be used without permission.
# Developed for the project: Gatekeeper


screen desktop():
    add "bg desktop"
    timer 1.0 repeat True action [Function(check_incoming_mail), Function(threat_tick)]

    draggroup:
        # ICONOS
        drag:
            xpos 40 ypos 60 draggable True
            button:
                xsize 80 ysize 90 background None 
                # CAMBIO AQUÍ: Usamos la nueva función
                action Function(open_mypc) 
                vbox:
                    spacing 5
                    frame:
                        xsize 50 ysize 50 background "#fff" xalign 0.5
                        text "PC" color "#000" size 20 bold True align(0.5,0.5)
                    text _("Mi PC") color "#fff" size 14 xalign 0.5 outlines [(1, "#000", 0, 0)]
        drag:
            xpos 40 ypos 180 draggable True
            button:
                xsize 80 ysize 90 background None action Function(toggle_mail)
                vbox:
                    spacing 5
                    frame:
                        xsize 50 ysize 50 background "#ebc934" xalign 0.5
                        if any(not e.is_read for e in inbox):
                            text "!" color "#f00" size 30 bold True align(1.0, 0.0)
                    text "SecuMail" color "#fff" size 14 xalign 0.5 outlines [(1, "#000", 0, 0)]
        drag:
            xpos 40 ypos 300 draggable True
            button:
                xsize 80 ysize 90 background None action Function(toggle_browser)
                vbox:
                    spacing 5
                    frame:
                        xsize 50 ysize 50 background "#344ceb" xalign 0.5
                        text "e" color "#fff" size 30 bold True align(0.5,0.5)
                    text "Torion" color "#fff" size 14 xalign 0.5 outlines [(1, "#000", 0, 0)]

        # ICONO PAPELERA DE RECICLAJE
        drag:
            xpos 40 ypos 420 draggable True 
            button:
                xsize 80 ysize 90 background None 
                action Function(open_bin)
                vbox:
                    spacing 5
                    frame:
                        xsize 50 ysize 50 background None xalign 0.5
                        # Emoji de basura
                        text "🗑" color "#fff" size 40 align(0.5,0.5) 
                    text _("Papelera") color "#fff" size 14 xalign 0.5 outlines [(1, "#000", 0, 0)]

        if virus_installed:
            drag:
                xpos 160 ypos 60 draggable True
                button:
                    xsize 80 ysize 90 background None action Jump("open_cursed_file")
                    vbox:
                        spacing 5
                        frame:
                            xsize 50 ysize 50 background "#f00" xalign 0.5
                            text "!" color "#fff" size 40 bold True align(0.5,0.5)
                        text _("LEEME") color "#fff" size 14 xalign 0.5 outlines [(1, "#000", 0, 0)]

       # --- VENTANA CMD ---
        if cmd_visible and not cmd_minimized:
            drag:
                drag_name "cmd_window"
                # CORRECCIÓN: Variables dinámicas + Callback de arrastre
                xpos cmd_x ypos cmd_y draggable True drag_handle (0, 0, 600, 30) drag_raise True dragged window_dragged
                
                # Foco al hacer click
                button:
                    xpos 0 ypos 30 xfill True yfill True background None action Function(set_focus, "cmd")
                    frame:
                        xsize 600 ysize 400 background "#c0c0c0"
                        frame: 
                            align (0.0, 0.0) xfill True ysize 2 background "#fff"
                        
                        # Barra Titulo
                        frame:
                            xpos 4 ypos 4 xsize 592 ysize 26 background "#000080"
                            text "CMD.EXE" color "#fff" bold True size 14 align (0.02, 0.5)
                            hbox:
                                align(0.98, 0.5) spacing 2
                                button:
                                    xsize 20 ysize 18 background "#c0c0c0" action Function(toggle_cmd)
                                    text "_" color "#000" size 12 align(0.5, 0.0) bold True
                                button:
                                    xsize 20 ysize 18 background "#c0c0c0" action Notify(_("Bloqueado"))
                                    text "X" color "#888" size 12 align(0.5, 0.5) bold True

                        # Contenido
                        frame:
                            xpos 10 ypos 40 xsize 580 ysize 350 background "#000"
                            button:
                                xfill True yfill True background None action Function(set_focus, "cmd")
                            vbox:
                                spacing 5
                                viewport:
                                    scrollbars "vertical" mousewheel True draggable True ysize 300 yinitial 1.0
                                    
                                    # IMPORTANTE: Usamos un vbox para agrupar los dos textos
                                    vbox:
                                        # Alinea estos dos 'text' perfectamente en vertical (misma cantidad de espacios)
                                        text _("Microsoft(R) Windows 98\nC:\\Users\\Admin> Subject_001.bat\n<ERROR>: SISTEMA BLOQUEADO.\n<PISTA>: INTRODUCE 'HELP' PARA COMENZAR.") color "#0f0" size 14 font "DejaVuSans.ttf"
                                        text cmd_history_text color "#0f0" size 14 font "DejaVuSans.ttf" substitute False

                                        hbox:
                                            text ">" color "#0f0" size 14
                                            if active_window == "cmd":
                                                input value CmdInputValue("cmd_input", Function(process_cmd)) length 60 color "#0f0" size 14

      # --- VENTANA EMAIL (CORREGIDA Y MOVIBLE) ---
        if mail_visible and not mail_minimized:
            drag:
                drag_name "mail_window"
                # Usa variables persistentes y callback de arrastre
                xpos mail_x ypos mail_y draggable True drag_handle (0, 0, 700, 30) drag_raise True dragged window_dragged
                
                frame:
                    xsize 700 ysize 500 background Solid("#c0c0c0")
                    
                    # Borde decorativo
                    frame: 
                        align (0.0, 0.0) xfill True ysize 2 background "#fff"

                    # Barra de Título (LIBRE PARA ARRASTRAR)
                    frame:
                        xpos 4 ypos 4 xsize 692 ysize 26 background Solid("#000080")
                        text "SecuMail v1.0" color "#fff" bold True size 14 align (0.02, 0.5)
                        hbox:
                            align(0.98, 0.5) spacing 2
                            button:
                                xsize 20 ysize 18 background "#c0c0c0" action Function(toggle_mail)
                                text "_" color "#000" size 12 align(0.5, 0.0) bold True
                            button:
                                xsize 20 ysize 18 background "#c0c0c0" action Function(close_mail)
                                text "X" color "#000" size 12 align(0.5, 0.5) bold True

                    # Foco: Solo si haces click fuera de la barra de título
                    button:
                        xpos 0 ypos 30 xfill True yfill True background None action Function(set_focus, "mail")

                    hbox:
                        xpos 10 ypos 40 spacing 5
                        # Lista de mensajes (Izquierda)
                        frame:
                            xsize 200 ysize 440 background "#fff"
                            viewport:
                                scrollbars "vertical" mousewheel True draggable True
                                vbox:
                                    spacing 2
                                    for i, email in enumerate(inbox):
                                        button:
                                            xfill True ysize 40
                                            if i == selected_email_index:
                                                background "#000080"
                                            else:
                                                background "#fff"
                                            action Function(select_email, i)
                                            vbox:
                                                xoffset 5
                                                text email.sender size 14 color ("#fff" if i == selected_email_index else "#000") bold True
                                                text email.subject size 12 color ("#ccc" if i == selected_email_index else "#555")
                        
                        # Lector de mensajes (Derecha)
                        frame:
                            xsize 470 ysize 440 background "#fff"
                            if selected_email_index != -1 and selected_email_index < len(inbox):
                                $ current_email = inbox[selected_email_index]
                                vbox:
                                    xoffset 10 yoffset 10 spacing 10
                                    text _("DE: <current_email.sender>") color "#000" bold True size 16
                                    text _("ASUNTO: <current_email.subject>") color "#000" size 16
                                    frame:
                                        xfill True ysize 2 background "#ccc"
                                    text current_email.body color "#000" size 14 xsize 440
                                    null height 20
                                    
                                    if not current_email.is_replied and current_email.mission_id != 3:
                                        textbutton _(">> REDACTAR RESPUESTA <<"):
                                            text_color "#fff" background "#00f" padding (10,5)
                                            action Function(open_reply_menu, current_email)
                                    elif current_email.is_replied:
                                        text _("< ENVIADO >")color "#0f0" bold True
                            else:
                                text _("Bandeja de entrada.") color "#aaa" align(0.5, 0.5)

        # --- VENTANA BROWSER (VERSIÓN CORREGIDA FINAL) ---
        if browser_visible and not browser_minimized:
            drag:
                drag_name "browser_window"
                xpos browser_x ypos browser_y draggable True drag_handle (0, 0, 800, 30) drag_raise True dragged window_dragged
                
                frame:
                    xsize 800 ysize 600 background "#c0c0c0"
                    
                    # Foco: Detecta click en el fondo para traer ventana al frente
                    button:
                        xfill True ysize 30 background None action Function(set_focus, "browser")

                    # BARRA DE TÍTULO
                    frame: 
                        xpos 4 ypos 4 xsize 792 ysize 26 background "#000080"
                        text "Torion Browser" color "#fff" bold True size 14 align (0.02, 0.5)
                        hbox:
                            align (0.98, 0.5) spacing 2
                            button:
                                xsize 20 ysize 18 background "#c0c0c0" action Function(toggle_browser)
                                text "_" color "#000" size 12 align (0.5, 0.0) bold True
                            button:
                                xsize 20 ysize 18 background "#c0c0c0" action Function(close_browser)
                                text "X" color "#000" size 12 align (0.5, 0.5) bold True

                    # ÁREA DE CONTENIDO (FONDO GRIS CLARO DETRÁS DE LA PÁGINA)
                    frame: 
                        xpos 10 ypos 40 xsize 780 ysize 550 background None
                        vbox:
                            spacing 10
                            
                            # --- BARRA DE NAVEGACIÓN Y URL ---
                            hbox:
                                spacing 5
                                
                                # BOTÓN ATRÁS (DENTRO DE UN FRAME PARA QUE RESALTE)
                                button:
                                    action Function(go_back)
                                    xsize 40 ysize 30
                                    yoffset -5
                                    background "#e0e0e0" # Un gris más claro que el fondo
                                    # Añadimos un borde negro simple (outline)
                                    frame:
                                        background None
                                        xfill True yfill True
                                        text "<" color "#000" bold True align(0.5, 0.5) size 20 outlines [(1, "#000", 0, 0)]
                                
                                # BARRA DE URL
                                frame:
                                    ysize 30 xsize 730 background "#fff" # Ajustado el ancho
                                    text get_site_data(current_site_id)["url"] color "#000" yalign 0.5 xoffset 5 size 14

                            # --- VISTA DE LA PÁGINA (VIEWPORT) ---
                            frame:
                                xfill True yfill True
                                # El fondo cambia según la página actual
                                background get_site_data(current_site_id)["bg"]
                                
                                viewport:
                                    scrollbars "vertical" mousewheel True draggable True
                                    
                                    vbox: 
                                        xoffset 20 yoffset 20 spacing 20
                                        
                                        # 1. PÁGINA DE INICIO (GHOOGLE)
                                        if current_site_id == "home":
                                            text "Ghoogle" color "#00f" size 60 bold True xalign 0.5
                                            hbox:
                                                spacing 10 xalign 0.5
                                                frame:
                                                    xsize 300 ysize 35 background "#fff"
                                                    if active_window == "browser":
                                                        input value SearchInputValue("search_query", Function(perform_search)) length 20 color "#000" yalign 0.5 xoffset 5
                                                    else:
                                                        text _("Haz click para buscar...") color "#ccc" size 14 yalign 0.5 xoffset 5
                                                textbutton "Search":
                                                    action Function(perform_search)
                                                    background "#c0c0c0" text_color "#000" padding (10, 5)

                                        # 2. PÁGINA DE RESULTADOS
                                        elif current_site_id == "results":
                                            text _("Resultados de búsqueda:") color "#000" size 16
                                            
                                            if not get_site_data("results")["links"]:
                                                null height 20
                                                text _("No se encontraron documentos para su búsqueda.") color "#000" size 14
                                                text _("Sugerencias:") color "#000" size 14
                                                text _("• Asegúrese de que todas las palabras estén escritas correctamente.") color "#000" size 14
                                                text _("• Intente usar palabras clave más generales.") color "#000" size 14
                                            else:
                                                # Renderizado de lista de resultados
                                                vbox:
                                                    spacing 15 
                                                    for title, url_txt, desc, site_id in get_site_data("results")["links"]:
                                                        button:
                                                            background None
                                                            xfill True
                                                            action Function(nav_to, site_id)
                                                            vbox:
                                                                text title color "#1a0dab" size 18 bold True hover_underline True
                                                                text url_txt color "#006621" size 12
                                                                text desc color "#545454" size 14 xsize 700

                                        # 3. PÁGINA DE INSTALACIÓN TOR
                                        elif current_site_id == "surface_tor":
                                            text "Onion Project" color "#fff" size 30 bold True
                                            text _("PROTOCOLO DE ENCRIPTACIÓN DISPONIBLE.") color "#fff" size 18
                                            null height 20
                                            textbutton _(">>> INSTALAR PARCHE <<<"):
                                                text_color "#0f0" text_bold True action [Function(install_deep_patch), With(dissolve)]

                                        # 4. PÁGINAS GENÉRICAS (El resto de sitios)
                                        else:
                                            # Título
                                            text get_site_data(current_site_id)["title"] color get_site_data(current_site_id).get("text_col", "#000") size 30 bold True
                                            
                                            # Breadcrumbs (Ruta)
                                            if "breadcrumbs" in get_site_data(current_site_id):
                                                text " > ".join(get_site_data(current_site_id)["breadcrumbs"]) color get_site_data(current_site_id).get("text_col", "#000") size 14
                                            
                                            # Contenido de texto
                                            text get_site_data(current_site_id)["content"] color get_site_data(current_site_id).get("text_col", "#000") size 18 xsize 740

                                            # Enlaces de navegación (Links)
                                            if "links" in get_site_data(current_site_id) and get_site_data(current_site_id)["links"]:
                                                vbox:
                                                    spacing 8
                                                    for link_title, link_target in get_site_data(current_site_id)["links"]:
                                                        textbutton "{u}[link_title!t]{/u}":
                                                            action Function(nav_to, link_target)
                                                            text_color "#00f" text_size 18

                                            # --- BOTONES ESPECIALES (Fuera del IF de links, dentro del ELSE) ---
                                            
                                            # Botón para descargar Subject_001
                                            if current_site_id == "deep_cursed":
                                                null height 30
                                                if not is_downloading and not virus_installed:
                                                    textbutton _("[[ DESCARGAR ]"):
                                                        text_color "#fff" background "#f00" padding (20,10) 
                                                        action Jump("start_download")

                                            # Botón para Log de Arlene
                                            if current_site_id == "cradle_site":
                                                null height 20
                                                textbutton _("[[ DESCARGAR LOG ]"):
                                                    text_color "#fff" background "#00f" padding (20,10)
                                                    action Function(download_file, "arlene_log")
                                            
                                            # Enlace externo Denis
                                            if current_site_id == "denis_site":
                                                null height 20
                                                textbutton _("[[ VISITAR PÁGINA REAL ]"):
                                                    text_color "#fff" background "#fa5c5c" padding (20,10)
                                                    action OpenURL("https://gamesdenis.itch.io/")
                                            
                                            # Enlace externo Alenia
                                            if current_site_id == "alenia_site":
                                                null height 20
                                                textbutton _("[[ VISITAR ITCH.IO ]"):
                                                    text_color "#000" background "#00d0ff" padding (20,10) text_bold True
                                                    action OpenURL("https://alenia-studios.itch.io/")

    # --- MENU FLOTANTE RESPUESTA ---
    if reply_menu_visible and replying_email:
        drag:
            xpos 400 ypos 200 draggable True
            frame:
                xsize 600 ysize 400 background Solid("#000080")
                frame:
                    align (0.5, 0.5) xsize 580 ysize 380 background "#fff"
                    vbox:
                        spacing 20 align(0.5, 0.5)
                        text _("SELECCIONA TU RESPUESTA:") color "#000" bold True xalign 0.5
                        if replying_email.options:
                            for idx, opt_text in enumerate(replying_email.options):
                                textbutton opt_text:
                                    text_color "#00f" text_hover_color "#f00" xalign 0.5
                                    action Function(submit_reply, idx)
                        textbutton _("[[ CANCELAR ]"):
                            text_color "#aaa" xalign 0.5
                            action SetVariable("reply_menu_visible", False)

    # --- BARRA TAREAS ---
    frame:
        align (0.5, 1.0) xsize 1920 ysize 45 background Solid("#c0c0c0")
        frame:
            yalign 0.0 xfill True ysize 2 background "#fff"
        button:
            align (0.01, 0.5) xsize 80 ysize 35 background "#c0c0c0"
            frame: 
                align (0.0, 0.0) xfill True ysize 2 background "#fff" 
            frame: 
                align (1.0, 1.0) xfill True ysize 2 background "#404040"
            text _("Inicio") color "#000" bold True size 16 align (0.5, 0.5)
        hbox:
            align (0.1, 0.5) spacing 5
            if browser_visible:
                button:
                    xsize 150 ysize 35 background "#c0c0c0"
                    action Function(toggle_browser)
                    if not browser_minimized:
                        frame: 
                            align (0.0, 0.0) xfill True ysize 2 background "#404040"
                        frame: 
                            align (1.0, 1.0) xfill True ysize 2 background "#fff"
                    else:
                        frame: 
                            align (0.0, 0.0) xfill True ysize 2 background "#fff"
                        frame: 
                            align (1.0, 1.0) xfill True ysize 2 background "#404040"
                    text "Torion" color "#000" size 14 align (0.5, 0.5)
            if mail_visible:
                button:
                    xsize 150 ysize 35 background "#c0c0c0"
                    action Function(toggle_mail)
                    if not mail_minimized:
                        frame: 
                            align (0.0, 0.0) xfill True ysize 2 background "#404040"
                        frame: 
                            align (1.0, 1.0) xfill True ysize 2 background "#fff"
                    else:
                        frame: 
                            align (0.0, 0.0) xfill True ysize 2 background "#fff"
                        frame: 
                            align (1.0, 1.0) xfill True ysize 2 background "#404040"
                    text "SecuMail" color "#000" size 14 align (0.5, 0.5)
            if cmd_visible:
                button:
                    xsize 150 ysize 35 background "#c0c0c0"
                    action Function(toggle_cmd)
                    if not cmd_minimized:
                        frame: 
                            align (0.0, 0.0) xfill True ysize 2 background "#404040"
                        frame: 
                            align (1.0, 1.0) xfill True ysize 2 background "#fff"
                    else:
                        frame: 
                            align (0.0, 0.0) xfill True ysize 2 background "#fff"
                        frame: 
                            align (1.0, 1.0) xfill True ysize 2 background "#404040"
                    text "MS-DOS" color "#000" size 14 align (0.5, 0.5)

            if mypc_visible:
                button:
                    xsize 150 ysize 35 background "#c0c0c0"
                    action Function(open_mypc)
                    
                    # Efecto visual de botón presionado o levantado
                    if not mypc_minimized:
                        frame: 
                            align (0.0, 0.0) xfill True ysize 2 background "#404040"
                        frame: 
                            align (1.0, 1.0) xfill True ysize 2 background "#fff"
                    else:
                        frame: 
                            align (0.0, 0.0) xfill True ysize 2 background "#fff"
                        frame: 
                            align (1.0, 1.0) xfill True ysize 2 background "#404040"
                    
                    text "System Properties" color "#000" size 14 align (0.5, 0.5)
            
            if chat_visible:
                button:
                    xsize 150 ysize 35 background "#c0c0c0"
                    # Usamos la función toggle_chat que definimos en 07_immersion.rpy
                    action Function(toggle_chat)
                    
                    if not chat_minimized:
                        frame: 
                            align (0.0, 0.0) xfill True ysize 2 background "#404040"
                        frame: 
                            align (1.0, 1.0) xfill True ysize 2 background "#fff"
                    else:
                        frame: 
                            align (0.0, 0.0) xfill True ysize 2 background "#fff"
                        frame: 
                            align (1.0, 1.0) xfill True ysize 2 background "#404040"
                    
                    hbox:
                        spacing 5 align(0.5, 0.5)
                        # Icono pequeño (círculo verde de conectado)
                        text "●" color "#0f0" size 10 
                        text "DarkWire" color "#000" size 14

        frame:
            align (0.99, 0.5) xsize 80 ysize 30 background "#c0c0c0"
            frame: 
                align (0.0, 0.0) xfill True ysize 1 background "#808080"
            frame: 
                align (1.0, 1.0) xfill True ysize 1 background "#fff"
            # CORREGIDO: Quité un corchete extra para que la hora se vea bien: [get_time()]
            text "[get_time()]" color "#000" size 14 align (0.5, 0.5)

    # --- CORRECCIÓN AQUÍ ---
    use mypc_window
    use virus_layer
    use chat_window
    use bin_window