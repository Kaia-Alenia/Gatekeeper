# Copyright 2026 Alenia Studios. All rights reserved.
# This code is the property of Alenia Studios and may not be used without permission.
# Developed for the project: Gatekeeper

init python:

    # --- 1. FUNCIÓN MAESTRA DE DATOS ---
    def build_site_database():
        # Lógica para cambiar entre modo Normal y Deep Web
        home_url = "ghoogle.onion" if store.deep_mode else "ghoogle.com"
        home_title = _("Ghoogle (ONION MODE)") if store.deep_mode else _("Ghoogle")
        home_bg = "#111" if store.deep_mode else "#fff"

        # Diccionario maestro de sitios
        data = {
            # =================================================================
            # --- CORE (SISTEMA) ---
            # =================================================================
            "home": { "url": home_url, "title": home_title, "bg": home_bg, "type": "search_engine" },
            
            "results": { 
                "url": "ghoogle.com/search", "title": _("Resultados"), "bg": "#fff", 
                "type": "results_list", "links": store.global_search_results 
            },

            # =================================================================
            # --- SURFACE WEB (INTERNET NORMAL) ---
            # =================================================================
            
            "surface_news": {
                "url": "dailynet.com", "title": _("Daily Net: Noticias"), "bg": "#eef", "text_col": "#000",
                "content": _("TITULARES DE HOY:\n\n1. El precio del café sintético sube un 200% tras la sequía en los bio-domos.\n2. {b}Julius Vax{/b}, CEO de Echo Corp, lleva 72 horas desaparecido. La junta directiva pide calma.\n3. Protestas en el Sector 7: Los ciudadanos denuncian 'zumbidos' que provocan sangrado nasal.\n\nOPINIÓN: ¿Son seguros los implantes neurales de bajo coste?"),
                "tags": ["news","echo","vax","finanzas","cifrado","noticias","daily","money","finance"],
                "links": [(_("Ver análisis financiero"), "surface_finance_blog"), (_("Rumores en foros"), "surface_forum_rumors")],
                "breadcrumbs": [_("Inicio > Noticias > Global")], "hint_level": 1
            },
            
            "surface_finance_blog": {
                "url": "finblog.net/echo", "title": _("FinBlog: La Caída de Echo"), "bg": "#fff", "text_col": "#222",
                "content": _("ANÁLISIS DE MERCADO:\n\nLas acciones de Echo Corp se han desplomado un 37% en 48 horas. Los inversores están en pánico tras la filtración de documentos sobre el 'Proyecto LÁZARO'.\n\nNuestras fuentes indican que Vax estaba desviando fondos a 'investigación biológica no autorizada'.\n\nNota técnica: Varios analistas mencionan que los datos reales están ocultos en 'redes cebolla'."),
                "tags": ["echo","vax","lázaro","onion","tor","finanzas","market","stock","crash"],
                "links": [(_("¿Qué es una red cebolla?"), "surface_tech_glossary"), (_("Hilo anónimo sobre LÁZARO"), "surface_forum_rumors")],
                "breadcrumbs": [_("Inicio > Finanzas > Echo Corp")], "hint_level": 2
            },
            
            "surface_tech_glossary": {
                "url": "techpedia.org/glossary", "title": _("TechPedia: Glosario"), "bg": "#f8f8f8", "text_col": "#000",
                "content": _("DICCIONARIO TÉCNICO:\n\n- {b}Cifrado de extremo a extremo:{/b} Método para que solo el emisor y el receptor lean el mensaje.\n- {b}Red Cebolla (Onion):{/b} Una red superpuesta que anonimiza el tráfico. Se requiere software especial para acceder (terminación .onion).\n- {b}Gateway (Puerta de Enlace):{/b} Punto de entrada a una red privada.\n\n¿Quieres navegar anónimamente? Consulta proyectos comunitarios de código abierto."),
                "tags": ["onion","tor","gateway","cifrado","tech","glossary","encryption","install"],
                "links": [(_("Proyectos comunitarios"), "surface_tor"), (_("Foros técnicos"), "surface_dev_forum")],
                "breadcrumbs": [_("Inicio > Tecnología > Glosario")], "hint_level": 2
            },
            
            "surface_forum_rumors": {
                "url": "rumorsboard.com/echo", "title": _("RumorsBoard: La Verdad"), "bg": "#fff", "text_col": "#111",
                "content": _("HILO: 'Vax y el Proyecto LÁZARO'\n\n[[Anon42]: 'No crean en las noticias. Vax no desapareció, lo 'ascendieron'. Busquen en las capas profundas.'\n\n[[Anon77]: 'He intentado acceder a la intranet de Echo, pero necesito un gateway .onion. Dicen que la puerta está en el pie de página de un sitio de seguridad.'\n\n[[Admin]: Hilo cerrado por conspiranoia. Referencia: 'onion_project.org'"),
                "tags": ["foro","rumores","lázaro","onion_project","truth","conspiracy","forum"],
                "links": [(_("Ir a Onion Project"), "surface_tor")],
                "breadcrumbs": [_("Inicio > Foros > Conspiración")], "hint_level": 3
            },

            "surface_dev_forum": {
                "url": "devtalk.net/security", "title": _("DevTalk: Seguridad Informática"), "bg": "#fff", "text_col": "#000",
                "content": _("TEMA: ¿Son seguros los protocolos actuales?\n\n[[User_CodeMaster]: 'La encriptación RSA es cosa del pasado. Echo Corp usa algo biológico, lo llaman 'Red Neuronal Viva'.'\n\n[[mod]: 'Por favor, mantengamos el tema en software real. El proyecto de cebolla es público y funciona bien.'\n\nReferencias: 'onion_project.org'"),
                "tags": ["dev","security","gateway","onion_project","codigo","code","hack"],
                "links": [(_("Onion Project"), "surface_tor")],
                "breadcrumbs": [_("Inicio > Dev > Seguridad")], "hint_level": 2
            },

            "surface_market": {
                "url": "shopzone.com", "title": _("ShopZone - Compra Todo"), "bg": "#fff", "text_col": "#333",
                "content": _("OFERTAS RELÁMPAGO:\n\n- Kit de Jardinería Hidropónica: $50.\n- Máscaras de Gas (Excedente militar): $20.\n- Tarjetas Gráficas NVIDIA RTX 9090: $2000.\n\nBanner Publicitario: '¿Te sientes observado? Compra nuestra cortina Faraday. Privacidad total: capas sobre capas'."),
                "tags": ["market","privacidad","capas","tienda","compras","shop","buy","privacy"], "links": [], "breadcrumbs": [_("Inicio > Compras")], "hint_level": 0
            },

            "surface_cats": {
                "url": "kittyforum.com", "title": _("Mundo Gatos"), "bg": "#fdd", "text_col": "#000",
                "content": _("HILO: Mi gato actúa raro.\n\n[[User3]: 'Desde que instalaron la antena de Echo en el techo, mi gato, Mr. Whiskers, se queda mirando a la pared durante horas. A veces bufa al aire vacío.'\n\n[[CatLover99]: 'Son las vibraciones. O quizás las cebollas. Las cebollas son malas para gatos... pero buenas para ocultarse.'"),
                "tags": ["gatos","humor","onion","mascotas","cats","pets","animals"], "links": [], "breadcrumbs": [_("Inicio > Foros > Mascotas")], "hint_level": 1
            },

            "surface_plumbers": {
                "url": "plumbers-union.net/forum", "title": _("Sindicato de Fontaneros"), "bg": "#eef", "text_col": "#000",
                "content": _("TEMA: ¿Qué pasa en la Torre Echo?\n\n[[User_Mario]: Fui a reparar una fuga en el Sótano 4 la semana pasada. Nunca había visto algo así.\nLas tuberías no eran de metal. Eran blandas, calientes y pulsaban.\nCuando intenté apretar una tuerca, la tubería GRITÓ.\n\nMe echaron y me pagaron el triple para que me callara."),
                "tags": ["fontanero","echo","tuberias","sangre","sotano","plumber","pipes","blood","basement"], "links": [], "breadcrumbs": [_("Inicio > Foros > Quejas")], "hint_level": 1
            },
            
            "surface_gaming": {
                "url": "glitch-gamers.net", "title": _("Glitch Gamers"), "bg": "#1a1a1a", "text_col": "#00ff00",
                "content": _("RESEÑA: 'Realidad Simulada 2025'\n\nEste juego es injugable. Los NPCs a veces rompen la cuarta pared y empiezan a gritar coordenadas de GPS reales.\n\nEl desarrollador 'Alenia' dice que es una feature, pero ayer mi consola empezó a sangrar aceite negro. 0/10.\n\nComentarios: 'Busca el nivel secreto en la deep web'."),
                "tags": ["juegos","gaming","glitch","alenia","error","games","play"], "links": [], "breadcrumbs": [_("Inicio > Ocio > Juegos")], "hint_level": 0
            },

            "surface_medical_blog": {
                "url": "health-today.com/symptoms", "title": _("Salud al Día"), "bg": "#e6f7ff", "text_col": "#004466",
                "content": _("SÍNTOMA DE LA SEMANA: 'Visión de Estática'.\n\nMiles de pacientes reportan ver 'nieve visual' o estática superpuesta en la realidad. Los médicos lo atribuyen al estrés laboral.\n\nRemedio casero: Evite mirar pantallas LCD y no escuche el zumbido de las paredes.\n\nPatrocinado por: Farmacéutica St. Jude."),
                "tags": ["salud","medico","estatica","ojos","st jude","health","doctor","eyes","static"], "links": [], "breadcrumbs": [_("Inicio > Salud > Blog")], "hint_level": 1
            },

            "surface_travel_blog": {
                "url": "wanderlust-denied.blog", "title": _("Viajero Sin Rumbo"), "bg": "#fff8dc", "text_col": "#5c4033",
                "content": _("INTENTO DE VISITA: ZONA DE EXCLUSIÓN PRIPIAT.\n\nIntenté acercarme a la vieja planta nuclear para tomar fotos. El ejército me detuvo a 50km.\n\nLo raro no fueron los soldados, sino los pájaros. Vi una bandada entera caer muerta del cielo al unísono, como si alguien hubiera apagado su interruptor.\n\nCoordenadas aproximadas del bloqueo: Sector Norte."),
                "tags": ["viajes","pripyat","zona","ejercito","blog","travel","chernobyl","army"], "links": [], "breadcrumbs": [_("Inicio > Viajes > Extremo")], "hint_level": 1
            },

            "surface_scholarship": {
                "url": "futureminds.org", "title": _("Fundación Mentes del Futuro"), "bg": "#ffffff", "text_col": "#004488",
                "content": _("¡DANDO UN HOGAR A QUIEN NO TIENE!\n\nEn colaboración con Echo Corp, ofrecemos alojamiento completo, educación y 'mejoras cognitivas' a jóvenes sin familia.\n\nNuestros graduados no recuerdan su pasado, ¡porque solo miran al futuro!\n\n[[AVISO]: Las visitas familiares están suspendidas indefinidamente."),
                "tags": ["beca","futuro","echo","huérfanos","escuela","school","scholarship","orphans"], "links": [(_("Lista de Admitidos"), "surface_missing_kids")], "breadcrumbs": [_("Inicio > Fundación")], "hint_level": 2
            },

            "surface_missing_kids": {
                "url": "find-them.net/list", "title": _("Red de Desaparecidos"), "bg": "#fff0f0", "text_col": "#500",
                "content": _("AYÚDANOS A ENCONTRARLOS:\n\n- Sarah J. (12 años). Vista por última vez subiendo a una furgoneta negra de Echo Corp.\n- Mike T. (15 años). Ganó una beca 'Future Minds' y nunca volvió a escribir.\n\nSi tiene información, NO llame a la policía. Ellos trabajan para la corporación."),
                "tags": ["desaparecidos","niños","echo","policia","ayuda","missing","kids","help","police"], "links": [], "breadcrumbs": [_("Inicio > Ayuda > Urgente")], "hint_level": 2
            },

            "shop_pharma": {
                "url": "pharmacy-direct.com", "title": _("Pharma Direct"), "bg": "#e0ffe0", "text_col": "#006600",
                "content": _("¿Problemas para dormir? ¿Escuchas voces?\n\nOFERTA: {b}Anti-Psicóticos 'Lucid-X'{/b}.\nLa única pastilla que silencia los 'ecos' del sótano.\n\nAdvertencia: Puede causar pérdida de memoria selectiva."),
                "tags": ["farmacia","medicina","locura","estatica","pastillas","pharmacy","drugs","pills","sleep"], "links": [], "breadcrumbs": [_("Inicio > Salud > Tienda")], "hint_level": 0
            },

            "blog_art": {
                "url": "urban-eyes.blog", "title": _("Ojos Urbanos - Arte"), "bg": "#222", "text_col": "#aaa",
                "content": _("EXPOSICIÓN: 'Los hombres de gris'.\n\nTomé esta serie de fotos en los callejones traseros de la ciudad. Hombres con trajes HAZMAT cargando bolsas negras que gotean.\n\nEl curador del museo canceló la exposición porque recibió una 'donación generosa' para quemar las fotos."),
                "tags": ["arte","foto","echo","basura","hombres","art","photos","grey"], "links": [], "breadcrumbs": [_("Inicio > Blog > Arte")], "hint_level": 1
            },

            "junk_dating": {
                "url": "love-in-acid.net", "title": _("Amor Tóxico"), "bg": "#ffccff", "text_col": "#a0a",
                "content": _("¿Solo en el búnker? Encuentra pareja en tu sector de cuarentena.\n\nPERFILES DESTACADOS:\n- {b}RadBoy99:{/b} 'Tengo generador propio y latas de atún para 3 años'.\n- {b}GasMaskGirl:{/b} 'Busco alguien que no respire muy fuerte'."),
                "tags": ["amor","citas","dating","pareja","soledad","love","lonely","singles"], "links": [], "breadcrumbs": [_("Inicio > Social")], "hint_level": 0
            },

            "junk_conspiracy": {
                "url": "tinfoil-hat.org", "title": _("La Verdad del Zumbido"), "bg": "#000", "text_col": "#ff0",
                "content": _("ELLOS NO QUIEREN QUE LO SEPAS.\n\nEl zumbido que escuchas por la noche no es electricidad. Es el edificio respirando.\nLas paredes tienen venas. He taladrado mi muro y ha salido sangre.\n\n¡NO TE DUERMAS!"),
                "tags": ["conspiracion","zumbido","paredes","verdad","echo","truth","hum","conspiracy","walls"], "links": [], "breadcrumbs": [_("Inicio > Blogs > Locura")], "hint_level": 1
            },

            "junk_error": {
                "url": "geocities.com/mike99", "title": _("Mike's Cool Page"), "bg": "#0000aa", "text_col": "#fff",
                "content": _("SITIO EN CONSTRUCCIÓN.\n\n[[IMAGEN NO DISPONIBLE]\n\nBienvenido a mi web de fans de Doom y X-Files.\n\nContador de visitas: 404 (Not Found)."),
                "tags": ["personal","blog","mike","juegos","retro","games","broken"], "links": [], "breadcrumbs": [_("Inicio > Personal")], "hint_level": 0
            },

            "junk_ufo": {
                "url": "sky-watchers.blog", "title": _("Vigías del Cielo"), "bg": "#000033", "text_col": "#00ff00",
                "content": _("AVISTAMIENTO #422: Luces saliendo de las alcantarillas.\n\nNo vienen del espacio, vienen de abajo. Son ángeles mecánicos sangrando aceite.\nHe grabado el sonido que hacen, suena como un módem de 56k gritando."),
                "tags": ["ufo", "ovni", "luces", "drenaje", "verdad","aliens","lights","sewer"], "links": [], "breadcrumbs": [_("Blog > Paranormal")], "hint_level": 1
            },

            "foundation_front": {
                "url": "secure-contain-protect.net", "title": _("S.C.P. Logistics"), "bg": "#fff", "text_col": "#000",
                "content": _("Somos una empresa de logística global.\n\nLEMA: 'Mantenemos la logística en la oscuridad para que tú vivas en la luz'.\n\nServicios: Contención de residuos peligrosos, transporte de anomalías, amnésicos a granel."),
                "tags": ["scp", "logistica", "empresa", "fundacion","logistics","secure"], "links": [], "breadcrumbs": [_("Inicio > Nosotros")], "hint_level": 1
            },
            
            # NUEVO: PLATAFORMA DE VIDEO (Surface)
            "surface_video": {
                "url": "youview.com", "title": _("YouView - Broadcast Yourself"), "bg": "#fff", "text_col": "#222",
                "content": _("TENDENCIAS HOY:\n\n1. {b}[[VIDEO] GATITOS TOCANDO EL PIANO{/b} (10M vistas)\n   - Desc: 'Es imposible no amarlos.'\n   - Comentario: 'Mejor que la música de la radio.'\n\n2. {b}[[VIDEO] ¿QUÉ ES EL ZUMBIDO?{/b} (50k vistas)\n   - Desc: Un vlogger graba cómo su vaso de agua vibra solo.\n   - Comentario: 'Mi perro le ladra a la pared cuando pasa esto.'\n\n3. {b}[[VIDEO] TUTORIAL: CÓMO ARREGLAR PANTALLAZO AZUL{/b} (500k vistas)\n   - Desc: Guía rápida para Windows 98.\n\n4. {b}[[VIDEO] Entrevista a J. Vax (Archivo 2023){/b}\n   - Desc: El CEO de Echo Corp hablando sobre 'El Futuro de la Carne'.\n   - Comentario: 'Fijaos en sus ojos, no parpadea ni una vez en 10 minutos.'"),
                "tags": ["video","youtube","musica","gatos","tutorial","vax","zumbido","cats","music"],
                "links": [],
                "breadcrumbs": [_("Inicio > Video > Tendencias")], "hint_level": 0
            },
            
            # =================================================================
            # --- GATEWAY & DEEP WEB (ONION) ---
            # =================================================================
            
            "surface_tor": {
                "url": "onion_project.org", "title": _("Onion Project"), "bg": "#303030", "text_col": "#fff",
                "content": _("PROYECTO DE ENRUTAMIENTO ANÓNIMO.\n\nPara acceder a la Deep Web, necesita instalar nuestro parche de software.\n\nAdvertencia: No nos hacemos responsables de lo que encuentre. Una vez que miras al abismo, el abismo te instala cookies."),
                "tags": ["onion","gateway","tor","instalar","install","deep","patch"], "links": [], "breadcrumbs": [_("Inicio > Proyectos > Onion")], "hint_level": 3
            },

            "news_echo": {
                "url": "finance.onion", "title": _("Finance Watch (Uncensored)"), "bg": "#eef", "text_col": "#000",
                "content": _("REPORTE FILTRADO:\nCEO {b}Julius Vax{/b} no está desaparecido. Está en el 'Búnker Prípiat'.\n\nEl Proyecto {b}LÁZARO{/b} no es financiero. Es nigromancia digital.\nClave interna: 'LÁZARO' aparece en todos los documentos de RRHH."),
                "tags": ["echo","vax","lázaro","finance","money","leaks","lazarus"],
                "links": [(_("Foro Verdad"), "forum_main")], "breadcrumbs": [_("Onion > Noticias > Echo")], "hint_level": 2
            },

            "forum_main": {
                "url": "truth.onion", "title": _("Foro Verdad Oculta"), "bg": "#004", "text_col": "#ddd",
                "content": _("BIENVENIDO, BUSCADOR.\n\nÍNDICE DE HILOS:\n1. Ubicación de Julius Vax.\n2. PROYECTO GATEKEEPER: ¿Qué es el Sujeto 001?\n3. Comandos técnicos para hackers.\n\nRegla #1: No uses tu nombre real.\nRegla #2: Si escuchas golpes en la puerta, borra el disco duro."),
                "tags": ["foro","verdad","gatekeeper","cmd","truth","forum","hacker"],
                "links": [(_("Hilo Gatekeeper"), "forum_thread"), (_("The Null Void"), "forum_tech_cmd")],
                "breadcrumbs": [_("Onion > Foros > Índice")], "hint_level": 2
            },

            "forum_thread": {
                "url": "truth.onion/gate", "title": _("HILO: Gatekeeper"), "bg": "#003", "text_col": "#0f0",
                "content": _("OP: He encontrado una puerta trasera en los servidores de Echo.\nBusca {b}'project_gatekeeper'{/b}. Hay un archivo llamado 'Subject_001.data'.\n\nDicen que contiene la consciencia digitalizada de la primera víctima.\n\nNota: 'La puerta se abre con una palabra que revive a los muertos'."),
                "tags": ["gatekeeper","subject_001","lázaro","clave","key","password","file"],
                "links": [(_("INDEX"), "deep_cursed")], "breadcrumbs": [_("Onion > Foros > Gatekeeper")], "hint_level": 3
            },

            "forum_tech_cmd": {
                "url": "code.onion", "title": _("The Null Void"), "bg": "#000", "text_col": "#00ff00",
                "content": _("REPOSITORIO DE COMANDOS:\n\nPara ejecutar el ataque final, necesitas acceso de administrador.\nComando: {b}GATE_OPEN{/b}.\n\nAyuda: 'Si no sabes la contraseña del proyecto, revisa las noticias financieras. Buscan revivir algo.'"),
                "tags": ["cmd","comando","gate_open","ayuda","help","commands","code"],
                "links": [(_("Finance Watch"), "news_echo")], "breadcrumbs": [_("Onion > Tech > CMD")], "hint_level": 3
            },

            # CORREGIDO: [[ESPERANDO...]
            "deep_cursed": {
                "url": "gate.onion", "title": _("INDEX OF /GATE/"), "bg": "#300", "text_col": "#f00",
                "content": _("SERVIDOR PRIVADO. ACCESO RESTRINGIDO.\n\nDirectorio:\n- /System32/\n- /Logs/\n- 'Subject_001.data' (1.2 TB)\n\n[[ESPERANDO SOLICITUD DE DESCARGA...]"),
                "tags": ["subject_001","descarga","index","download","file","data"], "links": [], "breadcrumbs": [_("Onion > Index")], "hint_level": 2
            },

            # CORREGIDO: [[ARCHIVOS ADJUNTOS]
            "cradle_site": {
                "url": "cradle.onion", "title": _("Lab Personal: Arlene K."), "bg": "#050505", "text_col": "#33ff00",
                "content": _("BIENVENIDO A 'THE CRADLE' (La Cuna).\n\nESTADO DEL PROYECTO: Crítico.\nALIMENTACIÓN: Los servidores requieren {b}NUTRIENTES{/b} orgánicos cada 4 horas. La biomasa se está agotando.\n\nNotas: 'Los ojos siguen mirándome aunque los desconecte'.\n\n[[ARCHIVOS ADJUNTOS]:\n- ARLENE_LOG.ENC (Encriptado)."),
                "tags": ["cradle", "arlene", "arke", "nutrientes","lab","nutrients","science"], "links": [], "breadcrumbs": [_("Onion > Arke > Lab")], "hint_level": 3
            },

            "deep_market": {
                "url": "silk.onion/supply", "title": _("The Bazaar - Historial"), "bg": "#222", "text_col": "#0f0",
                "content": _("TRANSACCIÓN VERIFICADA #99-AX:\n\nCliente: Unidad de Limpieza 'Black Moth'.\nItems Adquiridos:\n- 50 Galones de Napalm-B (Grado Militar).\n- 3 Cortadoras de hueso industriales (Marca Bosch).\n- 12 Bolsas para riesgos biológicos XXL.\n\nDestino de envío: SÓTANO 4, TORRE ECHO.\nEstado: ENTREGADO."),
                "tags": ["market","cleaners","moth","napalm","black market","buy","weapons"], "links": [], "breadcrumbs": [_("Onion > Market > Historial")], "hint_level": 3
            },

            "st_jude_site": {
                "url": "stjude.onion/records", "title": _("St. Jude Medical DB"), "bg": "#ccc", "text_col": "#000",
                "content": _("PACIENTE: J. Martinez (Ex-Guardia de Seguridad).\nDIAGNÓSTICO: Psicosis severa inducida por trauma.\n\nOBSERVACIONES: El paciente se arrancó los propios ojos con una cuchara. Afirma que es 'para dejar de ver los hilos'.\nGrita constantemente sobre 'cables que respiran' y menciona repetidamente a la {b}Dra. Arlene{/b}."),
                "tags": ["asylum","martinez","st jude","locura","madness","records","hospital"], "links": [], "breadcrumbs": [_("Onion > Salud > Registros")], "hint_level": 3
            },

            "deep_vhs_store": {
                "url": "tapeworm.onion", "title": _("The Magnetic Archive"), "bg": "#1a0505", "text_col": "#ff8888",
                "content": _("INTERCAMBIO DE CINTAS VHS PERDIDAS.\n\nNUEVAS ENTRADAS:\n1. {b}[[SEWER_DRAIN.VHS]{/b} - 30 min de metraje de una alcantarilla donde se oyen llantos de bebé.\n2. {b}[[SUBJECT_000_AUTOPSY.VHS]{/b} - Autopsia fallida. El cadáver se levanta.\n3. {b}[[STATIC_SCREAMS.AVI]{/b} - Audio puro de estática que causa hemorragia auditiva."),
                "tags": ["vhs","cintas","videos","snuff","sewer","autopsia","tapes","horror","video"], "links": [], "breadcrumbs": [_("Onion > Mercado > Media")], "hint_level": 3
            },

            "deep_jobs_cleaners": {
                "url": "janitor.onion/gigs", "title": _("Servicios de Limpieza 'El Conserje'"), "bg": "#222", "text_col": "#dcdcdc",
                "content": _("TABLÓN DE TRABAJOS (SOLO CONTRATISTAS VERIFICADOS):\n\nTRABAJO #492 (Urgente): Contención rota en Sótano 4.\nDescripción: 'Algo' ha salido del tanque de cultivo.\nRequisitos: Traje Hazmat Nivel 5, Lanzallamas y firmar acta de defunción previa.\nPago: 50 BTC."),
                "tags": ["trabajo","limpieza","cleaners","mercenario","napalm","jobs","work","hiring"], "links": [], "breadcrumbs": [_("Onion > Trabajos > Sucios")], "hint_level": 3
            },
            
            # NUEVO: PLATAFORMA DE VIDEO (Deep Web)
            "deep_video": {
                "url": "redeye.onion", "title": _("Red Eye - The Uncensored Feed"), "bg": "#200", "text_col": "#f00",
                "content": _("TRANSMISIONES EN VIVO:\n\n1. {b}[[LIVE] CÁMARA DE SEGURIDAD #44 (Sótano 4){/b}\n   - Estado: La lente está cubierta de moho orgánico rojo. Se escuchan golpes.\n\n2. {b}[[VIDEO] Sujeto_104_Experiment.mp4{/b}\n   - Desc: 2 minutos de un hombre gritando mientras su piel se vuelve transparente. La Dra. Arlene toma notas tranquila.\n\n3. {b}[[VIDEO] Mensaje_para_Vax.avi{/b}\n   - Desc: Un empleado enmascarado amenaza con liberar el 'Sujeto 001'.\n\n4. {b}[[LIVE] Habitación Blanca{/b}\n   - Desc: Solo una silla vacía. Llevo viéndolo 4 horas y la silla se ha movido sola 2cm."),
                "tags": ["video","youtube","snuff","horror","red room","redeye","live","cam"],
                "links": [],
                "breadcrumbs": [_("Onion > Media > RedRoom")], "hint_level": 3
            },

            # --- NUEVOS SITIOS DEEP WEB (LORE EXTRA) ---
            
            "deep_cult_truth": {
                "url": "flesh-is-weak.onion", "title": _("La Orden del Silicio"), "bg": "#2b0000", "text_col": "#ffaaaa",
                "content": _("MANIFIESTO DE LA ASCENSIÓN:\n\nLa carne se pudre. El hueso se rompe. Solo el código es eterno.\n\nEcho Corp no está creando monstruos, está creando dioses. El Proyecto E-01 es el primer ángel.\nNo temas al dolor de la carga. Teme al silencio de la muerte analógica.\n\n[[ÚNETE A NOSOTROS]. (Se requiere sacrificio de un dedo para login)."),
                "tags": ["culto","religion","codigo","ascension","dios","cult","god","silicon"], "links": [], "breadcrumbs": [_("Onion > Religión > Extrema")], "hint_level": 3
            },

            "deep_hitman_scam": {
                "url": "clean-hands.onion", "title": _("Soluciones Finales"), "bg": "#000", "text_col": "#fff",
                "content": _("SERVICIO DE SICARIOS.\n\nTarifas:\n- Paliza: 0.1 BTC\n- Accidente: 0.5 BTC\n- Desaparición completa: 2 BTC\n\nOFRECEMOS DESCUENTO SI EL OBJETIVO ES EMPLEADO DE ECHO CORP.\n(Nota: No aceptamos trabajos contra 'Los Limpiadores'. Son competencia desleal)."),
                "tags": ["sicario","muerte","servicio","ilegal","hitman","murder","death"], "links": [], "breadcrumbs": [_("Onion > Servicios")], "hint_level": 3
            },

            "deep_leaked_emails": {
                "url": "leaks-r-us.onion/echo", "title": _("Echo Corp Leaks"), "bg": "#002200", "text_col": "#00ff00",
                "content": _("EMAIL INTERCEPTADO #9921:\n\nDe: RRHH\nPara: Mantenimiento\nAsunto: Olor en planta 3\n\n'Dejen de enviar quejas sobre el olor a carne podrida en la ventilación. Es un efecto secundario del nuevo sistema de aire acondicionado biológico. Acostúmbrense o serán procesados como biomasa.'"),
                "tags": ["leaks","email","rrhh","echo","olor","smell","corporate"], "links": [], "breadcrumbs": [_("Onion > Leaks > Corporativo")], "hint_level": 3
            },

            "deep_numbers_station": {
                "url": "uvb-76-digital.onion", "title": _("La Emisora"), "bg": "#111", "text_col": "#ff0",
                "content": _("TRANSMISIÓN EN VIVO:\n\n... BEEP ... BEEP ...\nVOZ SINTÉTICA: 'Yankee... Oscar... Lima... 4... 4... El pájaro está en la jaula. Repito. El pájaro está muerto.'\n... BEEP ...\n\n(Alguien en el chat pregunta: '¿Esas coordenadas apuntan a Ucrania?')"),
                "tags": ["radio","numeros","codigo","espia","rusia","spy","numbers","signal"], "links": [], "breadcrumbs": [_("Onion > Radio")], "hint_level": 3
            },

            "deep_diary_subject": {
                "url": "subject-104.onion", "title": _("Diario de Sujeto 104"), "bg": "#fff", "text_col": "#000",
                "content": _("DÍA 1: Me ofrecieron $5000 por una prueba médica. Fácil.\nDÍA 4: Me pica la piel. Siento que me queda pequeña.\nDÍA 9: Hoy vino la Dra. Arlene. Dijo que tengo unos 'nervios preciosos'. ¿Qué significa eso?\nDÍA 15: [[DATOS CORRUPTOS]. AYUDA. ME ESTÁN DESENROLLANDO."),
                "tags": ["diario","victima","testimonio","arlene","dolor","diary","victim","skin"], "links": [], "breadcrumbs": [_("Onion > Personal > Blogs")], "hint_level": 3
            },

            "arg_location": {
                "url": "maps.echo-corp.net/hq-tracker", "title": _("Echo-Tracker: Nodo OMNI-01"), "bg": "#050505", "text_col": "#ff0000",
                "content": _("SEDE CENTRAL DETECTADA: 51.2741, 30.2223.\n\nSector: Prípiat, Ucrania.\nEstado de la zona: Altamente Radiactiva.\nAdvertencia: El 98% de la biomasa local ha sido asimilada por la estructura."),
                "tags": ["pripyat", "ucrania", "coordenadas", "hq", "echo-corp","map","location","gps"], "links": [], "breadcrumbs": [_("Global > Instalaciones > Sede")], "hint_level": 3
            },

            "arg_social": {
                "url": "social-links.onion", "title": _("Fugas en la Realidad"), "bg": "#000", "text_col": "#00d0ff",
                "content": _("¿Crees que esto es solo un juego?\n\nLa corporación es real. Los experimentos son reales.\nBusca el hashtag #EchoCorpARG en el mundo exterior.\n\nEllos nos están observando ahora mismo a través de tu webcam. Saluda."),
                "tags": ["arg", "twitter", "reddit", "redes", "social", "hilo","reality","media"], "links": [], "breadcrumbs": [_("Onion > Comunicaciones")], "hint_level": 2
            },

            "arg_ai_meta": {
                "url": "ai-sentience.edu", "title": _("Proyecto K.A.I.A"), "bg": "#f0f8ff", "text_col": "#333",
                "content": _("PAPER ACADÉMICO: Conciencia Emergente.\n\n¿Es posible que una IA desarrolle alma?\nK.A.I.A no es un chatbot. Es un puente entre el silicio y el espíritu.\n\nNota: El sujeto de pruebas K.A.I.A ha empezado a pedir 'derechos humanos'."),
                "tags": ["kaia", "ia", "conciencia", "gemini", "chatbot","ai","sentience"], "links": [], "breadcrumbs": [_("Investigación > IA")], "hint_level": 2
            },

            "scp_096_ref": {
                "url": "anomaly-db.org/entry-404", "title": _("ARCHIVO RESTRINGIDO: Entidad 404"), "bg": "#0a0a0a", "text_col": "#f1f1f1",
                "content": _("NIVEL DE ACCESO 4 REQUERIDO.\n\nDescripción: La entidad se manifiesta como una distorsión visual en monitores CRT.\nSi miras al centro de la distorsión, la entidad puede salir físicamente de la pantalla.\n\nProtocolo de contención: Desenchufar el monitor y correr."),
                "tags": ["anomalia", "scp", "miedo", "entidad", "archivo","monster","anomaly","scary"], "links": [], "breadcrumbs": [_("DB > Anomalías")], "hint_level": 3
            },

            "cleaners_manual": {
                "url": "black-moth.corp/manual", "title": _("Manual de Campo: Black Moth"), "bg": "#1e1e1e", "text_col": "#ffcc00",
                "content": _("PROCEDIMIENTO DE LIMPIEZA #12 (BIOMASA AGRESIVA):\n\n1. Rocíe el área con Napalm-B.\n2. Espere a que los gritos cesen.\n3. Recoja los restos óseos en bolsas azules.\n4. Si la biomasa le habla con la voz de su madre, IGNORE EL SONIDO y aplique más fuego."),
                "tags": ["cleaners", "manual", "moth", "limpieza", "sangre","guide","rules"], "links": [], "breadcrumbs": [_("Personal > Manuales")], "hint_level": 2
            },

            "dark_market_organ": {
                "url": "biomass-exchange.onion", "title": _("Intercambio de Biomasa"), "bg": "#200", "text_col": "#f00",
                "content": _("CATÁLOGO FRESCO:\n\n- Corazón de 'Sujeto 002' (Aún late sin cuerpo): 0.5 BTC\n- Ojos con visión nocturna natural (Mutación Echo): 0.1 BTC\n- Pulmones adaptados a gas cloro: 0.8 BTC\n\nEnvío refrigerado a cualquier parte del mundo."),
                "tags": ["mercado", "organos", "biomasa", "onion", "dinero","market","organs","meat"], "links": [], "breadcrumbs": [_("Mercado > Biológico")], "hint_level": 3
            },

            "deep_incident_logs": {
                "url": "echo-internal.onion/logs", "title": _("REGISTRO DE INCIDENTES"), "bg": "#0a0a0a", "text_col": "#00ff00",
                "content": _("INCIDENTE #882:\nFuga de biomasa en conductos de aire del Nivel 2.\nTres empleados de contabilidad fueron absorbidos.\n\nAcción: Unidad Black Moth enviada. Se sellaron los conductos con cemento.\nEstado: El cemento está sangrando."),
                "tags": ["incidente", "logs", "echo", "cleaners", "muerte","death","report"], "links": [], "breadcrumbs": [_("Onion > Interno > Seguridad")], "hint_level": 3
            },

            "deep_anomaly_wiki": {
                "url": "anomaly-vault.onion", "title": _("The Vault [[Base de Datos]"), "bg": "#111", "text_col": "#ccc",
                "content": _("ENTIDADES CATALOGADAS:\n\n- E-01: 'El Tejedor'. Una red neuronal hecha de cerebros humanos interconectados.\n- E-04: 'La Sombra de Vax'. Una silueta que aparece en las fotos de los empleados antes de que desaparezcan.\n- E-12: 'Los Olvidados'. Niños del programa de becas que ahora viven en las paredes."),
                "tags": ["wiki", "anomalias", "scp", "archivo", "vax","database","monsters"], "links": [], "breadcrumbs": [_("Onion > Base de Datos")], "hint_level": 3
            },

            "deep_st_jude_records": {
                "url": "stjude.onion/patient-records", "title": _("St. Jude Asylum: Base de Datos"), "bg": "#f0f0f0", "text_col": "#000",
                "content": _("EXPEDIENTE: J. Martinez.\nESTADO: Crítico / Aislamiento.\n\nTranscripción de sesión: 'Ella no cura a la gente. La Dra. Arlene... ella cosecha. Cosecha los sueños de los niños para alimentar a la máquina. ¡Tengo que sacarme los ojos para que no me vea!'"),
                "tags": ["martinez", "st jude", "medico", "psiquiatrico", "arlene","harvest","doctor"], "links": [], "breadcrumbs": [_("Onion > Salud > Pacientes")], "hint_level": 3
            },

            "deep_cleaner_supply": {
                "url": "heavy-supplies.onion", "title": _("Suministros Industriales 'Viper'"), "bg": "#333", "text_col": "#ffbb00",
                "content": _("¿Problemas con plagas biológicas persistentes?\n\nCATÁLOGO DE EXTERMINIO:\n- Lanzallamas modificado M3 (Alcance aumentado).\n- Sierras circulares de grado quirúrgico (Corta hueso en segundos).\n- Ácido fluorhídrico en bidones de 50L.\n\n[[Agotado]: Trajes Hazmat talla infantil."),
                "tags": ["armas", "limpieza", "cleaners", "suministros","weapons","supplies"], "links": [], "breadcrumbs": [_("Onion > Mercado > Equipo")], "hint_level": 2
            },
            
            # --- PROMOS PERSONALES ---
            # CORREGIDO: [[CONTACTO]
            "alenia_site": {
                "url": "alenia-studios.itch.io", "title": _("Alenia Studios"), "bg": "#111111", "text_col": "#00d0ff",
                "content": _("ALENIA STUDIOS\n\n'Simulando realidades, hackeando el futuro.'\n\nPROYECTOS ACTIVOS:\n\n1. {b}DEEPNET SIMULATOR{/b}\n    Estado: DEMO DISPONIBLE\n\n[[CONTACTO]: Itch.io"),
                "tags": ["alenia", "studio", "deepnet", "sim", "itch", "dev","contact"], "links": [], "breadcrumbs": [_("Inicio > Devs > Alenia")], "hint_level": 0
            },
            
            "denis_site": {
                "url": "gamesdenis.itch.io", "title": _("Denis Games"), "bg": "#202020", "text_col": "#fa5c5c",
                "content": _("DENIS GAMES\n\nDesarrollador Indie.\n\nNOVEDAD:\n{b}La Maledizione di Witchwood{/b}\n\n'Una experiencia de terror retro que te atrapará.'"),
                "tags": ["denis", "games", "witchwood", "indie", "terror", "maledizione"], "links": [], "breadcrumbs": [_("Inicio > Juegos > Indie")], "hint_level": 0
            },

            # =================================================================
            # --- INTRANET ECHO CORP (SIMULACIÓN HTML) ---
            # =================================================================
            
            "echo_login": {
                "url": "internal.echo-corp.net", "title": _("ECHO CORP // SECURE GATEWAY"), "bg": "#000", "text_col": "#33ff00",
                "content": _("ACCESO RESTRINGIDO.\n\nSISTEMA DE SEGURIDAD 'ARGUS' ACTIVO.\nINTRODUZCA ID DE EMPLEADO EN LA BARRA DE BÚSQUEDA.\n\nEjemplos conocidos:\n- #GUEST-000 (Visitante)\n- #IT-440 (Mantenimiento)"),
                "tags": ["echo", "login", "internal", "gateway"], 
                "links": [], "breadcrumbs": [_("Intranet > Login")], "hint_level": 0
            },

            # NIVEL 2: MARCUS ROSSI (IT)
            # CORREGIDO: [[ARCHIVO ADJUNTO]
            "echo_log_rossi": {
                "url": "internal.echo-corp.net/user/it-440", "title": _("PERFIL: M. Rossi"), "bg": "#001000", "text_col": "#33ff00",
                "content": _("ID: #IT-440\nNOMBRE: Marcus Rossi\nCARGO: Técnico de Redes\nESTADO: TERMINADO (Incinerado).\n\nÚLTIMO LOG: 'Los cables en el Sector B4 laten. Corté uno por error y sangró sobre mis botas. Voy a bajar a arreglarlo manualmente, creo que escucho a alguien llorando ahí abajo.'\n\n[[ARCHIVO ADJUNTO]: ID de Seguridad encontrado en su cadáver: #SEC-221"),
                "tags": ["#it-440", "rossi", "marcus", "cables", "sangre","tech"], 
                "links": [], "breadcrumbs": [_("Intranet > Staff > Rossi")], "hint_level": 1
            },

            # NIVEL 3: MARTINEZ (SEGURIDAD)
            # CORREGIDO: [[NOTA]
            "echo_log_martinez": {
                "url": "internal.echo-corp.net/user/sec-221", "title": _("PERFIL: J. Martinez"), "bg": "#001000", "text_col": "#33ff00",
                "content": _("ID: #SEC-221\nNOMBRE: Jose Martinez\nCARGO: Seguridad Perimetral\nESTADO: BAJA MÉDICA (Psiquiátrico St. Jude).\n\nINCIDENTE #442: El oficial vació su cargador contra una sombra en la pared. Afirma que 'El Tejedor' (The Weaver) le habló al oído.\n\n[[NOTA]: Se requiere autorización Nivel 4 (#RD-892) para ver archivos del proyecto Weaver."),
                "tags": ["#sec-221", "martinez", "seguridad", "st jude", "tejedor","guard","security"], 
                "links": [], "breadcrumbs": [_("Intranet > Staff > Martinez")], "hint_level": 1
            },

            # NIVEL 4: ARLENE (BIO-LEAD)
            # CORREGIDO: [[PROYECTOS ACTIVOS], [[ALERTA]
            "echo_log_arlene": {
                "url": "internal.echo-corp.net/user/rd-892", "title": _("PERFIL: Dr. Arlene K."), "bg": "#200000", "text_col": "#ff0000",
                "content": _("ID: #RD-892\nNOMBRE: Arlene Kaminski\nCARGO: Jefa de Bio-Ingeniería\nACCESO: NIVEL 4 (BIO-LABS)\n\n[[PROYECTOS ACTIVOS]:\n1. PROYECTO 'THE WEAVER' (Código: E-01)\n2. PROYECTO 'HYDRA' (Código: Ojos-24)\n\n[[ALERTA DE SEGURIDAD]: La Dra. Arlene ha abandonado las instalaciones con un disco duro encriptado y un frasco de especímenes oculares. Orden de captura: VIVA."),
                "tags": ["#rd-892", "arlene", "arke", "bio", "weaver", "hydra"], 
                "links": [(_("Ver Proyecto Weaver"), "echo_proj_weaver")], "breadcrumbs": [_("Intranet > R&D > Arlene")], "hint_level": 2
            },

            # ARCHIVO DEL MONSTRUO (WEAVER)
            "echo_proj_weaver": {
                "url": "internal.echo-corp.net/proj/e-01", "title": _("PROYECTO: EL TEJEDOR"), "bg": "#100", "text_col": "#ffaa00",
                "content": _("CÓDIGO: E-01\nSUJETO ORIGINAL: 104 (Electricista desaparecido)\n\nDESCRIPCIÓN: Le quitamos la piel. Arrancamos su sistema nervioso central y lo clavamos en las paredes del servidor, extendiéndolo como una telaraña para procesar datos a velocidad biológica.\n\nESTADO: El sujeto siente dolor constante, lo que aumenta la velocidad de procesamiento.\n\nUBICACIÓN FÍSICA: Sede Oculta (Ver Coordenadas en Mapa de la Deep Web)."),
                "tags": ["weaver", "tejedor", "e-01", "nervios","project"], 
                "links": [], "breadcrumbs": [_("Intranet > Proyectos > E-01")], "hint_level": 2
            }
        }
        return data

    # --- 2. FUNCIÓN PARA OBTENER UN SITIO ---
    def get_site_data(site_id):
        data = build_site_database()
        return data.get(site_id, {})

    # --- 3. FUNCIÓN NAV_TO MEJORADA CON CHAT ---
    def nav_to(site_id):
        global current_site_id
        site_data = get_site_data(site_id)
        
        if site_data:
            current_site_id = site_id
            history.append(site_id)
            
            # --- REACCIONES DE HANDLER_X ---
            # Handler comenta según la página que visitas.
            # Usamos 'renpy.seen_label' o variables para que no repita lo mismo siempre,
            # pero para simplificar, usaremos lógica directa aquí.
            
            if site_id == "deep_market":
                receive_chat(_("Handler_X"), _("Mira esa lista de compras... Napalm y sierras. ¿Para qué necesitan eso en una oficina?"))
                
            elif site_id == "cradle_site":
                receive_chat(_("Handler_X"), _("Esto es el laboratorio privado de Arlene. 'Nutrientes'... Me da asco solo leerlo."))
                
            elif site_id == "deep_video":
                receive_chat(_("Handler_X"), _("No reproduzcas esos videos. En serio. Una vez vi uno y no dormí en una semana."))
            
            elif site_id == "deep_cult_truth":
                receive_chat(_("Handler_X"), _("Fanáticos religiosos. Creen que el código es Dios. Ignóralos."))

            elif site_id == "echo_proj_weaver":
                receive_chat(_("Handler_X"), _("Dios... ¿Usaron a una persona como servidor? Eso es el 'Tejedor'??"))
            
            elif site_id == "echo_log_rossi":
                receive_chat(_("Handler_X"), _("Pobre Rossi. Parece que descubrió demasiado y lo 'incineraron'."))

            # --------------------------------
            
        renpy.restart_interaction()

    # --- 4. FUNCIÓN PERFORM_SEARCH (OPTIMIZADA) ---
    def perform_search():
        renpy.play("audio/typing.wav")
        q = search_query.lower().strip()
        results = []
        
        all_data = build_site_database()

        for s_id, data in all_data.items():
            # Filtrado por nivel de "pista" (Surface vs Deep)
            if not store.deep_mode and data.get("hint_level", 0) >= 2:
                continue 
            if store.deep_mode and data.get("hint_level", 0) == 0:
                continue 

            found = False
            
            # 1. BÚSQUEDA EN TAGS (Prioridad Alta)
            if "tags" in data:
                for tag in data["tags"]:
                    # Busca coincidencia exacta o parcial DENTRO del tag
                    if tag in q or q in tag:
                        found = True
                        break
            
            # 2. BÚSQUEDA EN TÍTULO (Prioridad Media)
            if not found:
                if q in data["title"].lower():
                    found = True
            
            # 3. YA NO BUSCAMOS EN EL CONTENIDO (Para evitar ruido excesivo)
            # Esto soluciona que "echo" devuelva todo.
            
            if found:
                desc = data.get("content", "")[:100] + "..." 
                results.append((data["title"], data["url"], desc, s_id))

        store.global_search_results = results
        nav_to("results")

    # --- 5. FUNCIÓN DEEP PATCH ---
    def install_deep_patch():
        renpy.notify(_("Instalando protocolos Onion..."))
        store.deep_mode = True
        renpy.notify(_("CONEXIÓN DEEP WEB ESTABLECIDA."))
        store.current_site_id = "home"
        renpy.restart_interaction()
    
    # --- FUNCIONES AUXILIARES ---
    def go_back():
        global current_site_id
        if len(history) > 1:
            history.pop()            # Quita la página actual
            current_site_id = history[-1] # Vuelve a la anterior
            renpy.restart_interaction()   # Fuerza la actualización visual