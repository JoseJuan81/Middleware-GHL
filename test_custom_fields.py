from Class.GhlCustomFields import GhlCustomFields

ghl_ones = [
    {
        "id": "DvSUc0cHIVhCawpm014b",
        "name": "expectativa_salarial",
        "fieldKey": "contact.expectativa_salarial",
        "placeholder": "Expectativa salarial",
        "dataType": "TEXT",
        "position": 100
    },
    {
        "id": "yIFS64o11m25KaiBCuOi",
        "name": "resumen_personal",
        "fieldKey": "contact.resumen_personal",
        "placeholder": "Mi Resumen personal",
        "dataType": "LARGE_TEXT",
        "position": 150
    },
    {
        "id": "GuekwxYETMJDgr7zYlUd",
        "name": "dni",
        "fieldKey": "contact.dni",
        "placeholder": "DNI",
        "dataType": "TEXT",
        "position": 200
    },
    {
        "id": "rFeH6m2p16ygtmyHrBM7",
        "name": "experiencia_laboral",
        "fieldKey": "contact.experiencia_laboral",
        "placeholder": "Tu Experiencia laboral",
        "dataType": "LARGE_TEXT",
        "position": 250
    }
]

def test_custom_fields_match__all_exist():
    scrapping_ones = dict([
        ("dni", "01392684"),
        ("expectativa_salarial",
         "S/ 2.000"),
        ("resumen_personal",
         "este es mi resumen personal para aplicar al trabajo"),
        ("experiencia_laboral",
         "Trabaje aqui y alla, tambien un poquito por aqui y otro poco por alla"),
    ])

    cf = GhlCustomFields("")
    result_exist, result_no_exist = cf.custom_fields_match(custom_fields=scrapping_ones, ghl_custom_fields=ghl_ones)

    expected = {
        "rFeH6m2p16ygtmyHrBM7": "Trabaje aqui y alla, tambien un poquito por aqui y otro poco por alla",
        "GuekwxYETMJDgr7zYlUd": "01392684",
        "yIFS64o11m25KaiBCuOi": "este es mi resumen personal para aplicar al trabajo",
        "DvSUc0cHIVhCawpm014b": "S/ 2.000"
    }

    assert result_exist == expected
    assert result_no_exist == {}

def test_custom_fields_match__all_no_exist():
    scrapping_ones = dict([
        ("cedula", "01392684"),
        ("expectativa salarial",
         "S/ 2.000"),
        ("resumen personal",
         "este es mi resumen personal para aplicar al trabajo"),
        ("experiencia laboral",
         "Trabaje aqui y alla, tambien un poquito por aqui y otro poco por alla"),
    ])

    cf = GhlCustomFields("")
    result_exist, result_no_exist = cf.custom_fields_match(custom_fields=scrapping_ones, ghl_custom_fields=ghl_ones)

    expected = scrapping_ones

    assert result_no_exist == expected
    assert result_exist == {}

def test_custom_fields_match__some_match():

    scrapping_ones = dict([
        ("dni", "01392684"),
        ("expectativa salarial",
         "S/ 2.000"),
        ("resumen_personal",
         "este es mi resumen personal para aplicar al trabajo"),
        ("experiencia laboral",
         "Trabaje aqui y alla, tambien un poquito por aqui y otro poco por alla"),
    ])

    cf = GhlCustomFields("")
    result_exist, result_no_exist = cf.custom_fields_match(custom_fields=scrapping_ones, ghl_custom_fields=ghl_ones)

    expected_exist = dict([
        ("GuekwxYETMJDgr7zYlUd", "01392684"),
        ("yIFS64o11m25KaiBCuOi",
         "este es mi resumen personal para aplicar al trabajo"),
    ])
    assert result_exist == expected_exist

    expected_no_exist = dict([
        ("expectativa salarial",
         "S/ 2.000"),
        ("experiencia laboral",
         "Trabaje aqui y alla, tambien un poquito por aqui y otro poco por alla"),
    ])

    assert result_no_exist == expected_no_exist

def test_build_body():
    cf = GhlCustomFields("")
    data = ("nombre", "jose juan")
    result = cf.build_body(data)

    expected = { "name": "nombre", "placeholder": "Nombre", "dataType": "TEXT"}
    assert result == expected