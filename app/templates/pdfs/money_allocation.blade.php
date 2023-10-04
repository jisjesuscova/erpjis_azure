<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
        <style type="text/css">
            body {
                font-family: Arial, Helvetica, sans-serif;
            }
            .page-break {
                page-break-after: always;
            }
        </style>
    </head>
    <body>
        <table class="table table-bordered" style="width:100%;">
            <thead>
                <tr>
                    <img style="width: 80px;" src="data:image/png;base64,{{ base64_encode(file_get_contents(public_path('backend/img/logo.png'))) }}"> 
                </tr>
            </thead>
        </table>
        <table class="table table-bordered" style="width:100%;">
            <thead>
                <tr>
                    <td><h3><center> ANEXO DE CONTRATO DE TRABAJO</center></h3></td>   
                </tr>
            </thead>
        </table>
        <hr>
        <table class="table" style="width:100%;">
            <tbody>
                <tr>
                    <td style="text-align: justify;">
                        En Santiago, {{ $date }}, entre JIS PARKING SPA RUT: 76063822-6 con domicilio en MATUCANA 40 Estacion
                        Central en adelante tambien "LA EMPRESA" por una parte, y la otra Sr(a) <strong>{{ $full_name }}</strong>, cédula de identidad Nº <strong>{{ $rut }}</strong> en adelante, también, "EL TRABAJADOR(a)" se deja testimonio y se ha acordado el finiquito que consta de las
                        siguientes cláusulas:<br><br>
                        PRIMERO:
                        Sr(a) <strong>{{ $full_name }}</strong>, Declara haberle prestado servicio en calidad de <strong>{{ $position }}</strong>, a JIS PARKING SPA desde el <strong>{{ $entrance_company }}</strong> hasta <strong>{{ $exit_document }}</strong>, Fecha de terminación de sus
                        servicios por la siguiente causal, Art. 161 Necesidades de la empresa, del código del Trabajo.<br><br>
                        SEGUNDO:
                        Sr(a) <strong>{{ $full_name }}</strong>, Declara recibir en este acto, a su entera satisfacción, de parte de JIS PARKING SPA,
                        las sumas que a continuación se indica, por los siguientes conceptos:<br><br>
                        Resumen Monto<br>
                        Indemnización Años de Servicios $ 534.062.208<br>
                        Indemnización Sustitutivo Aviso Previo $ 44.505.184<br>
                        Feriado Proporcional (29 dias) $ 34.916.000<br>
                        Total $ 613.483.392<br><br>
                        TERCERO:
                        Sr(a) <strong>{{ $full_name }}</strong>, deja constancia que durante todo el tiempo que prestó servicios a la firma JIS
                        PARKING SPA, recibió oportunamente el total de las remuneraciones, beneficios y demás prestaciones convenidas de acuerdo
                        a su contrato de trabajo, clase de trabajo ejecutado y disposiciones legales pertinentes, y que en tal virtud el empleador nada le
                        adeuda por tales conceptos, ni por horas extraordinarias, asignación familiar, feriado, indemnización por años de servicios,
                        imposiciones previsionales, así como por ningún otro concepto, ya sea legal o contractual, derivado de la prestación de sus
                        servicios, de su contrato de trabajo o de la terminación del mismo. En consecuencia «EL TRABAJADOR» declara que no tiene
                        reclamo alguno que formular en contra de JIS PARKING SPA, renunciando a todas las acciones que pudieran emanar del
                        contrato que los vinculó, y deja expresa constacia que JIS PARKING SPA nada le adeuda. en relación con los servicios
                        prestados, con el contrato de trabajo o con motivo de la terminación del mismo, por lo que libre y espontáneamente, y con el
                        pleno y cabal conocimiento de sus derechos, otorga a su empleador, el mas amplio, completo, total y definitivo finiquito por los
                        servicios prestados o la terminación de ellos, ya diga relación con remuneraciones, cotizaciones previsionales, de seguridad
                        social o de salud, subsidios,  beneficios contractuales adicionales a las remuneraciones, indemnizaciones, compensaciones, o
                        con cualquiera causa o concepto.<br><br><br><br><br><br>

                        <center><img style="width: 150px;" src="data:image/png;base64,{{ base64_encode(file_get_contents(public_path('backend/img/sign.png'))) }}">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;____________________</center>
                        <center>EMPLEADOR&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TRABAJADOR</center>
                        <center>76.063.822-6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ $rut }}&nbsp;&nbsp;</center>
                    </td>
                </tr>
            </tbody>
        </table>
     </body>
</html>