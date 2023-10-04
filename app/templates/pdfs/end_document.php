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
    <body style="width:100%; font-size: 12px;">
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
                    <td><h3><center>FINIQUITO</center></h3></td>   
                </tr>
            </thead>
        </table>
        <table class="table table-bordered">
            <thead>
                <tr>
                    <td style="text-aling: right;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Santiago, {{ $exit_date }}</td>   
                </tr>
            </thead>
        </table>
        <hr>
        <table class="table" style="width:100%;">
            <tbody>
                <tr>
                    <td style="text-align: justify;">
                        En Santiago, <strong>{{ $exit_date }}</strong>, entre <strong>JIS PARKING SPA RUT: 76063822-6</strong> con domicilio en MATUCANA 40 Estacion
                        Central en adelante tambien "LA EMPRESA" por una parte, y la otra don (a) <strong>{{ $full_name }}</strong> RUT:
                        <strong>{{ $rut }}</strong> en adelante, también, "EL TRABAJADOR(a)" se deja testimonio y se ha acordado el finiquito que consta de las
                        siguientes cláusulas:<br><br>
                        <strong>PRIMERO:</strong>
                        Sr(a) <strong>{{ $full_name }}</strong>, Declara haberle prestado servicio en calidad de <strong>{{ $position }}</strong>, a <strong>JIS PARKING SPA</strong> desde el <strong>{{ $entrance_date }}</strong> hasta el <strong>{{ $exit_date }}</strong>, Fecha de terminación de sus
                        servicios por la siguiente causal, {{ $causal }}, del código del Trabajo.<br><br>
                        <strong>SEGUNDO:</strong>
                        Sr(a) <strong>{{ $full_name }}</strong>, Declara recibir en este acto, a su entera satisfacción, de parte de <strong>JIS PARKING SPA</strong>,
                        las sumas que a continuación se indica, por los siguientes conceptos:<br><br>
                        <strong>Resumen Monto</strong><br><br>
                        <table style="text-aling: right; margin-right: 30px;">
                            <tr>
                                <td>
                                    Indemnización Años de Servicios 
                                </td>
                                <td style="text-align: right;">
                                    $ <strong>{{ $service_years }}.-</strong>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    Indemnización Sustitutivo Aviso Previo 
                                </td>
                                <td style="text-align: right;">
                                    $ <strong>{{ $sustituve_prior_notice }}.-</strong>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    Indemnización Voluntaria
                                </td>
                                <td style="text-align: right;">
                                    $ <strong>{{ $voluntary_compensation }}.-</strong>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    Feriado Proporcional (<strong>{{ $days }}</strong> dias)
                                </td>
                                <td style="text-align: right;">
                                    $ <strong>{{ $proportional_holiday }}.-</strong>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    Total
                                </td>
                                <td style="text-align: right;">
                                    $ <strong>{{ $total }}.-</strong>
                                </td>
                            </tr>
                        </table><br><br>
                        <strong>TERCERO:</strong>
                        Sr(a) <strong>{{ $full_name }}</strong>, deja constancia que durante todo el tiempo que prestó servicios a la firma <strong>JIS
                        PARKING SPA</strong>, recibió oportunamente el total de las remuneraciones, beneficios y demás prestaciones convenidas de acuerdo
                        a su contrato de trabajo, clase de trabajo ejecutado y disposiciones legales pertinentes, y que en tal virtud el empleador nada le
                        adeuda por tales conceptos, ni por horas extraordinarias, asignación familiar, feriado, indemnización por años de servicios,
                        imposiciones previsionales, así como por ningún otro concepto, ya sea legal o contractual, derivado de la prestación de sus
                        servicios, de su contrato de trabajo o de la terminación del mismo. En consecuencia "EL TRABAJADOR" declara que no tiene
                        reclamo alguno que formular en contra de <strong>JIS PARKING SPA</strong>, renunciando a todas las acciones que pudieran emanar del
                        contrato que los vinculó, y deja expresa constacia que <strong>JIS PARKING SPA</strong> nada le adeuda. en relación con los servicios
                        prestados, con el contrato de trabajo o con motivo de la terminación del mismo, por lo que libre y espontáneamente, y con el
                        pleno y cabal conocimiento de sus derechos, otorga a su empleador, el mas amplio, completo, total y definitivo finiquito por los
                        servicios prestados o la terminación de ellos, ya diga relación con remuneraciones, cotizaciones previsionales, de seguridad
                        social o de salud, subsidios, beneficios contractuales adicionales a las remuneraciones, indemnizaciones, compensaciones, o
                        con cualquiera causa o concepto.
                        <br><br><br><br><br><br><br><br>

                        <center><img style="width: 150px;" src="data:image/png;base64,{{ base64_encode(file_get_contents(public_path('backend/img/sign.png'))) }}">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;____________________</center>
                        <center>EMPLEADOR&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TRABAJADOR</center>
                        <center>76.063.822-6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ $rut }}&nbsp;&nbsp;</center>
                    </td>
                </tr>
            </tbody>
        </table>

        <br><br><center><font style="font-size: 10px;">1 de 2</font></center>

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
                    <td><h3><center>DECLARACIÓN JURADA</center></h3></td>   
                </tr>
            </thead>
        </table>
        <hr>
        <table class="table" style="width:100%;">
            <tbody>
                <tr>
                    <td style="text-align: justify;">
                        En Santiago, con fecha <strong>{{ $exit_date }}</strong>, <strong>Marcelo Alejandro Inzunza 
                        González</strong>, Cédula de Identidad N° <strong>10.033.741-K</strong>, En representación de la empresa 
                        <strong>Jis Parking SPA</strong> Rol Único Tributario N° <strong>76.063.822-6</strong>, Domiciliada en calle: AV. 
                        Matucana # 40, Comuna de Estación Central, Ciudad de Santiago, Región Metropolitana, en calidad de empleador de don (a) <strong>{{ $full_name }}</strong> RUT:
                        <strong>{{ $rut }}</strong>, Domiciliado en {{ $address }}, vengo en certificar lo siguiente: 
                        <br><br>
                        Declaro, que no hemos sido notificados por concepto de <strong>Retención Judicial por Pensión de alimentos, durante su periodo de contratación</strong>.
                        <br><br>
                        Don (a) <strong>{{ $full_name }}</strong>, prestó servicios para nuestra empresa en calidad de {{ $position }} desde el {{ $entrance_date }} al {{ $exit_date }}.
                        <br><br>
                        Se extiende el presente certificado a fin de cumplir con lo dispuesto según modificación <strong>Ley N° 14908 sobre Abandono de Familia y Pago de Pensiones Alimenticias</strong>, promulgado en el Diario Oficial de Fecha 18 de Noviembre del 2021.

                        <br><br><br><br><br><br><br><br>

                        <center><img style="width: 150px;" src="data:image/png;base64,{{ base64_encode(file_get_contents(public_path('backend/img/sign.png'))) }}">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;____________________</center>
                        <center>EMPLEADOR&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TRABAJADOR</center>
                        <center>76.063.822-6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ $rut }}&nbsp;&nbsp;</center>
                    </td>
                </tr>
            </tbody>
        </table>

        <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><center><font style="font-size: 10px;">2 de 2</font></center>
     </body>
</html>