import io
import os
import random
import PySimpleGUI as sg
from PIL import Image

KEP_MAPPA = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "kepek"
)




autok = [
    {
        "kep": "trabant.jpg",
        "marka": "Trabant 601",
        "opciok": ["Moszkvics 408", "Lada 2101", "Trabant 601", "Wartburg 353"],
    },
    {
        "kep": "latvija.jpg",
        "marka": "Latvija",
        "opciok": ["Latvija", "Robur", "IFA W50", "Zuk"],
    },
    {
        "kep": "moszkvics.jpg",
        "marka": "Moszkvics 2140",
        "opciok": ["Peugeot", "Lada 2107", "Moszkvics 2140", "Zaporozsec"],
    },
    {
        "kep": "kispolski.jpg",
        "marka": "Fiat 126p",
        "opciok": ["Fiat 126p", "Fiat 125", "Lada 2105", "Volga M24"],
    },
    {
        "kep": "wartburg.jpg",
        "marka": "Wartburg",
        "opciok": ["Wartburg", "Trabant 601", "Lada 2103", "Moszkvics 412"],
    },
    {
        "kep": "lada2101.jpg",
        "marka": "Lada 2101",
        "opciok": ["Lada 2101", "Wartburg 353", "Skoda 100", "Volga M24"],
    },
    {
        "kep": "zaporozsec.jpg",
        "marka": "Zaporozsec",
        "opciok": ["Zaporozsec", "Moszkvics 2140", "Trabant 601", "Lada 2105"],
    },
    {
        "kep": "skoda100.jpg",
        "marka": "Škoda 100",
        "opciok": ["Škoda 100", "Fiat 126p", "Wartburg 353", "Zaporozsec"],
    },
    {
        "kep": "volga.jpg",
        "marka": "Volga M24",
        "opciok": ["Volga M24", "Latvija", "Moszkvics 2140", "Lada 2101"],
    },
    {
        "kep": "ifa.jpg",
        "marka": "IFA W50",
        "opciok": ["IFA W50", "Robur", "Zuk", "Latvija"],
    },
    {
        "kep": "fiat125.jpg",
        "marka": "Fiat 125",
        "opciok": ["Fiat 125", "Fiat 126p", "Lada 2107", "Skoda 100"],
    },
    {
        "kep": "moszkvics403.jpg",
        "marka": "Moszkvics 403",
        "opciok": ["Moszkvics 403", "Latvija", "Fiat 124", "Lada 2102"],
    },
    {
        "kep": "csepel.jpg",
        "marka": "Csepel D344",
        "opciok": ["Kraz", "Csepel D344", "Scania", "Rába"],
    },
    {
        "kep": "mtz50.jpg",
        "marka": "Mtz 50",
        "opciok": ["Zetor", "Mtz 50", "Mtz 80", "Steiger Rába"],
    },
    {
        "kep": "pannonia.jpg",
        "marka": "Pannónia",
        "opciok": ["Harley Dawidson", "Simson", "Jawa", "Pannónia"],
    },
        {
        "kep": "zil.jpg",
        "marka": "Zil 130",
        "opciok": ["Aro", "Kraz", "Zil 130", "Nysa"],
    },
        {
        "kep": "nysa.jpg",
        "marka": "Nysa",
        "opciok": ["Nysa", "Mercedes", "Ford", "Tavria"],
    },
        {
        "kep": "tavria.jpg",
        "marka": "Tavria",
        "opciok": ["Lada Samara", "Tavria", "Moszkvics Aleko", "Lada Niva"],
    },
        {
        "kep": "niva.jpg",
        "marka": "Lada Niva",
        "opciok": ["Toyota", "Lada Niva", "Pobeda", "Rába"],
    },
        {
        "kep": "raba.jpg",
        "marka": "Rába S22",
        "opciok": ["Rába S22", "Liaz", "Rába U22", "Steiger Rába"],
    },
]

pontszam = 0
aktualis_auto = 0
jatek_vege = False



def kep_betoltese(kep_utvonal):
    kep = Image.open(kep_utvonal).convert("RGB")
    kep.thumbnail((520, 260))
    adat = io.BytesIO()
    kep.save(adat, format="PNG")
    return adat.getvalue()


def gombok_letiltasa(window):
    for i in range(4):
        window[f"-VALASZ{i}-"].update(
            disabled=True,
            button_color=("#777777", "#303030")
        )


def gombok_engedelyezese(window):
    szinek = [
        ("#FFFFFF", "#E53935"),
        ("#FFFFFF", "#1976D2"),
        ("#FFFFFF", "#009688"),
        ("#FFFFFF", "#F57C00"),
    ]

    for i in range(4):
        window[f"-VALASZ{i}-"].update(
            disabled=False,
            button_color=szinek[i]
        )


def kepernyo_valtas(window, kepernyo):
    window["-FO-MENU-"].update(visible=False)
    window["-JATEK-"].update(visible=False)
    window[kepernyo].update(visible=True)
    window.refresh()


def uj_jatek(window):
    global pontszam, aktualis_auto, jatek_vege

    pontszam = 0
    aktualis_auto = 0
    jatek_vege = False

    random.shuffle(autok)

    window["-PONT-"].update("PONTSZÁM: 0")
    window["-VEGE-CIM-"].update("", visible=False)
    window["-VEGE-SZOVEG-"].update("", visible=False)

    kepernyo_valtas(window, "-JATEK-")
    kovetkezo_auto(window)


def jatek_vege_kepernyo(window):
    global jatek_vege

    jatek_vege = True

    gombok_letiltasa(window)

    window["-KEP-"].update(data=None)

    window["-KERDES-"].update(
        "GRATULÁLUNK!"
    )

    window["-PONT-"].update(
        f"VÉGSŐ PONTSZÁM: {pontszam} / {len(autok)}"
    )

    if pontszam >= 18:
        window["-VEGE-CIM-"].update(
            "NAGYON PROFI VAGY!",
            visible=True
        )
    elif pontszam > 15:
        window["-VEGE-CIM-"].update(
            "JÓ TELJESÍTMÉNY!",
            visible=True
        )
    elif pontszam > 10:
        window["-VEGE-CIM-"].update(
            "HALADÓ TELJESÍTMÉNY!",
            visible=True
        )
    else:
        window["-VEGE-CIM-"].update(
            "KIS GYAKORLÁSSAL PROFI LEHETSZ!",
            visible=True
        )


    window["-VEGE-SZOVEG-"].update(
        f"Gratulálunk!\n\n"
        f"Végigjátszottad a teljes kvízt!\n\n"
        f"Végső pontszám: {pontszam} / {len(autok)}",
        visible=True
    )



def kovetkezo_auto(window):
    global aktualis_auto

    if aktualis_auto >= len(autok):
        jatek_vege_kepernyo(window)
        return

    auto = autok[aktualis_auto]

    kep_utvonal = os.path.join(
        KEP_MAPPA,
        auto["kep"]
    )

    print("Keresett kép:", kep_utvonal)
    print("Létezik:", os.path.exists(kep_utvonal))

    if not os.path.exists(kep_utvonal):
        sg.popup_error(
            f"A kép nem található:\n\n{kep_utvonal}",
            title="KÉP HIBA",
            keep_on_top=True
        )
        return

    try:
        kep_adat = kep_betoltese(kep_utvonal)
        window["-KEP-"].update(data=kep_adat)
    except Exception as e:
        sg.popup_error(
            f"Nem sikerült betölteni a képet:\n\n{e}",
            title="KÉP HIBA",
            keep_on_top=True
        )
        return

    window["-KERDES-"].update(
        f"MELYIK JÁRMŰ EZ?     {aktualis_auto + 1} / {len(autok)}"
    )

    opciok = auto["opciok"].copy()
    random.shuffle(opciok)

    for i in range(4):
        window[f"-VALASZ{i}-"].update(opciok[i])

    gombok_engedelyezese(window)


fomenu = [
    [
        sg.Text(
            "VETERÁN JÁRMŰ KVÍZ",
            font=("Arial", 32, "bold"),
            text_color="#FFD166",
            background_color="#151525",
            justification="center",
            expand_x=True,
        )
    ],
    [
        sg.Text(
            "TALÁLD EL A VETERÁN JÁRGÁNYOKAT!",
            font=("Arial", 16, "bold"),
            text_color="#00F5D4",
            background_color="#151525",
            justification="center",
            expand_x=True,
        )
    ],
    [
        sg.Button(
            "KEZDÉS",
            key="-KEZDES-",
            size=(22, 2),
            font=("Arial", 15, "bold"),
            button_color=("#FFFFFF", "#ffa500"),
            border_width=10,
        )
    ],
    [
        sg.Button(
            "KILÉPÉS",
            key="-KILEPES-",
            size=(22, 2),
            font=("Arial", 15, "bold"),
            button_color=("#FFFFFF", "#008000"),
            border_width=7,
        )
    ],
    [
        sg.Text(
            "owner: gobolygyurika",
            font=("Arial", 10),
            text_color="#ffefd5",
            background_color="#151525",
        ),
    ],
]


jatek = [
    [
        sg.Text(
            "RETRO KVÍZ",
            font=("Arial", 24, "bold"),
            text_color="#FFFFFF",
            background_color="#151525",
            justification="center",
            expand_x=True,
        )
    ],
    [
        sg.Text(
            "",
            key="-NEV-",
            font=("Arial", 11, "bold"),
            text_color="#FFD166",
            background_color="#151525",
            justification="center",
            expand_x=True,
        )
    ],
    [
        sg.Text(
            "MELYIK AUTÓ EZ?",
            key="-KERDES-",
            font=("Arial", 15, "bold"),
            text_color="#FFFFFF",
            background_color="#25253D",
            justification="center",
            expand_x=True,
        )
    ],
    [
        sg.Image(
            key="-KEP-",
            background_color="#202035",
        )
    ],
    [
        sg.Button(
            "",
            key="-VALASZ0-",
            size=(20, 2),
            font=("Arial", 11, "bold"),
            button_color=("#FFFFFF", "#E53935"),
        ),
        sg.Button(
            "",
            key="-VALASZ1-",
            size=(20, 2),
            font=("Arial", 11, "bold"),
            button_color=("#FFFFFF", "#1976D2"),
        ),
    ],
    [
        sg.Button(
            "",
            key="-VALASZ2-",
            size=(20, 2),
            font=("Arial", 11, "bold"),
            button_color=("#FFFFFF", "#009688"),
        ),
        sg.Button(
            "",
            key="-VALASZ3-",
            size=(20, 2),
            font=("Arial", 11, "bold"),
            button_color=("#FFFFFF", "#F57C00"),
        ),
    ],
    [
        sg.Text(
            "PONTSZÁM: 0",
            key="-PONT-",
            font=("Arial", 16, "bold"),
            text_color="#00F5D4",
            background_color="#151525",
            justification="center",
            expand_x=True,
        )
    ],
    [
        sg.Text(
            "",
            key="-VEGE-CIM-",
            font=("Arial", 22, "bold"),
            text_color="#FFD166",
            background_color="#171B2E",
            justification="center",
            expand_x=True,
            visible=False,
        )
    ],
    [
        sg.Text(
            "",
            key="-VEGE-SZOVEG-",
            font=("Arial", 13, "bold"),
            text_color="#FFFFFF",
            background_color="#171B2E",
            justification="center",
            expand_x=True,
            visible=False,
        )
    ],
    [
        sg.Button(
            "FŐMENÜ",
            key="-FO-MENU-GOMB-",
            size=(12, 2),
            font=("Arial", 10, "bold"),
            button_color=("#FFFFFF", "#0000ff"),
        ),
        sg.Button(
            "KILÉPÉS",
            key="-JATEK-KILEPES-",
            size=(12, 2),
            font=("Arial", 10, "bold"),
            button_color=("#FFFFFF", "#D90429"),
        ),
    ],
]


fo_container = sg.Column(
    [
        [
            sg.Column(
                fomenu,
                element_justification="center",
                background_color="#d3d3d3"
            )
        ]
    ],
    key="-FO-MENU-",
    background_color="#151525",
    justification="center",
    element_justification="center",
    expand_x=True,
    expand_y=True,
)


jatek_container = sg.Column(
    [
        [
            sg.Column(
                jatek,
                element_justification="center",
                background_color="#b8860b"
            )
        ]
    ],
    key="-JATEK-",
    background_color="#151525",
    justification="center",
    element_justification="center",
    expand_x=True,
    expand_y=True,
    visible=False,
)


layout = [
    [
        sg.Column(
            [
                [
                    fo_container,
                    jatek_container
                ]
            ],
            background_color="#d3d3d3",
            justification="center",
            element_justification="center",
            expand_x=True,
            expand_y=True,
        )
    ]
]



window = sg.Window(
    "GYURIKA | RETRÓ KVÍZ",
    layout,
    background_color="#d3d3d3",
    element_justification="center",
    resizable=True,
    margins=(0, 0),
    finalize=True,
)


window.Maximize()


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "-KEZDES-":
        uj_jatek(window)
        continue

    if event == "-FO-MENU-GOMB-":
        kepernyo_valtas(window, "-FO-MENU-")
        continue

    if event == "-JATEK-KILEPES-":
        break

    if event == "-KILEPES-":
        break

    if event in [
        "-VALASZ0-",
        "-VALASZ1-",
        "-VALASZ2-",
        "-VALASZ3-"
    ]:
        if jatek_vege:
            continue

        auto = autok[aktualis_auto]
        valasz = window[event].get_text()

        gombok_letiltasa(window)

        if valasz == auto["marka"]:
            pontszam += 1
        else:
            if pontszam == 0:
                sg.popup(
                    "JÁTÉK VÉGE",
                    "0 pontod volt és nem sikerült a válasz.\n\nPróbáld meg újra!",
                    title="JÁTÉK VÉGE",
                    background_color="#151525",
                    text_color="#FF4D6D",
                    button_color=("#FFFFFF", "#D90429"),
                    font=("Arial", 16, "bold"),
                    keep_on_top=True,
                )

                pontszam = 0
                aktualis_auto = 0
                jatek_vege = False

                random.shuffle(autok)

                window["-PONT-"].update("PONTSZÁM: 0")
                kepernyo_valtas(window, "-FO-MENU-")
                continue

            pontszam -= 1

            sg.popup(
                "HIBÁS VÁLASZ!",
                f"-1 PONT\n\nPONTSZÁM: {pontszam}",
                title="HIBÁS",
                background_color="#151525",
                text_color="#FF4D6D",
                button_color=("#FFFFFF", "#D90429"),
                font=("Arial", 16, "bold"),
                keep_on_top=True,
            )

        window["-PONT-"].update(
            f"PONTSZÁM: {pontszam}"
        )

        aktualis_auto += 1

        kovetkezo_auto(window)


window.close()
