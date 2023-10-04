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
                    <td><h3><center>ANEXO DE ACTUALIZACIÓN DE CONTRATO DE TRABAJO</center></h3></td>   
                </tr>
            </thead>
        </table>
        <hr>
        <table class="table" style="width:100%;">
            <tbody>
                <tr>
                    <td style="text-align: justify;">
                        En Santiago, <strong>{{ $start_date }}</strong>, entre <strong>Jis Parking SPA.</strong>, RUT <strong>76063822-6</strong>, representada por don(ña) <strong>Marcelo Alejandro
                        Inzunza González</strong>, cédula de identidad N° <strong>10.033.741-K</strong>, ambos domiciliados en <strong>Matucana # 40, Estación Central, Cuidad de
                        Santiago</strong>, en adelante el "EMPLEADOR" y por otra parte Sr(a) <strong>{{ $full_name }}</strong>, cédula de identidad Nº <strong>{{ $rut }}</strong>, en
                        adelante el(la) “TRABAJADOR(A)”; se ha convenido la celebración de la siguiente actualización de contrato de trabajo a partir de <strong>{{ $start_date }}</strong> de acuerdo a
                        lo establecido en el artículo 11 del Código del Trabajo:<br><br>
                        <strong>PRIMERO:</strong> El trabajador percibirá por sus servicios un sueldo base mensual de <strong>$ {{ $gross_salary }}.-</strong> brutos, proporcional a los días
                        efectivamente trabajados.<br><br>
                        Las ausencias y/o atrasos en el mes respectivo no darán derecho a pago de remuneración alguna.<br><br>
                        <strong>SEGUNDO:</strong> El (la) trabajador(a) se compromete y obliga a ejecutar el trabajo de Prevencionista de Riesgos.<br><br>
                        <strong>TERCERO:</strong> El (la) trabajador(a) se compromete y obliga a ejecutar el trabajo en la sucursal: <strong>{{ $branch_office_name }}</strong> ubicado(s) en <strong>{{ $branch_office_address }}</strong> o en cualquiera de los demás locales o dependencias de la empresa.<br><br>
                        En comprobante y previa lectura se firma el presente Anexo de Contrato en tres ejemplares, quedando uno en poder del (la)
                        trabajador(a) quien declara haberlo recibido a su entera conformidad y dos en poder del empleado.
                        <br><br><br><br><br><br>

                        <center><img style="width: 150px;" src="data:image/png;base64,{{ base64_encode(file_get_contents(public_path('backend/img/sign.png'))) }}">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;____________________</center>
                        <center>EMPLEADOR&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TRABAJADOR</center>
                        <center>76.063.822-6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ $rut }}&nbsp;&nbsp;</center>
                    </td>
                </tr>
            </tbody>
        </table>
     </body>
</html>